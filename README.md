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

## 📝API References

### Initialization Args

For complete `event` object properties, check out: [https://fullcalendar.io/docs/event-object](https://fullcalendar.io/docs/event-object)  
For complete `options` object properties, check out: [https://fullcalendar.io/docs](https://fullcalendar.io/docs)  
For complete `custom_css` options, check out: [https://fullcalendar.io/docs/css-customization](https://fullcalendar.io/docs/css-customization)

### Component Values

The component value, i.e. the return value of the `calendar(...)` instance, is a dict which properties depends on the current called callback.

For example, when the user clicked on an event, the component value would be:

```python
st.write(calendar)
# {
#   "callback": "eventClick",
#   "eventClick": {
#     "event": {
#       "allDay": true,
#       "title": "Event 1",
#       "start": "2023-07-03",
#       "end": "2023-07-05",
#       "backgroundColor": "#FF6C6C",
#       "borderColor": "#FF6C6C"
#     },
#     "view": {
#       "type": "dayGridMonth",
#       "title": "July 2023",
#       "activeStart": "2023-06-24T17:00:00.000Z",
#       "activeEnd": "2023-08-05T17:00:00.000Z",
#       "currentStart": "2023-06-30T17:00:00.000Z",
#       "currentEnd": "2023-07-31T17:00:00.000Z"
#     }
#   },
# }
```

The properties of each callback is explained as follows:

#### `dateClick`

Triggered when the user clicks on a date or a time.

Source: [https://fullcalendar.io/docs/dateClick](https://fullcalendar.io/docs/dateClick)

| Property |            Type            | Description                                                                                         |
| -------- | :------------------------: | --------------------------------------------------------------------------------------------------- |
| allDay   |         `boolean`          | `true` or `false` whether the click happened on an all-day cell.                                    |
| date     |          `string`          | a date for the clicked day/time in [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) format. |
| view     |     [`View`](#ViewApi)     | The current view.                                                                                   |
| resource | [`Resource`](#ResourceApi) | If the current view is a resource-view, the resource that owns this date.                           |

#### `eventClick`

Triggered when the user clicks an event.

Source: [https://fullcalendar.io/docs/eventClick](https://fullcalendar.io/docs/eventClick)

| Property |         Type         | Description           |
| -------- | :------------------: | --------------------- |
| event    | [`Event`](#EventApi) | The associated event. |
| view     |  [`View`](#ViewApi)  | The current view.     |

#### `eventChange`

Called after an event has been modified in some way.

Source: [https://fullcalendar.io/docs/eventChange](https://fullcalendar.io/docs/eventChange)

| Property      |          Type          | Description                                                                                                                                                               |
| ------------- | :--------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| oldEvent      |  [`Event`](#EventApi)  | An event with data prior to the change.                                                                                                                                   |
| event         |  [`Event`](#EventApi)  | An Event Object with the updated changed data.                                                                                                                            |
| relatedEvents | [`Event[]`](#EventApi) | An array of other related events that were also affected. An event might have other recurring event instances or might be linked to other events with the same `groupId`. |

#### `eventsSet`

Called after event data is initialized **OR** changed in any way.

Source: [https://fullcalendar.io/docs/eventsSet](https://fullcalendar.io/docs/eventsSet)

| Property |          Type          | Description                                            |
| -------- | :--------------------: | ------------------------------------------------------ |
| events   | [`Event[]`](#EventApi) | An array of events. It contains every event in memory. |

#### `select`

Triggered when a date/time selection is made.

Source: [https://fullcalendar.io/docs/select-callback](https://fullcalendar.io/docs/select-callback)

| Property |            Type            | Description                                                                                                          |
| -------- | :------------------------: | -------------------------------------------------------------------------------------------------------------------- |
| allDay   |         `boolean`          | `true` or `false` whether the selection happened on all-day cells.                                                   |
| start    |          `string`          | a date indicating the beginning of the selection in [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) format. |
| end.     |          `string`          | a date indicating the end of the selection in [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) format.       |
| view     |     [`View`](#ViewApi)     | The current view.                                                                                                    |
| resource | [`Resource`](#ResourceApi) | If the current view is a resource-view, the resource that owns this selection.                                       |

### Types

#### <a name="EventApi"></a>`Event`

Source: [https://fullcalendar.io/docs/event-object](https://fullcalendar.io/docs/event-object)

| Property        |     Type     | Description                                                                                                                                                                                |
| --------------- | :----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id              |   `string`   | A unique identifier of an event.                                                                                                                                                           |
| groupId         |   `string`   | Events that share a `groupId` will be dragged and resized together automatically.                                                                                                          |
| allDay          |  `boolean`   | Determines if the event is shown in the “all-day” section of relevant views. In addition, if `true` the time text is not displayed with the event.                                         |
| start           |   `string`   | An [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) representation of the start date. If the event is all-day, there will not be a time part.                                      |
| end             |   `string`   | An [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) representation of the end date. If the event is all-day, there will not be a time part.                                        |
| title           |   `string`   | The text that will appear on an event.                                                                                                                                                     |
| url             |   `string`   | A URL that will be visited when this event is clicked by the user.                                                                                                                         |
| classNames      |  `string[]`  | An array of strings like `[ 'myclass1', myclass2' ]`. Determines which HTML classNames will be attached to the rendered event.                                                             |
| display         |   `string`   | The rendering type of this event. Can be `'auto'`, `'block'`, `'list-item'`, `'background'`, `'inverse-background'`, or `'none'`.                                                          |
| backgroundColor |   `string`   | The `eventBackgroundColor` override for this specific event.                                                                                                                               |
| borderColor     |   `string`   | The `eventBorderColor` override for this specific event.                                                                                                                                   |
| textColor       |   `string`   | The `eventTextColor` override for this specific event.                                                                                                                                     |
| extendedProps   | `Dictionary` | A plain object holding miscellaneous other properties specified during parsing. Receives properties in the explicitly given `extendedProps` hash as well as other non-standard properties. |
| resourceId      |   `string`   | The unique string identifier for the resource of the event (if any).                                                                                                                       |

#### <a name="ResourceApi"></a>`Resource`

Source: [https://fullcalendar.io/docs/resource-object](https://fullcalendar.io/docs/resource-object)

| Property             |     Type     | Description                                                     |
| -------------------- | :----------: | --------------------------------------------------------------- |
| id                   |   `string`   | The unique string identifier for this resource.                 |
| title                |   `string`   | The title of this resource.                                     |
| eventBackgroundColor |   `string`   | Same as `Event.backgroundColor`.                                |
| eventBorderColor     |   `string`   | Same as `Event.borderColor`.                                    |
| eventTextColor       |   `string`   | Same as `Event.textColor`.                                      |
| eventClassNames      |  `string[]`  | Same as `Event.ClassNames`.                                     |
| extendedProps        | `Dictionary` | A hash of non-standard props that were specified during parsing |

#### <a name="ViewApi"></a>`View`

Source: [https://fullcalendar.io/docs/view-object](https://fullcalendar.io/docs/view-object)

| Property     |  Type  | Description                                                                                                                    |
| ------------ | :----: | ------------------------------------------------------------------------------------------------------------------------------ |
| type         | string | Name of one of the available views.                                                                                            |
| title        | string | Title text that is displayed at the top of the `headerToolbar`.                                                                |
| activeStart  | string | An [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) that is the first visible day.                                     |
| activeEnd    | string | An [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) that is the last visible day.                                      |
| currentStart | string | An [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) that is the start of the interval the view is trying to represent. |
| currentEnd   | string | An [ISO8601 string](https://en.wikipedia.org/wiki/ISO_8601) that is the end of the interval the view is trying to represent.   |

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
