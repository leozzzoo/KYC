from keras.models import load_model
import numpy as np
import cv2
import json
    
# Data to be written
diz_pokemon = {
    0: 'Abra',
    1: 'Aerodactyl',
    2: 'Alakazam',
    3: 'Arbok',
    4: 'Arcanine',
    5: 'Articuno',
    6: 'Beedrill',
    7: 'Bellsprout',
    8: 'Blastoise',
    9: 'Bulbasaur',
    10: 'Butterfree',
    11: 'Caterpie',
    12: 'Chansey',
    13: 'Charizard',
    14: 'Charmander',
    15: 'Charmeleon',
    16: 'Clefable',
    17: 'Clefairy',
    18: 'Cloyster',
    19: 'Cubone',
    20: 'Dewgong',
    21: 'Diglett',
    22: 'Ditto',
    23: 'Dodrio',
    24: 'Doduo',
    25: 'Dragonair',
    26: 'Dragonite',
    27: 'Dratini',
    28: 'Drowzee',
    29: 'Dugtrio',
    30: 'Eevee',
    31: 'Ekans',
    32: 'Electabuzz',
    33: 'Electrode',
    34: 'Exeggcute',
    35: 'Exeggutor',
    36: 'Farfetchd',
    37: 'Fearow',
    38: 'Flareon',
    39: 'Gastly',
    40: 'Gengar',
    41: 'Geodude',
    42: 'Gloom',
    43: 'Golbat',
    44: 'Goldeen',
    45: 'Golduck',
    46: 'Golem',
    47: 'Graveler',
    48: 'Grimer',
    49: 'Growlithe',
    50: 'Gyarados',
    51: 'Haunter',
    52: 'Hitmonchan',
    53: 'Hitmonlee',
    54: 'Horsea',
    55: 'Hypno',
    56: 'Ivysaur',
    57: 'Jigglypuff',
    58: 'Jolteon',
    59: 'Jynx',
    60: 'Kabuto',
    61: 'Kabutops',
    62: 'Kadabra',
    63: 'Kakuna',
    64: 'Kangaskhan',
    65: 'Kingler',
    66: 'Koffing',
    67: 'Krabby',
    68: 'Lapras',
    69: 'Lickitung',
    70: 'Machamp',
    71: 'Machoke',
    72: 'Machop',
    73: 'Magikarp',
    74: 'Magmar',
    75: 'Magnemite',
    76: 'Magneton',
    77: 'Mankey',
    78: 'Marowak',
    79: 'Meowth',
    80: 'Metapod',
    81: 'Mew',
    82: 'Mewtwo',
    83: 'Moltres',
    84: 'MrMime',
    85: 'Muk',
    86: 'Nidoking',
    87: 'Nidoqueen',
    88: 'Nidoran-f',
    89: 'Nidoran-m',
    90: 'Nidorina',
    91: 'Nidorino',
    92: 'Ninetales',
    93: 'Oddish',
    94: 'Omanyte',
    95: 'Omastar',
    96: 'Onix',
    97: 'Paras',
    98: 'Parasect',
    99: 'Persian',
    100: 'Pidgeot',
    101: 'Pidgeotto',
    102: 'Pidgey',
    103: 'Pikachu',
    104: 'Pinsir',
    105: 'Poliwag',
    106: 'Poliwhirl',
    107: 'Poliwrath',
    108: 'Ponyta',
    109: 'Porygon',
    110: 'Primeape',
    111: 'Psyduck',
    112: 'Raichu',
    113: 'Rapidash',
    114: 'Raticate',
    115: 'Rattata',
    116: 'Rhydon',
    117: 'Rhyhorn',
    118: 'Sandshrew',
    119: 'Sandslash',
    120: 'Scyther',
    121: 'Seadra',
    122: 'Seaking',
    123: 'Seel',
    124: 'Shellder',
    125: 'Slowbro',
    126: 'Slowpoke',
    127: 'Snorlax',
    128: 'Spearow',
    129: 'Squirtle',
    130: 'Starmie',
    131: 'Staryu',
    132: 'Tangela',
    133: 'Tauros',
    134: 'Tentacool',
    135: 'Tentacruel',
    136: 'Vaporeon',
    137: 'Venomoth',
    138: 'Venonat',
    139: 'Venusaur',
    140: 'Victreebel',
    141: 'Vileplume',
    142: 'Voltorb',
    143: 'Vulpix',
    144: 'Wartortle',
    145: 'Weedle',
    146: 'Weepinbell',
    147: 'Weezing',
    148: 'Wigglytuff',
    149: 'Zapdos',
    150: 'Zubat'}


def classify_pokemon(test_img, model, scale):
    # dict of pokemon
    with open('code/NN/pokemonNN.json') as f:
        diz_pokemon = json.load(f)

    # Read file
    #test_img = cv2.imread(test_file)
    # Resize the image testing with the input shape of neural network
    test_img = cv2.resize(test_img, scale)
    # change channel of color BGR to RGB
    test_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
    # scaling image
    test_img = np.expand_dims(test_img, axis=0)
    test_img = test_img/255
    
    # Loading the model 
    model = load_model(model)
    # Gives the prediction --> probability for each pokemon
    prediction_prob = model.predict(test_img)
    # Gives the pokemon with highest probability
    classes_x=np.argmax(prediction_prob,axis=1)
    # Return name Pokemon
    return diz_pokemon[str(classes_x[0])]