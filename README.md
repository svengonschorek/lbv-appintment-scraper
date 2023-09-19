# lbv-appintment-scraper
Python script to scrape data from LBV in Hamburg, Germany

## Getting started

Prerequisites:
- Python installed (version 3.11 currenly not working)

To setup the service locally, the following steps have to be executed:

<b>1 - Create virtual environment</b><br />
To do this, open a terminal and go to this directory. Then execute: `python -m venv venv`<br />
Afterwards activate the environment using `.\venv\Scripts\activate`

<b>2 - Install dependencies</b><br />
The required dependencies are saved in the requirements.txt file.<br />
To install the dependencies execute `pip install -r requirements.txt`

<b>3 - Set environment variables</b><br />
To set the environment variables, create a `.env` file. In this file the following variables have to be set:<br />

- vorname
- nachname
- email
- fin
- kennzeichen_ort
- kennzeichen_buchstaben
- kennzeichen_ziffern
- strasse
- hausnr
- plz
- ort
- cookie
- teams_hook
