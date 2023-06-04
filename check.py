import whois
domain = "wpfaisal.com"

w = whois.whois(domain)
print(w.expiration_date)
