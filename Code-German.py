import pandas as pd
from collections import Counter
import string

# Read the CSV file into a pandas DataFrame
file_path = 'C:\\Users\\shake\\Desktop\\MSC- Data Science\\Thesis\\Tables\\Agancies Data-CrowdTangle\\DLR.csv'
data = pd.read_csv(file_path, dtype={'Message': str}, low_memory=False,encoding='latin-1')

# Function to count word frequency in a text
def count_words(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    # Count word frequency
    word_count = Counter(text)
    return word_count

 # Define keywords for each field
international_relations_keywords = ['NASA','AWI', 'Antarktis','CNES', 'International Space Station','Astronautinnen','ESA','DLR',
                                    'internationale Partner', 'TanDEM-X', 'COSMO-SkyMed','Deutsche Raumfahrtagentur','ESA-Astronaut','CIMON 2.1',
                                    'digitales Crewmitglied', 'Fuֳballgrֳ¶ֳe', 'ESA-Astronaut', 'Matthias Maurer', 'CosmicKiss-Mission','psychosoziale Interaktion',
                                    'Maschine', 'Schwerelosigkeit', 'robotische Industrieproduktion', 'Bildung', 'Medizin', 'Pflege',
                                    'Experimente','Europäische Weltraumorganisation ESA']
                                    
education_community_keywords = ['Kinder und Jugendliche', 'Mitmach-Aktion', 'Bild', 'DLR_next','indigene Bevölkerungsgruppen',
                                'Inuvik Satellite Station Facility', 'CCMEO', 'lokale Künstlerinnen und Künstler','Testfeld', 'Unternehmen', 'Forschungsinstitute',
                                'Assistenzsysteme', 'autonome Schiffe', 'Co-Infrastruktur', 'HAGGIS', 'Umwelt', 'Verkehr', 'physisches Testfeld', 'LABSKAUS','ESA','Experiment', 'Micro Age', 'ISS', 'ESA-Astronaut', 'Matthias Maurer', 'Schwerelosigkeit', 'Muskelzellen',
                                'Mini-Laboren', 'KUBIKs', 'Planung', 'Bodenunterstֳ¼tzung', 'GSOC-Team', 'Oberpfaffenhofen', 'Experimentcontainer', 'Erde',
                                'Gletscher', 'Sorgen', 'Sֳ¼dpol', 'Erdbeobachtung', 'DLR', 'internationale Partner', 'Westantarktis', 'Meeresspiegel',
                                'TanDEM-X', 'COSMO-SkyMed', 'Satellitenmission','EarthObservation','Living Planet Symposium', 'LPS22', 'Forschende', 'Bֳ¼rger',
                                'Erdbeobachtung', 'globale Herausforderungen', 'nachhaltige Entwicklung', 'Klimawandel','EnMAP', 'Umweltsatellit', 'NASA', 'Kennedy Space Center', 'Hyperspektralinstrument', 'Infrarot-Spektrum', 'Erdoberflֳ₪che', 'Kohlenstoff', 'Pipeline', 'Methan', 'Deutsche Raumfahrtagentur',
                                'Deutsches Zentrum fֳ¼r Luft- und Raumfahrt', 'Bundesministerium fֳ¼r Wirtschaft und Klimaschutz', 'OHB-System AG',
                                'GeoForschungszentrums Potsdam', 'Deutsches Raumfahrtkontrollzentrum', 'Earth Observation Center','CIMON 2.1', 'digitales Crewmitglied', 'Fuֳballgrֳ¶ֳe', 'ESA-Astronaut', 'Matthias Maurer', 'CosmicKiss-Mission', 'psychosoziale Interaktion',
                                'Maschine', 'Schwerelosigkeit', 'robotische Industrieproduktion', 'Bildung',
                                'Medizin', 'Pflege', 'Experimente','Live-Schalte', 'YouTube', 'Projekt',
                                'Weltraum-Analogmission', 'Missionsinfos', 'Dossier','James Webb Space Telescope',
                                'Hintergründe','Artemis I', 'Mond', 'Schwerlastrakete SLS', 'NASA', 'Kennedy Space Center',
                                'Startfenster', 'NASA-Livestream', 'Raketenstart','Youtube-Kanal']
                                    
space_industry_keywords = ['NASA', 'Artemis 1', 'USB-Stick', 'Fracht', 'Mission','INNOspaceMaster', 'KMU',
                          'Ariane6', 'ArianeGroup','Start-ups', 'NewSpace-Entwicklung','Shannon Walker',
                          'Soichi Noguchi', 'Victor Glover', 'Michael Hopkins','Environment and Natural Resources in Canada',
                          'SSC - Swedish Space Corporation', 'CNES','ZAL Zentrum für Angewandte Luftfahrtforschung', 'Luftfahrt',
                          'Luftfahrtstandort', 'Hamburg Aviation', 'Industrie', 'Forschung', 'Innovationszentrum','Weltraumfieber', 'Thermo-Mini', 'Astronaut/innen', 'CosmicKiss-Mission', 'International Space Station', 'esa', 'Matthias Maurer', 'Gesundheitsüberwachung', 'Sensoren',
                          'Raumfahrt', 'Mission', 'experiment', 'ESA - European Space Agency',
                          'NASA - National Aeronautics and Space Administration','CosmicKiss','EnMAP', 'Umweltsatellit', 'NASA', 'Kennedy Space Center', 'Hyperspektralinstrument', 'Infrarot-Spektrum', 'Erdoberflֳ₪che', 'Kohlenstoff', 'Pipeline', 'Methan', 'Deutsche Raumfahrtagentur',
                          'Deutsches Zentrum fֳ¼r Luft- und Raumfahrt', 'Bundesministerium fֳ¼r Wirtschaft und Klimaschutz', 'OHB-System AG',
                          'GeoForschungszentrums Potsdam', 'Deutsches Raumfahrtkontrollzentrum', 'Earth Observation Center','CIMON 2.1', 'digitales Crewmitglied', 'Fuֳballgrֳ¶ֳe', 'ESA-Astronaut', 'Matthias Maurer', 'CosmicKiss-Mission', 'psychosoziale Interaktion',
                          'Maschine', 'Schwerelosigkeit', 'robotische Industrieproduktion', 'Bildung', 'Medizin',
                          'Pflege', 'Experimente','Jupiter ERS Team', 'James Webb Space Telescope']

research_technology_keywords =['NASA', 'Artemis 1', 'Mission', 'Astronauten', 'Mond','INNOspaceMaster', 
                               'Forschungsansätze', 'Konzepte', 'Prototypen', 'nachhaltige Infrastruktur', 'All', 'Erde',
                               'Atmosphäre', 'Venus', 'Untersuchung', 'Nachbarplanet', 'Bedingungen', 'DLR-Glutofen',
                               'Beschaffenheit', 'Oberfläche', 'Orbit', 'Gesteine', 'Instrument', 'Jahrzehnt',
                               'GREAT-Spektrometer', 'Forschungsflugzeug', 'SOFIA', 'Messung', 'Konzentration',
                               'atomarer Sauerstoff', 'Atmosphäre', 'Spektrometer', 'Technologie', 'Satellitenmissionen',
                               'Oberstufe', 'Trägerrakete', 'Ariane6', 'DLR-Prüfstand', 'Lampoldshausen',
                               'Hot Firing Modell', 'Test', 'ArianeGroup', 'Bremen', 'Countdown', 'Erststart',
                               'Waldbrände', 'Erdrutsche', 'Sturzfluten', 'Katastrophenfälle', 'schnelle Antworten', 'Leben retten',
                               'Projekt HEIMDALL', 'App', 'Satellitendaten', 'Maßnahmen', 'Einsatzpläne',
                               'Generaldirektor', 'ESA', 'European Space Agency', 'Josef Aschbacher', 'Zusammenarbeit','Forschungsobservatorium', 'Innovationscampus', 'Gestalt', 'Kuppel', 'Teleskop',
                               'Spezialkran', 'Rohbau', 'Teleskopeuropas', 'Weltraumschrott', 'Objekte', 'DLR-Institut für Technische Physik', 'Montage',
                               'Raketenklasse', 'Mikrolauncher', 'Kleinträger', 'Satelliten', 'Umlaufbahn', 'Deutsche Raumfahrtagentur', 'DLR','EarthObservation',
                               'Mikrolauncher-Wettbewerb', 'Start-up', 'Isar Aerospace Technologies', 'Spectrum-Rakete', 'Geschäftsmodell','CosmicKiss',
                               'HyImpulse Technologies GmbH', 'Rocket Factory Augsburg AG','SpaceX', 'Crew-1', 'Internationale Raumstation', 'Rückkehr',
                               'SET Level', 'Simulationswerkzeuge', 'Simulationsmethoden', 'Zulassung', 'automatisierte Fahrzeuge', 'Projektpartner', 'Realität',
                               'digital abzubilden', 'Simulative Tests', 'Meilenstein', 'Projekt-Team','fahrerlose', 'elektrobetriebene', 'Fahrzeugkonzept', 'U-Shift', 'German Innovation Award 2021', 'Karlsruher Institut für Technologie', 'FKFS - Forschungsinstitut für Kraftfahrwesen und Fahrzeugmotoren Stuttgart',
                               'Universität Ulm', 'studiokurbos', 'futuristisch', 'formschön', 'Prototyp','CNES','Satellitenempfangsstation', 'Inuvik', 'Arktis', 'Bodenstation', 'Erdbeobachtung', 'TanDEMX-Mission', 'Copernicus', 'Sentinel5P',
                               'Fernerkundungsdaten', 'Satellitenkontrolle', 'Bodenstation', 'Canada Centre for Mapping and Earth Observation',
                               'ESA','Kennedy Space Center','EnMAP', 'Umweltsatellit', 'NASA', 'Kennedy Space Center', 'Hyperspektralinstrument', 'Infrarot-Spektrum', 'Erdoberflֳ₪che', 'Kohlenstoff', 'Pipeline', 'Methan', 'Deutsche Raumfahrtagentur',
                               'Deutsches Zentrum fֳ¼r Luft- und Raumfahrt', 'Bundesministerium fֳ¼r Wirtschaft und Klimaschutz', 'OHB-System AG',
                               'GeoForschungszentrums Potsdam', 'Deutsches Raumfahrtkontrollzentrum', 'Earth Observation Center','CIMON 2.1', 'digitales Crewmitglied', 'Fuֳballgrֳ¶ֳe', 'ESA-Astronaut', 'Matthias Maurer', 'CosmicKiss-Mission', 'psychosoziale Interaktion',
                               'Maschine', 'Schwerelosigkeit', 'robotische Industrieproduktion', 'Bildung',
                               'Medizin', 'Pflege', 'Experimente','Jupiter', 'Polarlichter', 'James-Webb-Weltraumteleskop',
                               'NASA', 'Nahinfrarotkamera', 'Infrarotfilter', 'Große Rote Fleck', 'Sturm', 'Wolken',
                               'Sonnensystem','Artemis I', 'Mond', 'Schwerlastrakete SLS', 'NASA',
                               'Kennedy Space Center', 'Startfenster', 'NASA-Livestream', 'Raketenstart','Artificial Intelligence']


# Create a dictionary mapping each category to its corresponding keywords
keywords_dict = {
    'International Relations': international_relations_keywords,
    'Education and Community': education_community_keywords,
    'Space Industry': space_industry_keywords,
    'Research and Technology': research_technology_keywords
}

# Create columns for each field
for field in keywords_dict.keys():
    data[f"{field}_Related"] = 0

# Function to classify posts based on the presence of keywords
def classify_posts(row, keywords_dict):
    # Check if the value in the 'Message' column is a string
    if isinstance(row['Message'], str):
        post = row['Message'].lower()  # Convert post text to lowercase
        word_count = count_words(post)

        # Iterate through each field and set 1 if related keywords are found
        for field, keywords in keywords_dict.items():
            for keyword in keywords:
                if keyword.lower() in word_count:
                    row[f"{field}_Related"] = 1
                    break  # Exit loop if any related keyword is found
    return row

# Apply the updated classification function to categorize posts
data = data.apply(classify_posts, axis=1, keywords_dict=keywords_dict)

# Save the updated DataFrame to a new CSV file
output_file_path = 'C:\\Users\\shake\\Desktop\\MSC- Data Science\\Thesis\\Tables\\Agancies Data-CrowdTangle\\DLR.csv'
data.to_csv(output_file_path, index=False)

# Display the updated classification in the DataFrame
print(data[['Message', 'International Relations_Related', 'Education and Community_Related', 'Space Industry_Related', 'Research and Technology_Related']])