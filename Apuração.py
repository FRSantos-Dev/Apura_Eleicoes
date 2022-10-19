import pandas as pd
import requests
from time import sleep
from datetime import datetime, timedelta
import json
from IPython.display import clear_output

def get_results():
    to_gmt3 = datetime.now() - timedelta(hours=3)
    print(f'{to_gmt3.strftime("%H:%M:%S")} - Carregando resultados\n')
   
    r = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
    j = json.loads(r.content)
    return j

    while True:
        result = get_results()
    result_cand = pd.json_normalize(result['cand']).drop(columns=['seq', 'sqcand', 'nv', 'n', 'cc'])
    print(result_cand.to_markdown())
        
    sleep(10)
    clear_output(wait=True)