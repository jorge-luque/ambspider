import requests
import json
import time
from datetime import datetime
from repository import ExchangeRepository
import config

if __name__ == "__main__":

    url_source = "https://mercados.ambito.com/"
    delay_seconds = 5 * 60
    max_retries = 10

    url_map = {
        "dolar_turista": f"{url_source}/dolarturista/variacion",
        "dolar_qatar": f"{url_source}/dolarqatar/variacion",
        "dolar_informal": f"{url_source}/dolar/informal/variacion",
        "dolar_lujo": f"{url_source}/dolardelujo/variacion",
        "dolar_mayorista": f"{url_source}/dolar/mayorista/variacion",
        "dolar_contado_liquidacion": f"{url_source}/dolarrava/cl/variacion",
        "dolar_coldplay": f"{url_source}/dolarcoldplay/variacion",
        "dolar_mep": f"{url_source}/dolarrava/mep/variacion",
        "dolar_oficial": f"{url_source}/dolar/oficial/variacion",
        "dolar_ahorro": f"{url_source}/dolarahorro/variacion",
        "dolar_futuro": f"{url_source}/dolarfuturo/variacion",
        "dolar_nacion": f"{url_source}/dolarnacion/variacion"
    }

    config.init_firebase()

    exchange_repository = ExchangeRepository()

    retries = 0
    while (retries < max_retries):
        for currency, url in url_map.items():
            response = requests.get(url)
            if (response.status_code != 200):
                retries = retries + 1
                time.sleep(retries * retries)
                break
            else:
                retries = 0
            variation = response.json()
            variation["currency"] = currency
            variation["timestamp"] = datetime.timestamp(datetime.now())
            exchange_repository.save(variation)
        time.sleep(delay_seconds)