import React from 'react'
import OurEventsProvider from './OurEventsProvider'

const TestPage = () => {
  return (
    <>
      <OurEventsProvider>
        <div>Наши мероприятия</div>
      </OurEventsProvider>
    </>
  )
}

export default TestPage
