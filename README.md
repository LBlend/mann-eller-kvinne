<div align="center">
    <h1>🤵 Mann eller Kvinne? 💃</h1>
    <p>En nettside som gjetter om du er mann eller kvinne basert på hva du skriver</p>
    <img src="https://raw.githubusercontent.com/LBlend/mann-eller-kvinne/main/.static/mann-eller-kvinne.png?token=AF55TQTQ2EPX6JP33MO4NLK73QQZG">
    

<a href="README-en.md">English</a>
</div>

Nettsida gjetter om du er mann eller kvinne ved bruk av enkel maskinlæring.
Maskinlæringsmodellen er trent på over 3000 anmeldelser fra norsk media og har som formål å finne ut av hva som skiller kvinner og menn skriftlig.


Konseptet er inspirert av debatten som oppstod i Berteheussen-saken, hvor det skal ha blitt diskutert hvorvidt det er en mann som kan ha skrevet trusselbrevene som er omtalt. Dette på grunn av at ordet "tisse" ble brukt fremfor ordet "pisse". Du kan lese mer om saken [her](https://www.nrk.no/kultur/uenige-om-bruken-av-ordet-_tisse_-1.15206839)


Om du mener at denne kan forbedres, kan du gjerne bidra. Kan du react eller har kunnskap om maskinlæring så er det bare å åpne opp din favoritteditor og hive seg på!
Sjekk [bidragsguiden](CONTRIBUTING.md)

## En liten kommentar

Denne nettsiden er laget for å utforske forskjellene mellom menn og kvinner.
Det skal derimot sies at modellen som er brukt for å gjøre antagelser er lite optimert og er basert på en ganske liten mengde data.
Man skal dermed ikke ta denne så seriøst. Dette er bare et prosjekt laget for morrohetens skyld og er ikke ment for bruk til forskning eller andre seriøse formål.

## Kjør selv

<details>
  <summary>Docker</summary>
    
1. Gjør om navnet på `.env.example` filene i [frontend](frontend)- og [backend](backend) mappa til `.env` og erstatt verdiene med dine egne

#### ⚠️ Angående porter ⚠️
For å unngå problemer er det viktig at portene i `.env` filene, [docker-compose.yml](docker-compose.yml) filen og `dockerfile` i både frontend og backend samsvarer. Hvis du ikke vet hva du skal gjøre, unngå å endre porter om mulig. Dette er en rar løsning, men vi vil forbedre spesifisering av porter for Docker i fremtiden.

2. Bygg docker-bildene og kjør dem. Det er ulike måter å gå fram på her, men det anbefales å bruke docker-compose

```
docker-compose up
```

</details>

<details>
  <summary>Manuelt</summary>

0. Last ned repoet og installer avhengigheter

- node.js
- npm
- python3
- pip

#### Backend

1. Kjør build-scriptet for backend fra /backend mappa
   ```
   sh build_model.sh
   ```

2. Endre navnet på [.env.example](backend/.env.example) til `.env` og erstatt verdiene med dine egne

3. Kjør API-et med Python
   ```
   python3 src/api.py
   ```

#### Frontend

1. Installer avhengigheter for frontend  
   ```
   npm i
   ```

2. Endre navnet på [.env.example](frontend/.env.example) til `.env` og erstatt verdiene med dine egne

3. Kjør websiden med Node
   ```
   npm start
   ```

</details>

## Takk

Takk til [LtgOslo](https://www.mn.uio.no/ifi/english/research/groups/ltg/) som har laget det taggede korpuset, datasettet, som er brukt til å trene maskinlæringsmodellen.

Du kan finne korpuset som er brukt [her](https://github.com/ltgoslo/norec_gender)

```
@inproceedings{touileb-etal-2020-gender,
    title = "Gender and sentiment, critics and authors: a dataset of {N}orwegian book reviews",
    author = "Touileb, Samia and {\O}vrelid, Lilja and Velldal, Erik",
    booktitle = "Proceedings of the Second Workshop on Gender Bias in Natural Language Processing",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.gebnlp-1.11",
    pages = "125--138"
}
```

## Lisens

[GNU GPLv3](LICENSE)
