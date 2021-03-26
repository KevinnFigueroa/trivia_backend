import requests
import json
import os
import random
from random import randint


class RandomTrivia:
    def __init__(self):
        """
        credenciales de la api
        """
        self.app_id = "cabc512f"
        self.app_key = "3b63add2d492321f11b2cc2d2acabe58"
        self.language = "es"
        self.fields = "definitions"
        self.strictMatch = "false"

    def get_random_trivia(self):
        """
        TODO: Mejorar esta implementacion guardando en bd
        """
        lines = open("services/words.txt", encoding="utf8").read().splitlines()
        words_parsed = []
        response_data = []

        for line in lines:
            if line == "":
                continue
            else:
                words_parsed.append(line)

        for num in range(0, 5):
            random_word = words_parsed[randint(0, len(words_parsed) - 1)]
            url = (
                "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
                + self.language
                + "/"
                + random_word.lower()
                + "?fields="
                + self.fields
                + "&strictMatch="
                + self.strictMatch
            )

            r = requests.get(
                url, headers={"app_id": self.app_id, "app_key": self.app_key}
            )

            response = r.json()
            if "results" in response:
                definitions = []
                response = response["results"][0]["lexicalEntries"][0]["entries"][0][
                    "senses"
                ]

                # funcion que trae todas las definiciones de la palabra
                for definicion in range(0, len(response)):
                    definitions.append(response[definicion]["definitions"][0])

                random_word_data = {"word": random_word, "definitions": definitions}
                response_data.append(random_word_data)

        return response_data
