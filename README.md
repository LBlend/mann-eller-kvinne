<div align="center">
    <h1>🤵 Mann eller Kvinne? 💃</h1>
    <p>En nettside som gjetter om du er mann eller kvinne basert på hva du skriver</p>
    <img src="https://raw.githubusercontent.com/LBlend/mann-eller-kvinne/main/.static/mann-eller-kvinne.png?token=AF55TQTQ2EPX6JP33MO4NLK73QQZG">
</div>

Nettsida gjetter om du er mann eller kvinne ved bruk av enkel maskinlæring.
Maskinlæringsmodellen er trent på over 3000 anmeldelser fra norsk media og har som formål å finne ut av hva som skiller kvinner og menn skriftlig.

Om du mener at denne kan forbedres, kan du gjerne bidra. Kan du react eller har kunnskap om maskinlæring så er det bare å åpne opp din favoritteditor og hive seg på!
Sjekk [bidragsguiden](CONTRIBUTING.md)

## En liten kommentar

Denne nettsiden er laget for å utforske forskjellene mellom menn og kvinner.
Det skal derimot sies at modellen som er brukt for å gjøre antagelser er lite optimert og er basert på en ganske liten mengde data.
Man skal dermed ikke ta denne så seriøst. Dette er bare et prosjekt laget for morrohetens skyld og er ikke ment for bruk til forskning eller andre seriøse formål.

## Kjør selv

<details>
  <summary>Docker</summary>

Det er ulike måter å gå fram på her, men det anbefales å bruke docker-compose

`docker-compose up`

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
   `sh build_model.sh`

2. Kjør API-et med Python
   `python3 src/api.py`

#### Frontend

1. Installer avhengigheter for frontend  
   `npm i`

2. Kjør websiden med Node
   `npm start`

</details>

## Takk

Takk til [LtgOslo](https://www.mn.uio.no/ifi/english/research/groups/ltg/) som har laget det taggede korpuset, datasettet, som er brukt til å trene maskinlæringsmodellen.

Du kan finne korpuset som er brukt [her](https://github.com/ltgoslo/norec_gender)

```
@InProceedings{TouOvrVell20,
  author = {Samia Touileb and Lilja {\O}vrelid and Erik Velldal},
  title = {Gender and sentiment, critics and authors: a dataset of Norwegian book reviews},
  booktitle = {{Proceedings of the 2nd Workshop on Gender Bias in Natural Language Processing}},
  year = 2020
}
```

## Lisens

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
