import React from 'react'
import logo from '../../assets/images/logo.png'
import '../../css/Nav.css'

const Nav = () => {
  return (
    <nav className="navbar">
      <div className="logo-container">
        <img src={logo} alt="Логотип" className="logo" />
      </div>
    </nav>
  )
}

export default Nav
