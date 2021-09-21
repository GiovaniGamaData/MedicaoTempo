import time
import json
import requests
from main import Blog
from unittest import TestCase, main

class Testes(TestCase):

    def dowload_testeApi(self):
        start = time.time()
        blog = Blog("Teste")
        resultado = blog.posts()
        with open('arquivo.json','w') as json_file:
            json.dump(resultado, json_file)

        end = time.time()
        executa_time = end - start
        print("%0.3f ms" % (executa_time * 1000.))

        self.assertIsNotNone(resultado)
        self.assertIsInstance(resultado[0], dict)

if __name__ == "__main__":
    main()