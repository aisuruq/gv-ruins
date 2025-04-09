import React from 'react'
import photo from '../../assets/images/main.png'
import '../../css/Head.css'
import Nav from '../ui/Nav'
const MainSection = () => {
  return (
    <header className="header">
      <Nav />
      <div className="background-container">
        <img
          src={photo}
          alt="Фоновое изображение"
          className="background-image"
        />
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
