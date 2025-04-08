import React from 'react'
import '../../css/Card.css'

const Card = ({ title, img, time, location, description, details, price }) => {
  return (
    <div className="card">
      <div className="card-image-container">
        <img src={img} alt={title} className="card-image" />
      </div>
      <div className="card-content">
        <div className="card-header">
          <h3 className="card-title">{title}</h3>
          <span className="card-price">{price}</span>
        </div>

        <div className="card-time-location">
          <p className="card-time">{time}</p>
          <p className="card-location">{location}</p>
        </div>

        <p className="card-description">{description}</p>

        <ul className="card-details">
          {details.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>

        <button className="card-button">Запишитесь</button>
      </div>
    </div>
  )
}

export default Card
