import pygame

screen = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()

paddle = [[500, 900], [250, 10]]
ball = (10, 10)
brick = ([500, 100], [50, 50])
proj = ([625, 900], [10, 10])
launched = False
done = False
sx = 5
sy = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        paddle[0][0] -= 15

    if pressed[pygame.K_RIGHT]:
        paddle[0][0] += 15

    if pressed[pygame.K_UP] and not launched:
        launched = True
        proj[0][0] = paddle[0][0] + paddle[1][0] // 2

    if launched:
        proj[0][1] -= 15


    if ball[0] == 0 or ball[0] == 1280:
        sx *= -1
    if ball[1] == 0 or ball[1] == 960:
        sy *= -1
    if ball[0] >= paddle[0][0] and ball[0] <= (paddle[0][0] + 250) and ball[1] == paddle[0][1]:
        sy *= -1
    if ball[1] == 960 and ball[0] <= 1280:
        done = True
    if ball[0] >= brick[0][0] and ball[0] <= (brick[0][0] + 50) and ball[1] >= brick[0][1] and ball [1] <= (brick[0][1] + 50):
        sy *= -1
        brick[1][1] *= 0
        brick[1][0] *= 0

    if paddle[0][0] <= 0:
        paddle[0][0] = 0
    sw, sh = screen.get_size()
    if paddle[0][0] + paddle[1][0] > sw:
        paddle[0][0] = sw - paddle[1][0]

    if proj[0][1] == 0:
        launched = False
        proj[0][0] = paddle[0][0] + 125
        proj[0][1] = paddle[0][1]

    if proj[0][0] == ball[0] and proj[0][1] == ball[1]:
        sy *= -1
        launched = False

    if (proj[0][0] >= brick[0][0] and proj[0][0] <= brick[0][0] + 50) and (proj[0][1] >= brick[0][1])

    ball = (ball[0] + sx, ball[1] + sy)

    pygame.draw.rect(screen, (255, 0, 0), (475, 1025, 25, 25), 0 )

    screen.fill((0, 0, 0))
    if launched:
        pygame.draw.rect(screen, (255, 255,255), proj, 0)

    pygame.draw.rect(screen, (0, 255, 0), paddle, 0)
    pygame.draw.circle(screen,(0, 0, 255), ball, 12, 0 )
    pygame.draw.rect(screen, (255, 0, 0), brick, 1)
    pygame.display.flip()
    clock.tick(60)