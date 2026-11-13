"""Public wrapper contract; no frontend build or running server required."""

import importlib.util
import json
import sys
from importlib.metadata import version
from types import ModuleType
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


def load_calendar(component):
    source = Path(__file__).parents[1] / "streamlit_calendar" / "__init__.py"
    spec = importlib.util.spec_from_file_location("calendar_under_test", source)
    module = importlib.util.module_from_spec(spec)
    with patch("streamlit.components.v1.declare_component", return_value=component):
        spec.loader.exec_module(module)
    return module.calendar


class CalendarCallbackTests(unittest.TestCase):
    def test_callback_is_forwarded_and_component_value_returned(self):
        value = {"callback": "eventChange", "eventChange": {"event": {"id": "1"}}}
        component = Mock(return_value=value)
        calendar = load_calendar(component)
        callback = Mock()

        result = calendar(key="schedule", on_change=callback)

        self.assertIs(result, value)
        self.assertIs(component.call_args.kwargs["on_change"], callback)
        self.assertEqual(component.call_args.kwargs["key"], "schedule")
        callback.assert_not_called()

    def test_existing_positional_arguments_keep_their_meaning(self):
        component = Mock()
        calendar = load_calendar(component)
        events = [{"id": "1"}]
        options = {"editable": True}
        callbacks = ["eventChange"]

        calendar(events, options, ".fc {}", callbacks, "license", "schedule")

        component.assert_called_once_with(
            events=events,
            options=options,
            custom_css=".fc {}",
            callbacks=callbacks,
            license_key="license",
            key="schedule",
            default={},
        )

    def test_none_does_not_forward_new_keyword_to_old_streamlit(self):
        component = Mock()
        calendar = load_calendar(component)

        calendar(on_change=None)

        self.assertNotIn("on_change", component.call_args.kwargs)


@unittest.skipUnless(
    tuple(int(part) for part in version("streamlit").split(".")[:2]) >= (1, 36),
    "Python custom component callbacks require Streamlit >= 1.36",
)
class CalendarRuntimeTests(unittest.TestCase):
    def test_callback_reads_updated_state_once_before_rerun(self):
        from streamlit.components.v1.custom_component import CustomComponent
        from streamlit.proto.WidgetStates_pb2 import WidgetStates
        from streamlit.testing.v1 import AppTest

        component = CustomComponent(name="calendar_test", url="http://localhost:3001")
        module = ModuleType("calendar_callback_under_test")
        module.calendar = load_calendar(component)
        with patch.dict(sys.modules, {module.__name__: module}):
            app = AppTest.from_string(
                """
import streamlit as st
from calendar_callback_under_test import calendar


def changed():
    st.session_state["callback_count"] = st.session_state.get("callback_count", 0) + 1
    st.session_state["seen_value"] = st.session_state["schedule"]


calendar(key="schedule", on_change=changed)
st.button("Unrelated rerun")
"""
            ).run()
            self.assertFalse(app.exception)
            self.assertNotIn("callback_count", app.session_state)
            value = {"callback": "eventChange", "eventChange": {"event": {"id": "1"}}}
            # AppTest has no public interaction helper for custom components.
            # Supply the same widget state the frontend sends to Streamlit.
            states = WidgetStates()
            states.widgets.add(
                id=app.get("component_instance")[0].proto.id,
                json_value=json.dumps(value),
            )
            app._run(widget_state=states)
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["callback_count"], 1)
            self.assertEqual(app.session_state["seen_value"], value)
            app.button[0].click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["callback_count"], 1)


if __name__ == "__main__":
    unittest.main()
