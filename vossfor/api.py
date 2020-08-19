import requests
from typing import Dict

RequestHeaders = Dict[str,str]


def make_request(address: str, headers: RequestHeaders, verb:str="GET") -> Dict:
    """
    Sends a get request to MapQuest. (Only written for GET requests here.)
    :param params: String with protocol, url and parameters.
    :param: headers.
    :param: verb. (Only written for GET requests.)
    :return: JSON response
    """
    r = requests.request(verb, address, headers=headers)
    r.raise_for_status()
    return r.json()


class ForexConvert:

    def __init__(self):  # target:str='ZAR' (In case we later want to inherit classes with other target currencies.

        self._target = 'ZAR'  # Allowing for "rude" manipulation of target currency.
        self.__url = "https://api.exchangeratesapi.io/latest?symbols={}&base=".format(self._target)
        self.__headers = {}

    def get_rate(self, base:str='USD') -> float:

        if base not in ['USD', 'EUR', 'GBP']:
            raise ValueError("ForexConvert.get_rate(base) must be one of 'USD', 'EUR', 'GBP', not '{}'.".format(base))

        address = self.__url + base
        result = make_request(address = address, headers = self.__headers)

        if (
            not 'rates' in result or
            not self._target in result['rates']
        ):
            raise ValueError(
                "ForexConvert.get_rate could not retrieve an exchange rate from {}, instead got {}".format(
                    address,
                    result
                )
            )

        return result['rates'][self._target]

    def do_conversion(self, currency_code:str='USD', amount:float=1.00) -> float:

        rate = self.get_rate(base=currency_code)

        return rate * amount
