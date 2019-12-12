import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
width, height = 600, 95
image_size = 130, 80
size = width, height
screen = pygame.display.set_mode(size)
x = 10
v = 60  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")
    image = pygame.transform.scale(image, image_size)

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.y = 10

    def next_move(self):
        global v
        self.rect.x += v * fps / 1000
        if self.rect.x > width - image_size[0] or self.rect.x == 0:
            v *= (-1)
            self.image = pygame.transform.flip(self.image, 1, 0)


all_sprites = pygame.sprite.Group()

im = Car(all_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    im.next_move()
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
