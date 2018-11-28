# в глобальной области видимости становится доступным имя cbr_api
from api import cbr_api

import importlib

# создается переменная cbr_api_dynamic, ее тип - модуль
cbr_api_dynamic = importlib.import_module("api.cbr_api")


print(cbr_api_dynamic)
print(cbr_api)

print(cbr_api is cbr_api_dynamic)  # выведет True
