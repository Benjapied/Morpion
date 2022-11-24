#Morpion 
import random as r

def plateau () :
    '''Fonction qui va créer une grille 3x3 de morpion'''
    tab = []
    for i in range (3) :
        tab2 = []
        for j in range (3) :
            tab2.append(' ')
        tab.append(tab2) 
    return tab 

def printTab(tab): 
    '''Print un tableau a format tableau et non liste, technique de gitan askip'''
    for i in range (len(tab)) :
        print(tab[i])
        print()

def example() :
    '''Cette fonction affiche quelle case de la grille correspond à quel chiffre'''
    tab = []
    incrementeur = 1
    for i in range (3) :
        tab2 = []
        for j in range (3) :
            tab2.append(incrementeur)
            incrementeur = incrementeur + 1
        tab.append(tab2)
    print("Pour placer votre symbole, entrez un chiffre comme dans l'exemple ci-dessous")
    printTab(tab)

def pose_player(tab,nb,sign) :
    '''Fonction qui permet au joueur de placer son symbol en fonction du nombre qu'il rentre''' 
    if nb == '1' and tab[0][0] == ' ':
        tab[0][0] = str(sign) 
        return
    if nb == '2' and tab[0][1] == ' ' :
        tab[0][1] = str(sign)  
        return
    if nb == '3' and tab[0][2] == ' ':
        tab[0][2] = str(sign)  
        return
    if nb == '4' and tab[1][0] == ' ':
        tab[1][0] = str(sign) 
        return 
    if nb == '5' and tab[1][1] == ' ':
        tab[1][1] = str(sign)  
        return
    if nb == '6' and tab[1][2] == ' ':
        tab[1][2] = str(sign) 
        return 
    if nb == '7' and tab[2][0] == ' ':
        tab[2][0] = str(sign) 
        return 
    if nb == '8' and tab[2][1] == ' ':
        tab[2][1] = str(sign) 
        return 
    if nb == '9' and tab[2][2] == ' ' :
        tab[2][2] = str(sign) 
        return 
    else :
        nb = input("Entrez un nombre valide: ")
        pose_player(tab,nb) 
    
def cases_libres (tab):
    '''Fonction qui renovoie une liste contenant les cases vides, elle va servir à arreter le jeu si cette liste est vide'''
    liste = []
    for i in range (3) :
        for j in range(3) :
            if tab[i][j] == ' ' :
                liste.append((i,j))
    #Cette liste contient des tuples des coordonnées des cases libres
    return liste

def checkAll(tab,sign):
    '''Fonction qui vérifier à chaque tour si il y a un alignement de trois signes mis en parametre'''
    if tab[0][0] == str(sign) and tab[0][1] == str(sign) and tab[0][2] == str(sign) :
        return True
    if tab[1][0] == str(sign) and tab[1][1] == str(sign) and tab[1][2] == str(sign) :
        return True
    if tab[2][0] == str(sign) and tab[2][1] == str(sign) and tab[2][2] == str(sign) :
        return True
    if tab[0][0] == str(sign) and tab[1][0] == str(sign) and tab[2][0] == str(sign) :
        return True
    if tab[0][1] == str(sign) and tab[1][1] == str(sign) and tab[2][1] == str(sign) :
        return True
    if tab[0][2] == str(sign) and tab[1][2] == str(sign) and tab[2][2] == str(sign) :
        return True
    if tab[0][0] == str(sign) and tab[1][1] == str(sign) and tab[2][2] == str(sign) :
        return True
    if tab[0][2] == str(sign) and tab[1][1] == str(sign) and tab[2][0] == str(sign) :
        return True
    else:
        return False

def firstHit (tab) :
    '''Cette fonction va faire le premier coup du bot en fonction du premier coup du joueur'''
    if tab[1][1] == ' ' :
        tab[1][1] = '0' 
    else :
        tab[0][0] = '0'

def secondHit (tab) :
    '''Cette fonction va faire le deuxiemei coup du bot en fonction du deuxieme coup du joueur'''
    temp1 = align(tab)[6]
    temp2 = align(tab)[7]
    if temp1[0] == 'X' and temp1[1] == '0' and temp1[2] == 'X' :
        tab[0][1] = '0' 
        return
    elif temp2[0] == 'X' and temp2[1] == '0' and temp2[2] == 'X' :
        tab[0][1] = '0'
        return
    else :
        return

