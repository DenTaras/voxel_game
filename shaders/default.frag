#version 330 core

layout (location = 0) out vec4 fragColor;

void main() {
    vec3 color = vec3(1, 0, 0);
    fragColor(color, 1.0);
}
