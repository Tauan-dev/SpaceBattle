import pygame
from math import sin, cos, radians

class Bullet:

    def __init__(self, screen_width: int, screen_height: int, x: int, y: int, angle: float, is_white: bool):
        # Propriedades da Bala
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.angle = angle
        self.speed = 6
        self.is_white = is_white
        self.radius = 3
        self.time_alive = 0

    def keep_in_map(self) -> None:
        # Mantendo a bala dentro dos limites da tela
        if self.x >= self.screen_width:
            self.x = -self.radius
        elif self.x + self.radius <= 0:
            self.x = self.screen_width

        if self.y >= self.screen_height:
            self.y = -self.radius
        elif self.y + self.radius <= 0:
            self.y = self.screen_height

    def update(self) -> None:
        # Atualizando posição da bala
        self.x += -self.speed * sin(radians(self.angle))
        self.y += -self.speed * cos(radians(self.angle))
        self.keep_in_map()
        # Atualizando o tempo da bala "viva"
        self.time_alive += 1

    def draw(self, screen: pygame.Surface) -> None:
        # Desenhando o marcador na tela
        if self.is_white:
            pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
        else:
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)

    def to_dict(self):
        # Convertendo os parâmetros do marcador em um dicionário
        return vars(self)

    def data_from_dict(self, description_dict: dict) -> None:
        # Definindo os parâmetros de um marcador a partir de um dicionário
        self.x = description_dict['x']
        self.y = description_dict['y']
        self.angle = description_dict['angle']
        self.speed = description_dict['speed']
        self.is_white = description_dict['is_white']
        self.radius = description_dict['radius']
        self.time_alive = description_dict['time_alive']
