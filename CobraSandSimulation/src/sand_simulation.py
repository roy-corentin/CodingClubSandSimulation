import pygame
from src.world import World


def simulation_loop(world: World) -> int:
    clock: pygame.time.Clock = pygame.time.Clock()
    fps: int = 60
    run: bool = True

    while run:
        if world.handle_input() == 84:
            run = False
        world.update()
        world.draw()
        clock.tick(fps)
    return 0


def simulation() -> int:
    width: int = 800
    height: int = 800

    pygame.init()
    world = World(width, height)
    simulation_loop(world)
    pygame.quit()
    return 0
