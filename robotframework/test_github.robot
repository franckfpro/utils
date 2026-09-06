*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://github.com/franckfpro?tab=repositories
${BROWSER}    Firefox

*** Test Cases ***
Ouvrir Le Site De Github
    [Documentation]    Lance Firefox et navigue vers github.
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    
    # Pause de 5 secondes pour visualiser la page
    Sleep    5s
    
    # Ferme le navigateur à la fin
    Close Browser
