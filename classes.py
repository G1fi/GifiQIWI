import requests


class Wallet:

    def __init__(self, token: str):
        """
        Docs QiwiAPI - https://developer.qiwi.com/ru/qiwi-wallet-personal/

        :param token: QIWI API token
        """

        self._session = requests.Session()
        self._api_url = 'https://edge.qiwi.com/'

        self._session.headers['Accept'] = 'application/json'
        self._session.headers['Content-Type'] = 'application/json'
        self._session.headers['Authorization'] = 'Bearer ' + token

        self.wallet_info = None
        self.wallet_info = self.get_wallet_info()

    def change_token(self, new_token: str):
        self._session.headers['Authorization'] = 'Bearer ' + new_token

    def get_wallet_info(self) -> dict:
        return self.call('/person-profile/v1/profile/current', autofill=False)

    def call(self, method: str, params: dict = None, autofill: bool = True) -> dict:

        if autofill:
            method = method.replace('personId', self.wallet_info['authInfo']['personId'])

        response = self._session.get(self._api_url + method, params=params)

        return response.json() if response.ok else response.raise_for_status()


if __name__ == '__main__':
    test = Wallet(input('Input token: '))
    print(test.wallet_info)
