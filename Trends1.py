import os
import re
import csv
import time
import pandas as pd
from random import randint
from pytrends.request import TrendReq



pytrend = TrendReq()

os.chdir("/Users/xhe/PycharmProjects/Econometrics_Project/")
keywords = [["Voting"], ["Vote"]]

for word in keywords:
    keyname = word[0][:4].upper()

    # time.sleep(randint(10, 20))
    pytrend.build_payload(word, geo= "US", gprop='news', timeframe="all_2008")
    data = pytrend.interest_over_time()
    data.to_csv(keyname + ".csv")

#
# os.chdir("/Users/awei/Documents/FE/Sample 13")
# keywords = [["Accomplishment"], ["Achievement"], ["Ambition"], ["American Dream"], ["Apititude"],
#            ["Aspiration"], ["Courage"], ["Desire"], ["Determination"], ["Discipline"],
#            ["Effort"], ["Enthusiasm"], ["Fame"], ["Fire in Belly"], ["Fortitude"],
#            ["Greatness"], ["Grit"], ["Happiness"], ["Hard Work"], ["Independence"],
#            ["Individualism"], ["Motivation"], ["Purpose"], ["Recognition"], ["Resourcefulness"],
#            ["Self Interest"], ["Striving"], ["Struggle"], ["Success"], ["Tenacity"],
#            ["Willpower"]]
#
# states = ['US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA', 'US-WA', 'US-WV', 'US-WI',
#           'US-WY']
#
# for state in states:
#     for word in keywords:
#         statename = state[3:]
#         keyname = word[0][:4].upper()
#         pytrend = TrendReq()
#         # Increase for overnight
#         time.sleep(randint(25, 35))
#         pytrend.build_payload(word, timeframe='all', geo=state, gprop='news')
#         data = pytrend.interest_over_time()
#         data.to_csv(statename + "_" + keyname + ".csv")
#
# os.chdir("/Users/awei/Documents/Time/Sample 10")
# keywords = [["Accomplishment"], ["Achievement"], ["Ambition"], ["American Dream"], ["Apititude"],
#            ["Aspiration"], ["Courage"], ["Desire"], ["Determination"], ["Discipline"],
#            ["Effort"], ["Enthusiasm"], ["Fame"], ["Fire in Belly"], ["Fortitude"],
#            ["Greatness"], ["Grit"], ["Happiness"], ["Hard Work"], ["Independence"],
#            ["Individualism"], ["Motivation"], ["Purpose"], ["Recognition"], ["Resourcefulness"],
#            ["Self Interest"], ["Striving"], ["Struggle"], ["Success"], ["Tenacity"],
#            ["Willpower"]]
#
# for word in keywords:
#     keyname = word[0][:4].upper()
#     pytrend = TrendReq()
#     time.sleep(randint(10, 20))
#     pytrend.build_payload(word, timeframe='all', gprop='news')
#     data = pytrend.interest_over_time()
#     data.to_csv(keyname + ".csv")
#
# os.chdir("/Users/awei/Documents/Econ/Sample 5/FE")
# keywords = [["Laissez faire"], ["Free market"], ["Free enterprise"], ["Noninterference"], ["Nonintervention"],
#            ["Liberalism"], ["Capitalism"], ["Free competition"], ["Open market"], ["Free trade"]]
#
# states = ['US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DE', 'US-DC', 'US-FL',
#           'US-GA', 'US-HI', 'US-ID', 'US-IL', 'US-IN', 'US-IA', 'US-KS', 'US-KY', 'US-LA', 'US-ME',
#           'US-MD', 'US-MA', 'US-MI', 'US-MN', 'US-MS', 'US-MO', 'US-MT', 'US-NE', 'US-NV', 'US-NH',
#           'US-NJ', 'US-NM', 'US-NY', 'US-NC', 'US-ND', 'US-OH', 'US-OK', 'US-OR', 'US-PA', 'US-RI',
#           'US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA', 'US-WA', 'US-WV', 'US-WI',
#           'US-WY']
#
# for state in states:
#     for word in keywords:
#         statename = state[3:]
#         keyname = word[0][:4].upper()
#         pytrend = TrendReq()
#         # Increase for overnight
#         time.sleep(randint(10, 20))
#         pytrend.build_payload(word, timeframe='all', geo=state, gprop='news')
#         data = pytrend.interest_over_time()
#         data.to_csv(statename + "_" + keyname + ".csv")
#
# os.chdir("/Users/awei/Documents/Econ/Sample 5/Time")
# keywords = [["Laissez faire"], ["Free market"], ["Free enterprise"], ["Noninterference"], ["Nonintervention"],
#            ["Liberalism"], ["Capitalism"], ["Free competition"], ["Open market"], ["Free trade"]]
#
# for word in keywords:
#     keyname = word[0][:4].upper()
#     pytrend = TrendReq()
#     time.sleep(randint(10, 20))
#     pytrend.build_payload(word, timeframe='all', gprop='news')
#     data = pytrend.interest_over_time()
#     data.to_csv(keyname + ".csv")
