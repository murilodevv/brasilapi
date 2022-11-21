import requests
from pprint import pprint


class BrasilAPI():

    def __init__(self, **kwargs) -> None:
        self.cep = kwargs.get('cep')
        self.cnpj = kwargs.get('cnpj')

    def search_cep(self):
        page = requests.request('GET', f'https://brasilapi.com.br/api/cep/v1/{self.cep}')
        pprint(page.json())
    
    def search_cnpj(self):
        page = requests.request('GET', f'https://brasilapi.com.br/api/cnpj/v1/{self.cnpj}')
        pprint(page.json())


if __name__=='__main__':

    while True:
        print("\n|-----Welcome to the BrasilAPI!-----|")
        print('If you want to leave, enter "exit".\n')
        choice = input("Enter your choice (CNPJ, CEP...): ")

        if choice == 'CEP' or choice == 'cep':
            cep = input("enter your CEP: ")
            api = BrasilAPI(cep=cep)
            api.search_cep()
        elif choice == 'CNPJ' or choice == 'cnpj':
            cnpj = input("enter your CNPJ: ")
            api = BrasilAPI(cnpj=cnpj)
            api.search_cnpj()

        if choice == 'exit' or choice == "EXIT":
            print("See you later!")
            break