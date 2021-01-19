import React, { useState, useEffect } from 'react'

import { predict } from '../components/API'

function toPercent (n) {
  return `${Math.round(n * 100)}%`
}

function Prediction () {
  const [text, setText] = useState('')
  const [prediction, setPrediction] = useState('')
  const [man, setMan] = useState('')
  const [woman, setWoman] = useState('')
  const [toggle, setToggle] = useState(false)

  useEffect(() => {
    predict(text, toggle).then((result) => {
      setPrediction(result.probability.M > result.probability.F ? 'mann' : 'kvinne')
      setMan(toPercent(result.probability.M))
      setWoman(toPercent(result.probability.F))
    })
  }, [text, toggle])

  if (text === '') {
    document.body.style.backgroundColor = '#171520'
    return (
      <div className='prediction'>
        <textarea onChange={(e) => setText(e.target.value)} />
        <div className='toggleContainer'>
          <h4>Select model</h4>
          <p title='Naive Bayes'>Bayes</p>
          <label className='toggle'>
            <input type='checkbox' checked={toggle} onChange={(i) => setToggle(i.target.checked)} />
            <span className='slider' />
          </label>
          <p title='Recurrent Neural Network'>RNN</p>
        </div>
        <h3>🤖 Maskinen gjetter 🤖</h3>
        <p>ingenting... <i>foreløpig</i> 👀</p>
      </div>
    )
  }

  if (prediction === 'mann') {
    document.body.style.backgroundColor = '#2C77FF'
  } else if (prediction === 'kvinne') {
    document.body.style.backgroundColor = 'lightcoral'
  }

  return (
    <div className='prediction'>
      <textarea onChange={(e) => setText(e.target.value)} />
      <div className='toggleContainer'>
        <p title='Naive Bayes'>Bayes</p>
        <label className='toggle'>
          <input type='checkbox' checked={toggle} onChange={(i) => setToggle(i.target.checked)} />
          <span className='slider' />
        </label>
        <p title='Recurrent Neural Network'>RNN</p>
      </div>
      <h3>🤖 Maskinen gjetter 🤖</h3>
      <p>Du er sannsynligvis en <b>{prediction}</b></p>
      <br />
      <p>Sannsynlighet for mann: {man}</p>
      <p>Sannsynlighet for kvinne: {woman}</p>
    </div>
  )
}

export default Prediction
