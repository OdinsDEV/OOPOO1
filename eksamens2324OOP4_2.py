import requests

dati = requests.get(" https://restcountries.com/v3.1/all")
# Pārbauda, vai pieprasījums izdevās
if dati.status_code == 200:
    valstis =  dati.json()
    print("veiksmīgs pieprasījums")

    #Iegūsti un izvadi visu valstu vispārpieņemtos nosaukumus (“name” → “common”).
    for country in valstis: 
        if 'name' in country and 'common' in country['name']:
            print(country['name']['common'])
        
    # Iegūsti un izvadi kopējo valstu skaitu.
    print(f"Kopumā ir {len(valstis)} valstis.")

    #Iegūsti un izvadi visu valstu vidējo iedzīvotāju skaitu
    Kopējā_populācija = 0  # Saglabā kopējo populāciju
    Valstis_populacija = 0 #cik valstīm ir dati par iedzīvotājiem

    for country in valstis:
        if 'population' in country:  # Pārbauda, vai valstij ir dati par iedzīvotājiem
            Kopējā_populācija += country['population']
            Valstis_populacija += 1

    if Valstis_populacija > 0:
        # Aprēķina vidējo skaitu
        average_population = Kopējā_populācija / Valstis_populacija
        print(f"Vidējais iedzīvotāju skaits: {average_population:.0f}")  # Noapaļo

    #Iegūsti un izvadi valsti ar vislielāko iedzīvotāju skaitu. 
    lielaka_populacija = 0  # saglabā lielāko vērtību salīdzināšanai
    valsts_lielaka_populacija = ""  # saglabā valsti ar lielāko iedzīvotāju skaitu
    
    for country in valstis:
        if country['population'] > lielaka_populacija:
            lielaka_populacija = country['population']
            valsts_lielaka_populacija = country['name']['common']
    print(f"Valsts ar vislielāko iedzīvotāju skaitu: {valsts_lielaka_populacija}")
    print(f"Iedzīvotāju skaits: {lielaka_populacija}")

    #Iegūsti un izvadi visu valstu kopējo platību (“area”)
    kopeja_platiba = 0  # Saglabā kopējo platību
    for country in valstis:
        kopeja_platiba += country['area']
    print(f"Kopējā visu valstu platība: {kopeja_platiba} km²")

    #Izvade par Latviju
    for country in valstis:
        if 'name' in country and 'common' in country['name'] and country['name']['common'] == "Latvia":
            # atrod apakšreģionu
            apaksregions = country.get('subregion', 'N/A')
            print(f"Latvijas apakšreģions: {apaksregions}")

            # atrod robežvalstu kodus
            robezvalstis = country.get('borders', [])
            print(f"Latvijas robežvalstu kodi: {robezvalstis}")

           # break  # Pārstāj, kad atrod Latviju


else:
    # dod erroru
    print(f"Failed to retrieve data. Status code: {dati.status_code}")
