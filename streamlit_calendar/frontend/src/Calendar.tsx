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

interface State {
  dateClick: any
  eventClick: any
}

class Calendar extends StreamlitComponentBase<State> {
  public render = (): ReactNode => {
    const events = this.props.args["events"]
    const options = this.props.args["options"]

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
        events={events}
        schedulerLicenseKey="CC-Attribution-NonCommercial-NoDerivatives"
        {...options}
        dateClick={this.handleDateClick}
        eventClick={this.handleEventClick}
      />
    )
  }

  private handleDateClick = (arg: any) => {
    this.setState(
      (prevState) => ({ dateClick: JSON.parse(JSON.stringify(arg)) }),
      () => Streamlit.setComponentValue(this.state)
    )
  }

  private handleEventClick = (arg: any) => {
    this.setState(
      (prevState) => ({ eventClick: JSON.parse(JSON.stringify(arg)) }),
      () => Streamlit.setComponentValue(this.state)
    )
  }
}

export default withStreamlitConnection(Calendar)
