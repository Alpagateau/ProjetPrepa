import pygame
import numpy as np

class ball:
    def __init__(self, id, value, parentID):
        self.id = id
        self.value = value
        self.parentID = parentID

        self.position = [np.random.randint(0, 800) ,np.random.randint(0, 800)]
        self.speed = [0,0]
        self.acc = [0,0]
        self.mass = len(self.value) * 10

background_colour = (255,255,255)
(width, height) = (800, 800)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TREEEEEE')

test = [
    (0,[255,255,255], 2),
    (1, [255,255,255,255], 0),
    (2, [255,255,255,255], 1),
    (3, [255,255,255,255], 1),
    (4, [255,255,255,255], 1),
    (5, [255,255,255,255], 1)
]

balls = []
links = []

def populate(v):
    global balls, links
    for i in range(len(v)):
        x,y,z = v[i]
        balls += [ball(x, y, z)]
        links += [[x,z]]

    balls.sort(key= lambda b: b.id)

def draw(screen):
    for i in range(len(links)):
        pygame.draw.line(
            screen,
            (255,0,100),
            [int(balls[links[i][0]].position[0]), int(balls[links[i][0]].position[1])],
            [int(balls[links[i][1]].position[0]), int(balls[links[i][1]].position[1])],
            1
        )
    for i in range(len(balls)):
        pygame.draw.circle(
            screen,
            (255,0,0),
            [int(balls[i].position[0]), int(balls[i].position[1])],
            len(balls[i].value)**2
        )

def distance_vector(ball1, ball2):
    v = [ball2.position[0] - ball1.position[0], ball2.position[1] - ball1.position[1]]
    d = np.sqrt(v[0] ** 2 + v[1] ** 2)
    return (v, d)

def simulate(dt):
    #zero all balls acc:
    for i in range(len(balls)):
        balls[i].acc = [0,0]

    #increment force by distance
    baseDist = 100
    incr = -0.001
    for i in range(len(links)):
        v,d = distance_vector(balls[links[i][0]], balls[links[i][1]])
        if d > baseDist:
            balls[links[i][1]].position[0] += v[0] * incr * .5
            balls[links[i][1]].position[1] += v[1] * incr * .5

            balls[links[i][0]].position[0] -= v[0] * incr * .5
            balls[links[i][0]].position[1] -= v[1] * incr * .5
        if d<baseDist:
            balls[links[i][0]].position[0] += v[0] * incr * .5
            balls[links[i][0]].position[1] += v[1] * incr * .5

            balls[links[i][1]].position[0] -= v[0] * incr * .5
            balls[links[i][1]].position[1] -= v[1] * incr * .5
"""
    for i in range(len(balls)):
        for j in range(len(balls)):
            v,d = distance_vector(balls[i], balls[j])
            if d > baseDist:
                balls[j].position[0] += v[0] * incr * .1
                balls[j].position[1] += v[1] * incr * .1

                balls[i].position[0] -= v[0] * incr * .1
                balls[i].position[1] -= v[1] * incr * .1
            if d<baseDist:
                balls[i].position[0] += v[0] * incr * .1
                balls[i].position[1] += v[1] * incr * .1

                balls[j].position[0] -= v[0] * incr * .1
                balls[j].position[1] -= v[1] * incr * .1
"""
def start():
    global screen
    running = True
    while running:
        screen.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        simulate(0.01)
        draw(screen)
        pygame.display.flip()