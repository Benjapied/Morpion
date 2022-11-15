#Morpion 

def plateau () :
    '''Fonction qui va créer une grille 3x3 de morpion'''
    tab = []
    for i in range (3) :
        tab2 = []
        for j in range (3) :
            tab2.append(' ')
        tab.append(tab2) 
    return tab 

print(plateau())