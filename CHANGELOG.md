# Changelog

All notable changes to this project will be documented in this file. See
[Conventional Commits](https://conventionalcommits.org) for commit guidelines.

## [1.4.0](https://github.com/im-perativa/streamlit-calendar/compare/v1.3.2...v1.4.0) (2025-07-24)


### Features

* add support for eventMouseEnter callback ([#62](https://github.com/im-perativa/streamlit-calendar/issues/62)) ([be8328e](https://github.com/im-perativa/streamlit-calendar/commit/be8328e08a3f1be91795a5205887a8a09ab377be)), closes [#60](https://github.com/im-perativa/streamlit-calendar/issues/60)

## [1.3.2](https://github.com/im-perativa/streamlit-calendar/compare/v1.3.1...v1.3.2) (2025-07-19)


### Bug Fixes

* change initialEvents to events prop in FullCalendar component ([#61](https://github.com/im-perativa/streamlit-calendar/issues/61)) ([14978a9](https://github.com/im-perativa/streamlit-calendar/commit/14978a939aa378a3fa249579d186fc07096ae47b))

## [1.3.1](https://github.com/im-perativa/streamlit-calendar/compare/v1.3.0...v1.3.1) (2025-05-07)


### Bug Fixes

* include missing build artifact ([45cf68c](https://github.com/im-perativa/streamlit-calendar/commit/45cf68c4a3c82812314bdcffe1eb0ffa62f38ff0))
* poetry ([9f407c9](https://github.com/im-perativa/streamlit-calendar/commit/9f407c95caf7bc89259d43979d9a83f087c5cedd))

## [1.3.0](https://github.com/im-perativa/streamlit-calendar/compare/v1.2.1...v1.3.0) (2025-05-05)


### Features

* add view in eventset and eventchange callback ([e78229c](https://github.com/im-perativa/streamlit-calendar/commit/e78229c089d1cf086b001aadde61018a6fa03bc7))

## [1.2.1](https://github.com/im-perativa/streamlit-calendar/compare/v1.2.0...v1.2.1) (2024-12-14)


### Bug Fixes

* add resource id in callback ([#42](https://github.com/im-perativa/streamlit-calendar/issues/42)) ([9337e0c](https://github.com/im-perativa/streamlit-calendar/commit/9337e0ca19c800006aa1a672a8b9e692115b6573))

## [1.2.0](https://github.com/im-perativa/streamlit-calendar/compare/v1.1.0...v1.2.0) (2024-03-29)


### Features

* support recurring events with rrule plugin ([#29](https://github.com/im-perativa/streamlit-calendar/issues/29)) ([d9f1065](https://github.com/im-perativa/streamlit-calendar/commit/d9f1065319dccaacfc73b3458f94f8fbeb63d0e5))

## [1.1.0](https://github.com/im-perativa/streamlit-calendar/compare/v1.0.1...v1.1.0) (2023-12-21)


### Features

* implement fullcalendar 'select' callback ([#23](https://github.com/im-perativa/streamlit-calendar/issues/23)) ([7531e70](https://github.com/im-perativa/streamlit-calendar/commit/7531e70a8197868a64169c49b4d2d68c0b0d450f))

## [1.0.1](https://github.com/im-perativa/streamlit-calendar/compare/v1.0.0...v1.0.1) (2023-12-18)


### Bug Fixes

* **deps:** update fullcalendar monorepo to v6.1.10 ([f0a5a0e](https://github.com/im-perativa/streamlit-calendar/commit/f0a5a0e5f3f2b7c7756a182490dd1f43499c940b))

## [1.0.0](https://github.com/im-perativa/streamlit-calendar/compare/v0.7.0...v1.0.0) (2023-12-15)


### ⚠ BREAKING CHANGES

* **frontend:** some exposed properties will no longer be available

### Features

* **frontend:** component value payload improvements ([5abf62d](https://github.com/im-perativa/streamlit-calendar/commit/5abf62d1e93588b939e487056dcae33df92a1923))


### Bug Fixes

* **frontend:** add missing `resourceId` payload from `handleEventsSet` callback ([360dadb](https://github.com/im-perativa/streamlit-calendar/commit/360dadbe9f913f63341cf5993c700c7a34df5aad))
* **frontend:** refactor incorrect props ([b46b5ae](https://github.com/im-perativa/streamlit-calendar/commit/b46b5aeeaf61c882aa03edca90f35ca89f10d4e4))

## [0.7.0](https://github.com/im-perativa/streamlit-calendar/compare/v0.6.0...v0.7.0) (2023-11-23)


### Features

* add enabled callback configuration ([a8de8c9](https://github.com/im-perativa/streamlit-calendar/commit/a8de8c944eff6895711a443cd1385e3d81914a0e))

## [0.6.0](https://github.com/im-perativa/streamlit-calendar/compare/v0.5.0...v0.6.0) (2023-10-07)


### Features

* add css override ([df4a49a](https://github.com/im-perativa/streamlit-calendar/commit/df4a49abc6c02603a4f49714389ec24259dd1ef9))

## [0.5.0](https://github.com/im-perativa/streamlit-calendar/compare/v0.4.0...v0.5.0) (2023-08-30)


### Features

* update demo ([72eb8f0](https://github.com/im-perativa/streamlit-calendar/commit/72eb8f0ec8166abafd23fd404fbdcc024a89ccf2))


### Bug Fixes

* eventsSet result not returning resource id ([7bb8cc4](https://github.com/im-perativa/streamlit-calendar/commit/7bb8cc43d48e894a44b77f414c21e6c889d49af1)), closes [#2](https://github.com/im-perativa/streamlit-calendar/issues/2)
* **style:** prevent overlap hover background color ([7e9df8b](https://github.com/im-perativa/streamlit-calendar/commit/7e9df8b6f8f257818d76dbbeab84b0f9b4fc7349))

## [0.4.0](https://github.com/im-perativa/streamlit-calendar/compare/v0.3.0...v0.4.0) (2023-08-05)


### Features

* add eventChange and eventsSet callback support ([b19e498](https://github.com/im-perativa/streamlit-calendar/commit/b19e4989d3dc5da178e3de4ed1ef1a202882b2de))
