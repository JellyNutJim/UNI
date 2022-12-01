from items import *

bay = {    "name": "Cardiff Bay",
                   "id": "bay",
                   "description": """At the bay you are in the south of Cardiff. Around you there are many restaurants and cafes.\nThe Wales Millennium Centre is next to you and Mermaid Quay is ahead.""",
                   "items": [knife, rock, umbrella],
                   "city": ""
                   }

stadium = { "name": "Rugby Principality Stadium",
                    "id": "stadium",
                    "description": """The Principlaity Stadium is home to the welsh rugby team. You can go here to watch the six nations.""",
                    "items": [ball, pint],
                    "city": ""
                    }

bedroom = { "name": "Zelenskyy's Bedroom",
            "description": """Zelenskyy's bedroom is a hotspot for the local women.""",
            "id": "bedroom",
            "items": [balloon, boxers],
            "city": ""}

cathedral = {"name": "Holy Dormition Cathedral",
             "id": "cathedral",
             "description": """Massive church, the stained glass is pretty cool.""",
             "items": [candle, wine],
             "city": ""}

gardens = {    "name": "Royal Botanic Gardens Victoria",
                   "id": "gardens",
                   "description": """You're now in the Royal Botanic Gardens Victoria, founded in 1846. The gardens cover a total of 3800 acres of land,
                   meaning there's lots to look for!""",
                   "items": [watering, shears],
                   "city": ""
                   }

cricket = { "name": "Melbourne Cricket Ground",
                    "id": "cricket",
                    "description": """The Melbourne Cricket Ground is host to many famous cricket teams, the main being the men's national cricket team.
                    With cricket being such a big sport in Australia, and across the globe, many travellers and locals travel to \"The G\",
                    meaning there's plenty of enjoyment to be had here!""",
                    "items": [bat, helmet],
                    "city": ""}

park = {"name": "Central Park",
        "id": "park",
        "description": """The biggest park in New York City, central park is one of the hotspots for tourists
                visiting the city. It's actually the most visited urban park in the US""",
        "items": [apple, stick],
        "city": ""}


statue = {"name": "The Statue of Liberty",
          "id": "statue",
          "description": """A 305 ft statue of the coast of New York city, it is said to be the personification
           of liberty in the form of a woman""",
          "items": [cap, cocktail, torch],
          "city": ""}

abandoned_stadium = {"name": "Abandoned Olympic Stadium",
                     "id": "stadium",
                     "description": "Abandoned shortly after use, this stadium is devoid of all life",
                     "items": [medal, fencing_lame, rusty_fencing_sabre],
                     "city": ""}

sugarloaf = { "name": "Sugarloaf Mountain",
              "id": "sugarloaf",
              "description": "A giant 396m tall mountain located on a peninsula within rio.\nYou take a cable car to the peak of the mountain, the view is spectacular",
              "items": [binoculars, bottle_of_water, a_map],
              "city": ""
}

louvre = {"name": "The Louvre",
                     "id": "louvre",
                     "description": "You are in an art gallery. There are lots of mid level paintings.\n There is a strong smell of garlic.",
                     "items": [croissant, beret],
                     "city": ""}

stade_de_france = {"name": "Stade de France",
                     "id": "stade",
                     "description": "You enter a huge stadium. It is usually used for trying to play rugby.\n You are approached by a man wearing a black and white stripy top and starts hitting you with his baguette.",
                     "items": [red_wine, white_wine, eiffel_tower_model],
                     "city": ""}

tower = {"name": "Tokyo Tower",
               "id": "tower",
               "description": "You are stunned by the bright red-orange tower in the middle of the city.\nIt is covered in 7500 gallons of paint every 5 years to maintin its look, and it was built to symbolize the post-war boom in 1958.\nYou start climbing this tower to get away from the weeb tourists.",
               "items": [katana, body_pillow, karuta],
               "city": ""}

ueno = {"name": "Ueno Park",
             "id": "ueno",
             "description": "Here you can find the most famous cherry blossoms of Tokyo, and have a real therapeutic stroll across the park. You go to visit the temples and museums to get a taste of Japanese culture, and begin to feel like a samurai...",
             "items": [sushi, hot_spring],
             "city": ""}

# Cities -------------------------------------

cardiff = {"name": "Cardiff",
           "id": "cardiff",
           "description": "The capital city of Wales. It is never not raining and is always very cold.",
           "places": [bay, stadium],
           "connections": [] }

kyiv = {"name": "Kyiv",
        "id": "kyiv",
        "description": "The biggest city in Ukraine. it's freezing here!",
        "places": [bedroom, cathedral],
        "connections": [] }

paris = {"name": "Paris",
         "id": "paris",
         "description": "The capital of France. The city consists of lots of swearing and the lingering smell of cigarette smoke.",
         "places": [louvre, stade_de_france],
         "connections": []}

new_york = {"name": "New York",
            "id": "new_york",
            "description": "The most populated city in the united states of america. Home to over 8 million people",
            "places": [park, statue],
            "connections": []}

melbourne = {"name": "Melbourne",
             "id": "melbourne",
             "description": "Welcome down under! You step out of the plane and instantly feel the impact of the seething heat.",
             "places": [gardens, cricket],
             "connections": []}

tokyo = {"name": "Tokyo",
         "id": "tokyo",
         "description": "The largest city and the capital of Japan, and the most populous city in the world!",
         "places": [tower, ueno],
         "connections": []}

rio = {"name": "Rio De Janeiro",
       "id": "rio",
       "description": "Founded in 1565 and named the capital of brazil in 1763, this city of over 6.5 million people is something to behold.\nThe tropical climate is a nice bonus.",
       "places": [abandoned_stadium, sugarloaf],
       "connections": []}

cities = {
'cardiff': cardiff,
'kyiv': kyiv,
'paris': paris,
'new york': new_york,
'melbourne': melbourne,
'tokyo': tokyo,
'rio': rio
}

# Cardiff
cardiff["connections"] = cities
bay["city"] = cardiff
stadium["city"] = cardiff

# Kyiv
kyiv["connections"] = cities
bedroom["city"] = kyiv
cathedral["city"] = kyiv

# Melbourne
melbourne["connections"] = cities
gardens["city"] = melbourne
cricket["city"] = melbourne

# New York
new_york["connections"] = cities
park["city"] = new_york
statue["city"] = new_york

# Rio
rio["connections"] = cities
abandoned_stadium["city"] = rio
sugarloaf["city"] = rio

#Paris
paris["connections"] = cities
louvre["city"] = paris
stade_de_france["city"] = paris

#Tokyo
tokyo["connections"] = cities
tower["city"] = tokyo
ueno["city"] = tokyo
