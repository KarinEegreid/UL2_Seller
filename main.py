# Karl Paju IS22 ÜL 2 Tekstide ja piltide lisamine

import pygame # Impordib pygame

pygame.init() # Käivitab pygame

#Ekraani seaded

Screen = pygame.display.set_mode([640,480]) # Ekraani loomine
pygame.display.set_caption("Karl Paju IS22 ÜL2") # Ekraanile nime andmine
Screen.fill([204,255,204]) # Täidab ekraani sisestatud värvi hex koodiga.

#Lisame taustapildid ning muud

# Tausta pildi lisamine
bg = pygame.image.load("taust.jpg") # Tausta lisamine
Screen.blit(bg,[0,0]) # Pildi asukoht

#Selleri lisamine ekraanile
seller = pygame.image.load("seller.png") # Selleri lisamine ekraanile
seller = pygame.transform.scale(seller, [150,300]) #Selleri laiuse ja pikkuse muutmine
Screen.blit(seller, [10,120]) # Selleri asukohta  paigaldamine

#Jutumulli lisamine ekraanile
jutumull = pygame.image.load("jutumull.png") # Jutumulli lisamine ekraanile
jutumull = pygame.transform.scale(jutumull, [200,200]) # jutumulli laiuse ja pikkuse muutmine
Screen.blit(jutumull, [150,30]) # jutumulli asukoha paigaldamine

# Teksti lisamine ekraanile
font = pygame.font.Font(pygame.font.match_font("arial"),15)
text = font.render("Tervist, minu nimi on Karl", True, [255,255,255])

#Teksti kasti suurus
text_width = text.get_rect().width # muutuja
text_height = text.get_rect().height # muutuja

Screen.blit(text, [250-text_width/2,120-text_height/2]) # Ekraanil paigutatakse ära kus asub tekst


pygame.display.flip() # uuendab ekraani

# Loopi loomine
running = True


while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
