import requests
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
import pandas as pd
import numpy as np




def fetch_all_invoices(token, company_id):
    headers = {'Authorization': "Bearer " + token}
    url = f"https://api-v2.fattureincloud.it/c/{company_id}/issued_documents"
    all_data = []
    page = 1
    while True:
        params = {'type': 'invoice', 'page': page, 'per_page': 50, 'fieldset': 'detailed'}  # Adjust 'per_page' as needed up to the max limit
        response = requests.get(url, headers=headers, params=params)
        data = response.json()['data']
        if not data:
            break
        all_data.extend(data)
        page += 1
    
    return pd.DataFrame(all_data)

def fetch_all_expenses(token, company_id):
    headers = {'Authorization': "Bearer " + token}
    url = f"https://api-v2.fattureincloud.it/c/{company_id}/received_documents"
    all_data = []
    page = 1
    while True:
        params = {'type': 'expense', 'page': page, 'per_page': 50, 'fieldset': 'detailed'}  # Adjust 'per_page' as needed up to the max limit
        response = requests.get(url, headers=headers, params=params)
        data = response.json()['data']
        if not data:
            break
        all_data.extend(data)
        page += 1
    
    return pd.DataFrame(all_data)
