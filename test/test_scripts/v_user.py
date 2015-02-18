import time
import requests
from requests.auth import HTTPBasicAuth


class Transaction(object):

    url = 'http://127.0.0.1:5001/api/v0.0/sensor/31d3ed97-1575-4759-98ab-45b3902b6ac7/timeseries'
    payload = {'timeseries': [{'2134': 45}]}
    auth = HTTPBasicAuth('zhp@gmail.com', '1')

    def __init__(self):
        pass

    def run(self):
        s = time.time()
        requests.post(self.url, json=self.payload, auth=self.auth)
        e = time.time()
        self.custom_timers['Write Request'] = e-s


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
