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
forca = pg.transform.scale(pg.image.load("hangman.png"),(200,200))

label_lives = main_font.render(f"Lives: {game.lives}/6",True,(255,255,255))
label_word = main_font.render(' '.join(game.letters), True, (255,255,255))
label_failed = main_font.render(f"Failled attempts: {', '.join(game.failed)}", True, (255, 255, 255))
label2= main_font.render(f"The secret word is {game.word}", True, (255,255,255))

run = True
status = None
while run:
    events = pg.event.get()
    if status is None:
        screen.fill(BG_COLOR)
        input.update(events)
        screen.blit(forca, (200, 200))
        screen.blit(input.surface, (10, 10))

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
            # TODO desenhar o boneco no ecra com base no numero de tentativas falhadas

    if status == True or status == False:
        if status == True:
            label = main_font.render(f"You've won!!!", True, (255,255,255))
        else:
            label = main_font.render(f"LOOOOOOSER!!!", True, (255,255,255))

        screen.blit(label, (150, 50))
        screen.blit(label2, (150, 100))
    pg.display.update()
    clock.tick(60)


