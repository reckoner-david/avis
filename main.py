#!/usr/bin/python3

import json
import sys
from src.scrapper import avis_scrapper
from src.parameters import parameters
from src.smtp import smtp
from src.logger import logger

configuration = 'config.json'
force = False

def main():
    log = logger()
    log.start('avis.log', False)
    log.info('argv: {}'.format(str(sys.argv)))

    params = parameters(lambda param: log.warn('Parameter "{}" not recognized'.format(param)))
    params.register_parameter('configuration', lambda param: globals().update(configuration = param))
    params.register_switch('force', lambda: globals().update(force = True))
    params.parse(sys.argv[1:])
    try:
        with open(configuration, 'r') as data:
            config = json.load(data)
        log.info('Configuration loaded')
        scrapper = avis_scrapper('https://secure.avis.es/resultados-búsqueda')
        deal = scrapper.get_cheapest_deal(config['params'])
        if deal < config['threshold']: 
            dealFoundStr = 'Deal found: {}€'.format(deal)
            log.info(dealFoundStr)
            mail = smtp('smtp.gmail.com:587', config['mailfrom'], config['mailpassword'])
            mail.setSubject(dealFoundStr)
            mail.setBody(str(config['params']))
            mail.send(config['mailto'])
        else:
            noDealFoundStr = 'Too expensive ({}€)'.format(deal)
            log.info(noDealFoundStr)
            if (force):
                log.info('Mail forced')
                mail = smtp('smtp.gmail.com:587', config['mailfrom'], config['mailpassword'])
                mail.setSubject('No deal found')
                mail.setBody(str(config['params']) + '\n' + noDealFoundStr)
                mail.send(config['mailto'])
    except Exception as e:
        log.error(str(e))
        log.stop()
        sys.exit(1)
    log.stop()
    sys.exit(0)

if __name__== '__main__':
    main()
