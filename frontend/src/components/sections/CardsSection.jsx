import React, { useContext } from 'react'
import '../../css/CardsSection.css'
import OurEventsContext from '../../app/OurEvents/OurEventsContext'

const CardsSection = () => {
  const { data } = useContext(OurEventsContext)

  // const img_cards = [
  //   '../../assets/images/Card1.png',
  //   '../../assets/images/Card2.png',
  //   '../../assets/images/Card3.png',
  // ]

  return (
    <section className="cards-section">
      <div className="cards-container">
        {data.map((card) => (
          <div key={card.id} className="card-item">
            <h2 className="card-category">{card.name}</h2>
            <div className="flip-card">
              <div className="flip-card-inner">
                <div className="flip-card-front">
                  <img src="" alt={card.name} className="card-image" />
                  <div className="price-tag">{card.cost}</div>
                </div>
                <div className="flip-card-back">
                  <div className="card-content">
                    <h3>{card.title}</h3>
                    <p className="datetime">{card.datetime}</p>
                    <p className="route">{card.route}</p>
                    <p className="description">{card.description}</p>
                    <p className="description">{card.details}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default CardsSection
