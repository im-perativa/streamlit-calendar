import adaptivePlugin from "@fullcalendar/adaptive" // premium
import dayGridPlugin from "@fullcalendar/daygrid"
import interactionPlugin from "@fullcalendar/interaction"
import listPlugin from "@fullcalendar/list"
import multiMonthPlugin from "@fullcalendar/multimonth"
import resourceDayGridPlugin from "@fullcalendar/resource-daygrid" // premium
import resourceTimeGridPlugin from "@fullcalendar/resource-timegrid" // premium
import resourceTimelinePlugin from "@fullcalendar/resource-timeline" // premium
import timeGridPlugin from "@fullcalendar/timegrid"
import timelinePlugin from "@fullcalendar/timeline" // premium

import { EventApi, EventChangeArg, EventClickArg } from "@fullcalendar/core"
import FullCalendar from "@fullcalendar/react"
import { ReactNode } from "react"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import styled from "styled-components"
import "./Calendar.css"

interface State {
  dateClick: any
  eventClick: any
  eventChange: any
  eventsSet: any
}

const FullCalendarWrapper = styled.div<{ $customCSS?: string }>`
  ${(props) => props.$customCSS}
`
class Calendar extends StreamlitComponentBase<State> {
  public render = (): ReactNode => {
    const events = this.props.args["events"]
    const options = this.props.args["options"]
    const customCSS = this.props.args["custom_css"]
    const callbacks = this.props.args["callbacks"]
    const licenseKey = this.props.args["license_key"]

    const plugins = [
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
    ]

    return (
      <FullCalendarWrapper $customCSS={customCSS}>
        <FullCalendar
          plugins={plugins}
          initialEvents={events}
          schedulerLicenseKey={licenseKey}
          dateClick={
            callbacks.includes("dateClick") ? this.handleDateClick : null
          }
          eventClick={
            callbacks.includes("eventClick") ? this.handleEventClick : null
          }
          eventChange={
            callbacks.includes("eventChange") ? this.handleEventChange : null
          }
          eventsSet={
            callbacks.includes("eventsSet") ? this.handleEventsSet : null
          }
          {...options}
        />
      </FullCalendarWrapper>
    )
  }

  private handleDateClick = (arg: any) => {
    this.setState(
      (prevState) => ({
        dateClick: JSON.parse(JSON.stringify(arg)),
        eventClick: null,
        eventChange: null,
        eventsSet: null,
      }),
      () => Streamlit.setComponentValue(this.state)
    )
  }

  private handleEventClick = (arg: EventClickArg) => {
    this.setState(
      (prevState) => ({
        eventClick: JSON.parse(JSON.stringify(arg)),
        dateClick: null,
        eventChange: null,
        eventsSet: null,
      }),
      () => Streamlit.setComponentValue(this.state)
    )
  }

  private handleEventChange = (arg: EventChangeArg) => {
    this.setState(
      (prevState) => ({
        eventChange: JSON.parse(JSON.stringify(arg)),
        dateClick: null,
        eventClick: null,
      }),
      () => Streamlit.setComponentValue(this.state)
    )
  }

  private handleEventsSet = (events: EventApi[]) => {
    const eventsWithResource = events.map((e) => {
      return {
        ...JSON.parse(JSON.stringify(e)),
        resourceId: e.getResources()[0]?.id,
      }
    })

    this.setState(
      (prevState) => ({
        eventsSet: eventsWithResource,
        dateClick: null,
        eventClick: null,
      }),
      () => Streamlit.setComponentValue(this.state)
    )
  }
}

export default withStreamlitConnection(Calendar)
