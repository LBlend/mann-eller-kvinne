import React from 'react';


function About() {
  return (
    <div>
      <nav>
        <a href='/'>Tilbake</a>
      </nav>
        <article>
            <h1>Om siden</h1>
            <img src='https://raw.githubusercontent.com/LBlend/mann-eller-kvinne/main/.static/mann-eller-kvinne.png?token=AF55TQTQ2EPX6JP33MO4NLK73QQZG' alt="Logo"></img>
            <p>Nettsida gjetter om du er mann eller kvinne ved bruk av enkel maskinlæring. Maskinlæringsmodellen er trent på over 3000 anmeldelser fra norsk media og har som formål å finne ut av hva som skiller kvinner og menn skriftlig.</p>
            <p>Konseptet er inspirert av debatten som oppstod i Berteheussen-saken, hvor det skal ha blitt diskutert hvorvidt det er en mann som kan ha skrevet trusselbrevene som er omtalt. Dette på grunn av at ordet "tisse" ble brukt fremfor ordet "pisse". Du kan lese mer om saken <a href='https://www.nrk.no/kultur/uenige-om-bruken-av-ordet-_tisse_-1.15206839'>her</a>.</p>
            <p>Om du mener at denne kan forbedres, kan du gjerne bidra. Kan du react eller har kunnskap om maskinlæring så er det bare å åpne opp din favoritteditor og hive seg på!</p>
            <p>Denne nettsiden er laget for å utforske forskjellene mellom menn og kvinner. Det skal derimot sies at modellen som er brukt for å gjøre antagelser er lite optimert og er basert på en ganske liten mengde data. Man skal dermed ikke ta denne så seriøst. Dette er bare et prosjekt laget for morrohetens skyld og er ikke ment for bruk til forskning eller andre seriøse formål.</p>
            <p>Takk til LtgOslo som har laget det taggede korpuset, datasettet, som er brukt til å trene maskinlæringsmodellen.</p>
        </article>
    </div>
  );
}

export default About;
