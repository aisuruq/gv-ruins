import React from 'react'
import card1 from '../../assets/images/Card1.png'
import card2 from '../../assets/images/Card2.png'
import card3 from '../../assets/images/Card3.png'
import '../../css/CardsSection.css'
// import OurEventsContext from '../../app/OurEvents/OurEventsContext'

const cardsData = [
  {
    category: 'Вагонка Ратсхов',
    title: 'Экскурсия по старому городу',
    img: card1,
    time: '6 апреля (вс) 11:00-13:00',
    location: 'Район Ратсхоф, город-сад в городе К.',
    description: 'Прогулка по историческому району',
    details: [
      'Район построен в начале ХХ века для рабочих завода Штайнфурт',
      'Посетим вагоностроительный завод',
      'В конце экскурсии по желанию выпьем кофе :)',
    ],
    price: '1000 руб',
  },
  {
    category: 'Почтовая история',
    title: 'Экскурсия по старому городу',
    img: card2,
    time: '23 марта (вс) 11:00-13:00',
    location: 'Район Ратсхоф • город-сад в городе К.',
    description:
      'Прогулка по району, построенному в начале XX века для рабочих завода Штайнфурт',
    details: [
      'Посетим вагоностроительный завод',
      'В конце экскурсии по желанию выпьем кофе :)',
    ],
    price: '1200 руб',
  },
  {
    category: 'Готическое кольцо',
    title: 'Экскурсия по старому городу',
    img: card3,
    time: '6 апреля (вс) 11:00–13:00',
    location: 'Район Ратсхоф • город-сад в городе К.',
    description:
      'Прогулка по району, построенному в начале XX века для рабочих завода Штайнфурт',
    details: [
      'Посетим вагоностроительный завод',
      'В конце экскурсии по желанию выпьем кофе :)',
    ],
    price: '1500 руб',
  },
]

const CardsSection = () => {
  // const { data } = useContext(OurEventsContext)

  return (
    <section className="cards-section">
      <div className="cards-container">
        {cardsData.map((card) => (
          <div key={card.id} className="card-item">
            <h2 className="card-category">{card.category}</h2>
            <div className="flip-card">
              <div className="flip-card-inner">
                <div className="flip-card-front">
                  <img src={card.img} alt={card.title} className="card-image" />
                  <div className="price-tag">{card.price}</div>
                </div>
                <div className="flip-card-back">
                  <div className="card-content">
                    <h3>{card.title}</h3>
                    <p className="time">{card.time}</p>
                    <p className="location">{card.location}</p>
                    <p className="description">{card.description}</p>
                    <ul className="details">
                      {card.details.map((detail, i) => (
                        <li key={i}>{detail}</li>
                      ))}
                    </ul>
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
