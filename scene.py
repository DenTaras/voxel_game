from settings import *
from world import World
# from meshes.quad_mesh import QuadMesh
from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.cube = Cube(self.app)

    def update(self):
        self.world.update()


    def render(self):
        self.world.render()
        self.cube.render()