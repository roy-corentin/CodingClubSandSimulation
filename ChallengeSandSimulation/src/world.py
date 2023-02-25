from typing import List, Tuple
from src.cellule import Cellule, Earth, Empty, Sand
import pygame


class World:
    def __init__(self, width: int = 800, height: int = 800) -> None:
        """WINDOWS/SURFACE"""
        self.size_win: Tuple[int, int] = (width, height)
        self.window: pygame.surface.Surface = pygame.display.set_mode(
            self.size_win, pygame.RESIZABLE, pygame.DOUBLEBUF
        )
        self.size_cell: int = 5
        self.width: int = width // self.size_cell
        self.height: int = height // self.size_cell
        """COLOR"""
        self.black: Tuple[int, int, int] = (0, 0, 0)
        self.white: Tuple[int, int, int] = (250, 250, 250)
        """CELLULE"""
        self.cellules: List[List[Cellule]] = [
            [Empty() for _ in range(self.width)] for _ in range(self.height - 1)
        ]
        self.cellules.append([Earth() for _ in range(self.width)])

    def draw(self) -> None:
        self.window.fill(self.black)
        for line, y in zip(self.cellules, range(self.height)):
            for cellule, x in zip(line, range(self.width)):
                if isinstance(cellule, Empty):
                    continue
                cellule.updated = False
                self.__draw_cell(cellule, x, y)
        pygame.display.flip()

    def handle_input(self) -> int:
        pos: Tuple[int, int] = pygame.mouse.get_pos()
        x: int = pos[0] // self.size_cell
        y: int = pos[1] // self.size_cell
        mouse_key = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 84

        """ Gérer clique souris pour créer ou supprimer des élements """
        ## si clique gauche
        ## Créer block de Sable
        ## si clique droit
        ## Créer block de Vide

        return 0

    def update(self) -> None:
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                current_cell: Cellule = self.cellules[y][x]
                if isinstance(current_cell, Sand):
                    self.__move_sand(x, y)

    def __move_sand(self, x: int, y: int) -> None:
        """Verifier si les cellules voisines sont disponibles"""
        ##
        ##
        ##
        ##
        ##
        self.cellules[y][x].updated = True

    def __draw_cell(self, cellule: Cellule, x: int, y: int) -> None:
        rect: pygame.Rect = pygame.Rect(
            x * self.size_cell,
            y * self.size_cell,
            self.size_cell,
            self.size_cell,
        )
        pygame.draw.rect(
            self.window,
            cellule.get_color(),
            rect,
        )

    def __create_block_of_sand(self, x: int, y: int) -> None:
        pos_list: List[Tuple[int, int]] = [
            (x, y),
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x + 1, y + 1),
            (x - 1, y + 1),
        ]
        for pos in pos_list:
            pos_x, pos_y = pos
            if self.__in_range(pos_x, pos_y):
                self.cellules[pos_y][pos_x] = Sand()

    def __create_block_of_empty(self, x: int, y: int) -> None:
        pos_list: List[Tuple[int, int]] = [
            (x, y),
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x + 1, y + 1),
            (x - 1, y + 1),
        ]
        for pos in pos_list:
            pos_x, pos_y = pos
            if self.__in_range(pos_x, pos_y):
                self.cellules[pos_y][pos_x] = Empty()

    def __switch_cell(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> None:
        temp: Cellule = self.cellules[pos1[1]][pos1[0]]
        self.cellules[pos1[1]][pos1[0]] = self.cellules[pos2[1]][pos2[0]]
        self.cellules[pos2[1]][pos2[0]] = temp
        self.cellules[pos1[1]][pos1[0]].updated = True
        self.cellules[pos2[1]][pos2[0]].updated = True

    def __is_empty_cell(self, x: int, y: int) -> bool:
        return self.__in_range(x, y) and isinstance(self.cellules[y][x], Empty)

    def __in_range(self, x: int, y: int) -> bool:
        if y >= self.height or y < 0:
            return False
        if x >= self.width or x < 0:
            return False
        return True
