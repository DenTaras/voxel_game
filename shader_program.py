from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        # --------- shaders ------------ #
        self.chunk = self.get_program(shader_name='chunk')
        self.quad = self.get_program(shader_name='quad')
        self.triangle = self.get_program(shader_name='triangle')
        # ------------------------------ #
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        self.chunk['m_proj'].write(self.player.m_proj)
        self.chunk['m_model'].write(glm.mat4())
        self.chunk['u_texture_0'] = 0

        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

        self.triangle['m_proj'].write(self.player.m_proj)
        self.triangle['m_model'].write(glm.mat4())

    def update(self):
        self.chunk['m_view'].write(self.player.m_view)
        self.quad['m_view'].write(self.player.m_view)
        self.triangle['m_view'].write(self.player.m_view)

        m_model = glm.rotate(glm.mat4(), self.app.time, glm.vec3(0, 1, 0))
        self.triangle['m_model'].write(m_model)

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

