"""
Dados de todas as figurinhas do Álbum Panini Copa do Mundo 2026.

Total: 980 figurinhas
  - FWC : 20 figurinhas de abertura
  - 48 seleções × 20 figurinhas cada = 960

ID de cada figurinha: "<CÓDIGO> <NÚMERO>", ex: "FRA 10", "BRA 5", "FWC 3".

Estrutura padrão de cada seleção (20 figurinhas):
  1  Brasão
  2  Foto Elenco
  3–20  18 jogadores
"""


def make_stickers(code: str, labels: list) -> list:
    """Gera figurinhas com IDs no formato 'CODE N'."""
    if len(labels) != 20:
        raise ValueError(f"Seção '{code}' precisa de exatamente 20 labels (recebeu {len(labels)})")
    return [{"id": f"{code} {i}", "label": label} for i, label in enumerate(labels, start=1)]


def _team(name: str, players: list) -> list:
    """Gera os 20 labels de uma seleção: brasão + foto elenco + 18 jogadores."""
    if len(players) != 18:
        raise ValueError(f"{name}: precisa de 18 jogadores (recebeu {len(players)})")
    return [f"Brasão {name}", "Foto Elenco", *players]


# ─── ABERTURA ────────────────────────────────────────────────────────────────

SECTIONS = [
    {
        "id": "fwc", "label": "Copa do Mundo 2026", "emoji": "🌍", "color": "#f59e0b",
        "stickers": make_stickers("FWC", [
            "Capa / Logotipo",
            "Troféu FIFA",
            "Mascote Oficial",
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
            "Início da Copa 2026",
        ]),
    },

    # ─── EUROPA (16 seleções) ─────────────────────────────────────────────────

    {
        "id": "fra", "label": "França", "emoji": "🇫🇷", "color": "#1d4ed8",
        "stickers": make_stickers("FRA", _team("França", [
            "Kylian Mbappé", "Antoine Griezmann", "Ousmane Dembélé",
            "Marcus Thuram", "Aurélien Tchouaméni", "Adrien Rabiot",
            "Eduardo Camavinga", "N'Golo Kanté", "Raphaël Varane",
            "Dayot Upamecano", "Théo Hernandez", "Mike Maignan",
            "Randal Kolo Muani", "Bradley Barcola", "Mathys Tel",
            "Kingsley Coman", "Jonathan Clauss", "Jules Koundé",
        ])),
    },
    {
        "id": "eng", "label": "Inglaterra", "emoji": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "color": "#dc2626",
        "stickers": make_stickers("ENG", _team("Inglaterra", [
            "Jude Bellingham", "Harry Kane", "Phil Foden",
            "Bukayo Saka", "Declan Rice", "Trent Alexander-Arnold",
            "John Stones", "Marc Guehi", "Kyle Walker",
            "Jordan Pickford", "Marcus Rashford", "Cole Palmer",
            "Conor Gallagher", "Anthony Gordon", "Morgan Rogers",
            "Kieran Trippier", "Kobbie Mainoo", "Ezri Konsa",
        ])),
    },
    {
        "id": "esp", "label": "Espanha", "emoji": "🇪🇸", "color": "#fbbf24",
        "stickers": make_stickers("ESP", _team("Espanha", [
            "Pedri", "Gavi", "Lamine Yamal",
            "Nico Williams", "Rodri", "Mikel Merino",
            "Aymeric Laporte", "Pau Torres", "Alejandro Grimaldo",
            "David Raya", "Álvaro Morata", "Dani Olmo",
            "Fabián Ruiz", "Ferran Torres", "Yeremy Pino",
            "Martin Zubimendi", "Nacho Fernández", "Alejandro Baena",
        ])),
    },
    {
        "id": "por", "label": "Portugal", "emoji": "🇵🇹", "color": "#b91c1c",
        "stickers": make_stickers("POR", _team("Portugal", [
            "Cristiano Ronaldo", "Bruno Fernandes", "Bernardo Silva",
            "João Félix", "Rafael Leão", "Vitinha",
            "Rúben Dias", "Pepe", "Nuno Mendes",
            "Diogo Costa", "Gonçalo Ramos", "João Neves",
            "Pedro Neto", "Otávio", "Rúben Neves",
            "Nelson Semedo", "Diogo Dalot", "Francisco Conceição",
        ])),
    },
    {
        "id": "ger", "label": "Alemanha", "emoji": "🇩🇪", "color": "#6b7280",
        "stickers": make_stickers("GER", _team("Alemanha", [
            "Jamal Musiala", "Florian Wirtz", "Kai Havertz",
            "Leroy Sané", "Leon Goretzka", "Joshua Kimmich",
            "Antonio Rüdiger", "Nico Schlotterbeck", "David Raum",
            "Manuel Neuer", "Serge Gnabry", "Niclas Füllkrug",
            "Robert Andrich", "Konrad Laimer", "Maximilian Mittelstädt",
            "Thomas Müller", "Benjamin Henrichs", "Jonathan Tah",
        ])),
    },
    {
        "id": "ned", "label": "Holanda", "emoji": "🇳🇱", "color": "#f97316",
        "stickers": make_stickers("NED", _team("Holanda", [
            "Virgil van Dijk", "Cody Gakpo", "Memphis Depay",
            "Xavi Simons", "Frenkie de Jong", "Tijjani Reijnders",
            "Nathan Aké", "Denzel Dumfries", "Bart Verbruggen",
            "Donyell Malen", "Wout Weghorst", "Brian Brobbey",
            "Steven Bergwijn", "Joshua Zirkzee", "Mark Flekken",
            "Daley Blind", "Matthijs de Ligt", "Ryan Gravenberch",
        ])),
    },
    {
        "id": "bel", "label": "Bélgica", "emoji": "🇧🇪", "color": "#ef4444",
        "stickers": make_stickers("BEL", _team("Bélgica", [
            "Kevin De Bruyne", "Romelu Lukaku", "Yannick Carrasco",
            "Amadou Onana", "Jan Vertonghen", "Thibaut Courtois",
            "Leandro Trossard", "Charles De Ketelaere", "Lois Openda",
            "Jérémy Doku", "Timothy Castagne", "Arthur Theate",
            "Hans Vanaken", "Maxim De Cuyper", "Orel Mangala",
            "Johan Bakayoko", "Toby Alderweireld", "Loïs Openda",
        ])),
    },
    {
        "id": "cro", "label": "Croácia", "emoji": "🇭🇷", "color": "#dc2626",
        "stickers": make_stickers("CRO", _team("Croácia", [
            "Luka Modrić", "Ivan Perišić", "Marcelo Brozović",
            "Mateo Kovačić", "Mario Pašalić", "Lovro Majer",
            "Joško Gvardiol", "Dejan Lovren", "Josip Juranović",
            "Dominik Livaković", "Andrej Kramarić", "Bruno Petković",
            "Nikola Vlašić", "Luka Sučić", "Josip Stanišić",
            "Martin Erlić", "Borna Sosa", "Šime Vrsaljko",
        ])),
    },
    {
        "id": "sui", "label": "Suíça", "emoji": "🇨🇭", "color": "#dc2626",
        "stickers": make_stickers("SUI", _team("Suíça", [
            "Granit Xhaka", "Xherdan Shaqiri", "Breel Embolo",
            "Remo Freuler", "Denis Zakaria", "Manuel Akanji",
            "Nico Elvedi", "Ricardo Rodríguez", "Yann Sommer",
            "Dan Ndoye", "Zeki Amdouni", "Michel Aebischer",
            "Christian Fassnacht", "Fabian Rieder", "Leonidas Stergiou",
            "Ruben Vargas", "Silvan Widmer", "Edimilson Fernandes",
        ])),
    },
    {
        "id": "tur", "label": "Turquia", "emoji": "🇹🇷", "color": "#dc2626",
        "stickers": make_stickers("TUR", _team("Turquia", [
            "Hakan Çalhanoğlu", "Arda Güler", "Kerem Aktürkoğlu",
            "Salih Özcan", "Orkun Kökçü", "Merih Demiral",
            "Çağlar Söyüncü", "Ferdi Kadıoğlu", "Uğurcan Çakır",
            "Cenk Tosun", "Barış Yıldız", "Barış Alper Yılmaz",
            "Kenan Karaman", "Burak Yılmaz", "Abdülkerim Bardakcı",
            "Zeki Çelik", "Mert Günok", "İrfan Can Kahveci",
        ])),
    },
    {
        "id": "sco", "label": "Escócia", "emoji": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "color": "#1d4ed8",
        "stickers": make_stickers("SCO", _team("Escócia", [
            "Andy Robertson", "Scott McTominay", "Che Adams",
            "Ryan Christie", "Billy Gilmour", "John McGinn",
            "Grant Hanley", "Kieran Tierney", "Angus Gunn",
            "Lyndon Dykes", "Ryan Porteous", "Lewis Ferguson",
            "Callum McGregor", "Nathan Patterson", "Kenny McLean",
            "Stuart Armstrong", "Ryan Jack", "Lawrence Shankland",
        ])),
    },
    {
        "id": "swe", "label": "Suécia", "emoji": "🇸🇪", "color": "#fbbf24",
        "stickers": make_stickers("SWE", _team("Suécia", [
            "Viktor Gyökeres", "Emil Forsberg", "Dejan Kulusevski",
            "Alexander Isak", "Victor Lindelöf", "Jens Cajuste",
            "Ludwig Augustinsson", "Pontus Jansson", "Robin Olsen",
            "Jordan Larsson", "Anthony Elanga", "Mattias Svanberg",
            "Jesper Karlsson", "Sam Larsson", "Filip Helander",
            "Kristoffer Olsson", "Isak Hien", "Zlatan Ibrahimović",
        ])),
    },
    {
        "id": "aut", "label": "Áustria", "emoji": "🇦🇹", "color": "#dc2626",
        "stickers": make_stickers("AUT", _team("Áustria", [
            "Marcel Sabitzer", "Christoph Baumgartner", "Marko Arnautovic",
            "Stefan Lainer", "Florian Grillitsch", "Maximilian Wöber",
            "Philipp Lienhart", "Patrick Pentz", "Michael Gregoritsch",
            "Nicolas Seiwald", "Romano Schmid", "Alexander Prass",
            "Junior Adamu", "Patrick Wimmer", "Xaver Schlager",
            "David Alaba", "Kevin Danso", "Karim Onisiwo",
        ])),
    },
    {
        "id": "bih", "label": "Bósnia", "emoji": "🇧🇦", "color": "#1d4ed8",
        "stickers": make_stickers("BIH", _team("Bósnia", [
            "Miralem Pjanić", "Edin Džeko", "Ermedin Demirović",
            "Sead Kolašinac", "Benjamin Tahirović", "Amar Dedić",
            "Rade Krunić", "Armin Hodžić", "Haris Hajradinović",
            "Elvis Sarić", "Jasmin Mujezinović", "Demir Kovačević",
            "Vedran Ćorluka", "Nermin Zolotić", "Asmir Begović",
            "Anel Ahmedhodžić", "Dario Šarenac", "Eldar Šehić",
        ])),
    },
    {
        "id": "cze", "label": "República Tcheca", "emoji": "🇨🇿", "color": "#dc2626",
        "stickers": make_stickers("CZE", _team("República Tcheca", [
            "Tomáš Souček", "Patrik Schick", "Adam Hložek",
            "Vladimír Coufal", "Ondřej Duda", "Tomáš Holeš",
            "Tomáš Vaclík", "Ondřej Lingr", "Ladislav Krejčí",
            "Jan Kuchta", "Jakub Jankto", "Jakub Brabec",
            "Matěj Jurásek", "Antonín Barák", "Alex Král",
            "Lukáš Provod", "Václav Jurečka", "Jindřich Staněk",
        ])),
    },
    {
        "id": "nor", "label": "Noruega", "emoji": "🇳🇴", "color": "#ef4444",
        "stickers": make_stickers("NOR", _team("Noruega", [
            "Erling Haaland", "Martin Ødegaard", "Alexander Sørloth",
            "Sander Berge", "Stefan Strandberg", "Leo Østigård",
            "Kristian Thorstvedt", "Morten Thorsby", "Ørjan Nyland",
            "Patrick Berg", "Fredrik Aursnes", "Veton Berisha",
            "Mohamed Elyounoussi", "Niklas Hermansen", "Julian Ryerson",
            "Andreas Hanche-Olsen", "Mathias Normann", "Jørgen Strand Larsen",
        ])),
    },

    # ─── AMÉRICA DO SUL (6 seleções) ──────────────────────────────────────────

    {
        "id": "bra", "label": "Brasil", "emoji": "🇧🇷", "color": "#16a34a",
        "stickers": make_stickers("BRA", _team("Brasil", [
            "Vinicius Jr.", "Rodrygo", "Raphinha",
            "Richarlison", "Casemiro", "Bruno Guimarães",
            "Lucas Paquetá", "Marquinhos", "Éder Militão",
            "Danilo", "Alisson", "Endrick",
            "Gabriel Martinelli", "Gabriel (Brighton)", "Savinho",
            "Gerson", "Bremer", "Ederson",
        ])),
    },
    {
        "id": "arg", "label": "Argentina", "emoji": "🇦🇷", "color": "#60a5fa",
        "stickers": make_stickers("ARG", _team("Argentina", [
            "Lionel Messi", "Julián Álvarez", "Lautaro Martínez",
            "Rodrigo De Paul", "Alexis Mac Allister", "Enzo Fernández",
            "Nicolás Otamendi", "Cristian Romero", "Nahuel Molina",
            "Emiliano Martínez", "Thiago Almada", "Ángel Di María",
            "Paulo Dybala", "Nicolás González", "Germán Pezzella",
            "Marcos Acuña", "Lisandro Martínez", "Leandro Paredes",
        ])),
    },
    {
        "id": "uru", "label": "Uruguai", "emoji": "🇺🇾", "color": "#60a5fa",
        "stickers": make_stickers("URU", _team("Uruguai", [
            "Darwin Núñez", "Federico Valverde", "Rodrigo Bentancur",
            "Matías Vecino", "José María Giménez", "Mathías Olivera",
            "Sergio Rochet", "Nicolás De la Cruz", "Ronald Araújo",
            "Facundo Torres", "Manuel Ugarte", "Facundo Pellistri",
            "Maxi Gómez", "Diego Godín", "Brian Rodríguez",
            "Agustín Canobbio", "Sebastián Cáceres", "Lucas Olaza",
        ])),
    },
    {
        "id": "col", "label": "Colômbia", "emoji": "🇨🇴", "color": "#fbbf24",
        "stickers": make_stickers("COL", _team("Colômbia", [
            "James Rodríguez", "Luis Díaz", "Juan Cuadrado",
            "Wilmar Barrios", "Mateus Uribe", "Yerry Mina",
            "Dávinson Sánchez", "David Ospina", "Rafael Santos Borré",
            "Jhon Durán", "Luis Sinisterra", "Déiver Machado",
            "Jorge Carrascal", "Jefferson Lerma", "Jhon Córdoba",
            "Lerma", "Richard Ríos", "Santiago Arias",
        ])),
    },
    {
        "id": "ecu", "label": "Equador", "emoji": "🇪🇨", "color": "#fbbf24",
        "stickers": make_stickers("ECU", _team("Equador", [
            "Enner Valencia", "Moisés Caicedo", "Jeremy Sarmiento",
            "Gonzalo Plata", "Carlos Gruezo", "Romario Ibarra",
            "Byron Castillo", "Piero Hincapié", "Pervis Estupiñán",
            "Hernán Galíndez", "Ángel Mena", "Michael Estrada",
            "Kevin Rodríguez", "Jackson Porozo", "Alan Minda",
            "Diego Palacios", "Angelo Preciado", "John Yeboah",
        ])),
    },
    {
        "id": "par", "label": "Paraguai", "emoji": "🇵🇾", "color": "#dc2626",
        "stickers": make_stickers("PAR", _team("Paraguai", [
            "Miguel Almirón", "Ángel Romero", "Óscar Romero",
            "Matías Rojas", "Gustavo Gómez", "Omar Alderete",
            "Junior Alonso", "Antony Silva", "Julio Enciso",
            "Alberto Espínola", "Richard Sánchez", "Andrés Cubas",
            "Braian Samudio", "Marcelo Pereira", "Sergio Díaz",
            "Óscar Cardozo", "Antonio Sanabria", "Robert Morales",
        ])),
    },

    {
        "id": "ven", "label": "Venezuela", "emoji": "🇻🇪", "color": "#dc2626",
        "stickers": make_stickers("VEN", _team("Venezuela", [
            "Yangel Herrera", "Yeferson Soteldo", "Salomón Rondón",
            "Josef Martínez", "Darwin Machis", "Tomás Rincón",
            "Roberto Rosales", "Jhon Chancellor", "Alexander González",
            "Wuilker Faríñez", "Adalberto Peñaranda", "Júnior Moreno",
            "Eric Ramírez", "Rolf Feltscher", "Nahuel Ferraresi",
            "Jon Aramburu", "Romulo Otero", "Francisco La Rosa",
        ])),
    },

    # ─── CONCACAF (6 seleções) ────────────────────────────────────────────────

    {
        "id": "usa", "label": "Estados Unidos", "emoji": "🇺🇸", "color": "#3b82f6",
        "stickers": make_stickers("USA", _team("Estados Unidos", [
            "Christian Pulisic", "Tyler Adams", "Gio Reyna",
            "Weston McKennie", "Josh Sargent", "Tim Weah",
            "Matt Turner", "Sergiño Dest", "Yunus Musah",
            "Caden Clark", "Folarin Balogun", "Ricardo Pepi",
            "Joe Scally", "Malik Tillman", "Daryl Dike",
            "Luca de la Torre", "Joe Kessler", "Brenden Aaronson",
        ])),
    },
    {
        "id": "can", "label": "Canadá", "emoji": "🇨🇦", "color": "#ef4444",
        "stickers": make_stickers("CAN", _team("Canadá", [
            "Alphonso Davies", "Jonathan David", "Cyle Larin",
            "Tajon Buchanan", "Stephen Eustáquio", "Milan Borjan",
            "Sam Adekugbe", "Alistair Johnston", "Derek Cornelius",
            "Ismael Koné", "Liam Millar", "Charles-Andreas Brym",
            "Jacob Shaffelburg", "Richie Laryea", "Theo Bair",
            "Cyle Larin", "Kamal Miller", "Jonathan Osorio",
        ])),
    },
    {
        "id": "mex", "label": "México", "emoji": "🇲🇽", "color": "#22c55e",
        "stickers": make_stickers("MEX", _team("México", [
            "Hirving Lozano", "Raúl Jiménez", "Héctor Herrera",
            "Edson Álvarez", "Guillermo Ochoa", "César Montes",
            "Alexis Vega", "Uriel Antuna", "Santiago Giménez",
            "Roberto Alvarado", "Luis Chávez", "Kevin Álvarez",
            "Julián Araujo", "Johan Vásquez", "Carlos Rodríguez",
            "Orbelín Pineda", "Henry Martín", "Jesús Gallardo",
        ])),
    },
    {
        "id": "pan", "label": "Panamá", "emoji": "🇵🇦", "color": "#ef4444",
        "stickers": make_stickers("PAN", _team("Panamá", [
            "Aníbal Godoy", "Rolando Blackburn", "José Fajardo",
            "Adalberto Carrasquilla", "Gabriel Torres", "Roderick Miller",
            "Fidel Escobar", "Harold Cummings", "Luis Mejía",
            "Cecilio Waterman", "Alberto Quintero", "Ismael Díaz",
            "Édgar Bárcenas", "Michael Murillo", "César Yanis",
            "José Luis Rodríguez", "Éric Davis", "Armando Cooper",
        ])),
    },
    {
        "id": "hai", "label": "Haiti", "emoji": "🇭🇹", "color": "#1d4ed8",
        "stickers": make_stickers("HAI", _team("Haiti", [
            "Duckens Nazon", "Maxwel Cornet", "Wilde-Donald Guerrier",
            "Kervens Désir", "Mechack Jérôme", "James Léandre",
            "Constant Béthelier", "Bobby Démosthène", "Gersil Paul",
            "Nicolas Moïse", "Ronald Mathurin", "Herby Léger",
            "Kevin Fortune", "Jeff Louis", "Steeven Saba",
            "Alexandre Claudet", "Frantzdy Pierrot", "Sherly Jeudy",
        ])),
    },
    {
        "id": "cuw", "label": "Curaçao", "emoji": "🇨🇼", "color": "#0ea5e9",
        "stickers": make_stickers("CUW", _team("Curaçao", [
            "Cuco Martina", "Leandro Bacuna", "Elson Hooi",
            "Rangelo Janga", "Jair Marwijk", "Celton Biai",
            "Gianluca Nijholt", "Brandley Kuwas", "Quentin Rustal",
            "Shaquille Martina", "Kenji Gorré", "Terrence Boyd",
            "Etienne Reijnen", "Jafar Arias", "Javier Martina",
            "Cuco Martina", "Juriën Gaari", "Gevaro Nepomuceno",
        ])),
    },

    # ─── ÁFRICA (9 seleções) ──────────────────────────────────────────────────

    {
        "id": "mar", "label": "Marrocos", "emoji": "🇲🇦", "color": "#dc2626",
        "stickers": make_stickers("MAR", _team("Marrocos", [
            "Achraf Hakimi", "Hakim Ziyech", "Youssef En-Nesyri",
            "Sofyan Amrabat", "Azzedine Ounahi", "Romain Saïss",
            "Nayef Aguerd", "Noussair Mazraoui", "Yassine Bounou",
            "Abdessamad Ezzalzouli", "Anass Zaroury", "Bilal El Khannouss",
            "Selim Amallah", "Jawad El Yamiq", "Youssef En-Nesyri",
            "Ibrahim Diaz", "Yahya Attiat-Allah", "Badr Benoun",
        ])),
    },
    {
        "id": "sen", "label": "Senegal", "emoji": "🇸🇳", "color": "#16a34a",
        "stickers": make_stickers("SEN", _team("Senegal", [
            "Sadio Mané", "Kalidou Koulibaly", "Ismaila Sarr",
            "Idrissa Gueye", "Cheikhou Kouyaté", "Nampalys Mendy",
            "Abdou Diallo", "Saliou Ciss", "Édouard Mendy",
            "Boulaye Dia", "Nicolas Jackson", "Pape Matar Sarr",
            "Habib Diallo", "Lamine Camara", "Formose Mendy",
            "Pape Gueye", "Krepin Diatta", "Cheikh Tall",
        ])),
    },
    {
        "id": "egy", "label": "Egito", "emoji": "🇪🇬", "color": "#dc2626",
        "stickers": make_stickers("EGY", _team("Egito", [
            "Mohamed Salah", "Mohamed Elneny", "Omar Marmoush",
            "Emam Ashour", "Tarek Hamed", "Ahmed Hegazi",
            "Mohamed Abdelmonem", "Mohamed El-Shenawy", "Mostafa Mohamed",
            "Ahmed Sayed Zizo", "Ramadan Sobhi", "Kahraba",
            "Trezeguet", "Ahmed Fatouh", "Omar Kamal",
            "Akram Tawfik", "Ahmed Abdelkader", "Essam El-Hadary",
        ])),
    },
    {
        "id": "civ", "label": "Costa do Marfim", "emoji": "🇨🇮", "color": "#f97316",
        "stickers": make_stickers("CIV", _team("Costa do Marfim", [
            "Franck Kessié", "Wilfried Zaha", "Sébastien Haller",
            "Nicolas Pépé", "Jean Michaël Seri", "Simon Deli",
            "Eric Bailly", "Serge Aurier", "Badra Ali Sangaré",
            "Amad Diallo", "Max-Alain Gradel", "Christian Kouamé",
            "Karim Konaté", "Odilon Kossounou", "Wilfried Kanon",
            "Oumar Diakité", "Ibrahim Sangaré", "Gonçalo Ramos",
        ])),
    },
    {
        "id": "gha", "label": "Gana", "emoji": "🇬🇭", "color": "#fbbf24",
        "stickers": make_stickers("GHA", _team("Gana", [
            "Thomas Partey", "Jordan Ayew", "André Ayew",
            "Mohammed Salisu", "Tariq Lamptey", "Daniel Amartey",
            "Alexander Djiku", "Baba Rahman", "Lawrence Ati-Zigi",
            "Iñaki Williams", "Felix Afena-Gyan", "Antoine Semenyo",
            "Mohammed Kudus", "Daniel-Kofi Kyereh", "Dede Ayew",
            "Joseph Paintsil", "Abdul Fatawu", "Benjamin Asante",
        ])),
    },
    {
        "id": "alg", "label": "Argélia", "emoji": "🇩🇿", "color": "#16a34a",
        "stickers": make_stickers("ALG", _team("Argélia", [
            "Riyad Mahrez", "Islam Slimani", "Ramy Bensebaini",
            "Ismael Bennacer", "Baghdad Bounedjah", "Youcef Belaïli",
            "Djamel Benlamri", "Hicham Boudaoui", "Raïs M'Bolhi",
            "Youcef Atal", "Sofiane Feghouli", "Haris Belkebla",
            "Farès Chaïbi", "Said Benrahma", "Houssem Aouar",
            "Adem Zorgane", "Djamel Belmadi", "Mehdi Tahrat",
        ])),
    },
    {
        "id": "cod", "label": "RD Congo", "emoji": "🇨🇩", "color": "#fbbf24",
        "stickers": make_stickers("COD", _team("RD Congo", [
            "Chancel Mbemba", "Cédric Bakambu", "Yoane Wissa",
            "Paul-José M'Poku", "Gael Kakuta", "Christian Luyindama",
            "Marcel Tisserand", "Merveille Bokadi", "Silas Nsimba",
            "Arthur Masuaku", "Yannick Bolasie", "Neeskens Kebano",
            "Jonathan Bolingi", "Glody Ngonda", "Edo Kayembe",
            "Donatien Dibango", "Steve Mounié", "Arlind Ajeti",
        ])),
    },
    {
        "id": "rsa", "label": "África do Sul", "emoji": "🇿🇦", "color": "#fbbf24",
        "stickers": make_stickers("RSA", _team("África do Sul", [
            "Percy Tau", "Themba Zwane", "Bongani Zungu",
            "Ronwen Williams", "Teboho Mokoena", "Ethan Ntsuntsha",
            "Sfiso Hlanti", "Nduduzo Sibiya", "Luther Singh",
            "Keagan Dolly", "Sipho Mbule", "Yusuf Maart",
            "Lyle Foster", "Happy Mashiane", "Evidence Makgopa",
            "Terrence Mashego", "Siyanda Xulu", "Itumeleng Khune",
        ])),
    },
    {
        "id": "cav", "label": "Cabo Verde", "emoji": "🇨🇻", "color": "#1d4ed8",
        "stickers": make_stickers("CAV", _team("Cabo Verde", [
            "Ryan Mendes", "Garry Rodrigues", "Jamiro Monteiro",
            "Stopira", "Steven Fortes", "Nando",
            "Bebé", "Deroy Duarte", "Dany Tavares",
            "Diogo Tavares", "Mickaël Pereira", "Marco Soares",
            "Kenny Rocha", "Odair Fortes", "Cláudio Winck",
            "Bryan Teixeira", "Gilson Benchimol", "Dylan Tavares",
        ])),
    },

    {
        "id": "tun", "label": "Tunísia", "emoji": "🇹🇳", "color": "#dc2626",
        "stickers": make_stickers("TUN", _team("Tunísia", [
            "Wahbi Khazri", "Youssef Msakni", "Hannibal Mejbri",
            "Ellyes Skhiri", "Anis Slimane", "Naim Sliti",
            "Yassine Meriah", "Montassar Talbi", "Ali Maaloul",
            "Aymen Dahmen", "Seifeddine Jaziri", "T.Y. Khenissi",
            "Mohamed Drager", "Aïssa Laïdouni", "Nader Ghandri",
            "Ben Romdhane", "Ferjani Sassi", "Bechir Ben Said",
        ])),
    },

    # ─── ÁSIA (8 seleções) ────────────────────────────────────────────────────

    {
        "id": "jpn", "label": "Japão", "emoji": "🇯🇵", "color": "#dc2626",
        "stickers": make_stickers("JPN", _team("Japão", [
            "Takumi Minamino", "Daichi Kamada", "Ritsu Doan",
            "Wataru Endo", "Junya Ito", "Maya Yoshida",
            "Takehiro Tomiyasu", "Yuto Nagatomo", "Shuichi Gonda",
            "Takuma Asano", "Kaoru Mitoma", "Ao Tanaka",
            "Daizen Maeda", "Ayase Ueda", "Hidemasa Morita",
            "Koki Machida", "Mao Hosoya", "Keito Nakamura",
        ])),
    },
    {
        "id": "kor", "label": "Coreia do Sul", "emoji": "🇰🇷", "color": "#dc2626",
        "stickers": make_stickers("KOR", _team("Coreia do Sul", [
            "Son Heung-min", "Hwang Hee-chan", "Lee Jae-sung",
            "Jung Woo-young", "Kim Min-jae", "Hwang In-beom",
            "Kim Young-gwon", "Lee Yong", "Kim Seung-gyu",
            "Cho Gue-sung", "Lee Gang-in", "Kwon Chang-hoon",
            "Oh Hyeon-gyu", "Hong Chul", "Jeong Woo-yeong",
            "Kim Jin-su", "Lee Kang-in", "Seol Young-woo",
        ])),
    },
    {
        "id": "aus", "label": "Austrália", "emoji": "🇦🇺", "color": "#fbbf24",
        "stickers": make_stickers("AUS", _team("Austrália", [
            "Mat Ryan", "Martin Boyle", "Mathew Leckie",
            "Aaron Mooy", "Ajdin Hrustic", "Ryan Rowles",
            "Miloš Degenek", "Trent Sainsbury", "Aziz Behich",
            "Andrew Redmayne", "Mitchell Duke", "Craig Goodwin",
            "Keanu Baccus", "Jackson Irvine", "Nestory Irankunda",
            "Nathaniel Atkinson", "Cameron Devlin", "Marco Tilio",
        ])),
    },
    {
        "id": "ira", "label": "Irã", "emoji": "🇮🇷", "color": "#16a34a",
        "stickers": make_stickers("IRA", _team("Irã", [
            "Mehdi Taremi", "Sardar Azmoun", "Alireza Jahanbakhsh",
            "Saeid Ezatolahi", "Alireza Beiranvand", "Saman Ghoddos",
            "Morteza Pouraliganji", "Majid Hosseini", "Ehsan Hajsafi",
            "Karim Ansarifard", "Ramin Rezaeian", "Milad Mohammadi",
            "Ali Karimi", "Ahmad Noorollahi", "Shojae Khalilzadeh",
            "Hassan Pourshahbaz", "Omid Noorafkan", "Kaveh Rezaei",
        ])),
    },
    {
        "id": "ksa", "label": "Arábia Saudita", "emoji": "🇸🇦", "color": "#16a34a",
        "stickers": make_stickers("KSA", _team("Arábia Saudita", [
            "Mohammed Al-Owais", "Salem Al-Dawsari", "Firas Al-Buraikan",
            "Saleh Al-Shehri", "Sami Al-Najei", "Ali Al-Bulaihi",
            "Hassan Tambakti", "Yasser Al-Shahrani", "Hattan Bahebri",
            "Abdulelah Al-Malki", "Mohamed Kanno", "Haitham Asiri",
            "Mohammed Al-Buraik", "Sultan Al-Ghannam", "Abdullah Al-Khaibri",
            "Ali Al-Hassan", "Salman Al-Faraj", "Yahya Al-Shehri",
        ])),
    },
    {
        "id": "qat", "label": "Qatar", "emoji": "🇶🇦", "color": "#8b1a1a",
        "stickers": make_stickers("QAT", _team("Qatar", [
            "Hassan Al-Haydos", "Almoez Ali", "Akram Afif",
            "Abdulaziz Hatem", "Karim Boudiaf", "Bassam Al-Rawi",
            "Boualem Khoukhi", "Pedro Miguel", "Salah Zakaria",
            "Meshaal Barsham", "Mohammed Muntari", "Ismaeel Mohammad",
            "Assim Madibo", "Homam Ahmed", "Tarek Salman",
            "Ahmed Alaaeldin", "Yusuf Abdurisag", "Jassem Gaber",
        ])),
    },
    {
        "id": "jor", "label": "Jordânia", "emoji": "🇯🇴", "color": "#007a3d",
        "stickers": make_stickers("JOR", _team("Jordânia", [
            "Yazan Al-Naimat", "Baha Faisal", "Nour Mansour",
            "Ahmad Sardar", "Osama Rashid", "Hamza Al-Dardour",
            "Ahmad Al-Salihiya", "Musa Al-Tamari", "Mohannad Abu Nimer",
            "Abdullah Nasib", "Zaid Qunbar", "Ahmad Ibrahim",
            "Jalal Hassan", "Dhurgham Ismail", "Bashar Resan",
            "Ali Olwan", "Ahmad Al-Ahmad", "Ibrahim Zdanowicz",
        ])),
    },
    {
        "id": "uzb", "label": "Uzbequistão", "emoji": "🇺🇿", "color": "#1d6b3e",
        "stickers": make_stickers("UZB", _team("Uzbequistão", [
            "Eldor Shomurodov", "Jamshid Iskanderov", "Sanjar Tursunov",
            "Jasur Yaxshiboyev", "Sherzod Nasrullayev", "Odil Ahmedov",
            "Otabek Shukurov", "Islom Tukhtahujaev", "Timur Djalilov",
            "Shukhrat Mukhammadiev", "Bobur Abdixoliqov", "Khojiakbar Alijonov",
            "Ortiq Zoirov", "Bahodir Jaloliddinov", "Abbosbek Fayzullaev",
            "Jaloliddin Masharipov", "Oston Urunov", "Akbar Tursunmurodov",
        ])),
    },

    # ─── OCEANIA (1 seleção) ──────────────────────────────────────────────────

    {
        "id": "nzl", "label": "Nova Zelândia", "emoji": "🇳🇿", "color": "#6b7280",
        "stickers": make_stickers("NZL", _team("Nova Zelândia", [
            "Chris Wood", "Winston Reid", "Tim Payne",
            "Clayton Lewis", "Joe Bell", "Elijah Just",
            "Michael Boxall", "Liberato Cacace", "Storm Roux",
            "Stefan Marinovic", "Matthew Garbett", "Sarpreet Singh",
            "Marko Stamenic", "Deklan Wynne", "Callan Elliott",
            "Ben Old", "Dane Ingham", "Alex Rufer",
        ])),
    },
]


def get_all_sticker_ids() -> list:
    """Retorna lista plana de todos os IDs de figurinhas."""
    return [s["id"] for sec in SECTIONS for s in sec["stickers"]]


def get_total() -> int:
    return sum(len(s["stickers"]) for s in SECTIONS)
