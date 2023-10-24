from settings import *
from world import World
from meshes.quad_mesh import QuadMesh



class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.quad = QuadMesh(self.app)

    def update(self):
        self.world.update()


    def render(self):
        self.world.render()
        self.quad.render()