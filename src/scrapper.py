import requests

class avis_scrapper:
    def __init__(self, url):
        self._url = url

    def get_cheapest_deal(self, req_params):
        req = requests.get(self._url, params=req_params)
        if (req.status_code == 200):
            return self._find_cheapest_deal(req.text)
        else:
            raise Exception('Unsuccessful request')

    def _find_cheapest_deal(self, html):
        for line in html.splitlines():
            if 'offeredPayLaterPricesEUR' in line:
                line = line.strip()
                line = line[line.find('['):-1]
                prices = eval(line)
                return prices[0]
