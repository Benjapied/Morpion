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

def pose_player(tab,nb) :
    '''Fonction qui permet au joueur de placer son symbol en fonction du nombre qu'il rentre''' 
    if nb == '1' :
        if tab[0][0] == ' ':
            tab[0][0] = 'X' 
    if nb == '2' :
        if tab[0][1] == ' ':
            tab[0][1] = 'X' 
    if nb == '3' :
        if tab[0][2] == ' ':
            tab[0][2] = 'X' 
    if nb == '4' :
        if tab[1][0] == ' ':
            tab[1][0] = 'X' 
    if nb == '5' :
        if tab[1][1] == ' ':
            tab[1][1] = 'X' 
    if nb == '6' :
        if tab[1][2] == ' ':
            tab[1][2] = 'X' 
    if nb == '7' :
        if tab[2][0] == ' ':
            tab[2][0] = 'X' 
    if nb == '8' :
        if tab[2][1] == ' ':
            tab[2][1] = 'X' 
    if nb == '9' :
        if tab[2][2] == ' ':
            tab[2][2] = 'X' 
    else :
        print("Entrez un nombre valide")
    
def cases_libres (tab):
    '''Fonction qui renovoie une liste contenant les cases vides, elle va servir à arreter le jeu si cette liste est vide'''
    liste = []
    for i in range (3) :
        for j in range(3) :
            if tab[i][j] == ' ' :
                liste.append((i,j))
    #Cette liste contient des tuples des coordonnées des cases libres
    return liste
                
def pose_bot (tab) :
    '''Fonction qui va placer un signe du bot aléatoirement sur la grille'''
    liste =  cases_libres(tab) 
    #Cette liste de tuple contenant les coordonnées libres va permettre de ne pas placer de symbol sur une case déja prise
    #Mais aussi à savoir si le bot peut placer un symbol si la grille est pleine 
    if liste != []:
        coo = r.choice(liste)
        tab[coo[0]][coo[1]] = 'O' 
        return 
    else :
        return 

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

#----- A garder -----
tableau = plateau()
printTab(tableau)

example()
#-------------------

'''while cases_libres(tableau) != [] :
    #On demande au joueur de choisir son chiffre et on place son symbol sur la grille
    nombre = input("Choisissez un nombre pour placer votre croix: ")
    pose_player(tableau,nombre)
    printTab(tableau)
    if checkAll(tableau,'X') == True :
        print("Le joueur a gagné")
        break
    pose_bot(tableau)
    printTab(tableau)
    if checkAll(tableau,'0') == True :
        print("Le bot a gagné")
        break'''


#Bot inbattable 
#On définit une fonction qui va placer des symbols 

def firstHit (tab) :
    if tab[1][1] == ' ' :
        tab[1][1] = '0' 
    else :
        tab[0][0] = '0'

def bot2fou (tab) :
    #Si c'est le premier ou le deuxieme coup
    print(len(cases_libres(tab)))
    if len(cases_libres(tab)) == 9 or len(cases_libres(tab)) == 8 : 
        firstHit(tab)
    temp = mybWin (tableau, 'X')
    if temp != False :
        if temp == 0 :
            if tab[0][0] == ' ' :
                tab[0][0] = '0' 
            if tab[0][1] == ' ' :
                tab[0][1] = '0' 
            if tab[0][2] == ' ' :
                tab[0][2] = '0' 
        if temp == 1 :
            if tab[1][0] == ' ' :
                tab[1][0] = '0' 
            if tab[1][1] == ' ' :
                tab[1][1] = '0' 
            if tab[1][2] == ' ' :
                tab[1][2] = '0' 
        if temp == 2 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
        if temp == 2 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
        if temp == 2 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
        if temp == 2 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
        if temp == 2 :
            if tab[2][0] == ' ' :
                tab[2][0] = '0' 
            if tab[2][1] == ' ' :
                tab[2][1] = '0' 
            if tab[2][2] == ' ' :
                tab[2][2] = '0' 
        

    
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
    print(liste)
    return liste

def mybWin (tab,sign) :
    ali = align(tab)
    for i in range (len(ali)) :
        if str(sign) in ali[i] and str(sign) in ali[i] and ' ' in ali[i] :
            return i 
    return False

tableau[1][1] = 'X' 
tableau[1][2] = 'X' 

bot2fou(tableau)

printTab(tableau)

print(mybWin(tableau, 'X'))