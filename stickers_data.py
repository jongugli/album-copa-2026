"""
Dados de todas as figurinhas do Álbum Panini Copa do Mundo 2026.

Total: 980 figurinhas
  - FWC : 20 figurinhas de abertura (IDs: FWC 1 … FWC 20)
  - 48 seleções × 20 figurinhas cada = 960 (IDs: BRA 1 … BRA 20, FRA 1 … etc.)

ID de cada figurinha: "<CÓDIGO> <NÚMERO>", ex: "FRA 10", "BRA 5", "FWC 3".

Estrutura padrão de cada seleção (20 figurinhas):
  1  Brasão ✦            (foil)
  2  Foto Elenco
  3  Estádio / Sede
  4  Capitão ✦           (foil)
  5–18  14 jogadores
  19 Craque do Time ✦   (foil)
  20 Figurinha Especial ✦ (foil)
"""


def make_stickers(code: str, labels: list) -> list:
    """Gera figurinhas com IDs no formato 'CODE N'."""
    if len(labels) != 20:
        raise ValueError(f"Seção '{code}' precisa de exatamente 20 labels (recebeu {len(labels)})")
    return [{"id": f"{code} {i}", "label": label} for i, label in enumerate(labels, start=1)]


def _team(name: str, captain: str, players: list) -> list:
    """Gera os 20 labels padrão de uma seleção (capitão + 14 jogadores + especiais)."""
    if len(players) != 14:
        raise ValueError(f"{name}: precisa de 14 jogadores (recebeu {len(players)})")
    return [
        f"Brasão {name} ✦",
        "Foto Elenco",
        "Estádio / Sede",
        f"{captain} ✦ (Capitão)",
        *players,
        "Craque do Time ✦",
        "Figurinha Especial ✦",
    ]


# ─── ABERTURA ────────────────────────────────────────────────────────────────

