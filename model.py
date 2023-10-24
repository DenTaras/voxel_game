import numpy as np
import glm


class Cube:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.program = self.app.shader_program.triangle
        self.vao = self.get_vao()

    def update(self):
        pass


    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices) * 10
        return vertex_data

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')


    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def get_vao(self):
        vao = self.ctx.vertex_array(self.program, [(self.vbo, '3f', 'in_position')])
        return vao