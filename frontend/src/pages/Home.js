import React from 'react';

import Prediction from '../components/Prediction';

function Home() {
  return (
    <div>
      <nav>
        <a href='/om'>Om siden</a>
      </nav>
      <main>
      <h1>🤵 Mann eller Kvinne? 💃</h1>
      <p>Skriv og la maskinen gjette om du er mann eller kvinne</p>
      <Prediction />
      </main>
    </div>
  );
}

export default Home;