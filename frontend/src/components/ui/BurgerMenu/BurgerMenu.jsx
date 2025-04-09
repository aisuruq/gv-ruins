import { useState } from 'react'
import styles from './BurgerMenu.module.css'

const BurgerMenu = () => {
  const [isOpen, setIsOpen] = useState(false)

  const toggleMenu = () => {
    setIsOpen(!isOpen)
  }

  return (
    <div className={styles.wrapper}>
      <button className={styles.burger} onClick={toggleMenu}>
        <span />
        <span />
        <span />
      </button>

      {isOpen && (
        <nav className={styles.menu}>
          <ul>
            <li>
              <a href="#">Главная</a>
            </li>
            <li>
              <a href="#">О нас</a>
            </li>
            <li>
              <a href="#">Контакты</a>
            </li>
          </ul>
        </nav>
      )}
    </div>
  )
}

export default BurgerMenu
