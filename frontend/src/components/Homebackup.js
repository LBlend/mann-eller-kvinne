import React from 'react'

function Home () {
  return (
    <div>
      <nav>
        <a href='/om'>Om siden</a>
      </nav>
      <main>
        <h1>🤵 Mann eller Kvinne? 💃</h1>
        <p>Skriv og la maskinen gjette om du er mann eller kvinne</p>
        <textarea />
        <div className='prediction'>
          <h3>🤖 Maskinen gjetter 🤖</h3>
          <p />
        </div>
      </main>
    </div>
  )
}

export default Home
