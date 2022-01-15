<div align="center">
    <h1>🤵 Mann eller Kvinne? 💃</h1>
    <p>A website that guesses whether you're a man or a woman based on what you type</p>
    <img src="https://raw.githubusercontent.com/LBlend/mann-eller-kvinne/main/.static/mann-eller-kvinne.png?token=AF55TQTQ2EPX6JP33MO4NLK73QQZG">
</div>

<a href="README.md">🇳🇴 Norsk</a>

_This repo is the backend for the mann-eller-kvinne project. You can find the repo for the fontend by clicking [this link](https://github.com/LBlend/mann-eller-kvinne-frontend)._

The website makes a guess by using simple machine learning algorithms.
The model is trained on 3000+ book reviews featured in norwegian media and its goal is to highlight the difference between men and women in the way they write.

The concept of this website is inspired by a controversy in Norway. This controversy stemmed from a criminal offense case where threatning letters had been sent. There was discussion about whether or not the letters were written by a man or a woman due to the letter using the word "tisse" instead of "pisse". You can read more about the case [here](https://www.nrk.no/kultur/uenige-om-bruken-av-ordet-_tisse_-1.15206839)

You're welcome to contribute if you feel like there's something missing or if there's something that can be improved. If have any expreience with machine learning we highly appreaciate any contributions.
Before contributing though, check out the [contribution guide](CONTRIBUTING-en.md). If you know React or have any experience with web development and want to contribute to the frontend, head over to its repo.

## A quick note

This website's purpose is to discover the difference between men and women in their writing.
It should be noted though that the models that are used to make predictions are not optimized and are trained on a fairly small dataset.
In other words, you should think critically about the results. This project's is not meant for any serious purpose or reasearch.

## Get started

<details>
  <summary>Docker</summary>
    
1. Run the webapp

```
docker run -d -p 5000:5000 --name mann-eller-kvinne-backend ghcr.io/lblend/mann-eller-kvinne:latest
```

You are free to change the variables as you desire.

</details>

<details>
  <summary>Manual</summary>

0. Clone this repo and install the dependencies

- Python 3.10+
- Pip

1. Run the build/installation script
   `sh build.sh`

_Note that this script assumes that you have set `python3` as the PATH to your Python installation. If this isn't the case, you have to modify the script or change your path accordingly._

2. Run the API
   ```
   uvicorn src.main:app --host 0.0.0.0 --port 5000 --proxy-headers
   ```

</details>

## Thank you

We want to thank [LtgOslo](https://www.mn.uio.no/ifi/english/research/groups/ltg/) for making the corpus/dataset that is used to train the machine learning model.

You can find the source for this corpus [here](https://github.com/ltgoslo/norec_gender)

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
