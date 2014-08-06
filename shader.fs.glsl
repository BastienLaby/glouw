#version 150

in vec3 frag_normal;
in vec3 frag_position;
in vec2 frag_uv;

out vec4 Color;

void main(void)
{
    Color = vec4(frag_normal, 1.0);
}