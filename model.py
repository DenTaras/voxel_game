import numpy as np


class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.program = app.shader_program.default
        self.vao = self.get_vao()


    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()

    def get_vao(self):
        vao = self.ctx.vertex_array(self.program, [self.vbo, '3f', 'in_position'])

    def get_vertex_data(self):
        vertex_data = [(-0.6, -0.8, 0.0),
                       (0.6, -0.8, 0.0),
                       (00.0, 0.8, 0.0)]
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
