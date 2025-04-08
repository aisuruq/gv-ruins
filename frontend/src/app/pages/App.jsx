import React from 'react'
import '../../css/Nav.css'
import '../../css/fonts.css'
import MainSection from '../../components/sections/MainSection'
import AboutSection from '../../components/sections/AboutSection'
import CardsSection from '../../components/sections/CardsSection'
import OurEventsProvider from '../OurEvents/OurEventsProvider'

const App = () => {
  return (
    <section className="app-container">
      <MainSection />
      <main className="main-content">
        <AboutSection />
        <OurEventsProvider>
          <CardsSection />
        </OurEventsProvider>
      </main>
    </section>
  )
}

export default App
