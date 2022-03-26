#!/usr/bin/python3

import json
import sys
from src.scrapper import avis_scrapper
from src.smtp import smtp
from src.logger import logger

def main():
    log = logger()
    log.start('avis.log', False)
    try:
        with open('config.json', 'r') as data:
            config = json.load(data)
        log.info('Configuration loaded')
        scrapper = avis_scrapper('https://secure.avis.es/resultados-búsqueda')
        deal = scrapper.get_cheapest_deal(config['params'])
        if deal < config['threshold']: log.info('Deal found: {}€'.format(deal))
        else: log.info('Too expensive ({}€)'.format(deal))
        mail = smtp('smtp.gmail.com:587', config['mailfrom'], config['mailpassword'])
        mail.setBody(str(config['params']))
        mail.send(config['mailto'])
    except Exception as e:
        log.error(str(e))
        log.stop()
        sys.exit(1)
    log.stop()
    sys.exit(0)

if __name__== '__main__':
    main()
