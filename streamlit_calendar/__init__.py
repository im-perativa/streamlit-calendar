import os

import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("calendar"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "calendar",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("calendar", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def calendar(
    events=[],
    options={},
    custom_css="",
    callbacks=["dateClick", "eventClick", "eventChange", "eventsSet"],
    license_key="CC-Attribution-NonCommercial-NoDerivatives",
    key=None,
):
    """Create a new instance of "calendar".

    Parameters
    ----------
    events: event[]
        Array of event object. For complete event object properties,
        check out: https://fullcalendar.io/docs/event-object
    options: dict
        Dictionary of calendar options. For complete options,
        check out: https://fullcalendar.io/docs
    custom_css: string
        Custom CSS to customize the style of FullCalendar. For more information,
        check out: https://fullcalendar.io/docs/css-customization
    license_key: str
        An optional license key of FullCalendar. The package will use
        evaluation version which is licensed under a Creative Commons
        license that does not allow distribution of source code modifications
        nor use in commercial production websites or products if
        no license_key is provided.
    callbacks: str[]
        List of callback to enable. Set to empty list to disable all callbacks.
        List may contain 'dateClick', 'eventClick', 'eventChange', 'eventsSet'
    key: str or None
        An optional key that uniquely identifies this component. If this set to
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        State value from dateClick, eventClick, eventChange and eventsSet callback

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(
        events=events,
        options=options,
        custom_css=custom_css,
        callbacks=callbacks,
        license_key=license_key,
        key=key,
        default={},
    )

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run calendar/__init__.py`
if not _RELEASE:
    import streamlit as st

    st.set_page_config(page_title="Demo for streamlit-calendar", page_icon="📆")

    st.markdown(
        "## Demo for [streamlit-calendar](https://github.com/im-perativa/streamlit-calendar) 📆"
    )

    st.markdown(
        "[![](https://img.shields.io/github/stars/im-perativa/streamlit-calendar?style=social)](https://github.com/im-perativa/streamlit-calendar)"
    )

    mode = st.selectbox(
        "Calendar Mode:",
        (
            "daygrid",
            "timegrid",
            "timeline",
            "resource-daygrid",
            "resource-timegrid",
            "resource-timeline",
            "list",
            "multimonth",
        ),
    )

    events = [
        {
            "title": "Event 1",
            "color": "#FF6C6C",
            "start": "2023-07-03",
            "end": "2023-07-05",
            "resourceId": "a",
        },
        {
            "title": "Event 2",
            "color": "#FFBD45",
            "start": "2023-07-01",
            "end": "2023-07-10",
            "resourceId": "b",
        },
        {
            "title": "Event 3",
            "color": "#FF4B4B",
            "start": "2023-07-20",
            "end": "2023-07-20",
            "resourceId": "c",
        },
        {
            "title": "Event 4",
            "color": "#FF6C6C",
            "start": "2023-07-23",
            "end": "2023-07-25",
            "resourceId": "d",
        },
        {
            "title": "Event 5",
            "color": "#FFBD45",
            "start": "2023-07-29",
            "end": "2023-07-30",
            "resourceId": "e",
        },
        {
            "title": "Event 6",
            "color": "#FF4B4B",
            "start": "2023-07-28",
            "end": "2023-07-20",
            "resourceId": "f",
        },
        {
            "title": "Event 7",
            "color": "#FF4B4B",
            "start": "2023-07-01T08:30:00",
            "end": "2023-07-01T10:30:00",
            "resourceId": "a",
        },
        {
            "title": "Event 8",
            "color": "#3D9DF3",
            "start": "2023-07-01T07:30:00",
            "end": "2023-07-01T10:30:00",
            "resourceId": "b",
        },
        {
            "title": "Event 9",
            "color": "#3DD56D",
            "start": "2023-07-02T10:40:00",
            "end": "2023-07-02T12:30:00",
            "resourceId": "c",
        },
        {
            "title": "Event 10",
            "color": "#FF4B4B",
            "start": "2023-07-15T08:30:00",
            "end": "2023-07-15T10:30:00",
            "resourceId": "d",
        },
        {
            "title": "Event 11",
            "color": "#3DD56D",
            "start": "2023-07-15T07:30:00",
            "end": "2023-07-15T10:30:00",
            "resourceId": "e",
        },
        {
            "title": "Event 12",
            "color": "#3D9DF3",
            "start": "2023-07-21T10:40:00",
            "end": "2023-07-21T12:30:00",
            "resourceId": "f",
        },
        {
            "title": "Event 13",
            "color": "#FF4B4B",
            "start": "2023-07-17T08:30:00",
            "end": "2023-07-17T10:30:00",
            "resourceId": "a",
        },
        {
            "title": "Event 14",
            "color": "#3D9DF3",
            "start": "2023-07-17T09:30:00",
            "end": "2023-07-17T11:30:00",
            "resourceId": "b",
        },
        {
            "title": "Event 15",
            "color": "#3DD56D",
            "start": "2023-07-17T10:30:00",
            "end": "2023-07-17T12:30:00",
            "resourceId": "c",
        },
        {
            "title": "Event 16",
            "color": "#FF6C6C",
            "start": "2023-07-17T13:30:00",
            "end": "2023-07-17T14:30:00",
            "resourceId": "d",
        },
        {
            "title": "Event 17",
            "color": "#FFBD45",
            "start": "2023-07-17T15:30:00",
            "end": "2023-07-17T16:30:00",
            "resourceId": "e",
        },
    ]
    calendar_resources = [
        {"id": "a", "building": "Building A", "title": "Room A"},
        {"id": "b", "building": "Building A", "title": "Room B"},
        {"id": "c", "building": "Building B", "title": "Room C"},
        {"id": "d", "building": "Building B", "title": "Room D"},
        {"id": "e", "building": "Building C", "title": "Room E"},
        {"id": "f", "building": "Building C", "title": "Room F"},
    ]

    calendar_options = {
        "editable": "true",
        "navLinks": "true",
        "resources": calendar_resources,
    }

    if "resource" in mode:
        if mode == "resource-daygrid":
            calendar_options = {
                **calendar_options,
                "initialDate": "2023-07-01",
                "initialView": "resourceDayGridDay",
                "resourceGroupField": "building",
            }
        elif mode == "resource-timeline":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
                },
                "initialDate": "2023-07-01",
                "initialView": "resourceTimelineDay",
                "resourceGroupField": "building",
            }
        elif mode == "resource-timegrid":
            calendar_options = {
                **calendar_options,
                "initialDate": "2023-07-01",
                "initialView": "resourceTimeGridDay",
                "resourceGroupField": "building",
            }
    else:
        if mode == "daygrid":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": "2023-07-01",
                "initialView": "dayGridMonth",
            }
        elif mode == "timegrid":
            calendar_options = {
                **calendar_options,
                "initialView": "timeGridWeek",
            }
        elif mode == "timeline":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "timelineDay,timelineWeek,timelineMonth",
                },
                "initialDate": "2023-07-01",
                "initialView": "timelineMonth",
            }
        elif mode == "list":
            calendar_options = {
                **calendar_options,
                "initialDate": "2023-07-01",
                "initialView": "listMonth",
            }
        elif mode == "multimonth":
            calendar_options = {
                **calendar_options,
                "initialView": "multiMonthYear",
            }

    state = calendar(
        events=st.session_state.get("events", events),
        options=calendar_options,
        custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
        """,
        key=mode,
    )

    if state.get("eventsSet") is not None:
        st.session_state["events"] = state["eventsSet"]

    st.write(state)

    st.markdown("## API reference")
    st.help(calendar)
