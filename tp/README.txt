Instructions pour les scripts du TP1 :

  Pour convertir les étiquettes PTB en étiquettes Universelles :
    
    (dans le dossier contenant POSTags_PTB_Universal_Linux.txt et
    wsj_0010_sentence.pos.ref) 

    python ptb_to_univ.py

    Le fichier de sortie est wsj_0010_sample.txt.pos.univ.ref.

  Pour générer le tableau des entités nommées d'un texte :

    (dans le dossier contenant votre fichier avec les entités
    nommées)    

    python ner_to_table.py votre_fichier

    L'argument est votre fichier après analyse par l'outil de
    reconnaissance des entités nommées.
    Le script renvoie le résultat dans votre_fichier.table.
