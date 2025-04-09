import React, { useContext, useState } from 'react'
import styles from './CardSection.module.css'
import OurEventsContext from '../../../app/OurEvents/OurEventsContext'
import card1 from '../../../assets/images/Card1.png'
import card2 from '../../../assets/images/Card2.png'
import card3 from '../../../assets/images/Card3.png'
import ModalWin from '../../widgets/ModalWin'

function formatDateToHuman(inputDateTime) {
  const date = new Date(inputDateTime)

  const days = ['вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб']
  const months = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
  ]

  const day = date.getDate()
  const month = months[date.getMonth()]
  const weekday = days[date.getDay()]

  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')

  const endHours = (date.getHours() + 2).toString().padStart(2, '0')

  return `${day} ${month} (${weekday}) ${hours}:${minutes}-${endHours}:${minutes}`
}

const CardsSection = () => {
  const { data } = useContext(OurEventsContext)

  const [activeCardId, setActiveCardId] = useState(null)
  const [DialogOpen, setDialogOpen] = useState(false)
  const [CurrentCard, setCurrentCard] = useState(null)

  const openDialog = (card) => {
    setCurrentCard(card)
    setDialogOpen(true)
  }

  const closeDialog = () => {
    setDialogOpen(false)
    setCurrentCard(null)
  }

  const toggleCard = (id) => {
    setActiveCardId(activeCardId === id ? null : id)
  }
  const img_cards = [card1, card2, card3]

  data.forEach((item, index) => {
    item.image = img_cards[index]
  })

  return (
    <section className={styles.section}>
      {DialogOpen && CurrentCard && (
        <ModalWin closeDialog={closeDialog} currentCard={CurrentCard} />
      )}
      <div className={styles.container}>
        {data.map((card) => (
          <div key={card.id} className={styles.card}>
            <h2 className={styles.title}>{card.name}</h2>
            <div className={styles.cardInner}>
              {activeCardId === card.id ? (
                <div
                  className={styles.cardBack}
                  onClick={() => toggleCard(card.id)}
                >
                  <div className={styles.cardContent}>
                    <p className={styles.description}>{card.description}</p>
                    <p className={styles.description}>{card.details}</p>
                  </div>
                </div>
              ) : (
                <div
                  className={styles.cardFront}
                  onClick={() => toggleCard(card.id)}
                >
                  <img
                    src={card.image}
                    alt={card.name}
                    className={styles.cardImage}
                  />
                </div>
              )}

              <div className={styles.contentUnderCard}>
                <p className={styles.datetime}>
                  {formatDateToHuman(card.datetime)}
                </p>
                <div className={styles.priceTag}>{card.cost} р.</div>
                <button
                  className={styles.button}
                  onClick={() => openDialog(card)}
                >
                  Запишитесь
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default CardsSection
