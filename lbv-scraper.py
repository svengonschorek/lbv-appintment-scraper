import os, requests, sched, time, pymsteams


from bs4 import BeautifulSoup
from datetime import datetime, date

from dotenv import load_dotenv

load_dotenv()

# Load env variables
teams_hook = os.getenv('teams_hook')

vorname=os.getenv('vorname')
nachname=os.getenv('nachname')
email=os.getenv('email')
fin=os.getenv('fin')
kennzeichen_ort=os.getenv('kennzeichen_ort')
kennzeichen_buchstaben=os.getenv('kennzeichen_buchstaben')
kennzeichen_ziffern=os.getenv('kennzeichen_ziffern')
strasse=os.getenv('strasse')
hausnr=os.getenv('hausnr')
plz=os.getenv('plz')
ort=os.getenv('ort')

cookie = os.getenv('cookie')

def sent_to_teams(lbv_date):

    if lbv_date == date.fromisoformat('2023-09-22'):
        teams_channel = '{}'.format(teams_hook)
        teams_notification = pymsteams.connectorcard(teams_channel)

        teams_notification.title("Neuer passender Termin beim LBV!")
        teams_notification.text("Der Termin ist frei am: {}". format(lbv_date))
        teams_notification.send()

def scrape_lbv(scheduler):
    scheduler.enter(60, 1, scrape_lbv, (scheduler,))

    url = 'https://lbv-termine.de/frontend/standortauswahl.php'

    form_data = {
        'vorname': '{}'.format(vorname),
        'nachname': '{}'.format(nachname),
        'email': '{}'.format(email),
        'fin': '{}'.format(fin),
        'kennzeichen_ort': '{}'.format(kennzeichen_ort),
        'kennzeichen_buchstaben': '{}'.format(kennzeichen_buchstaben),
        'kennzeichen_ziffern': '{}'.format(kennzeichen_ziffern),
        'strasse': '{}'.format(strasse),
        'hausnr': '{}'.format(hausnr),
        'plz': '{}'.format(plz),
        'ort': '{}'.format(ort),
        'mecheckbox': 1
    }

    cookies = {"ZMS-LBV_Webinterface":"{}".format(cookie)}

    page = requests.get(url, data=form_data, cookies=cookies)
    soup = BeautifulSoup(page.content, 'html.parser')

    all_appointments = soup.find_all('div', attrs={'class': 'card-body', 'class':'clear-both'})

    appointments = []
    for i in all_appointments:
        if "verfügbar ab" in str(i):
            ds = i.text.split()[2]
            appointments.append(datetime.strptime(ds, '%d.%m.%Y').date())
    now = datetime.now()

    print('{dt} - Next Appointment: {na}'.format(dt=now.strftime("%d/%m/%Y %H:%M:%S"), na=min(appointments)))
    sent_to_teams(min(appointments))


if __name__ == '__main__':
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(60, 1, scrape_lbv, (my_scheduler,))
    my_scheduler.run()
