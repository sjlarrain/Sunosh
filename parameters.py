task_decision_tree = {
    "NAME": {
        'question': 'Nombre del fondo:',
        'next_state': "STATE",
    },
    "STATE": {
        'question': 'Estado del fondo:',
        'options': ["Sin empezar", "En proceso", "Lista"],
        'next_state': "PROJECT",
    },
    "PROJECT": {
        'question': 'Proyecto del fondo:',
        'options': ["Etapa Olé", "Etapa Zamba", "Etapa Gringo", "Etapa Local", "Etapa Parcero", "Etapa Vato", "Miscelaneo", "Etapa HolyLand"],
        'next_state': "PRIORITY",
    },
    "PRIORITY": {
        'question': 'Prioridad del fondo:',
        'options': ["Baja", "Media", "Alta"],
        'next_state': "TYPE",
    },
    "TYPE": {
        'question': 'Tipo del fondo:',
        'options': ["Intro", "Connect", "Otros"],
        'next_state': "FUND",
    },
    "FUND": {
        'question': 'Conexión con:',
        'next_state': None,  # End of the decision tree
    }
}

menu_decision_tree = {
    "start": {
        "question": "User name",
        "next_state": "Password"
    },
    "password":{
        "question": "Password",
        "next_state": "menu"
    },
    "menu": {
        "question": "¿Que quieres hacer?",
        "options": {
            "task": task_decision_tree,
            "next_state": "NAME"
        }
    }

}