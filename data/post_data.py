from dotenv import load_dotenv
from elastic_enterprise_search import AppSearch
import json
import os


def post():
    load_dotenv()
    url = "https://lyfsavr.ent.eastus2.azure.elastic-cloud.com/api/as/v1/engines/lyfsavr-backend/documents"

    token = os.environ.get("TOKEN")

    app_search = AppSearch(url, http_auth=token)

    with open("resources.json", "r") as f:
        data = json.load(f)

    app_search.index_documents(engine_name="lyfsavr-backend", documents=data)

    print(app_search.list_engines())
