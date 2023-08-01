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
def calendar(events=[], options={},
             license_key='CC-Attribution-NonCommercial-NoDerivatives', key=None):
    """Create a new instance of "calendar".

    Parameters
    ----------
    events: event[]
        Array of event object. For complete event object properties, 
        check out: https://fullcalendar.io/docs/event-object
    options: dict
        Dictionary of calendar options. For complete options, 
        check out: https://fullcalendar.io/docs
    license_key: str
        An optional license key of FullCalendar. The package will use 
        evaluation version which is licensed under a Creative Commons 
        license that does not allow distribution of source code modifications 
        nor use in commercial production websites or products if 
        no license_key is provided.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        State value from eventClick and dateClick callback

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(events=events, options=options,
                                      license_key=license_key, key=key, default={})

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run calendar/__init__.py`
if not _RELEASE:
    import streamlit as st

    options_dict = {
        'headerToolbar': {
            'left': 'today prev,next',
            'center': 'title',
            'right': 'resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth'
        },
        'slotMinTime': '06:00:00',
        'slotMaxTime': '18:00:00',
        'initialView': 'resourceTimelineDay',
        'resourceGroupField': 'building',
        'resources': [
            {'id': 'a', 'building': 'Building A', 'title': 'Room A'},
            {'id': 'b', 'building': 'Building A', 'title': 'Room B'},
            {'id': 'c', 'building': 'Building B', 'title': 'Room C'},
            {'id': 'd', 'building': 'Building B', 'title': 'Room D'},
            {'id': 'e', 'building': 'Building C', 'title': 'Room E'},
            {'id': 'f', 'building': 'Building C', 'title': 'Room F'},
        ]
    }

    state = calendar(events=[
        {"title": "Event 1", "start": "2023-07-31T08:30:00", "end": "2023-07-31T10:30:00", "resourceId": "a"},
        {"title": "Event 2", "start": "2023-07-31T07:30:00", "end": "2023-07-31T10:30:00", "resourceId": "b"},
        {"title": "Event 3", "start": "2023-07-31T10:40:00", "end": "2023-07-31T12:30:00", "resourceId": "a"},
    ], options=options_dict, key="foo")

    st.write(state)
