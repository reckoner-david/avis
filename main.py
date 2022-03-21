#!/usr/bin/python3

from src.logger import logger
from datetime import date, timedelta

def main():
    log = logger()
    log.start('avis.log', False)
    try:
        print('Hello world')
    except Exception as e:
        log.error(str(e))
    log.stop()

if __name__== '__main__':
    main()
