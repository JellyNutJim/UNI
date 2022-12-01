room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "MJ and Simon's room", "east": "your personal tutor's office", "west": "Parking"} 
}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    # ADD EXITS HERE!
    "exits": {"north": "Reception"}
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    # ADD EXITS HERE!
    "exits": {"west": "Reception"}
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    # ADD EXITS HERE!
    "exits": {"south": "Reception", "east": "Office"}
    
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    # ADD EXITS HERE!
    "exits": {"west": "Parking"}
    
}



rooms = {
    "Reception": room_reception,
    "MJ and Simon's room": room_admins,
    "your personal tutor's office": room_tutor,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
