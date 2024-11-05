from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time
import game_framework
import title_mode
import play_mode
from pico2d import*
from pannel import Pannel
import game_world

def init():
    global pannel
    pannel= Pannel()
    game_world.add_object(pannel)


def finish():
    game_world.remove_object(pannel)
def update():
    pass
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_0):
            play_mode.boy.set_item('None')
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_1):
            print('Smallball')
            play_mode.boy.set_item('SmallBall')  
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_2):
            play_mode.boy.set_item('BigBall')   

            
def pause():
    pass
def resume():
    pass