import datetime
from dateutil import relativedelta
import whois
import pandas as pd

def checkDomain(domain):
    
    w = whois.whois(domain)

    expirationDate = w.expiration_date

    if type(expirationDate) is list:
        date = expirationDate[0]
    else:
        date = expirationDate

    today = datetime.datetime.today()

    diff = relativedelta.relativedelta(date, today)

    years = diff.years
    months = diff.months
    days = diff.days

    return '{} years {} months {} days'.format(years, months, days)

domainsInfo = []
domainNames = []

with open('domains.txt') as f:
    domains = f.readlines()
    for text in domains:
        domain = text.rstrip("\n")
        checkDomain(domain)
        domainNames.append(domain)
        domainsInfo.append(checkDomain(domain))

df = pd.DataFrame({'Domain Name': domainNames,
                   'Time left': domainsInfo})
print(df)
df.to_csv('domains.csv', index=False)