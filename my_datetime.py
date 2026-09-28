import datetime #arvuti kellaaja moodul/juurdepääs süsteemi kellajaale

#ajaväärtuse muudatuse salvestamine. now muutuja

now = datetime.datetime.now() #küsib op.süsteemilt praegust kuupäeva ja kellaaega

print(now) #prindi kuupäev ja kellaaaeg terminali/prindi now muutuja

print(now.year) #kuvab praeguse aasta
print(now.month) #kuvab praeguse kuu 1-12
print(now.day) #kuvab päeva 1-31
print(now.hour) #kuvab tunni 0-23
print(now.minute)

weekday = now.strftime("%A") #sõne formaadis. a - lühendi jaoks. A terve sõna jaoks
print(weekday)