# streamlit-calendar 📆

[![PyPI](https://img.shields.io/pypi/v/streamlit-calendar)](https://pypi.org/project/streamlit-calendar/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pypistats.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/streamlit-calendar/)
[![PyPI downloads](https://img.shields.io/pypi/dm/streamlit-calendar.svg)](https://pypistats.org/packages/streamlit-calendar)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/im-perativa/streamlit-calendar/ci.yml)](https://github.com/im-perativa/streamlit-calendar/actions)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

**A Streamlit component to show calendar view using [FullCalendar](https://fullcalendar.io/) with support for Streamlit light/dark theme, callbacks, and custom CSS**

## 🌏Demo [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://calendar-component.streamlit.app/)

![](https://github.com/im-perativa/streamlit-calendar-demo/blob/main/demo.gif)

## ⚙️Installation

```bash
pip install streamlit-calendar
```

## 💻Usage

```python
from streamlit_calendar import calendar

calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Building A", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}
calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]
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
"""

calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
st.write(calendar)
```

For complete `event` object properties, check out: [https://fullcalendar.io/docs/event-object](https://fullcalendar.io/docs/event-object)  
For complete `options` object properties, check out: [https://fullcalendar.io/docs](https://fullcalendar.io/docs)  
For complete `custom_css` options, check out: [https://fullcalendar.io/docs/css-customization](https://fullcalendar.io/docs/css-customization)

## 🛠️Development

Note: you only need to run these steps if you want to change this component or
contribute to its development!

### Setup

First, clone the repository:

```bash
git clone https://github.com/im-perativa/streamlit-calendar.git
cd streamlit-calendar
```

Install the Python dependencies:

```bash
poetry install
```

And install the frontend dependencies:

```bash
cd streamlit_calendar/frontend
npm install
```

### Making changes

To make changes, first go to `streamlit_calendar/__init__.py` and make sure the
variable `_RELEASE` is set to `False`. This will make the component use the local
version of the frontend code, and not the built project.

Then, start one terminal and run:

```bash
cd streamlit_calendar/frontend
npm start
```

This starts the frontend code on port 3001.

Open another terminal and run:

```bash
cd streamlit_calendar
poetry shell
streamlit run __init__.py
```

This runs the development version on local Streamlit server. Now you can make changes to the Python or Javascript
code in `streamlit_calendar` and the demo app should update automatically!

If nothing updates, make sure the variable `_RELEASE` in `streamlit_calendar/__init__.py` is set to `False`.
