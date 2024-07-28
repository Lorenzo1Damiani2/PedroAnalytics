import functions_framework
import mysql.connector
import logging
import pandas as pd
import numpy as np
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
from datetime import datetime

from sql_commands import create_table_invoices
from API_calls import fetch_all_invoices, fetch_all_expenses

@functions_framework.http
def hello_world(request):
    # Database connection details
    db_user = 'root'
    db_password = 'lorenz12/'
    db_name = 'sudsliceofitaly'
    db_host = '34.175.168.246'  # Replace with your Cloud SQL instance public IP

    create_table_invoices(db_user, db_password, db_host, db_name)

    # Defining the host is optional and defaults to https://api-v2.fattureincloud.it
    # See configuration.py for a list of all supported configuration parameters.
    configuration = fattureincloud_python_sdk.Configuration(
        host = "https://api-v2.fattureincloud.it"
    )

    # The client must configure the authentication and authorization parameters
    # in accordance with the API server security policy.
    # Check out the Authentication section to retrieve the Access Token
    configuration.access_token = "a/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZWYiOiJ4SXkxRzBpdjZKSFNaU0prN2M5eEJHbjBjRDBwakU2WSJ9.BsiVxzGJJs67gm2qQTVIphr4AQSeuo1ErPaViEDRoIs"

    # for this example we define the token as string, but you should have obtained it in the previous steps
    token = "*****"

    # these parameters are usually retrieved through our APIs or stored in a DB
    company_id = "****"

    # fetch invoices from API of fattureincloud
    df_invoices = fetch_all_invoices(token, company_id)

    # fetch expenses from API of fattureincloud
    expense = fetch_all_expenses(token, company_id)

    return "Cloud Function successfully run"
