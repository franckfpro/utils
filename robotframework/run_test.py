# pip install robotframework robotframework-seleniumlibrary
# robot test_github.robot

import robot

def lancer_test():
    print("Démarrage du test Robot Framework...")
    
    # La fonction run() exécute le fichier .robot et génère 
    # automatiquement les rapports (log.html, report.html)
    robot.run("test_github.robot")
    
    print("Test terminé. Vous pouvez consulter le fichier log.html généré.")

if __name__ == "__main__":
    lancer_test()
