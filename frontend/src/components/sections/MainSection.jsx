import React from 'react'
import FON from '../../assets/images/fon.jpg'
import '../../css/Head.css'
import Nav from '../ui/Nav'
const MainSection = () => {
  return (
    <header className="header">
      <Nav />
      <div className="background-container">
        <img src={FON} alt="Фоновое изображение" className="background-image" />
      </div>
      <div className="title-container">
        <h1 className="main-title">
          Загляни <br />в историю
        </h1>
      </div>
    </header>
  )
}

export default MainSection
