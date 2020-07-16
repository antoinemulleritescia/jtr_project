# On importe Tkinter
from tkinter import *
from tkinter import filedialog
from Process import *
from tkinter.messagebox import *



def envoi():
    if fenetre.filename != 0:
        #on recup toutes les options de brute force
        login = login_box.get()
        check = check_box.get()
        type = typeatta.get()
        var_maj = maj.get()
        var_addcara = addcara.get()
        var_addchif = addchif.get()
        var_revdou = revdou.get()
        var_comboani = combo.get()
        var_voy = voy.get()
        nbchiffre = int(spinaddchif.get())
        #le fichier
        file = fenetre.filename
        # on envoi
        mdp = selection(login,check,var_maj,var_addcara,var_addchif,var_revdou,var_comboani,var_voy,file,type,nbchiffre)
        textecrit.config(text = mdp)

def importfile(): #explicite
    fenetre.filename = filedialog.askopenfilename(initialdir="C:", title="Import bibliotheque ", filetypes=(("genre un fichier texte","*.txt"),("all files","*.*")))

def info(): #Msg d info
    info = ['Attention',
            '',
            'Ceci est une V1, les fonctions de bases sont fonctionnel',
            '',
            'il est possible que le programme affiche "ne répond pas" pas de panique celui-ci génère et travail sur la liste des élèments a vérifier',
            '',
            'Si utilisation d une bibliothèque, il est possible que le logiciel le retravail et recrèer un fichier avec le meme nom suivi de _clean',
            '',
            'Future Update : ',
            '',
            'Afin d eviter les problemes de saturation de ram et donc les plantages sur les longues liste, il sera possible d enrengistrer l ensemble des elements a tester en créant un fichier avec tout les combinaisons. Mais cela prends plus de temps et dépendra de la vitesse du HDD' ]
    showinfo("Information importante", "\n".join(info))

# On crée une fenêtre, racine de notre interface

fenetre = Tk()
fenetre.title("Not John The Ripper")
fenetre.filename = 1
fenetre.geometry("550x500")




#Yolo variable
maj = IntVar()
addcara = IntVar()
addchif = IntVar()
typeatta = IntVar()
revdou = IntVar()
combo = IntVar()
voy = IntVar()

login_box = StringVar()
check_box = StringVar()
typeatta = IntVar()
choix = 0

file = ""

#def des elements


champ_label = Label(fenetre, text="Brute Force MD5 (by Antoine MULLER)", width=32, height=1, relief=GROOVE)
bouton_choix1 = Checkbutton(fenetre, text="Varation de majuscule", variable=maj)
bouton_choix2 = Checkbutton(fenetre, text="Ajout d'un caractere", variable=addcara)
bouton_choix3 = Checkbutton(fenetre, text="Ajout de chiffre", variable=addchif)
spinaddchif = Spinbox(fenetre, from_=0,to=10, width=3)
bouton_choix4 = Checkbutton(fenetre, text="Inverser le mot et le doubler", variable=revdou)
bouton_choix5 = Checkbutton(fenetre, text="Combinaison de deux mots collé", variable=combo)
bouton_choix6 = Checkbutton(fenetre, text="Convertir les voyelles en chiffre", variable=voy)

text_typeatta = Label(fenetre, text="Type d'attaque", width=20, height=1, relief=GROOVE)
atta_pseudo = Radiobutton(fenetre, text="Via pseudo", variable=typeatta, value=0)
atta_bibli = Radiobutton(fenetre, text="Via biblithèque", variable=typeatta, value=1)

text_varia = Label(fenetre, text="Options de brute force", width=20, height=1, relief=GROOVE)

bouton = Button(fenetre, text="GO", command=envoi)
text_login = Label(fenetre, text="Login")
text_check = Label(fenetre, text="Hash a vérifier (md5)")
saisie_login = Entry(fenetre, textvariable=login_box, width=30)
saisie_check = Entry(fenetre, textvariable=check_box, width=34)
bouton_import = Button(fenetre, text="Importer un fichier bibliothéque", command=importfile)

text_resultat = Label(fenetre, text="Voici le mot de passe trouvé")
textecrit = Label(fenetre, width=15, relief=RAISED)

bouton_info = Button(fenetre, text="Info", command=info)


# SECTION PACK POUR AFFICHAGE DANS FENETRE (placement)

champ_label.place(x=170, y=10)

text_login.place(x=120, y=50)
saisie_login.place(x=50, y=70)

text_check.place(x=340, y=50)
saisie_check.place(x=300, y=70)

text_typeatta.place(x=200, y=190)
atta_pseudo.place(x=150, y=220)
atta_bibli.place(x=300, y=220)

text_varia.place(x=200, y=290)

bouton_choix1.place(x=100, y=320)
bouton_choix2.place(x=100, y=340)
bouton_choix3.place(x=100, y=360)
spinaddchif.place(x=211, y=363)
bouton_choix4.place(x=300, y=320)
bouton_choix5.place(x=300, y=340)
bouton_choix6.place(x=300, y=360)

bouton.place(x=250, y=450)
bouton_import.place(x=30, y=450)

text_resultat.place(x=200, y=100)
textecrit.place(x=220, y=120)

bouton_info.place(x=400, y=450)

# fin de fenetre


fenetre.mainloop()



