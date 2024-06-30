import pandas as pd
from collections import Counter
import string

# Read the CSV file into a pandas DataFrame
file_path = 'C:\\Users\\shake\\Desktop\\MSC- Data Science\\Thesis\\Tables\\Agancies Data-CrowdTangle\\CNES.csv'
data = pd.read_csv(file_path, dtype={'Message': str}, low_memory=False,encoding='utf-8')

# Function to count word frequency in a text
def count_words(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    # Count word frequency
    word_count = Counter(text)
    return word_count

 # Define keywords for each field
international_relations_keywords = ['diplomatie', 'politique étrangère', 'coopération internationale', 'affaires mondiales', 'intention', 'déclaration', 'intention stratégique',
                                   'diplomate', 'ambassadeur', 'traité', 'sommet', 'ambassade', 'ONU', 'Nations Unies', 'maintien de la paix', 'dirigeants mondiaux',
                                   'relations bilatérales', 'accord', 'signature', 'partenariat stratégique', 'Premier ministre', 'géopolitique', 'organisations internationales',
                                   'conseil de sécurité', 'multilatéral', 'agences spatiales internationales', 'ministre des Affaires étrangères', 'protocole',
                                   'mission diplomatique', 'dialogue international', 'Bonne année', 'résolution des conflits', 'communication interculturelle', 'accords commerciaux',
                                   'gouvernance mondiale', 'traités internationaux', 'relations diplomatiques', 'conférences internationales', 'diplomatie économique',
                                   'échange culturel', 'alliances stratégiques', 'négociations de paix', 'affaires étrangères', 'analyse politique', 'Agence spatiale',
                                   'affaires mondiales', 'coexistence', 'corps diplomatique', 'immunité diplomatique', 'paysage géopolitique', 'aide étrangère',
                                   'coopération régionale', 'liens diplomatiques', 'sommets internationaux', 'stabilité régionale', 'Sous-comité scientifique et technique',
                                   'Nations Unies', 'Utilisations pacifiques de l\'espace extra-atmosphérique', 'COPUOS', 'ressources spatiales', 'protocole diplomatique',
                                   'politique internationale', 'relations transfrontalières', 'droit international', 'communauté diplomatique', 'commerce extérieur',
                                   'relations intergouvernementales', 'diplomatie publique', 'diplomatie mondiale', 'négociations diplomatiques', 'missions diplomatiques',
                                   'conventions internationales', 'Station spatiale internationale', 'diplomatie des droits de l\'homme', 'analyse de la politique étrangère',
                                   'stratégies diplomatiques', 'initiatives diplomatiques', 'coopération mondiale', 'affaires internationales', 'accords de paix',
                                   'communication interculturelle', 'leadership mondial', 'efforts diplomatiques', 'analyse des affaires étrangères', 'dialogue diplomatique',
                                   'relations étrangères', 'diplomatie transfrontalière', 'consolidation de la paix', 'corps diplomatique', 'collaboration internationale',
                                   'communication internationale', 'coopération intergouvernementale', 'dialogue politique', 'diplomatie économique', 'relations diplomatiques',
                                   'sécurité internationale', 'engagement diplomatique', 'diplomatie internationale', 'diplomatie multilatérale', 'partenariats stratégiques',
                                   'missions diplomatiques', 'initiatives diplomatiques', 'diplomatie interculturelle', 'négociations mondiales', 'accords internationaux',
                                   'communauté diplomatique', 'protocole diplomatique', 'relations interculturelles', 'discours diplomatique', 'gouvernance mondiale',
                                   'dialogue diplomatique', 'négociations de paix', 'paysage géopolitique', 'analyse de politique étrangère', 'traités internationaux',
                                   'négociations diplomatiques', 'affaires mondiales', 'coexistence', 'efforts diplomatiques', 'coopération internationale',
                                   'diplomatie économique', 'échanges culturels', 'stabilité régionale', 'liens diplomatiques', 'aide étrangère', 'missions diplomatiques',
                                   'immunité diplomatique', 'sommets internationaux', 'stratégies diplomatiques', 'ministre des Affaires étrangères', 'protocole', 'dialogue international',
                                   'liens diplomatiques', 'droit international', 'mission lunaire Apollo 11', 'Apollo 11', 'diplomatie des droits de l\'homme', 'commerce extérieur',
                                   'politique internationale', 'période des fêtes', 'relations transfrontalières', 'protocole diplomatique', 'conventions internationales',
                                   'communauté diplomatique', 'astronautes', 'Station spatiale internationale', 'analyse de la politique étrangère', 'traités internationaux',
                                   'négociations diplomatiques', 'affaires mondiales', 'président', 'coexistence', 'efforts diplomatiques', 'coopération internationale',
                                   'diplomatie économique', 'échange culturel', 'stabilité régionale', 'liens diplomatiques', 'aide étrangère', 'Artemis', 'Mission Artemis', 'Accords Artemis',
                                   'lancement', 'missions diplomatiques', 'immunité diplomatique', 'sommets internationaux', 'stratégies diplomatiques', 'ministre des Affaires étrangères',
                                   'protocole', 'dialogue international', 'liens diplomatiques', 'droit international', 'diplomatie des droits de l\'homme', 'commerce extérieur',
                                   'politique internationale', 'relations transfrontalières', 'protocole diplomatique', 'conventions internationales', 'communauté diplomatique',
                                   'analyse de politique étrangère', 'diplomatie mondiale', 'négociations diplomatiques', 'relations intergouvernementales', 'relations diplomatiques',
                                   'collaboration internationale', 'communication internationale', 'dialogue politique', 'efforts diplomatiques', 'communication interculturelle',
                                   'relations extérieures', 'diplomatie internationale', 'sécurité internationale', 'engagement diplomatique', 'missions diplomatiques',
                                   'diplomatie interculturelle', 'Agenda', '#Agenda', 'négociations mondiales', 'accords internationaux', 'communauté diplomatique', 'protocole diplomatique',
                                   'annoncé', 'relations interculturelles', 'discours diplomatique', 'gouvernance mondiale', 'dialogue', 'Congrès astronautique international',
                                   'négociations de paix', 'paysage géopolitique', 'politique étrangère', 'télescope James Webb', 'James Webb', 'Artemis', 'mission', 'faits marquants','Artemis', 'missions diplomatiques', 'immunité diplomatique', 'sommets internationaux', 'stratégies diplomatiques', 'ministre des Affaires étrangères',
                           'protocole', 'dialogue international', 'liens diplomatiques', 'droit international', 'diplomatie des droits de l\'homme', 'commerce extérieur', 'politique internationale',
                           'période des fêtes', 'relations transfrontalières', 'protocole diplomatique', 'conventions internationales', 'communauté diplomatique', 'astronautes',
                           'Station spatiale internationale', 'analyse de la politique étrangère', 'traités internationaux', 'négociations diplomatiques', 'affaires mondiales', 'président',
                           'coexistence', 'efforts diplomatiques', 'coopération internationale', 'diplomatie économique', 'échange culturel', 'stabilité régionale', 'liens diplomatiques',
                           'aide étrangère', '#Artemis', 'Artemis', 'Mission Artemis', 'Accords Artemis', 'lancement', 'missions diplomatiques', 'immunité diplomatique', 'sommets internationaux',
                           'stratégies diplomatiques', 'ministre des Affaires étrangères', 'protocole', 'dialogue international', 'liens diplomatiques', 'droit international',
                           'diplomatie des droits de l\'homme', 'commerce extérieur', 'international politique nationale', 'relations transfrontalières', 'protocole diplomatique',
                           'conventions internationales', 'communauté diplomatique', 'analyse de politique étrangère', 'diplomatie mondiale', 'négociations diplomatiques',
                           'relations intergouvernementales', 'relations diplomatiques', 'collaboration internationale', 'communication internationale', 'dialogue politique',
                           'efforts diplomatiques', 'communication interculturelle', 'relations extérieures', 'diplomatie internationale', 'sécurité internationale', 'engagement diplomatique',
                           'missions diplomatiques', 'diplomatie interculturelle', 'négociations mondiales', 'accords internationaux', 'communauté diplomatique', 'protocole diplomatique',
                           'relations interculturelles', 'discours diplomatique', 'gouvernance mondiale', 'dialogue diplomatique', 'négociations de paix', 'paysage géopolitique',
                           'analyse de politique étrangère', 'traités internationaux', 'négociations diplomatiques', 'affaires mondiales', 'coexistence', 'efforts diplomatiques',
                           'coopération internationale', 'diplomatie économique', 'échanges culturels', 'stabilité régionale', 'liens diplomatiques', 'aide étrangère',
                           '#Artemis', 'Artemis', 'Mission Artemis', 'Accords Artemis', 'lancement', 'missions diplomatiques', 'immunité diplomatique', 'sommets internationaux',
                           'stratégies diplomatiques', 'ministre des Affaires étrangères', 'protocole', 'dialogue international', 'liens diplomatiques', 'droit international',
                           'diplomatie des droits de l\'homme', 'commerce extérieur', 'politique internationale', 'relations transfrontalières', 'protocole diplomatique',
                           'conventions internationales', 'communauté diplomatique', 'analyse de politique étrangère', 'diplomatie mondiale', 'négociations diplomatiques',
                           'relations intergouvernementales', 'relations diplomatiques', 'collaboration internationale', 'communication internationale', 'dialogue politique',
                           'efforts diplomatiques', 'communication interculturelle', 'relations extérieures', 'diplomatie internationale', 'sécurité internationale',
                           'engagement diplomatique', 'missions diplomatiques', 'diplomatie interculturelle', 'Agenda', '#Agenda', 'négociations mondiales', 'accords internationaux',
                           'communauté diplomatique', 'protocole diplomatique', 'annoncé', 'relations interculturelles', 'discours diplomatique', 'gouvernance mondiale', 'dialogue',
                           'Congrès astronautique international', 'négociations de paix', 'paysage géopolitique', 'politique étrangère', 'télescope James Webb', 'James Webb', 'Artemis',
                           'mission', 'faits marquants']
                                    
education_community_keywords =  ['éducation', 'sensibilisation communautaire', 'logo', 'design', 'à bientôt!', 'livestream', 'festival', 'pluie de météores', 'vivre ici', 'en direct', 'compétition', 
                      'apprentissage', 'Un nouvel article', 'équipage', 'impact social', 'Directeur adjoint', 'Centre', 'vol spatial habité', 'webinaire', 'étudiant', 'projets', 'projet', 
                      'supérieures de premier cycle', 'école', 'étudiants', 'enseignants', 'salle de classe', 'système éducatif', 'James Webb Telescope', 'James Webb', 'Artemis', 'Encourager', 
                      'jeune', 'S\'inscrire', 'Tag', 'copernicus eu', 'copernicus', 'atelier', 'développement communautaire', 'bénévolat', 'mentorat', 'engagement des jeunes', 'Jeunesse', 'Science', 
                      'forum', 'STEM', 'Découverte', 'Prof.', 'Rejoignez-nous', 'vidéo', 'artiste', 'médias sociaux', 'fun', 'météore', 'douche', 'universitaire', 'bourse d\'études', 'alphabétisation', 
                      'autonomisation', 'développement des compétences', 'éducateurs', 'ateliers', 'Rejoindre', 'Centre de découverte', 'Découverte', 'centre', 'Découvrir plus', 'ESA', 'NASA', 'ESA', 
                      'Congrès', 'programme éducatif', 'réussite des élèves', 'ressources éducatives', 'district scolaire', 'choses que vous devez savoir', 'Le saviez-vous', 'Jupiter', 'art', 'En direct maintenant', 
                      '#Artémis', 'environnement d\'apprentissage', 'politique éducative', 'développement de programmes scolaires', 'technologie éducative', 'voyage à travers notre univers', 'Saturne', 'Crédits :', 
                      'en direct maintenant', 'Pour plus d\'informations', 'Regarder en direct', 'Éducation STEM', 'formation des enseignants', 'éducation inclusive', 'éducation spécialisée', 'défis', 'visite virtuelle', 
                      'voler', 'campagne', 'étoile', 'à des années-lumière de la Terre', 'années-lumière', 'développement communautaire', 'engagement civique', 'responsabilité sociale', 'philanthropie', 'bulletin d\'information', 
                      'Découvrir', 'écoles', 'organisations de jeunesse', 'centres scientifiques', 'symposium virtuel', 'virtuel', 'symposium', 'organisation à but non lucratif', 'service communautaire', 'fondation caritative', 
                      'justice sociale', 'INSCRIVEZ-VOUS MAINTENANT', 'INSCRIVEZ-VOUS', 'Visitez notre guide', 'musées', 'accueil', 'conférence de presse', 'presse', 'conférence', 'direction scolaire', 'implication des parents', 
                      'communauté d\'apprentissage', 'programme parascolaire', 'Le saviez-vous', 'faits saillants', 'Ever entendu', 'orion', 'Soleil', 'Mercure', 'Vénus', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 
                      'autonomisation de l\'éducation', 'initiative éducative', 'plaidoyer pour l\'éducation', 'impact communautaire', 'Earth Photo', 'modèles d\'impression 3D', 'jeux vidéo', 'livre électronique', 
                      'autonomisation des jeunes', 'réforme de l\'éducation', 'sensibilisation éducative', 'équité éducative', 'éclipse lunaire', 'capturé', 'actualité', 'actualités', 'presse', 'veuillez vous inscrire', 
                      'réussite éducative', 'soutien communautaire', 'éducation pour tous', 'programme éducatif', 'galaxies', 'Voie lactée', 'saison des vacances', 'atelier en ligne', 'professeurs', 'recherche', 'universitaires']
                                    
space_industry_keywords = [
    "secteur spatial", "industrie spatiale", "entreprises", "dirigeants", "Space Edge computing", "Edge computing", "industrie", "sociétés", "fabrication",
    "fusée", "cosmos", "orbite", "vaisseau spatial", "extraterrestre", "télescope James Webb", "James Webb", "STEM", "industries spatiales",
    "céleste", "planète", "cosmonaute", "agence spatiale", "ateliers", "nouvelles opportunités", "opportunités d'investissement", "investissement", "investissements", "opportunités", "national",
    "interstellaire", "technologie spatiale", "astronaute", "station spatiale", "secteur spatial", "secteur", "lancement d'applications", "lancement", "applications",
    "galaxie", "système solaire", "cosmique", "exploration", "stellaire", "secteur", "mises à jour de l'industrie", "activités réglementaires", "industrie spatiale", "embauche", "lancement",
    'interplanétaire', 'recherche spatiale', 'rayons cosmiques', 'astronomique', 'observatoire', 'économie', 'SpaceX', 'actifs industriels', 'industriel',
    "astrophysique", "voyage spatial", "gravité", "science spatiale", "astrobiologie", "défis",
    "poussière cosmique", "évolution stellaire", "orbite", "lancement spatial", "astrophotographe",
    "navette spatiale", "innovation spatiale", "vie extraterrestre", "planétarium", "sortie dans l'espace",
    "sonde spatiale", "phénomènes spatiaux", "météo spatiale", "agence spatiale", "rayonnement cosmique",
    "observation spatiale", "lancement de fusée", "exploration spatiale", "vol spatial humain",
    "technologie spatiale", "lancement de satellite", "télescope spatial", "science des fusées", "colonisation spatiale", "Jupiter", "aurores boréales",
    "politique spatiale", "actualités de l'industrie spatiale", "organisation de recherche spatiale", "course à l'espace", "lié à l'espace",
    "mécanique orbitale", "communication spatiale", "recherche en sciences spatiales", "développement de technologies spatiales", "mises à jour des missions spatiales",
    "propulsion de fusée", "innovation en matière de voyages spatiaux", "corps célestes", "exploration d'astéroïdes",
    "phénomènes cosmiques", "découvertes spatiales", "collaboration entre agences spatiales", "exploration planétaire", "recherche sur les stations spatiales", "technologie laser",
    "exploration galactique", "découvertes astronomiques", "développement de vaisseaux spatiaux", "découvertes spatiales", "rover", "starlink",
    "progrès de l'industrie spatiale", "coopération spatiale internationale", "jalons de l'exploration spatiale", "technologie d'exploration spatiale", "missions d'exploration spatiale",
    "technologie des fusées", "percées dans l'exploration spatiale", "résultats de la recherche spatiale", "succès des missions spatiales", "technologie des satellites",
    "initiatives de recherche spatiale", "découvertes scientifiques spatiales", "mises à jour sur l'exploration spatiale", "réalisations des astronautes", "développements de l'industrie spatiale",
    "missions orbitales", "exploration interplanétaire", "réalisations des agences spatiales", "débris spatiaux",
    "collaborations en matière de recherche spatiale", "innovations technologiques spatiales", "communications par satellite", "conférences de l'industrie spatiale", "recherche scientifique planétaire",
    "tendances de l'industrie spatiale", "histoire de l'exploration spatiale", "exploration cosmique", "sécurité des voyages spatiaux", "défis de l'industrie spatiale",
    "technologies de lancement de fusées", "progrès de la science spatiale", "recherche en mécanique orbitale", "documentaire sur l'exploration spatiale", "impact de l'industrie spatiale",
    "traités spatiaux internationaux", "missions d'exploration spatiale", "partenariats avec l'industrie spatiale", "succès de lancement de fusées", "applications des technologies spatiales",
    "observation des corps célestes", "percées astronomiques", "technologies des engins spatiaux", "documentaires sur l'exploration spatiale", "avancées en matière de lancement de fusées",
    "innovations en mécanique orbitale", "conférences de l'industrie spatiale", "initiatives de recherche spatiale", "réalisations en matière d'exploration spatiale", "objectifs d'exploration spatiale",
    "technologies de communication par satellite", "collaborations avec l'industrie spatiale", "innovations en matière de propulsion de fusée", "conférences sur les technologies spatiales", "histoire de l'exploration spatiale",
    "documentaires d'exploration cosmique", "mesures de sécurité des voyages dans l'espace", "défis et solutions de l'industrie spatiale", "impact de l'industrie spatiale sur la société",
    "mesures de sécurité pour le lancement de fusées", "recherche sur les technologies spatiales", "technologies d'observation des corps célestes", "carrière", "emplois", "croissance",
    "documentation sur les découvertes astronomiques", "développement des technologies des engins spatiaux", "impact des documentaires sur l'exploration spatiale", "avancées des technologies de lancement de fusées", "résultats des conférences de l'industrie spatiale",
    "résultats des initiatives de recherche spatiale", "impact des réalisations de l'exploration spatiale", "résultats des objectifs de l'exploration spatiale", "impact des technologies de communication par satellite", "résultats des collaborations avec l'industrie spatiale",
    "résultats des innovations en matière de propulsion de fusée", "résultats des conférences sur la technologie spatiale", "documentation sur l'histoire de l'exploration spatiale", "impact des documentaires sur l'exploration cosmique", "résultats des mesures de sécurité des voyages spatiaux",
    "les défis de l'industrie spatiale et les résultats des solutions", "l'impact de l'industrie spatiale sur les résultats de la société", "les résultats des partenariats d'exploration spatiale",
    "résultats des mesures de sécurité des lancements de fusées", "résultats de la recherche sur les technologies spatiales", "impact des technologies d'observation des corps célestes", "impact de la documentation des découvertes astronomiques", "résultats du développement des technologies des engins spatiaux",
    "technologies de lancement de fusée avancées", "impact des résultats", "impact des résultats des conférences de l'industrie spatiale", "impact des résultats des initiatives de recherche spatiale", "impact des réalisations de l'exploration spatiale sur la société",
    "impact des technologies de communication par satellite sur la société", "impact sur les résultats des collaborations avec l'industrie spatiale", "impact sur les résultats des innovations en matière de propulsion des fusées", "impact sur les résultats des conférences sur les technologies spatiales",
    "Impact des documentaires d'exploration cosmique sur la société", "Impact sur les résultats des mesures de sécurité des voyages spatiaux", "Impact sur les résultats des défis et des solutions de l'industrie spatiale", "Impact des tendances de l'exploration spatiale sur la société",
    "impact de l'industrie spatiale sur les résultats de la société", "impact des résultats des mesures de sécurité des lancements de fusées", "impact des résultats de la recherche sur les technologies spatiales",
    "l'impact des technologies d'observation des corps célestes sur la société", "l'impact de la documentation des découvertes astronomiques sur la société", "l'impact des résultats du développement des technologies des engins spatiaux", "l'impact des documentaires d'exploration spatiale sur les résultats de la société",
    "Les avancées technologiques en matière de lancement de fusées ont un impact sur la société", "Les résultats des conférences de l'industrie spatiale ont un impact sur la société", "Les résultats des initiatives de recherche spatiale ont un impact sur la société", "Les réalisations de l'exploration spatiale ont un impact sur les résultats de la société", "Droit de l'espace", "Droit international de l'espace", "Traité sur l'espace extra-atmosphérique", "gouvernance spatiale"
]

research_technology_keywords =[
    "Organisation de recherche", "technologie", "satellite", "télescope", "astronomie", "innovation", "panneau", "système solaire", "directeur adjoint", "équipage", "pluie de météores", "météore",
    "douche", "vols spatiaux habités", "progrès scientifique", "R&D", "Nébuleuse", "intelligence artificielle", "apprentissage automatique", "traitement de pointe", "théories", "recherche scientifique",
    "laboratoire", "expérience", "découverte", "vol spatial humain", "invention", "Space Edge computing", "Edge computing", "Artemis", "Dr", "débris spatiaux", "chercheur", "scientifique", "percée",
    "analyse de données", "progrès technologique", "défis mondiaux", "changement climatique", "catastrophes naturelles", "zéro net", "SpaceX", "pointe", "prototype", "biotechnologie", "nanotechnologie",
    "ingénierie", "télescope James Webb", "James Webb", "Dr", "scientifique en chef", "scientifique", "étude de recherche", "recherche universitaire", "méthodologie de recherche", "projet de recherche",
    "concours", "lancement de fusées", "communauté scientifique", "mission", "STEM", "aurore", "années-lumière Depuis la terre", "résultats de recherche", "document de recherche", "institut de recherche",
    "subvention de recherche", "collaboration de recherche", "système solaire", "science", "aurores", "recherche et développement", "technologies innovantes", "technologies émergentes", "tendances technologiques",
    "transfert de technologie", "Mars", "systèmes spatiaux", "adoption de technologies", "intégration technologique", "innovation technologique", "innovation en recherche", "découverte scientifique",
    "catastrophes naturelles", "communauté scientifique", "littérature scientifique", "revue scientifique", "à comité de lecture", "conférence scientifique", "feux de brousse", "inondations", "lancement",
    "recherche expérimentale", "recherche appliquée", "recherche fondamentale", "percée scientifique", "publication de recherche", "éclipses lunaires", "éthique de la recherche", "financement de la recherche",
    "résultats de la recherche", "impact de la recherche", "qualité de la recherche", "missions Artemis", "recherche biomédicale", "biomédical", 'secteur technologique', 'solutions technologiques',
    'technologie de pointe', 'technologie avancée', 'développement technologique', 'années-lumière', 'évaluation technologique', 'écosystème dinnovation', 'infrastructure de recherche', 'excellence en recherche',
    'progrès technologiques', 'éclipses solaires', 'Saturne', 'partenariat de recherche', 'collaboration en matière de recherche', 'réseau de recherche', 'normes technologiques', 'initiative de recherche',
    'face cachée de la Lune', 'Chandrayaan', 'convergence technologique', 'centre de recherche', 'axé sur la technologie', 'installations de recherche', 'gestion technologique', 'Terre', 'Rover', 'oxygène',
    'Président', 'programme de recherche', 'investissement technologique', 'stratégie dinnovation', 'écosystème de recherche', 'marché technologique', 'astronomes', 'astéroïde', 'congrès', 'axe de recherche',
    'paysage technologique', 'pôle de recherche', 'pôle technologique', 'défis de recherche', 'défis technologiques', 'Voie lactée', 'stratosphère', 'percées en recherche', 'impact technologique',
    'recherche et innovation', 'déploiement technologique', 'recherche et développement', 'basse atmosphère', 'atmosphère', 'solutions technologiques', 'impact de la recherche', 'tendances technologiques',
    'intégration de la recherche', 'adoption de la technologie', 'prévisions météorologiques', 'événements climatiques', 'frontière de la recherche', 'frontière technologique', 'paysage de la recherche',
    'paysage technologique', 'programme de recherche', 'ciel', 'éclipse lunaire', 'agenda technologique', 'méthodologies de recherche', 'transformation technologique', 'leadership en recherche',
    'leadership technologique', 'étoile', 'galaxies', 'Vénus', 'capacités de recherche', 'capacités technologiques', 'collaboration en matière de recherche', 'collaboration technologique',
    'avancement de la recherche', 'Rover', 'atelier en ligne', 'professeurs', 'recherche', 'universitaires', 'universités', 'progrès technologique', 'résultats de la recherche', 'résultats technologiques',
    'excellence de la recherche', 'excellence technologique', 'pluies de météores', 'Journée universitaire', 'stratégie de recherche', 'stratégie technologique', 'recherche et technologie',
    'technologie et innovation', 'recherche et développement', 'lacs', 'rivières', 'flux', 'environnement', 'changements climatiques', 'Pêche', 'Océans', 'technologie et société', 'recherche et industrie',
    'technologie et progrès', 'recherche et innovation', 'Lune', 'antenne pour lespace lointain', 'espace lointain', 'technologie et progrès', 'tendances en recherche et technologie', 'technologie et avenir',
    'tendances en recherche et développement', 'astrophotographe', 'hydrologie', 'océanographie', 'Webb', 'tendances technologiques et dinnovation', 'impact de la recherche et de la technologie',
    'impact de la technologie et de la société', 'impact de la recherche et du développement', 'incendies de forêt', 'technologie et affaires', 'recherche et solutions technologiques', 'technologie et défis mondiaux',
    'recherche et intégration technologique', 'CubeSats', 'technologie et croissance économique', 'recherche et convergence technologique', 'technologie et durabilité', 'recherche et collaboration technologique',
    'Rosetta', 'progrès de la technologie et de la recherche', 'innovation et technologie', 'recherche et progrès technologiques', 'excellence de la technologie et de la recherche',
    'partenariat de recherche et de technologie', 'technologie et installations de recherche', 'investissement dans la recherche et la technologie', 'capacités technologiques et de recherche', 'station de recherche',
    'recherche et déploiement technologique', 'programme technologique et recherche', 'recherche et leadership technologique', 'transformation technologique et recherche', 'paysage de la recherche et de la technologie',
    'défis de la technologie et de la recherche', 'résultats de la recherche et de la technologie', 'stratégie de la technologie et de la recherche', 'COSPAR', 'Copernicus EU', 'collaboration en matière de recherche et de technologie',
    'avancement de la technologie et de la recherche', 'résultats de la recherche et de la technologie', 'excellence en matière de technologie et de recherche', 'NASA', 'charge utile', 'poussée du vide',
    'stratégie de recherche et technologie', 'capacités de technologie et de recherche', 'soleil', 'solutions de recherche et technologie', 'impact de la technologie et de la recherche', 'intégration de la recherche et de la technologie',
    'technologie et innovation en matière de recherche', 'recherche et frontière technologique', 'paysage technologique et de la recherche', 'Lire la suite', 'recherche et transformation technologique',
    'technologie et méthodologies de recherche', 'recherche et convergence technologique', 'partenariat technologique et de recherche', 'miroir flottant', 'ondes spatiales', 'recherche et déploiement technologique',
    'technologie et infrastructure de recherche', 'recherche et collaboration technologique', 'technologie et réseau de recherche', 'centre de recherche et de technologie', 'technologie et programme de recherche',
    'installations de recherche et de technologie', 'centre de technologie et de recherche', 'technologie laser', 'recherche dans les pays en développement', 'leadership en matière de recherche et de technologie',
    'défis de la technologie et de la recherche', 'impact de la recherche et de la technologie', 'agenda technologique et de recherche', 'Découvrir', 'pôle de recherche et de technologie', 'technologie et programme de recherche',
    'infrastructure de recherche et de technologie', 'Copernicus', 'réseau de technologie et de recherche', 'mars', 'cycles de leau', 'Observation de la Terre', 'centre de recherche et de technologie',
    'technologie et écosystème de recherche', 'recherche et investissement technologique', 'technologie et capacités de recherche', 'Dr.', '#NASA', '#ESA', '#JAXA', '#ISRO', '#CSA', '#UKSA', '#UAESA', '#LSA', '#ISA', '#DLR', '#CNES',
    'recherche et déploiement technologique', 'convergence de la technologie et de la recherche', 'paysage de la recherche et de la technologie', 'nuages', 'expertise technique', 'excellence en technologie et en recherche',
    'scientifique planétaire', "Centre d'observation de la Terre", 'spécialiste', 'observation de la Terre', 'météorologie', 'météo', 'éclipse lunaire', 'recherche sur les médicaments dans lespace',
    'recherche sur les médicaments', 'humidité du sol', 'satellites', 'type de végétation', 'utilisation des terres', 'Prof.', 'système solaire'
] 


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
output_file_path = 'C:\\Users\\shake\\Desktop\\MSC- Data Science\\Thesis\\Tables\\Agancies Data-CrowdTangle\\CNES.csv'
data.to_csv(output_file_path, index=False,encoding='utf-8')

# Display the updated classification in the DataFrame
print(data[['Message', 'International Relations_Related', 'Education and Community_Related', 'Space Industry_Related', 'Research and Technology_Related']])
