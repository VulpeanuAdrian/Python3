
# import time


# def fib(n):
#     if n <= 1:
#         return n
#     t = fib(n-1)+fib(n-2)
#     return t


# t0 = time.process_time()
# n = 35
# result = fib(n)
# t1 = time.process_time()
# print("fib({0})={1},({2:.2f} secs)".format(n, result, t1-t0))
# #Pag161

import pygame
import math
pygame.init()

surface_size = 1024
main_surface = pygame.display.set_mode((surface_size, surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, size, position, heading, color=(0, 0, 0), depth=0):
    trunk_ratio = 0.29
    trunk = size*trunk_ratio
    delta_x = trunk*math.cos(heading)
    delta_y = trunk*math.sin(heading)
    (u, v) = position
    newposition = (u+delta_x, v+delta_y)
    pygame.draw.line(main_surface, color, position, newposition)
    if order > 0:
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        else:
            color1 = color
            color2 = color

        newsize = size*(1-trunk_ratio)
        draw_tree(order-1, theta, newsize, newposition,
                  heading-theta, color1, depth+1)
        draw_tree(order-1, theta, newsize, newposition,
                  heading+theta, color2, depth+1)


def gameloop():
    theta = 0
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        theta += 0.01

        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size*0.9,
                  (surface_size//2, surface_size-50), -math.pi/2)
        pygame.display.flip()
        my_clock.tick(120)


gameloop()
pygame.quit()