SECTIONS = [
    {
        "id": "fwc",
        "label": "Copa do Mundo 2026",
        "emoji": "🌍",
        "color": "#f59e0b",
        "stickers": make_stickers("FWC", [
            "Capa / Logotipo ✦",
            "Troféu FIFA ✦",
            "Mascote Oficial ✦",
            "Mapa das Sedes",
            "Estádio MetLife (Nova York)",
            "Estádio Rose Bowl (Los Angeles)",
            "Estádio AT&T (Dallas)",
            "Estádio Azteca (Cidade do México)",
            "Estádio BC Place (Vancouver)",
            "Estádio BMO Field (Toronto)",
            "Sede Nova York / New Jersey",
            "Sede Los Angeles",
            "Sede Dallas",
            "Sede Miami",
            "Sede Seattle",
            "Sede San Francisco",
            "Sede Kansas City",
            "Sede Guadalajara",
            "Sede Monterrey",
            "Início da Copa 2026 ✦",
        ]),
    },

    # ─── EUROPA (16 seleções) ─────────────────────────────────────────────────

    {
        "id": "fra", "label": "França", "emoji": "🇫🇷", "color": "#1d4ed8",
        "stickers": make_stickers("FRA", _team("França", "Kylian Mbappé", [
            "Antoine Griezmann", "Ousmane Dembélé", "Marcus Thuram",
            "Aurélien Tchouaméni", "Adrien Rabiot", "Eduardo Camavinga",
            "N'Golo Kanté", "Raphaël Varane", "Dayot Upamecano",
            "Théo Hernandez", "Mike Maignan", "Randal Kolo Muani",
            "Bradley Barcola", "Mathys Tel",
        ])),
    },
    {
        "id": "eng", "label": "Inglaterra", "emoji": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "color": "#dc2626",
        "stickers": make_stickers("ENG", _team("Inglaterra", "Harry Kane", [
            "Jude Bellingham", "Phil Foden", "Bukayo Saka",
            "Declan Rice", "Trent Alexander-Arnold", "John Stones",
            "Marc Guehi", "Kyle Walker", "Jordan Pickford",
            "Marcus Rashford", "Cole Palmer", "Conor Gallagher",
            "Anthony Gordon", "Morgan Rogers",
        ])),
    },
    {
        "id": "esp", "label": "Espanha", "emoji": "🇪🇸", "color": "#fbbf24",
        "stickers": make_stickers("ESP", _team("Espanha", "Rodri", [
            "Pedri", "Gavi", "Lamine Yamal",
            "Nico Williams", "Mikel Merino", "Aymeric Laporte",
            "Pau Torres", "Alejandro Grimaldo", "David Raya",
            "Álvaro Morata", "Dani Olmo", "Fabián Ruiz",
            "Ferran Torres", "Yeremy Pino",
        ])),
    },
    {
        "id": "por", "label": "Portugal", "emoji": "🇵🇹", "color": "#b91c1c",
        "stickers": make_stickers("POR", _team("Portugal", "Cristiano Ronaldo", [
            "Bruno Fernandes", "Bernardo Silva", "João Félix",
            "Rafael Leão", "Vitinha", "Rúben Dias",
            "Pepe", "Nuno Mendes", "Diogo Costa",
            "Gonçalo Ramos", "João Neves", "Pedro Neto",
            "Otávio", "Rúben Neves",
        ])),
    },
    {
        "id": "ger", "label": "Alemanha", "emoji": "🇩🇪", "color": "#6b7280",
        "stickers": make_stickers("GER", _team("Alemanha", "Manuel Neuer", [
            "Jamal Musiala", "Florian Wirtz", "Kai Havertz",
            "Leroy Sané", "Leon Goretzka", "Joshua Kimmich",
            "Antonio Rüdiger", "Nico Schlotterbeck", "David Raum",
            "Serge Gnabry", "Niclas Füllkrug", "Robert Andrich",
            "Konrad Laimer", "Maximilian Mittelstädt",
        ])),
    },
    {
        "id": "ned", "label": "Holanda", "emoji": "🇳🇱", "color": "#f97316",
        "stickers": make_stickers("NED", _team("Holanda", "Virgil van Dijk", [
            "Cody Gakpo", "Memphis Depay", "Xavi Simons",
            "Frenkie de Jong", "Tijjani Reijnders", "Nathan Aké",
            "Denzel Dumfries", "Bart Verbruggen", "Donyell Malen",
            "Wout Weghorst", "Brian Brobbey", "Steven Bergwijn",
            "Joshua Zirkzee", "Mark Flekken",
        ])),
    },
    {
        "id": "bel", "label": "Bélgica", "emoji": "🇧🇪", "color": "#ef4444",
        "stickers": make_stickers("BEL", _team("Bélgica", "Kevin De Bruyne", [
            "Romelu Lukaku", "Yannick Carrasco", "Amadou Onana",
            "Jan Vertonghen", "Thibaut Courtois", "Leandro Trossard",
            "Charles De Ketelaere", "Lois Openda", "Jérémy Doku",
            "Timothy Castagne", "Arthur Theate", "Hans Vanaken",
            "Maxim De Cuyper", "Orel Mangala",
        ])),
    },
    {
        "id": "ita", "label": "Itália", "emoji": "🇮🇹", "color": "#1d4ed8",
        "stickers": make_stickers("ITA", _team("Itália", "Gianluigi Donnarumma", [
            "Federico Chiesa", "Nicolò Barella", "Sandro Tonali",
            "Lorenzo Pellegrini", "Alessandro Bastoni", "Giovanni Di Lorenzo",
            "Gianluca Scamacca", "Giacomo Raspadori", "Davide Frattesi",
            "Federico Dimarco", "Davide Calabria", "Nicolò Zaniolo",
            "Mateo Retegui", "Riccardo Calafiori",
        ])),
    },
    {
        "id": "cro", "label": "Croácia", "emoji": "🇭🇷", "color": "#dc2626",
        "stickers": make_stickers("CRO", _team("Croácia", "Luka Modrić", [
            "Ivan Perišić", "Marcelo Brozović", "Mateo Kovačić",
            "Mario Pašalić", "Lovro Majer", "Joško Gvardiol",
            "Dejan Lovren", "Josip Juranović", "Dominik Livaković",
            "Andrej Kramarić", "Bruno Petković", "Nikola Vlašić",
            "Luka Sučić", "Josip Stanišić",
        ])),
    },
    {
        "id": "sui", "label": "Suíça", "emoji": "🇨🇭", "color": "#dc2626",
        "stickers": make_stickers("SUI", _team("Suíça", "Granit Xhaka", [
            "Xherdan Shaqiri", "Breel Embolo", "Remo Freuler",
            "Denis Zakaria", "Manuel Akanji", "Nico Elvedi",
            "Ricardo Rodríguez", "Yann Sommer", "Dan Ndoye",
            "Zeki Amdouni", "Michel Aebischer", "Christian Fassnacht",
            "Fabian Rieder", "Leonidas Stergiou",
        ])),
    },
    {
        "id": "den", "label": "Dinamarca", "emoji": "🇩🇰", "color": "#dc2626",
        "stickers": make_stickers("DEN", _team("Dinamarca", "Christian Eriksen", [
            "Pierre-Emile Höjbjerg", "Martin Braithwaite", "Yussuf Poulsen",
            "Thomas Delaney", "Mathias Jensen", "Simon Kjær",
            "Andreas Christensen", "Joakim Mæhle", "Kasper Schmeichel",
            "Jonas Wind", "Andreas Skov Olsen", "Mikkel Damsgaard",
            "Rasmus Højlund", "Jesper Lindstrøm",
        ])),
    },
    {
        "id": "srb", "label": "Sérvia", "emoji": "🇷🇸", "color": "#c2410c",
        "stickers": make_stickers("SRB", _team("Sérvia", "Dušan Vlahović", [
            "Aleksandar Mitrović", "Nemanja Matić", "Sergej Milinković-Savić",
            "Filip Kostić", "Andrija Živković", "Strahinja Pavlović",
            "Nikola Milenković", "Filip Mladenović", "Vanja Milinković-Savić",
            "Luka Jović", "Saša Lukić", "Ivan Ilić",
            "Dušan Tadić", "Nemanja Radonjić",
        ])),
    },
    {
        "id": "pol", "label": "Polônia", "emoji": "🇵🇱", "color": "#dc2626",
        "stickers": make_stickers("POL", _team("Polônia", "Robert Lewandowski", [
            "Piotr Zieliński", "Arkadiusz Milik", "Kamil Grosicki",
            "Grzegorz Krychowiak", "Mateusz Klich", "Jan Bednarek",
            "Kamil Glik", "Bartosz Bereszyński", "Wojciech Szczęsny",
            "Karol Świderski", "Damian Szymański", "Przemysław Frankowski",
            "Jakub Kiwior", "Nicola Zalewski",
        ])),
    },
    {
        "id": "tur", "label": "Turquia", "emoji": "🇹🇷", "color": "#dc2626",
        "stickers": make_stickers("TUR", _team("Turquia", "Hakan Çalhanoğlu", [
            "Arda Güler", "Kerem Aktürkoğlu", "Salih Özcan",
            "Orkun Kökçü", "Merih Demiral", "Çağlar Söyüncü",
            "Ferdi Kadıoğlu", "Uğurcan Çakır", "Cenk Tosun",
            "Barış Yıldız", "Barış Alper Yılmaz", "Kenan Karaman",
            "Burak Yılmaz", "Abdülkerim Bardakcı",
        ])),
    },
    {
        "id": "sco", "label": "Escócia", "emoji": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "color": "#1d4ed8",
        "stickers": make_stickers("SCO", _team("Escócia", "Andy Robertson", [
            "Scott McTominay", "Che Adams", "Ryan Christie",
            "Billy Gilmour", "John McGinn", "Grant Hanley",
            "Kieran Tierney", "Stephen O'Donnell", "Angus Gunn",
            "Lyndon Dykes", "Ryan Porteous", "Lewis Ferguson",
            "Callum McGregor", "Nathan Patterson",
        ])),
    },
    {
        "id": "swe", "label": "Suécia", "emoji": "🇸🇪", "color": "#fbbf24",
        "stickers": make_stickers("SWE", _team("Suécia", "Emil Forsberg", [
            "Viktor Gyökeres", "Dejan Kulusevski", "Alexander Isak",
            "Victor Lindelöf", "Jens Cajuste", "Ludwig Augustinsson",
            "Pontus Jansson", "Robin Olsen", "Jordan Larsson",
            "Anthony Elanga", "Mattias Svanberg", "Jesper Karlsson",
            "Sam Larsson", "Filip Helander",
        ])),
    },

    # ─── AMÉRICA DO SUL (8 seleções) ──────────────────────────────────────────

    {
        "id": "bra", "label": "Brasil", "emoji": "🇧🇷", "color": "#16a34a",
        "stickers": make_stickers("BRA", _team("Brasil", "Marquinhos", [
            "Vinicius Jr.", "Rodrygo", "Raphinha",
            "Richarlison", "Casemiro", "Bruno Guimarães",
            "Lucas Paquetá", "Éder Militão", "Danilo",
            "Alisson", "Endrick", "Gabriel Martinelli",
            "Gabriel (Brighton)", "Savinho",
        ])),
    },
    {
        "id": "arg", "label": "Argentina", "emoji": "🇦🇷", "color": "#60a5fa",
        "stickers": make_stickers("ARG", _team("Argentina", "Lionel Messi", [
            "Julián Álvarez", "Lautaro Martínez", "Rodrigo De Paul",
            "Alexis Mac Allister", "Enzo Fernández", "Nicolás Otamendi",
            "Cristian Romero", "Nahuel Molina", "Emiliano Martínez",
            "Thiago Almada", "Ángel Di María", "Paulo Dybala",
            "Nicolás González", "Germán Pezzella",
        ])),
    },
    {
        "id": "uru", "label": "Uruguai", "emoji": "🇺🇾", "color": "#60a5fa",
        "stickers": make_stickers("URU", _team("Uruguai", "Diego Godín", [
            "Darwin Núñez", "Federico Valverde", "Rodrigo Bentancur",
            "Matías Vecino", "José María Giménez", "Mathías Olivera",
            "Sergio Rochet", "Nicolás De la Cruz", "Brian Rodríguez",
            "Facundo Torres", "Manuel Ugarte", "Ronald Araújo",
            "Facundo Pellistri", "Maxi Gómez",
        ])),
    },
    {
        "id": "col", "label": "Colômbia", "emoji": "🇨🇴", "color": "#fbbf24",
        "stickers": make_stickers("COL", _team("Colômbia", "James Rodríguez", [
            "Luis Díaz", "Juan Cuadrado", "Wilmar Barrios",
            "Mateus Uribe", "Yerry Mina", "Dávinson Sánchez",
            "David Ospina", "Rafael Santos Borré", "Jhon Durán",
            "Luis Sinisterra", "Déiver Machado", "Jorge Carrascal",
            "Jefferson Lerma", "Jhon Córdoba",
        ])),
    },
    {
        "id": "ecu", "label": "Equador", "emoji": "🇪🇨", "color": "#fbbf24",
        "stickers": make_stickers("ECU", _team("Equador", "Enner Valencia", [
            "Moisés Caicedo", "Jeremy Sarmiento", "Gonzalo Plata",
            "Carlos Gruezo", "Romario Ibarra", "Byron Castillo",
            "Piero Hincapié", "Pervis Estupiñán", "Hernán Galíndez",
            "Ángel Mena", "Michael Estrada", "Kevin Rodríguez",
            "Jackson Porozo", "Alan Minda",
        ])),
    },
    {
        "id": "ven", "label": "Venezuela", "emoji": "🇻🇪", "color": "#dc2626",
        "stickers": make_stickers("VEN", _team("Venezuela", "Tomás Rincón", [
            "Salomón Rondón", "Yeferson Soteldo", "Josef Martínez",
            "Darwin Machis", "Roberto Rosales", "Jhon Chancellor",
            "Alexander González", "Wuilker Faríñez", "Adalberto Peñaranda",
            "Júnior Moreno", "Yangel Herrera", "Christian Makoun",
            "Eric Ramírez", "Rolf Feltscher",
        ])),
    },
    {
        "id": "chi", "label": "Chile", "emoji": "🇨🇱", "color": "#dc2626",
        "stickers": make_stickers("CHI", _team("Chile", "Arturo Vidal", [
            "Alexis Sánchez", "Ben Brereton Díaz", "Charles Aránguiz",
            "Erick Pulgar", "Guillermo Maripán", "Gary Medel",
            "Claudio Bravo", "Eduardo Vargas", "Pablo Galdames",
            "Darío Osorio", "Víctor Dávila", "Diego Valdés",
            "Paulo Díaz", "Sebastián Vegas",
        ])),
    },
    {
        "id": "per", "label": "Peru", "emoji": "🇵🇪", "color": "#dc2626",
        "stickers": make_stickers("PER", _team("Peru", "Paolo Guerrero", [
            "André Carrillo", "Gianluca Lapadula", "Renato Tapia",
            "Christian Cueva", "Pedro Aquino", "Alexander Callens",
            "Miguel Araujo", "Luis Advíncula", "Pedro Gallese",
            "Edison Flores", "Aldo Corzo", "Andy Polo",
            "Joao Grimaldo", "Raziel García",
        ])),
    },

    # ─── CONCACAF (6 seleções) ────────────────────────────────────────────────

    {
        "id": "usa", "label": "Estados Unidos", "emoji": "🇺🇸", "color": "#3b82f6",
        "stickers": make_stickers("USA", _team("Estados Unidos", "Christian Pulisic", [
            "Tyler Adams", "Gio Reyna", "Weston McKennie",
            "Josh Sargent", "Tim Weah", "Matt Turner",
            "Sergiño Dest", "Yunus Musah", "Caden Clark",
            "Folarin Balogun", "Ricardo Pepi", "Joe Scally",
            "Malik Tillman", "Daryl Dike",
        ])),
    },
    {
        "id": "can", "label": "Canadá", "emoji": "🇨🇦", "color": "#ef4444",
        "stickers": make_stickers("CAN", _team("Canadá", "Alphonso Davies", [
            "Jonathan David", "Cyle Larin", "Tajon Buchanan",
            "Stephen Eustáquio", "Milan Borjan", "Sam Adekugbe",
            "Alistair Johnston", "Derek Cornelius", "Ismael Koné",
            "Liam Millar", "Charles-Andreas Brym", "Jacob Shaffelburg",
            "Richie Laryea", "Theo Bair",
        ])),
    },
    {
        "id": "mex", "label": "México", "emoji": "🇲🇽", "color": "#22c55e",
        "stickers": make_stickers("MEX", _team("México", "Guillermo Ochoa", [
            "Hirving Lozano", "Raúl Jiménez", "Héctor Herrera",
            "Edson Álvarez", "César Montes", "Alexis Vega",
            "Uriel Antuna", "Santiago Giménez", "Roberto Alvarado",
            "Luis Chávez", "Kevin Álvarez", "Julián Araujo",
            "Johan Vásquez", "Carlos Rodríguez",
        ])),
    },
    {
        "id": "pan", "label": "Panamá", "emoji": "🇵🇦", "color": "#ef4444",
        "stickers": make_stickers("PAN", _team("Panamá", "Aníbal Godoy", [
            "Rolando Blackburn", "José Fajardo", "Adalberto Carrasquilla",
            "Gabriel Torres", "Roderick Miller", "Fidel Escobar",
            "Harold Cummings", "Luis Mejía", "Cecilio Waterman",
            "Alberto Quintero", "Ismael Díaz", "Édgar Bárcenas",
            "Michael Murillo", "César Yanis",
        ])),
    },
    {
        "id": "crc", "label": "Costa Rica", "emoji": "🇨🇷", "color": "#1d4ed8",
        "stickers": make_stickers("CRC", _team("Costa Rica", "Keylor Navas", [
            "Bryan Ruiz", "Joel Campbell", "Celso Borges",
            "Yeltsin Tejeda", "Ronald Matarrita", "Bryan Oviedo",
            "Óscar Duarte", "Francisco Calvo", "Patrick Sequeira",
            "Alonso Martínez", "Johan Venegas", "Marco Ureña",
            "Anthony Contreras", "Jewison Bennette",
        ])),
    },
    {
        "id": "jam", "label": "Jamaica", "emoji": "🇯🇲", "color": "#fbbf24",
        "stickers": make_stickers("JAM", _team("Jamaica", "Leon Bailey", [
            "Michail Antonio", "Bobby Decordova-Reid", "Shamar Nicholson",
            "Je-Vaughn Watson", "Kemar Lawrence", "Gregory Leigh",
            "Damion Lowe", "Oniel Fisher", "Andre Blake",
            "Liam Moore", "Daniel Johnson", "Ethan Pinnock",
            "Demarai Gray", "Amari'i Bell",
        ])),
    },

    # ─── ÁFRICA (9 seleções) ──────────────────────────────────────────────────

    {
        "id": "mar", "label": "Marrocos", "emoji": "🇲🇦", "color": "#dc2626",
        "stickers": make_stickers("MAR", _team("Marrocos", "Achraf Hakimi", [
            "Hakim Ziyech", "Youssef En-Nesyri", "Sofyan Amrabat",
            "Azzedine Ounahi", "Selim Amallah", "Romain Saïss",
            "Nayef Aguerd", "Noussair Mazraoui", "Yassine Bounou",
            "Abdessamad Ezzalzouli", "Anass Zaroury", "Bilal El Khannouss",
            "Abde Ezzalzouli", "Jawad El Yamiq",
        ])),
    },
    {
        "id": "nga", "label": "Nigéria", "emoji": "🇳🇬", "color": "#16a34a",
        "stickers": make_stickers("NGA", _team("Nigéria", "Victor Osimhen", [
            "Wilfred Ndidi", "Samuel Chukwueze", "Alex Iwobi",
            "Joe Aribo", "Terem Moffi", "William Troost-Ekong",
            "Semi Ajayi", "Calvin Bassey", "Francis Uzoho",
            "Cyriel Dessers", "Taiwo Awoniyi", "Ademola Lookman",
            "Kelechi Iheanacho", "Chidera Ejuke",
        ])),
    },
    {
        "id": "sen", "label": "Senegal", "emoji": "🇸🇳", "color": "#16a34a",
        "stickers": make_stickers("SEN", _team("Senegal", "Sadio Mané", [
            "Kalidou Koulibaly", "Ismaila Sarr", "Idrissa Gueye",
            "Cheikhou Kouyaté", "Nampalys Mendy", "Abdou Diallo",
            "Saliou Ciss", "Édouard Mendy", "Boulaye Dia",
            "Nicolas Jackson", "Pape Matar Sarr", "Habib Diallo",
            "Lamine Camara", "Formose Mendy",
        ])),
    },
    {
        "id": "egy", "label": "Egito", "emoji": "🇪🇬", "color": "#dc2626",
        "stickers": make_stickers("EGY", _team("Egito", "Mohamed Salah", [
            "Mohamed Elneny", "Omar Marmoush", "Emam Ashour",
            "Tarek Hamed", "Ahmed Hegazi", "Mohamed Abdelmonem",
            "Omar Kamal", "Mohamed El-Shenawy", "Mostafa Mohamed",
            "Ahmed Sayed Zizo", "Ramadan Sobhi", "Kahraba",
            "Trezeguet", "Ahmed Fatouh",
        ])),
    },
    {
        "id": "cmr", "label": "Camarões", "emoji": "🇨🇲", "color": "#16a34a",
        "stickers": make_stickers("CMR", _team("Camarões", "Eric Choupo-Moting", [
            "André Onana", "Bryan Mbeumo", "Vincent Aboubakar",
            "Frank Zambo Anguissa", "Martin Hongla", "Jean-Charles Castelletto",
            "Harold Moukoudi", "Collins Fai", "Karl Toko Ekambi",
            "Nicolas Nkoulou", "Léandre Tawamba", "Clinton Njie",
            "Gaëtan Bong", "Christopher Wooh",
        ])),
    },
    {
        "id": "civ", "label": "Costa do Marfim", "emoji": "🇨🇮", "color": "#f97316",
        "stickers": make_stickers("CIV", _team("Costa do Marfim", "Franck Kessié", [
            "Wilfried Zaha", "Sébastien Haller", "Nicolas Pépé",
            "Jean Michaël Seri", "Oumar Diakité", "Simon Deli",
            "Eric Bailly", "Serge Aurier", "Badra Ali Sangaré",
            "Amad Diallo", "Max-Alain Gradel", "Christian Kouamé",
            "Karim Konaté", "Odilon Kossounou",
        ])),
    },
    {
        "id": "gha", "label": "Gana", "emoji": "🇬🇭", "color": "#fbbf24",
        "stickers": make_stickers("GHA", _team("Gana", "Thomas Partey", [
            "Jordan Ayew", "André Ayew", "Mohammed Salisu",
            "Daniel-Kofi Kyereh", "Tariq Lamptey", "Daniel Amartey",
            "Alexander Djiku", "Baba Rahman", "Lawrence Ati-Zigi",
            "Iñaki Williams", "Felix Afena-Gyan", "Antoine Semenyo",
            "Mohammed Kudus", "Dede Ayew",
        ])),
    },
    {
        "id": "tun", "label": "Tunísia", "emoji": "🇹🇳", "color": "#dc2626",
        "stickers": make_stickers("TUN", _team("Tunísia", "Wahbi Khazri", [
            "Youssef Msakni", "Hannibal Mejbri", "Ellyes Skhiri",
            "Anis Slimane", "Naim Sliti", "Yassine Meriah",
            "Montassar Talbi", "Ali Maaloul", "Aymen Dahmen",
            "Seifeddine Jaziri", "T.Y. Khenissi", "Mohamed Drager",
            "Aïssa Laïdouni", "Nader Ghandri",
        ])),
    },
    {
        "id": "alg", "label": "Argélia", "emoji": "🇩🇿", "color": "#16a34a",
        "stickers": make_stickers("ALG", _team("Argélia", "Riyad Mahrez", [
            "Islam Slimani", "Ramy Bensebaini", "Ismael Bennacer",
            "Baghdad Bounedjah", "Youcef Belaïli", "Amar Bennacer",
            "Djamel Benlamri", "Hicham Boudaoui", "Raïs M'Bolhi",
            "Youcef Atal", "Sofiane Feghouli", "Haris Belkebla",
            "Farès Chaïbi", "Said Benrahma",
        ])),
    },

    # ─── ÁSIA (8 seleções) ────────────────────────────────────────────────────

    {
        "id": "jpn", "label": "Japão", "emoji": "🇯🇵", "color": "#dc2626",
        "stickers": make_stickers("JPN", _team("Japão", "Maya Yoshida", [
            "Takumi Minamino", "Daichi Kamada", "Ritsu Doan",
            "Wataru Endo", "Junya Ito", "Takehiro Tomiyasu",
            "Yuto Nagatomo", "Shuichi Gonda", "Takuma Asano",
            "Kaoru Mitoma", "Ao Tanaka", "Daizen Maeda",
            "Ayase Ueda", "Hidemasa Morita",
        ])),
    },
    {
        "id": "kor", "label": "Coreia do Sul", "emoji": "🇰🇷", "color": "#dc2626",
        "stickers": make_stickers("KOR", _team("Coreia do Sul", "Son Heung-min", [
            "Hwang Hee-chan", "Lee Jae-sung", "Jung Woo-young",
            "Kim Min-jae", "Hwang In-beom", "Kim Young-gwon",
            "Lee Yong", "Kim Seung-gyu", "Cho Gue-sung",
            "Lee Gang-in", "Kwon Chang-hoon", "Oh Hyeon-gyu",
            "Hong Chul", "Jeong Woo-yeong",
        ])),
    },
    {
        "id": "aus", "label": "Austrália", "emoji": "🇦🇺", "color": "#fbbf24",
        "stickers": make_stickers("AUS", _team("Austrália", "Mat Ryan", [
            "Martin Boyle", "Mathew Leckie", "Aaron Mooy",
            "Ajdin Hrustic", "Ryan Rowles", "Miloš Degenek",
            "Trent Sainsbury", "Aziz Behich", "Andrew Redmayne",
            "Mitchell Duke", "Craig Goodwin", "Keanu Baccus",
            "Jackson Irvine", "Nestory Irankunda",
        ])),
    },
    {
        "id": "irn", "label": "Irã", "emoji": "🇮🇷", "color": "#16a34a",
        "stickers": make_stickers("IRN", _team("Irã", "Mehdi Taremi", [
            "Sardar Azmoun", "Alireza Jahanbakhsh", "Saeid Ezatolahi",
            "Alireza Beiranvand", "Saman Ghoddos", "Morteza Pouraliganji",
            "Majid Hosseini", "Ehsan Hajsafi", "H. Kanaanizadegan",
            "Karim Ansarifard", "Ramin Rezaeian", "Milad Mohammadi",
            "Ali Karimi", "Ahmad Noorollahi",
        ])),
    },
    {
        "id": "ksa", "label": "Arábia Saudita", "emoji": "🇸🇦", "color": "#16a34a",
        "stickers": make_stickers("KSA", _team("Arábia Saudita", "Mohammed Al-Owais", [
            "Salem Al-Dawsari", "Firas Al-Buraikan", "Saleh Al-Shehri",
            "Sami Al-Najei", "Ali Al-Bulaihi", "Hassan Tambakti",
            "Yasser Al-Shahrani", "Hattan Bahebri", "Abdulelah Al-Malki",
            "Mohamed Kanno", "Haitham Asiri", "Mohammed Al-Buraik",
            "Sultan Al-Ghannam", "Abdullah Al-Khaibri",
        ])),
    },
    {
        "id": "qat", "label": "Qatar", "emoji": "🇶🇦", "color": "#8b1a1a",
        "stickers": make_stickers("QAT", _team("Qatar", "Hassan Al-Haydos", [
            "Almoez Ali", "Akram Afif", "Abdulaziz Hatem",
            "Karim Boudiaf", "Bassam Al-Rawi", "Boualem Khoukhi",
            "Pedro Miguel", "Salah Zakaria", "Meshaal Barsham",
            "Mohammed Muntari", "Ismaeel Mohammad", "Assim Madibo",
            "Homam Ahmed", "Tarek Salman",
        ])),
    },
    {
        "id": "irq", "label": "Iraque", "emoji": "🇮🇶", "color": "#16a34a",
        "stickers": make_stickers("IRQ", _team("Iraque", "Ali Adnan", [
            "Mohanad Ali", "Amjad Attwan", "Safaa Hadi",
            "Ahmed Yasin", "Hussein Ali", "Ali Jabbar",
            "Alaa Abdul-Zahra", "Jalal Hassan", "Dhurgham Ismail",
            "Mustafa Mohammed", "Sherko Karimi", "Saad Natiq",
            "Ahmed Ibrahim", "Bashar Resan",
        ])),
    },
    {
        "id": "uzb", "label": "Uzbequistão", "emoji": "🇺🇿", "color": "#1d6b3e",
        "stickers": make_stickers("UZB", _team("Uzbequistão", "Eldor Shomurodov", [
            "Jamshid Iskanderov", "Sanjar Tursunov", "Jasur Yaxshiboyev",
            "Sherzod Nasrullayev", "Odil Ahmedov", "Otabek Shukurov",
            "Islom Tukhtahujaev", "Timur Djalilov", "Shukhrat Mukhammadiev",
            "Bobur Abdixoliqov", "Khojiakbar Alijonov", "Ortiq Zoirov",
            "Bahodir Jaloliddinov", "Muhammadkodir Hamrobekov",
        ])),
    },

    # ─── OCEANIA (1 seleção) ──────────────────────────────────────────────────

    {
        "id": "nzl", "label": "Nova Zelândia", "emoji": "🇳🇿", "color": "#6b7280",
        "stickers": make_stickers("NZL", _team("Nova Zelândia", "Chris Wood", [
            "Winston Reid", "Tim Payne", "Clayton Lewis",
            "Joe Bell", "Elijah Just", "Michael Boxall",
            "Liberato Cacace", "Storm Roux", "Stefan Marinovic",
            "Matthew Garbett", "Sarpreet Singh", "Marko Stamenic",
            "Deklan Wynne", "Callan Elliott",
        ])),
    },
]


def get_all_sticker_ids() -> list:
    """Retorna lista plana de todos os IDs de figurinhas."""
    return [s["id"] for sec in SECTIONS for s in sec["stickers"]]


def get_total() -> int:
    return sum(len(s["stickers"]) for s in SECTIONS)
