ACTION_RESULT = {
    ('wizard', 'warrior'): 1,
    ('warrior', 'robber'): 1,
    ('robber', 'wizard'): 1,
    ('warrior', 'wizard'): -1,
    ('robber', 'warrior'): -1,
    ('wizard', 'robber'): -1,
    ('wizard', 'wizard'): 0,
    ('robber', 'robber'): 0,
    ('warrior', 'warrior'): 0
}

HEROES = {
    '1': 'wizard',
    '2': 'warrior',
    '3': 'robber'
}

LIVES = 5

RULES = '''
            RULES OF THE GAME  

    To win, you need to guess which card the       
    opponent will choose and choose the one that   
    will defeat the opponent's card.               
    Available cards: Warrior, Robber, Wizard. 

        The Wizard defeats the Warrior.         
        The Warrior defeats the Robber.         
        The Robber defeats the Wizard.          	
   	
            Key 1 - Warrior
            Key 2 - Robber
            Key 3 - Wizard
'''
