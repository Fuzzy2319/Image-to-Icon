import sys
import os
from PIL import Image
nomImage=""
while(nomImage == ""):
    nomImage=input("Veuillez saisir le chemin de l'image : ")
    if(nomImage == ""):
        print("Le chemin ne doit pas être vide")
try:
    img=Image.open(nomImage)
except IOError:
    print("Erreur sur ouverture du fichier " + nomImage)
    input()
    sys.exit(1)
taille=img.size
colonne=taille[0]
ligne=taille[1]
if(img.mode == "RGBA"):
    print(img.format,taille[0],"X",taille[1], img.mode)
    imgF=Image.new(img.mode,img.size)
    for i in range(ligne-1,0,-1):
        for j in range(colonne-1,0,-1):
            pixel = img.getpixel((j,i))
            p = (pixel[0], pixel[1], pixel[2], pixel[3])
            imgF.putpixel((j,i), p)
else:
    print(img.format,taille[0],"X",taille[1], img.mode)
    imgF=Image.new(img.mode,img.size)
    for i in range(ligne-1,0,-1):
        for j in range(colonne-1,0,-1):
            pixel = img.getpixel((j,i))
            p = (pixel[0], pixel[1], pixel[2])
            imgF.putpixel((j,i), p)
imgF.save("icon.ico","ICO")
imgF.close()
os.system("start .")