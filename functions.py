import requests
import json
from io import StringIO
from datetime import date
import pandas as pd


TODAY = date.today().strftime("%d-%b-%Y")
TOKEN = "bda1701c2db22bbef579618483d1d9f4"

def forecast_15days ():
    urlsp = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token=" + TOKEN
    urlpa = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/5346/days/15?token=" + TOKEN
    urlct = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/6731/days/15?token=" + TOKEN
    urlrj = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/5959/days/15?token=" + TOKEN
    responsesp = requests.request("GET", urlsp)
    responsepa = requests.request("GET", urlpa)
    responsect = requests.request("GET", urlct)
    responserj = requests.request("GET", urlrj)

    id = 100
    ids = []
    city = []
    state = []
    date = []
    probability = []

    sp = json.loads(responsesp.text)
    pa = json.loads(responsepa.text)
    ct = json.loads(responsect.text)
    rj = json.loads(responserj.text)

    dataListSP = sp["data"]
    dataListPA = pa["data"]
    dataListCT = ct["data"]
    dataListRJ = rj["data"]

    for x in dataListSP:
        ids.append(id)
        city.append(sp["name"])
        state.append(sp["state"])
        date.append(x["date"])
        probability.append(x["rain"]["probability"])
        id += 10
    for x in dataListPA:
        ids.append(id)
        city.append(pa["name"])
        state.append(pa["state"])
        date.append(x["date"])
        probability.append(x["rain"]["probability"])
        id += 10
    for x in dataListCT:
        ids.append(id)
        city.append(ct["name"])
        state.append(ct["state"])
        date.append(x["date"])
        probability.append(x["rain"]["probability"])
        id += 10
    for x in dataListRJ:
        ids.append(id)
        city.append(rj["name"])
        state.append(rj["state"])
        date.append(x["date"])
        probability.append(x["rain"]["probability"])
        id += 10

    dict = {'id': ids, 'cidade': city, 'estado': state, 'data': date, 'probabilidade': probability}
    df = pd.DataFrame(dict)
    df.to_csv("previsao-cidades-2021.csv")
    #return response.text

def forecast_72hours (id):
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + id + "/hours/72?token=" + TOKEN

    response = requests.request("GET", url)

    return response.text

def forecast_3days_region (region):
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/region/" + region + "?token=" + TOKEN

    response = requests.request("GET", url)

    return response.text

