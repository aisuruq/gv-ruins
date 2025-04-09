import { createContext } from 'react'

const OurEventsContext = createContext({
  loading: false,
  loaded: false,
  data: [],
  error: null,
})

export default OurEventsContext
