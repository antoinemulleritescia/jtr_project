import codecs
from tkinter.messagebox import *

def importmot(file):
     listmot = []
     fichiersource = file
     choix = ""
     infile = codecs.open(fichiersource, 'r', encoding='utf-8')
     x = 0

     for line in infile:
          if choix == "":
               if int(line.find("Ã©")) > int(-1): # jaurai pu faire la vérif sur plus de caract spéciaux
                    choix = askyesno(title="Euuhhhh", message="Attention : il y a des caractere mal formaté, souhaitez vous retravailler le fichier ? (celui-ci sera chargé automatiquement)")
               else:
                    listmot.append(line.replace("\r\n", "")) #si pas de caract speciaux, importer dans une liste


#Je re ecrit l'ensemble des elements dans un fichier avec un autre formatage puis je l import a ma list de traitement

     if choix == True:
          infile = codecs.open(fichiersource, 'r', encoding='utf-8')
          outfile = codecs.open(fichiersource[:-4]+"_clean.txt", 'w', encoding='latin1')
          for ligne in infile:
               outfile.write(ligne)
          outfile.close()
          infile.close()
          cleanfile = open(fichiersource[:-4]+"_clean.txt", 'r', encoding='utf-8')
          for mot in cleanfile:
               listmot.append(mot)

          longlistmot = len(listmot) - 1
          while x < longlistmot:
               swap = listmot[x]
               listmot[x] = swap[:-1]
               x = x + 1

     return listmot

