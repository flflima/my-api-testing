import json
import logging
import os

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
FILES_PATH = './src/resources'

logging.basicConfig(level=logging.INFO)


def erase_files():
    logging.info('Deleting output files...')
    for filename in os.listdir(f'{FILES_PATH}/output'):
        try:
            os.remove(f'{FILES_PATH}/output/{filename}')
        except OSError:
            pass


def load_breeds():
    logging.info('Loading all breeds...')
    with open(f'{FILES_PATH}/input/dogs.txt', 'r') as reader:
        breeds = []

        for line in reader.readlines():
            breeds.append(line.rstrip('\n'))

        return breeds


def execute(breeds):
    logging.info('Calling API')
    for breed in breeds:

        api_url = f'{config.get("HOST")}/{config.get("URL")}/{breed}/{config.get("RESOURCE")}'

        headers = {}

        response = requests.get(api_url, headers=headers)

        if response.status_code < 300:
            logging.debug(
                f'Success getting dog breed {breed} - status: {response.status_code}')

            with open(f'{FILES_PATH}/output/{breed}.json', 'w', encoding='UTF-8') as outfile:
                json.dump(
                    response.json(),
                    outfile,
                    indent=4,
                    ensure_ascii=False)
        else:
            logging.warning(
                f'Error on GET breed {breed} - {api_url} - status: {response.status_code}')

            with open(f'{FILES_PATH}/output/errors.txt', 'a') as outfile:
                outfile.write(
                    f'Breed: {breed} - {api_url} - Status: {response.status_code}, {response.reason}\n')


erase_files()
breeds = load_breeds()
execute(breeds)
