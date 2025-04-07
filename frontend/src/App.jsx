import { useContext } from 'react'
import './App.css'
import TestPage from './app/OurEvents/TestPage'
import OurEventsContext from './app/OurEvents/OurEventsContext'

function App() {
  const { data } = useContext(OurEventsContext)
  console.log(data)
  return (
    <>
      <TestPage />
    </>
  )
}

export default App
