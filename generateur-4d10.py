import random
import sys

def lancer_des(nombre=1):
    """Simule les lancers de dés pour l'action et le risque."""
    for _ in range(nombre):
        de_action_1 = random.randint(0, 9)
        de_action_2 = random.randint(0, 9)
        de_risque_1 = random.randint(0, 9)
        de_risque_2 = random.randint(0, 9)
        
        print(f"Dé action 1 : {de_action_1} - Dé action 2 : {de_action_2} - Dé risque 1 : {de_risque_1} - Dé risque 2 : {de_risque_2}")

if __name__ == "__main__":
    # Récupération du nombre de lancers depuis les arguments du script (sys.argv)
    nb_lancers = 1
    if len(sys.argv) > 1:
        try:
            nb_lancers = int(sys.argv[1])
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
            sys.exit(1)
            
    lancer_des(nb_lancers)