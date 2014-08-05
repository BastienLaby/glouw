#version 150

in vec3 a_position;
in vec3 a_normal;
in vec2 a_uv;

uniform mat4 u_projection = mat4(1.0);;
uniform mat4 u_view = mat4(1.0);;
uniform mat4 u_model = mat4(1.0);

void main(void)
{
    gl_Position = u_projection * u_view * u_model * vec4(a_position, 1.0);
}