def history_city ():
    #url = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/" + id + "?token="+ TOKEN + "-hist&from=" + init + "&to=" + end
    urlspjan = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/3477?token=" + TOKEN + "-hist&from=2021-01-01&to=2021-01-31"
    urlspfev = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/3477?token=" + TOKEN + "-hist&from=2021-02-01&to=2021-02-28"
    urlspmar = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/3477?token=" + TOKEN + "-hist&from=2021-03-01&to=2021-03-31"
    urlspabr = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/3477?token=" + TOKEN + "-hist&from=2021-04-01&to=2021-04-30"
    urlspmai = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/3477?token=" + TOKEN + "-hist&from=2021-05-01&to=2021-05-28"
    urlpajan = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5346?token=" + TOKEN + "-hist&from=2021-01-01&to=2021-01-31"
    urlpafev = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5346?token=" + TOKEN + "-hist&from=2021-02-01&to=2021-02-28"
    urlpamar = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5346?token=" + TOKEN + "-hist&from=2021-03-01&to=2021-03-31"
    urlpaabr = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5346?token=" + TOKEN + "-hist&from=2021-04-01&to=2021-04-30"
    urlpamai = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5346?token=" + TOKEN + "-hist&from=2021-05-01&to=2021-05-28"
    urlctjan = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/6731?token=" + TOKEN + "-hist&from=2021-01-01&to=2021-01-31"
    urlctfev = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/6731?token=" + TOKEN + "-hist&from=2021-02-01&to=2021-02-28"
    urlctmar = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/6731?token=" + TOKEN + "-hist&from=2021-03-01&to=2021-03-31"
    urlctabr = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/6731?token=" + TOKEN + "-hist&from=2021-04-01&to=2021-04-30"
    urlctmai = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/6731?token=" + TOKEN + "-hist&from=2021-05-01&to=2021-05-28"
    urlrjjan = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5959?token=" + TOKEN + "-hist&from=2021-01-01&to=2021-01-31"
    urlrjfev = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5959?token=" + TOKEN + "-hist&from=2021-02-01&to=2021-02-28"
    urlrjmar = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5959?token=" + TOKEN + "-hist&from=2021-03-01&to=2021-03-31"
    urlrjabr = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5959?token=" + TOKEN + "-hist&from=2021-04-01&to=2021-04-30"
    urlrjmai = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/5959?token=" + TOKEN + "-hist&from=2021-05-01&to=2021-05-28"
    responsespjan = requests.request("GET", urlspjan)
    responsespfev = requests.request("GET", urlspfev)
    responsespmar = requests.request("GET", urlspmar)
    responsespabr = requests.request("GET", urlspabr)
    responsespmai = requests.request("GET", urlspmai)
    responsepajan = requests.request("GET", urlpajan)
    responsepafev = requests.request("GET", urlpafev)
    responsepamar = requests.request("GET", urlpamar)
    responsepaabr = requests.request("GET", urlpaabr)
    responsepamai = requests.request("GET", urlpamai)
    responsectjan = requests.request("GET", urlctjan)
    responsectfev = requests.request("GET", urlctfev)
    responsectmar = requests.request("GET", urlctmar)
    responsectabr = requests.request("GET", urlctabr)
    responsectmai = requests.request("GET", urlctmai)
    responserjjan = requests.request("GET", urlrjjan)
    responserjfev = requests.request("GET", urlrjfev)
    responserjmar = requests.request("GET", urlrjmar)
    responserjabr = requests.request("GET", urlrjabr)
    responserjmai = requests.request("GET", urlrjmai)

    id = 1000
    ids = []
    city = []
    state = []
    date = []
    precipitation = []
    city1 = []
    state1 = []
    date1 = []
    precipitation1 = []
    city2 = []
    state2 = []
    date2 = []
    precipitation2 = []
    city3 = []
    state3 = []
    date3 = []
    precipitation3 = []
    city4 = []
    state4 = []
    date4 = []
    precipitation4 = []
    city5 = []
    state5 = []
    date5 = []
    precipitation5 = []
    spjan = json.loads(responsespjan.text)
    spfev = json.loads(responsespfev.text)
    spmar = json.loads(responsespmar.text)
    spabr = json.loads(responsespabr.text)
    spmai = json.loads(responsespmai.text)
    pajan = json.loads(responsepajan.text)
    pafev = json.loads(responsepafev.text)
    pamar = json.loads(responsepamar.text)
    paabr = json.loads(responsepaabr.text)
    pamai = json.loads(responsepamai.text)
    ctjan = json.loads(responsectjan.text)
    ctfev = json.loads(responsectfev.text)
    ctmar = json.loads(responsectmar.text)
    ctabr = json.loads(responsectabr.text)
    ctmai = json.loads(responsectmai.text)
    rjjan = json.loads(responserjjan.text)
    rjfev = json.loads(responserjfev.text)
    rjmar = json.loads(responserjmar.text)
    rjabr = json.loads(responserjabr.text)
    rjmai = json.loads(responserjmai.text)
    print (pamai)
    dataListSPJan = spjan["data"]
    dataListSPFev = spfev["data"]
    dataListSPMar = spmar["data"]
    dataListSPAbr = spabr["data"]
    dataListSPMai = spmai["data"]
    dataListPAJan = pajan["data"]
    dataListPAFev = pafev["data"]
    dataListPAMar = pamar["data"]
    dataListPAAbr = paabr["data"]
    dataListPAMai = pamai["data"]
    dataListCTJan = ctjan["data"]
    dataListCTFev = ctfev["data"]
    dataListCTMar = ctmar["data"]
    dataListCTAbr = ctabr["data"]
    dataListCTMai = ctmai["data"]
    dataListRJJan = rjjan["data"]
    dataListRJFev = rjfev["data"]
    dataListRJMar = rjmar["data"]
    dataListRJAbr = rjabr["data"]
    dataListRJMai = rjmai["data"]

    for x in dataListSPJan:
        ids.append(id)
        city1.append(spjan["name"])
        state1.append(spjan["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListSPFev:
        ids.append(id)
        city1.append(spfev["name"])
        state1.append(spfev["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListSPMar:
        ids.append(id)
        city1.append(spmar["name"])
        state1.append(spmar["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListSPAbr:
        ids.append(id)
        city1.append(spabr["name"])
        state1.append(spabr["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListSPMai:
        ids.append(id)
        city1.append(spmai["name"])
        state1.append(spmai["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListPAJan:
        ids.append(id)
        city1.append(pajan["name"])
        state1.append(pajan["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListPAFev:
        ids.append(id)
        city1.append(pafev["name"])
        state1.append(pafev["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListPAMar:
        ids.append(id)
        city1.append(pamar["name"])
        state1.append(pamar["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListPAAbr:
        ids.append(id)
        city1.append(paabr["name"])
        state1.append(paabr["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListPAMai:
        ids.append(id)
        city1.append(pamai["name"])
        state1.append(pamai["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListCTJan:
        ids.append(id)
        city1.append(ctjan["name"])
        state1.append(ctjan["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListCTFev:
        ids.append(id)
        city1.append(ctfev["name"])
        state1.append(ctfev["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListCTMar:
        ids.append(id)
        city1.append(ctmar["name"])
        state1.append(ctmar["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListCTAbr:
        ids.append(id)
        city1.append(ctabr["name"])
        state1.append(ctabr["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListCTMai:
        ids.append(id)
        city1.append(ctmai["name"])
        state1.append(ctmai["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListRJJan:
        ids.append(id)
        city1.append(rjjan["name"])
        state1.append(rjjan["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListRJFev:
        ids.append(id)
        city1.append(rjfev["name"])
        state1.append(rjfev["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListRJMar:
        ids.append(id)
        city1.append(rjmar["name"])
        state1.append(rjmar["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListRJAbr:
        ids.append(id)
        city1.append(rjabr["name"])
        state1.append(rjabr["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10
    for x in dataListRJMai:
        ids.append(id)
        city1.append(rjmai["name"])
        state1.append(rjmai["state"])
        date1.append(x["date"])
        precipitation1.append(x["rain"]["precipitation"])
        id += 10

    for x in city1:
        city.append(x)
    for x in city2:
        city.append(x)
    for x in city3:
        city.append(x)
    for x in city4:
        city.append(x)
    for x in city5:
        city.append(x)
    for x in state1:
        state.append(x)
    for x in state2:
        state.append(x)
    for x in state3:
        state.append(x)
    for x in state4:
        state.append(x)
    for x in state5:
        state.append(x)
    for x in date1:
        date.append(x)
    for x in date2:
        date.append(x)
    for x in date3:
        date.append(x)
    for x in date4:
        date.append(x)
    for x in date5:
        date.append(x)
    for x in precipitation1:
        precipitation.append(x)
    for x in precipitation2:
        precipitation.append(x)
    for x in precipitation3:
        precipitation.append(x)
    for x in precipitation4:
        precipitation.append(x)
    for x in precipitation5:
        precipitation.append(x)

    dict = {'id': ids, 'cidade': city, 'estado': state, 'data': date, 'precipitacao': precipitation}
    df = pd.DataFrame(dict)
    df.to_csv("historico-cidades-2021.csv")

def lightning_history_localeid (localeId, init, end, outputFormat):
    url = "http://apiadvisor.climatempo.com.br/api/v1/lightning/strikes?token=" + TOKEN + "-light&from=" + init + "&to=" + end + "&localeId=" + localeId + "&outputFormat=" + outputFormat

    response = requests.request("GET", url)

    return response.text

def lightning_history_coordinates (latitude, longitude, radius, init, end, outputFormat):
    url = "http://apiadvisor.climatempo.com.br/api/v1/lightning/strikes?token=" + TOKEN + "-light&from=" + init + "&to=" + end + "&latitude=" + latitude + "&longitude=" + longitude + "&radius=" + radius + "&outputFormat=" + outputFormat

    response = requests.request("GET", url)
    return response.text

def lightning_geometry_localeid (localeId, init, end):
    url = "http://apiadvisor.climatempo.com.br/api/v1/lightning/strikes?token=" + TOKEN + "-light&from=" + init + "&to=" + end + "&localeId=" + localeId

    response = requests.request("GET", url)
    convert =  StringIO(response.text)
    result = [json.dumps(record) for record in json.load(convert)]
    return result

def flood_risk (latitude, longitude):
    url = "http://apiadvisor.climatempo.com.br/api/v1/flood/risk?token=" + TOKEN + "-flood&latitude=" + latitude + "&longitude=" + longitude

    response = requests.request("GET", url)

    return response.text

#print(lightning_geometry_localeid("3477", "2021-04-01", "2021-04-30"))
#print(flood_risk("-23.647066", "-46.63954"))
history_city()
#forecast_15days()