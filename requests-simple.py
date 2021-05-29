import requests
from datetime import date
import pandas as pd

TODAY = date.today().strftime("%d-%b-%Y")
TOKEN = "bda1701c2db22bbef579618483d1d9f4"

# Previsão por cidade - 15 dias
def forecast_15days (id):
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + id + "/days/15?token=" + TOKEN

    response = requests.request("GET", url)

    return response.text

# Previsão por cidade - Próximas 72 horas
def forecast_72hours (id):
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + id + "/hours/72?token=" + TOKEN

    response = requests.request("GET", url)

    return response.text

# Previsão por região - Próximos 3 dias
def forecast_3days_region (region):
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/region/" + region + "?token=" + TOKEN

    response = requests.request("GET", url)

    return response.text

# Histórico por cidade - Informar data inicial
def history_city (id, init, end):
    url = "http://apiadvisor.climatempo.com.br/api/v1/history/locale/" + id + "?token="+ TOKEN + "-hist&from=" + init + "&to=" + end

    response = requests.request("GET", url)

    return response.text

    df = pd.read_json(response.text)
    df.to_csv(r'history-' + id + '-' + TODAY + '.csv', index=None)

# Histórico de trovoada por cidade - Informar data inicial, data final e formato de output (geojson ou json)
def lightning_history_localeid (localeId, init, end, outputFormat):
    url = "http://apiadvisor.climatempo.com.br/api/v1/lightning/strikes?token=" + TOKEN + "-light&from=" + init + "&to=" + end + "&localeId=" + localeId + "&outputFormat=" + outputFormat

    response = requests.request("GET", url)

    return response.text

# Histórico de trovoada por latitude, longitude e raio a partir do ponto - Informar data de início, data final e formato de output (geojson ou json)
def lightning_history_coordinates (latitude, longitude, radius, init, end, outputFormat):
    url = "http://apiadvisor.climatempo.com.br/api/v1/lightning/strikes?token=" + TOKEN + "-light&from=" + init + "&to=" + end + "&latitude=" + latitude + "&longitude=" + longitude + "&radius=" + radius + "&outputFormat=" + outputFormat

    response = requests.request("GET", url)

    return response.text

# Histórico geométrico de trovoada por cidade - Informar data de início e data final
def lightning_geometry_localeid (localeId, init, end):
    url = "http://apiadvisor.climatempo.com.br/api/v1/lightning/strikes?token=" + TOKEN + "-light&from=" + init + "&to=" + end + "&localeId=" + localeId

    response = requests.request("GET", url)
    return response.text

# Risco de alagamento - Informat latitude e longitude
def flood_risk (latitude, longitude):
    url = "http://apiadvisor.climatempo.com.br/api/v1/flood/risk?token=" + TOKEN + "-flood&latitude=" + latitude + "&longitude=" + longitude

    response = requests.request("GET", url)

    return response.text

# TESTANDO OS CÓDIGOS
print(history_city("3477","2021-04-01","2021-04-30"))

