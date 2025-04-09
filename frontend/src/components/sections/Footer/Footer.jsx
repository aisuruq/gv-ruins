import React from 'react'
import styles from './Footer.module.css'

const Footer = () => {
  return (
    <section className={styles.section}>
      <div className={styles.content}>
        <h2>Наши контакты</h2>
        <div className={styles.contact}>
          <p>г, Калининград</p>
          <p>tel:79527960392</p>
          <p>ruin.keepers</p>
          <p>@ruin_keepers</p>
        </div>
        <h2>Наши контакты</h2>
        <div className={styles.list}>
          <p>Изучаем и приводим в порядок исторические руины.</p>
          <p>Присоединяйтесь!</p>
        </div>
        <span className={styles.span}>2020-2025</span>
      </div>
    </section>
  )
}
export default Footer
