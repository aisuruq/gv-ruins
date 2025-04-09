import React, { useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import OurEventsContext from './OurEventsContext'

function OurEventsProvider({ children, query }) {
  const [loaded, setLoaded] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [data, setData] = useState([])

  useEffect(() => {
    fetch('/api/v1/events/list')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Ошибка при загрузке данных')
        }
        return response.json()
      })
      .then((data) => {
        setData(data)
        setLoading(false)
        setLoaded(true)
      })
      .catch((e) => {
        setError(e.message)
        setLoading(false)
      })
  }, [query])

  const contextValue = {
    loaded,
    loading,
    error,
    data,
  }

  return (
    <OurEventsContext.Provider value={contextValue}>
      {children}
    </OurEventsContext.Provider>
  )
}

OurEventsProvider.propTypes = {
  children: PropTypes.node,
  query: PropTypes.shape({
    type: PropTypes.string,
  }),
}

export default OurEventsProvider
