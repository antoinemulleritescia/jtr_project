from os import *
import os
from f_import_file import *
from f_hash import *
from gen import *


#recup de tout les trucs a taff
def selection(login,check,var_maj,var_addcara,var_addchif,var_revdou,var_comboani,var_voy,file,type,nbchiffre):


    #Import du fichier, si deja présent pour eviter de le reimport a chaque fois sinon on fait le test sur le pseudo
    if file != 0 and type == 1:
        conv = file[:-4]+"_clean.txt"
        if os.path.exists(conv) == True:
            file = conv
            listfinal = importmot(file)
        else:
            listfinal = importmot(file)
    else:
        listfinal = [login]

    # ========================================================================
    # ===============ALORS JE CROIS QUE J INITIALISE LA CLASS========¿¿¿======
    # ========================================================================

    list = generateur(listfinal)
    end = listfinal

    #en fonction des options je crèer tout les variation

    if var_maj == 1:            #Maj et minus
        end = list.convMaj()

    if var_addcara == 1:  # Ajout d un caract
        end = list.addCarac()

    if var_addchif == 1:  # Ajout des chiffres avant et arrierre
        end = list.chiffreAD(nbchiffre)

    if var_revdou == 1:  # Inversion du mot et le double
        end = list.reversedouble()

    if var_comboani == 1:  # Combo de deux animaux
        end = list.comboani()

    if var_voy == 1:  # Voy
        end = list.voy()

    #j envoi la list final au checker
    mdp = tohash(check,end)
    return mdp
