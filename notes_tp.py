note_tp_1 = float(input("Quelle est ta première note de TP?"))
note_tp_2 = float(input("Quelle est ta deuxième note de TP?"))
note_tp_3 = float(input("Quelle est ta troisième note de TP?"))
L = [note_tp_1, note_tp_2, note_tp_3]
total_notes = note_tp_1 + note_tp_2 + note_tp_3
moyenne_tp = total_notes / len(L)
if note_tp_1 > note_tp_2 and note_tp_1 > note_tp_3:
    print("La meilleure note est ta première note de TP :", note_tp_1)
if note_tp_2 > note_tp_1 and note_tp_2 > note_tp_3 :
    print("La meilleure note est ta deuxième note de TP:", note_tp_2)
if note_tp_3 > note_tp_1 and note_tp_3 > note_tp_2:
    print("La meilleure note est ta troisième note de TP:", note_tp_3)
print("Ta moyenne est de", moyenne_tp)

modification_note = int(input("Quel numéro de la note de TP souhaites-tu modifier ?"))
valeur_note_modifiee = float(input("Quelle valeur souhaites-tu remplacer ?"))
if modification_note == 1 :
    note_tp_1 = valeur_note_modifiee
    L[0] = valeur_note_modifiee
    print ("Tes 3 notes de TP sont maintenant :", L)
if modification_note == 2 :
    note_tp_2 = valeur_note_modifiee
    L[1] = valeur_note_modifiee
    print ("Tes 3 notes de TP sont maintenant :", L)
if modification_note == 3 :
    note_tp_3 = valeur_note_modifiee
    L[2] = valeur_note_modifiee
    print ("Tes 3 notes de TP sont maintenant :", L)
else : print("Erreur")
