import json
import requests

class Blog:

    def __init__(self, nome):
        self.nome = nome

    def posts(self):
        endereco_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco_url)

    def __repr__(self):
        return '<Blog: {}>'.format(self.nome)



if __name__ == '__main__':
    main()