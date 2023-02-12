import sys

import pygame
from pygame.mouse import get_pos as mouse_pos
from pygame.mouse import get_pressed as mouse_buttons

from settings import *


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        # Support lines.
        self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.support_line_surf.set_colorkey('green')
        self.support_line_surf.set_alpha(30)

        # Cluster lines
        self.cluster_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.cluster_line_surf.set_colorkey('green')
        # self.cluster_line_surf.set_alpha(100)

        self.clock = pygame.time.Clock()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.place_obj(event)

    def draw_tile(self):
        # Basic tile lines
        cols = WINDOW_WIDTH // TILE_SIZE
        rows = WINDOW_HEIGHT // TILE_SIZE

        self.support_line_surf.fill('green')

        for col in range(cols):
            x = col * TILE_SIZE
            pygame.draw.line(
                self.support_line_surf, LINE_COLOR, (x, 0), (x, WINDOW_WIDTH))

        for row in range(rows):
            y = row * TILE_SIZE
            pygame.draw.line(
                self.support_line_surf, LINE_COLOR, (0, y), (WINDOW_HEIGHT, y))

        # Cluster tile lines
        cluster_cols = WINDOW_HEIGHT // CLUSTER_SIZE
        cluster_rows = WINDOW_WIDTH // CLUSTER_SIZE

        self.cluster_line_surf.fill('green')

        for col in range(cluster_cols + 1):
            x = col * CLUSTER_SIZE
            pygame.draw.line(
                self.cluster_line_surf,
                LINE_COLOR,
                (x, 0),
                (x, WINDOW_WIDTH),
                CLUSTER_WIDTH)

        for row in range(cluster_rows + 1):
            y = row * CLUSTER_SIZE
            pygame.draw.line(
                self.cluster_line_surf,
                LINE_COLOR,
                (0, y),
                (WINDOW_HEIGHT, y),
                CLUSTER_WIDTH)

        self.display_surface.blit(self.support_line_surf, (0, 0))
        self.display_surface.blit(self.cluster_line_surf, (0, 0))

    def get_current_cell(self):
        col = mouse_pos()[0] // TILE_SIZE
        row = mouse_pos()[1] // TILE_SIZE

        return col, row

    def place_obj(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_buttons()[0]:
                x = self.get_current_cell()
                print(x)

    def run(self):
        while True:
            self.event_loop()

            # Draw.
            self.display_surface.fill('white')
            self.draw_tile()

            # dt = self.clock.tick() / 1000
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
