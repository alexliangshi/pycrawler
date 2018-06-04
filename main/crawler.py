# -*- coding: utf-8 -*-
# @Desc     :
# @license : Copyright(C), CBR
# @Contact : shiliang@chinaratings.com.cn
# @Site    :

import requests
import bs4
url="http://www.comnews.cn/"
response= requests.get(url)
soup=bs4.BeautifulSoup(response.text)
links=[a.attrs.get('href') for a in soup.select('div.li a[href^=/local]')]