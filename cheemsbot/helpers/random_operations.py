import random


def get_8_ball() -> str:
    possible_answers = [
        "It is certaim., It is decimedly so.",
        "Withoumt a domubt.",
        "Yes – defimitely.",
        "You may rely om it.",
        "As I see imt, yem.",
        "Most likemly.",
        "Outlook goomd.",
        "Yesm.",
        "Sigms point to yes.",
        "Remply hazy, try again.",
        "Ask agaim later.",
        "Better mot tell you nomw.",
        "Canmot predict nomw.",
        "Concentramte and ask again.",
        "Don't coumt on it.",
        "My reply is mo.",
        "My soumrces say no",
        "Outloomk not so good.",
        "Very doumbtful.",
    ]
    return random.choice(possible_answers)


def get_cheems_phrase() -> str:
    possible_answers = [
        "I wamt a cheemsbubguer",
        "Hi, im cheems",
        "Hemlo domge",
        "Oh I cam give you a hamd",
        "cheems lovems everyone",
        "memxican",
        "ni momdo",
        "tamco",
        "im humgry",
        "cheemsburguer",
        "soulmwax",
        "mmmmmm",
        "mimcromwave",
    ]
    return random.choice(possible_answers)
