import pygame
import player, map, ghost

pygame.init()
myfont = pygame.font.SysFont(None, 25)
score = 0
screen = pygame.display.set_mode((570, 660))
done = False

ghosts = []

ghosts.append(ghost.Ghost(270, 270))
ghosts.append(ghost.Ghost(270, 270))
ghosts.append(ghost.Ghost(270, 270))
ghosts.append(ghost.Ghost(240, 270))

player = player.Player()

level = map.Map()
map = level.getmap()

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        player.moveUp(map)
    if pressed[pygame.K_DOWN]:
        player.moveDown(map)
    if pressed[pygame.K_LEFT]:
        player.moveLeft(map)
    if pressed[pygame.K_RIGHT]:
        player.moveRigth(map)
    if pressed[pygame.K_ESCAPE]:
        done = True

    if map[player.y / 30][player.x / 30] == 2:
        map[player.y / 30][player.x / 30] = 1
        score += 100

    for ghost in ghosts:
        ghost.move(map)

    screen.fill((0, 0, 0))
    map_y = len(map[0])
    map_x = len(map)
    for a in xrange(map_y):
        for b in xrange(map_x):
            if map[b][a] == 0:
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(a * 30, b * 30, 30, 30))
            if map[b][a] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(a * 30, b * 30, 30, 30))
            if map[b][a] == 2:
                pygame.draw.circle(screen, (255, 255, 255), (a * 30 + 15, b * 30 + 15), 5, 0)
    player.draw(screen)
    if level.ispoints():
        print "win"
        label = myfont.render("YOU WON! Your score: " + str(score), 1, (255, 255, 0))
        screen.blit(label, (225, 335))
        pygame.display.flip()
        clock.tick(0.5)
        done = True
    for ghost in ghosts:
        ghost.draw(screen)
        if ghost.overlap(player.y, player.x):
            print "dead"
            label = myfont.render("YOU'RE DEAD", 1, (255, 255, 0))
            screen.blit(label, (225, 335))
            pygame.display.flip()
            clock.tick(0.5)
            done = True
    scoretext = "Score: " + str(score)
    label = myfont.render(scoretext, 1, (255, 255, 0))
    screen.blit(label, (5, 5))
    pygame.display.flip()

    clock.tick(100)
