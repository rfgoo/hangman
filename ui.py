import pygame as pg
import pygame_textinput as pgi
import hangman_back as hg
game = hg.Hangman()
BG_COLOR=(250,128,114)
TXT_COLOR=(0,0,0)
main_font = pg.font.SysFont("comicsans", 30)
pg.init()

input = pgi.TextInputVisualizer(font_color=TXT_COLOR)
clock = pg.time.Clock()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Hangman")
forca = pg.transform.scale(pg.image.load("hangman.png"),(300, 300))
head = pg.transform.scale(pg.image.load("head.png"), (64, 64))
torso = pg.transform.scale(pg.image.load("torso.png"), (64, 64))
l_arm = pg.transform.scale(pg.image.load("l_arm.png"), (40, 40))
r_arm = pg.transform.flip(l_arm, True, False)
l_leg = pg.transform.scale(pg.image.load("leg.png"), (60, 60))
r_leg = pg.transform.flip(l_leg, True, False)

label_lives = main_font.render(f"Lives: {game.lives}/6",True,(255,255,255))
label_word = main_font.render(' '.join(game.letters), True, (255,255,255))
label_failed = main_font.render(f"Failled attempts: {', '.join(game.failed)}", True, (255, 255, 255))
label2 = main_font.render(f"The secret word is {game.word}", True, (255, 255, 255))

run = True
status = None
while run:
    events = pg.event.get()
    if status is None:
        screen.fill(BG_COLOR)
        input.update(events)
        screen.blit(forca, (150, 100))
        screen.blit(input.surface, (10, 10))

    if game.lives >= 1:
        screen.blit(head, (355,185))
    if game.lives >= 2:
        screen.blit(torso,(355,185+63))
    if game.lives >= 3:
        screen.blit(l_arm, (323, 185 + 50))
    if game.lives >= 4:
        screen.blit(r_arm, (326+85, 185 + 50))
    if game.lives >= 5:
        screen.blit(l_leg, (323+50, 185 + 50+50+25))
    if game.lives >= 6:
        screen.blit(r_leg, (323+20, 185 +50+50+25))

    for event in events:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and status is None:


            status = game.play(input.value)

            label_lives = main_font.render(f"Lives: {game.lives}/6", True, (255, 255, 255))
            label_word = main_font.render(' '.join(game.letters), True, (255, 255, 255))
            label_failed = main_font.render(f"Failled attempts: {', '.join(game.failed)}", True, (255, 255, 255))

            input.value = ""

    screen.blit(label_lives,(0,550))
    screen.blit(label_word, (200, 400))
    screen.blit(label_failed, (165, 550))

    if status == True or status == False:
        if status == True:
            label = main_font.render(f"You've won!!!", True, (255,255,255))
        else:
            label = main_font.render(f"LOOOOOOSER!!!", True, (255,255,255))

        screen.blit(label, (150, 10))
        screen.blit(label2, (150, 60))
    pg.display.update()
    clock.tick(60)
