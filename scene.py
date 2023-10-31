from settings import *
from world import World
from model import *
from world_objects.voxel_marker import VoxelMarker

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.cube = Cube(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)

    def update(self):
        self.world.update()
        self.voxel_marker.update()


    def render(self):
        self.world.render()
        self.cube.render()
        self.voxel_marker.render()