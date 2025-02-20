import requests

dati = requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=1000")

# Pārbauda, vai pieprasījums izdevās
if dati.status_code == 200:
    print("veiksmīgs pieprasījums\n")
    atkritumi =  dati.json()
    rekordi = atkritumi["result"]["records"]
    unique_pilsetanovadi = set()
    unique_pilsetanovadi1 = set()
    unique_pilsetanovadi2 = set()




    #Izvadīt attiecīgā atkritumu nodošanas punkta adresi, kurā var nodot baterijas un  akumulatorus.
    print("Adreses, kur nodot baterijas un akumulatorus: \n")
    for vieta in rekordi:
        if vieta.get('8 : Baterijas un akumulatori') == 'x':
            print(vieta.get('adrese'))
            pilsetanovads = vieta.get('pilsetanovads')
            if pilsetanovads:  #nepievienot tukšas vērtības
                unique_pilsetanovadi.add(pilsetanovads)
    print("______________\n")
    print("Novadi, kur nodot baterijas un akumulatorus:\n")
    for pilseta in unique_pilsetanovadi:
        print(pilseta)
    print("______________\n")

    #Izvadīt attiecīgā atkritumu nodošanas punkta adresi, kurā var nodot nolietotās riepas.
    print("Adreses, kur nodot nolietotas riepas: \n")
    for vieta in rekordi:
        if vieta.get('10 : Nolietotās riepas') == 'x':
            print(vieta.get('adrese'))
            pilsetanovads1 = vieta.get('pilsetanovads')
            if pilsetanovads1:  #nepievienot tukšas vērtības
                unique_pilsetanovadi1.add(pilsetanovads1)
    print("______________\n")
    print("Novadi, kur nodot nolietotas riepas:\n")
    for pilseta1 in unique_pilsetanovadi1:
        print(pilseta1)
    print("______________\n")

    #Izvadīt attiecīgā atkritumu nodošanas punkta adresi, kurā var nodot metālu.
    print("Adreses, kur nodot metālu: \n")
    for vieta in rekordi:
        if vieta.get('3 : Metāls') == 'x':
            print(vieta.get('adrese'))
            pilsetanovads2 = vieta.get('pilsetanovads')
            if pilsetanovads2:  #nepievienot tukšas vērtības
                unique_pilsetanovadi2.add(pilsetanovads2)
    print("______________\n")
    print("Novadi, kur nodot metālu:\n")
    for pilseta2 in unique_pilsetanovadi2:
        print(pilseta2)
    print("______________\n")

else:
    # dod erroru
    print(f"Failed to retrieve data. Status code: {dati.status_code}")