def bot2fou (tab) :
    #Si c'est le premier ou le deuxieme coup, le bot va placer son signe au centre 
    temp = mybWin (tab, '0')
    temp2 = mybWin (tab, 'X')
    if len(cases_libres(tab)) == 9 or len(cases_libres(tab)) == 8 : 
        firstHit(tab)
        return
    if len(cases_libres(tab)) == 7 or len(cases_libres(tab)) == 6 : 
        secondHit(tab)
        if len(cases_libres(tab)) == 5 or len(cases_libres(tab)) == 4 :
            return
    if temp != False :
        if temp == 1 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[0][1] == ' ' :
                tab[0][1] = '0' 
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
            return
        if temp == 2 :
            if tab[1][0] == ' ' :
                tab[1][0] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[1][2] == ' ' :
                tab[1][2] = '0'
            return 
        if temp == 3 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
            return
        if temp == 4 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[1][0] == ' ' :
                tab[1][0] = '0' 
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            return
        if temp == 5 :
            if tab[0][1] == ' ' :
                tab[0][1] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            return
        if temp == 6 :
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
            if tab[1][2] == ' ' :
                tab[1][2] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
            return
        if temp == 7 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
            return
        if temp == 8 :
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            return
    elif temp2 != False :
        if temp2 == 1 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[0][1] == ' ' :
                tab[0][1] = '0' 
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
            return
        if temp2 == 2 :
            if tab[1][0] == ' ' :
                tab[1][0] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[1][2] == ' ' :
                tab[1][2] = '0' 
            return
        if temp2 == 3 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
            return
        if temp2 == 4 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[1][0] == ' ' :
                tab[1][0] = '0' 
            if tab[2][0] == ' ' :
                tab[2][0] = '0'
            return 
        if temp2 == 5 :
            if tab[0][1] == ' ' :
                tab[0][1] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            return
        if temp2 == 6 :
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
            if tab[1][2] == ' ' :
                tab[1][2] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
            return
        if temp2 == 7 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
            return
        if temp2 == 8 :
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[2][0] == ' ' :
                tab[2][0] = '0'
            return
    elif tab[0][0] == ' ' :
        tab[0][0] = '0' 
        return
    elif tab[0][2] == ' ' :
        tab[0][2] = '0'
        return
    elif tab[2][2] == ' ' :
        tab[2][2] = '0'
        return
    elif tab[2][0] == ' ' :
        tab[2][0] = '0'
        return
    else :
        coo = r.choice(cases_libres(tab))
        tab[coo[0]][coo[1]] = '0'
        return


def align(tab) :
    '''Fonction qui crée une liste avec des listes contenant les alignements de la grilles.
    Il y en a 8 '''
    liste = []
    liste.append(tab[0])
    liste.append(tab[1])
    liste.append(tab[2])
    l2 = []
    for i in range (3) :
        l2.append(tab[0][i])
        l2.append(tab[1][i])
        l2.append(tab[2][i])
        liste.append(l2)
        l2 = []
    liste.append([tab[0][0],tab[1][1],tab[2][2]])
    liste.append([tab[2][0],tab[1][1],tab[0][2]])
    return liste

def mybWin (tab,sign) :
    '''Cette fonction va voir si il y a un alignement qui est sur le point de gagner
    si la premiere ligne par exemple contient deux signes, on va renvoyer l'indice de l'alignement ou il y a une possibilité de win'''
    ali = align(tab)
    #ali contient la liste des alignements
    for i in range (len(ali)) :
        if ali[i].count(str(sign)) == 2 and ali[i].count(' ') :
            return i + 1
    return False

#----- A garder -----
print(" __  __                          _                 ")
print("|  \/  |                        (_)                ")
print("| \  / |   ___    _ __   _ __    _    ___    _ __  ")
print("| |\/| |  / _ \  | '__| | '_ \  | |  / _ \  | '_ \ ")
print("| |  | | | (_) | | |    | |_) | | | | (_) | | | | |")
print("|_|  |_|  \___/  |_|    | .__/  |_|  \___/  |_| |_|")
print("                        | |                        ")
print("                        |_|                        ")

tableau = plateau()

example()
#-------------------

print("Jouer contre un bot ou contre un ami ?")
answer = ""
while answer != "Bot" and answer != "Ami" and answer != "Seul" :
    answer = input("Bot/ Ami: ")
if answer == "Bot" :
    while cases_libres(tableau) != [] :
        #On demande au joueur de choisir son chiffre et on place son symbol sur la grille
        nombre = input("Choisissez un nombre pour placer votre croix: ")
        pose_player(tableau,nombre,'X')
        printTab(tableau)
        if checkAll(tableau,'X') == True :
            print("Le joueur a gagné")
            break
        print("Le bot a joué ici")
        bot2fou(tableau)
        printTab(tableau)
        if checkAll(tableau,'0') == True :
            print("Le bot a gagné")
            break
        if cases_libres(tableau) == [] :
            print("Egalité")
            break 
elif answer == "Ami" :
    while cases_libres(tableau) != [] :
        #On demande au joueur de choisir son chiffre et on place son symbol sur la grille
        nombre = input("Choisissez un nombre pour placer votre croix: ")
        pose_player(tableau,nombre,'X')
        printTab(tableau)
        if checkAll(tableau,'X') == True :
            print("Le joueur 1 a gagné")
            break
        nombre = input("Choisissez un nombre pour placer votre rond: ")
        pose_player(tableau,nombre,'0')
        printTab(tableau)
        print("Le joueur 2 a joué ici")
        if checkAll(tableau,'0') == True :
            print("Le joueur 2 a gagné")
            break
        if cases_libres(tableau) == [] :
            print("Egalité")
            break 
elif answer == "Seul" :
    tabb = [['X','X','X'],['X','X','X'],['X','X','X']]
    printTab(tabb)
    print("Bravo vous avez gagné")



