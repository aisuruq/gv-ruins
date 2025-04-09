import React, { useState } from 'react'
import './MDW.css'

const ModalWin = ({ currentCard }) => {
  const prepayment = (currentCard.cost / 100) * 40

  const [formData, setFormData] = useState({
    name: '',
    surname: '',
    patronymic: '',
    phone: '',
    tg_username: '',
    comment: '',
    event_name: currentCard.name,
    event_id: currentCard.id,
    people_count: 0,
  })

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const fullPayload = {
      participants: {
        name: formData.name,
        surname: formData.surname,
        patronymic: formData.patronymic,
        phone: formData.phone,
        tg_username: formData.tg_username,
        comment: formData.comment,
        event_name: formData.event_name,
        event_id: formData.event_id,
        people_count: parseInt(formData.people_count),
        payment: currentCard.cost,
        prepayment: prepayment,
      },
      yokassa: {
        amount: parseInt(prepayment),
        description: currentCard.name,
      },
    }

    try {
      const response = await fetch('/api/v1/participants/register_and_pay', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(fullPayload),
      })

      if (!response.ok) {
        const errorText = await response.text()
        throw new Error('Ошибка регистрации и оплаты: ' + errorText)
      }

      const data = await response.json()
      console.log('Регистрация и платёж успешно:', data)

      if (data.payment_url) {
        window.location.href = data.payment_url
      } else {
        alert('Ошибка: не удалось получить ссылку на оплату')
      }
    } catch (error) {
      console.error(' Ошибка:', error)
      alert('Что-то пошло не так. Попробуйте ещё раз.')
    }
  }

  return (
    <dialog className="form-page" open>
      <h2>{currentCard.name}</h2>
      <div className="form-block">
        <form onSubmit={handleSubmit}>
          <div className="form-input">
            <input
              type="text"
              name="name"
              placeholder="Фамилия"
              required
              value={formData.name}
              onChange={handleInputChange}
            />
            <input
              type="text"
              name="surname"
              placeholder="Имя"
              required
              value={formData.surname}
              onChange={handleInputChange}
            />
            <input
              type="text"
              name="patronymic"
              placeholder="Отчество"
              value={formData.patronymic}
              onChange={handleInputChange}
            />
            <input
              type="tel"
              name="phone"
              placeholder="Телефон"
              required
              value={formData.phone}
              onChange={handleInputChange}
            />
            <input
              type="text"
              name="tg_username"
              placeholder="Телеграмм @aisuruq"
              required
              value={formData.tg_username}
              onChange={handleInputChange}
            />
            <input
              type="number"
              name="people_count"
              placeholder="Количество участников"
              required
              value={formData.people_count}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-comment">
            <textarea
              name="comment"
              placeholder="Ваш комментарий"
              value={formData.comment}
              onChange={handleInputChange}
            ></textarea>
          </div>
          <span>{prepayment}р. за одного участника</span>
          <input type="submit" value="Внести предоплату" />
        </form>
      </div>
    </dialog>
  )
}

export default ModalWin
