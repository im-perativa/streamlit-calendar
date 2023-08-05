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

import FullCalendar from "@fullcalendar/react"
import { ReactNode } from "react"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import "./Calendar.css"

interface State {
  dateClick: any
  eventClick: any
  eventChange: any
  eventsSet: any
}

class Calendar extends StreamlitComponentBase<State> {
  public render = (): ReactNode => {
    const events = this.props.args["events"]
    const options = this.props.args["options"]
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
      <FullCalendar
        plugins={plugins}
        initialEvents={events}
        schedulerLicenseKey={licenseKey}
        dateClick={this.handleDateClick}
        eventClick={this.handleEventClick}
        eventChange={this.handleEventChange}
        eventsSet={this.handleEventsSet}
        {...options}
      />
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

  private handleEventClick = (arg: any) => {
    this.setState(
      (prevState) => ({
        eventClick: JSON.parse(JSON.stringify(arg)),
        dateClick: null,
        eventChange: null,
        eventsSet: null,
      }),
      () => {
        Streamlit.setComponentValue(this.state)
      }
    )
  }

  private handleEventChange = (arg: any) => {
    this.setState(
      (prevState) => ({
        eventChange: JSON.parse(JSON.stringify(arg)),
        dateClick: null,
        eventClick: null,
      }),
      () => {
        Streamlit.setComponentValue(this.state)
      }
    )
  }

  private handleEventsSet = (arg: any) => {
    this.setState(
      (prevState) => ({
        eventsSet: JSON.parse(JSON.stringify(arg)),
        dateClick: null,
        eventClick: null,
      }),
      () => Streamlit.setComponentValue(this.state)
    )
  }
}

export default withStreamlitConnection(Calendar)
