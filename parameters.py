task_decision_tree = {
    "NAME": {
        'question': 'Nombre del fondo:',
        'next_state': "STATE",
        "next_type": False
    },
    "STATE": {
        'question': 'Estado del fondo:',
        'options': ["Sin empezar", "En proceso", "Lista"],
        'next_state': "PROJECT",
        "next_type": False
    },
    "PROJECT": {
        'question': 'Proyecto del fondo:',
        'options': ["Etapa Olé", "Etapa Zamba", "Etapa Gringo", "Etapa Local", "Etapa Parcero", "Etapa Vato", "Miscelaneo", "Etapa HolyLand"],
        'next_state': "PRIORITY",
        "next_type": False
    },
    "PRIORITY": {
        'question': 'Prioridad del fondo:',
        'options': ["Baja", "Media", "Alta"],
        'next_state': "next_type",
        "next_type": False
    },
    "next_type": {
        'question': 'Tipo del fondo:',
        'options': ["Intro", "Connect", "Otros"],
        'next_state': "FUND",
        "next_type": False
    },
    "FUND": {
        'question': 'Conexión con:',
        'next_state': None,  # End of the decision tree
        "next_type": None
    }
}

menu_decision_tree = {
    "start": {
        "question": "Username",
        "next_state": "password",
        "next_type": True
    },
    "password":{
        "question": "Password",
        "next_state": "menu",
        "next_type": False
    },
    "menu": {
        "question": "¿Que quieres hacer?",
        "options": {
            "task": task_decision_tree,
            
        },
        "next_type": True,
        "next_state": "NAME"
    }

}