from nslookup import Nslookup
import os
dns_query = Nslookup()

a = dns_query.dns_lookup(os.getenv('BROKER_URL').split(':')[2].split("@")[1])

with open('.dockerenv', 'a') as f:
    f.write(f'BROKER_API={a.answer[0]}')
    f.write(f"BROKER_USER={os.getenv('BROKER_URL').split(':')[1].split('/')[2]}")
    f.write(f"BROKER_PASS={os.getenv('BROKER_URL').split(':')[2].split('@')[0]}")
