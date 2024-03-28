export type ViewValue = {
  type: string
  title: string
  activeStart: string
  activeEnd: string
  currentStart: string
  currentEnd: string
}

export type ResourceValue = {
  id?: string
  title?: string
  eventBackgroundColor?: string
  eventBorderColor?: string
  eventTextColor?: string
  eventClassNames?: string[]
  extendedProps?: Record<string, unknown>
}

export type EventValue = {
  allDay?: boolean
  id?: string
  title?: string
  start?: string
  end?: string
  groupId?: string
  url?: string
  display?:
    | "auto"
    | "block"
    | "list-item"
    | "background"
    | "inverse-background"
    | "none"
  backgroundColor?: string
  borderColor?: string
  textColor?: string
  classNames?: string[]
  extendedProps?: Record<string, unknown>
  resourceId?: string
}

export type DateClickValue = {
  allDay: boolean
  date: string
  view: ViewValue
  resource?: ResourceValue
}

export type EventClickValue = {
  event: EventValue
  view: ViewValue
}

export type EventChangeValue = {
  oldEvent: EventValue
  event: EventValue
  relatedEvents: EventValue[]
}

export type EventsSetValue = {
  events: EventValue[]
}

export type SelectValue = {
  allDay: boolean
  start: string;
  end: string;
  view: ViewValue
  resource?: ResourceValue
}

export type DateClickComponentValue = {
  callback: "dateClick"
  dateClick: DateClickValue
}

export type EventClickComponentValue = {
  callback: "eventClick"
  eventClick: EventClickValue
}

export type EventChangeComponentValue = {
  callback: "eventChange"
  eventChange: EventChangeValue
}

export type EventsSetComponentValue = {
  callback: "eventsSet"
  eventsSet: EventsSetValue
}

export type SelectComponentValue = {
  callback: "select"
  select: SelectValue
}

export type ComponentValue =
  | DateClickComponentValue
  | EventClickComponentValue
  | EventChangeComponentValue
  | EventsSetComponentValue
  | SelectComponentValue

export type Callback = ComponentValue["callback"]
