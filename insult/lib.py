import random


def try_me():
    nouns = [
        'painting', 'advertisement', 'grass', 'parrot', 'afternoon', 'greece',
        'pencil', 'airport', 'guitar', 'piano', 'ambulance', 'hair', 'pillow',
        'animal', 'hamburger', 'pizza', 'answer', 'helicopter', 'planet',
        'apple', 'helmet', 'plastic', 'army', 'holiday', 'portugal',
        'australia', 'honey', 'potato', 'balloon', 'horse', 'queen', 'banana',
        'hospital', 'quill', 'battery', 'house', 'rain', 'beach', 'hydrogen',
        'rainbow', 'beard', 'ice', 'raincoat', 'bed', 'insect', 'refrigerator',
        'belgium', 'insurance', 'restaurant', 'boy', 'iron', 'river', 'branch',
        'island', 'rocket', 'breakfast', 'jackal', 'room', 'brother', 'jelly',
        'rose', 'camera', 'jewellery', 'russia', 'candle', 'jordan',
        'sandwich', 'car', 'juice', 'school', 'caravan', 'kangaroo', 'scooter',
        'carpet', 'king', 'shampoo', 'cartoon', 'kitchen', 'shoe', 'china',
        'kite', 'soccer', 'church', 'knife', 'spoon', 'crayon', 'lamp',
        'stone', 'crowd', 'lawyer', 'sugar', 'daughter', 'leather', 'sweden',
        'death', 'library', 'teacher', 'denmark', 'lighter', 'telephone',
        'diamond', 'lion', 'television', 'dinner', 'lizard', 'tent', 'disease',
        'lock', 'thailand', 'doctor', 'london', 'tomato', 'dog', 'lunch',
        'toothbrush', 'dream', 'machine', 'traffic', 'dress', 'magazine',
        'train', 'easter', 'magician', 'truck', 'egg', 'manchester', 'uganda',
        'eggplant', 'market', 'umbrella', 'egypt', 'match', 'van', 'elephant',
        'microphone', 'vase', 'energy', 'monkey', 'vegetable', 'engine',
        'morning', 'vulture', 'england', 'motorcycle', 'wall', 'evening',
        'nail', 'whale', 'eye', 'napkin', 'window', 'family', 'needle', 'wire',
        'finland', 'nest', 'xylophone', 'fish', 'nigeria', 'yacht', 'flag',
        'night', 'yak', 'flower', 'notebook', 'zebra', 'football', 'ocean',
        'zoo', 'forest', 'oil', 'garden', 'fountain', 'orange', 'gas',
        'france', 'oxygen', 'girl', 'furniture', 'oyster', 'glass', 'garage'
    ]

    adj = [
        'dorable', 'adventurous', 'aggressive', 'agreeable', 'alert', 'alive',
        'amused', 'angry', 'annoyed', 'annoying', 'anxious', 'arrogant',
        'ashamed', 'attractive', 'average', 'awful', 'bad', 'beautiful',
        'better', 'bewildered', 'black', 'bloody', 'blue', 'blue-eyed',
        'blushing', 'bored', 'brainy', 'brave', 'breakable', 'bright', 'busy',
        'calm', 'careful', 'cautious', 'charming', 'cheerful', 'clean',
        'clear', 'clever', 'cloudy', 'clumsy', 'colorful', 'combative',
        'comfortable', 'concerned', 'condemned', 'confused', 'cooperative',
        'courageous', 'crazy', 'creepy', 'crowded', 'cruel', 'curious', 'cute',
        'dangerous', 'dark', 'dead', 'defeated', 'defiant', 'delightful',
        'depressed', 'determined', 'different', 'difficult', 'disgusted',
        'distinct', 'disturbed', 'dizzy', 'doubtful', 'drab', 'dull', 'eager',
        'easy', 'elated', 'elegant', 'embarrassed', 'enchanting',
        'encouraging', 'energetic', 'enthusiastic', 'envious', 'evil',
        'excited', 'expensive', 'exuberant', 'fair', 'faithful', 'famous',
        'fancy', 'fantastic', 'fierce', 'filthy', 'fine', 'foolish', 'fragile',
        'frail', 'frantic', 'friendly', 'frightened', 'funny', 'gentle',
        'gifted', 'glamorous', 'gleaming', 'glorious', 'good', 'gorgeous',
        'graceful', 'grieving', 'grotesque', 'grumpy', 'handsome', 'happy',
        'healthy', 'helpful', 'helpless', 'hilarious', 'homeless', 'homely',
        'horrible', 'hungry', 'hurt', 'ill', 'important', 'impossible',
        'inexpensive', 'innocent', 'inquisitive', 'itchy', 'jealous',
        'jittery', 'jolly', 'joyous', 'kind', 'lazy', 'light', 'lively',
        'lonely', 'long', 'lovely', 'lucky', 'magnificent', 'misty', 'modern',
        'motionless', 'muddy', 'mushy', 'mysterious', 'nasty', 'naughty',
        'nervous', 'nice', 'nutty', 'obedient', 'obnoxious', 'odd',
        'old-fashioned', 'open', 'outrageous', 'outstanding', 'panicky',
        'perfect', 'plain', 'pleasant', 'poised', 'poor', 'powerful',
        'precious', 'prickly', 'proud', 'putrid', 'puzzled', 'quaint', 'real',
        'relieved', 'repulsive', 'rich', 'scary', 'selfish', 'shiny', 'shy',
        'silly', 'sleepy', 'smiling', 'smoggy', 'sore', 'sparkling',
        'splendid', 'spotless', 'stormy', 'strange', 'stupid', 'successful',
        'super'
    ]
    return f"You are a {random.choice(adj)} {random.choice(nouns)}"


if __name__ == "__main__":
    print(try_me())
