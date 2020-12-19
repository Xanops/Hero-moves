import pygame

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite(sprites)
sprite.image = pygame.image.load('data/creature.png')
sprite.rect = sprite.image.get_rect()
sprite.rect.x, sprite.rect.y = 0, 0
sprites.draw(screen)
pygame.display.flip()

if __name__ == '__main__':
    pygame.display.set_caption('Герой двигается!')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                screen.fill((255, 255, 255))
                if event.key == pygame.K_UP:
                    sprite.rect.y -= 10
                    sprites.draw(screen)
                    pygame.display.flip()
                if event.key == pygame.K_LEFT:
                    sprite.rect.x -= 10
                    sprites.draw(screen)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    sprite.rect.x += 10
                    sprites.draw(screen)
                    pygame.display.flip()

                if event.key == pygame.K_DOWN:
                    sprite.rect.y += 10
                    sprites.draw(screen)
                    pygame.display.flip()

            if event.type == pygame.QUIT:
                running = False
    # завершение работы:
    pygame.quit()
