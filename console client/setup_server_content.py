from server_system_setup import server_system
import os


def setup_server_content():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    sprites_dir = os.path.join(root_dir, 'Sprites')
    if not os.path.exists(sprites_dir):
        server_system.download_server_texture()
    