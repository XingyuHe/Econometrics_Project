import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('https://trends.google.com/trends/explore?date=all_2008&geo=US&gprop=news&q=free%20trade', proxies=proxies)