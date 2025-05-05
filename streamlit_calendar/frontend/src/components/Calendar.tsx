import "../styles/Calendar.css"

import adaptivePlugin from "@fullcalendar/adaptive" // premium
import dayGridPlugin from "@fullcalendar/daygrid"
import interactionPlugin, { DateClickArg } from "@fullcalendar/interaction"
import listPlugin from "@fullcalendar/list"
import multiMonthPlugin from "@fullcalendar/multimonth"
import FullCalendar from "@fullcalendar/react"
import resourceDayGridPlugin from "@fullcalendar/resource-daygrid" // premium
import resourceTimeGridPlugin from "@fullcalendar/resource-timegrid" // premium
import resourceTimelinePlugin from "@fullcalendar/resource-timeline" // premium
import timeGridPlugin from "@fullcalendar/timegrid"
import timelinePlugin from "@fullcalendar/timeline" // premium
import rrulePlugin from "@fullcalendar/rrule"; //

import {
  CalendarOptions,
  DateSelectArg,
  EventApi,
  EventChangeArg,
  EventClickArg,
  EventSourceInput,
  ViewApi,
} from "@fullcalendar/core"
import React, { useRef } from "react"
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib"
import { ComponentProps } from "streamlit-component-lib/dist/StreamlitReact"
import styled from "styled-components"
import {
  Callback,
  DateClickComponentValue,
  DateClickValue,
  EventChangeComponentValue,
  EventChangeValue,
  EventClickComponentValue,
  EventClickValue,
  EventsSetComponentValue,
  EventsSetValue,
  SelectComponentValue,
  SelectValue,
  ViewValue,
} from "../types/Calendar.type"

const ENABLED_PLUGINS = [
  adaptivePlugin,
  dayGridPlugin,
  interactionPlugin,
  listPlugin,
  multiMonthPlugin,
  resourceDayGridPlugin,
  resourceTimeGridPlugin,
  resourceTimelinePlugin,
  timeGridPlugin,
  timelinePlugin,
  rrulePlugin,
]

const FullCalendarWrapper = styled.div<{ $customCSS?: string }>`
  ${(props) => props.$customCSS}
`

type Props = ComponentProps<{
  events?: EventSourceInput
  options?: CalendarOptions
  custom_css?: string
  callbacks?: Callback[]
  license_key?: string
}>

const CalendarFC: React.FC<Props> = ({
  args: { events, options, custom_css, callbacks, license_key },
}) => {
  const calendarRef = useRef<FullCalendar>(null)
  
  const getViewValue = (view: ViewApi): ViewValue => ({
    type: view.type,
    title: view.title,
    activeStart: view.activeStart.toISOString(),
    activeEnd: view.activeEnd.toISOString(),
    currentStart: view.currentStart.toISOString(),
    currentEnd: view.currentEnd.toISOString(),
  })
  
  const handleDateClick = (arg: DateClickArg) => {
    const dateClick: DateClickValue = {
      allDay: arg.allDay,
      date: arg.date.toISOString(),
      view: getViewValue(arg.view),
      resource: arg.resource?.toJSON(),
    }

    const componentValue: DateClickComponentValue = {
      callback: "dateClick",
      dateClick,
    }

    Streamlit.setComponentValue(componentValue)
  }

  const handleEventClick = (arg: EventClickArg) => {
    const eventClick: EventClickValue = {
      event: {
        ...arg.event.toJSON(),
        resourceId: arg.event.getResources()[0]?.id,
      },
      view: getViewValue(arg.view),
    }

    const componentValue: EventClickComponentValue = {
      callback: "eventClick",
      eventClick,
    }

    Streamlit.setComponentValue(componentValue)
  }

  const handleEventChange = (arg: EventChangeArg) => {
    const eventChange: EventChangeValue = {
      oldEvent: {
        ...arg.oldEvent.toJSON(),
        resourceId: arg.oldEvent.getResources()[0]?.id,
      },
      event: {
        ...arg.event.toJSON(),
        resourceId: arg.event.getResources()[0]?.id,
      },
      relatedEvents: arg.relatedEvents.map((related) => related.toJSON()),
      ...(calendarRef.current?.getApi() && {
        view: getViewValue(calendarRef.current.getApi().view)
      })
    }

    const componentValue: EventChangeComponentValue = {
      callback: "eventChange",
      eventChange,
    }

    Streamlit.setComponentValue(componentValue)
  }

  const handleEventsSet = (events: EventApi[]) => {
    const eventsSet: EventsSetValue = {
      events: events.map((event) => ({
        ...event.toJSON(),
        resourceId: event.getResources()[0]?.id,
      })),
      ...(calendarRef.current?.getApi() && {
        view: getViewValue(calendarRef.current.getApi().view)
      })
    };
    const componentValue: EventsSetComponentValue = {
      callback: "eventsSet",
      eventsSet,
    }

    Streamlit.setComponentValue(componentValue)
  }

  const handleSelect = (arg: DateSelectArg) => {
    const select: SelectValue = {
      allDay: arg.allDay,
      start: arg.start.toISOString(),
      end: arg.end.toISOString(),
      view: getViewValue(arg.view),
      resource: arg.resource?.toJSON(),
    }

    const componentValue: SelectComponentValue = {
      callback: "select",
      select,
    }

    Streamlit.setComponentValue(componentValue)
  }

  React.useEffect(() => {
    Streamlit.setFrameHeight()
  }, [])

  return (
    <FullCalendarWrapper $customCSS={custom_css}>
      <FullCalendar
        ref={calendarRef}
        plugins={ENABLED_PLUGINS}
        initialEvents={events}
        schedulerLicenseKey={license_key}
        dateClick={
          callbacks?.includes("dateClick") ? handleDateClick : undefined
        }
        eventClick={
          callbacks?.includes("eventClick") ? handleEventClick : undefined
        }
        eventChange={
          callbacks?.includes("eventChange") ? handleEventChange : undefined
        }
        eventsSet={
          callbacks?.includes("eventsSet") ? handleEventsSet : undefined
        }
        select={
          callbacks?.includes("select") ? handleSelect : undefined
        }
        {...options}
      />
    </FullCalendarWrapper>
  )
}

export default withStreamlitConnection(CalendarFC)
