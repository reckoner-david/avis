#!/usr/bin/python3

import json
import sys
from src.scrapper import avis_scrapper
from src.avis import avis
from src.logger import logger

def main():
    log = logger()
    log.start('avis.log', False)
    try:
        with open('config.json', 'r') as data:
            config = json.load(data)
        scrapper = avis_scrapper('https://secure.avis.es/resultados-búsqueda')
        print(scrapper.get_cheapest_deal(config['params']))
    except Exception as e:
        log.error(str(e))
        log.stop()
        sys.exit(1)
    log.stop()
    sys.exit(0)

if __name__== '__main__':
    main()
