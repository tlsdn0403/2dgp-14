import game_framework
from pico2d import*
#타이틀 모드를 import 하되, 이름을 바꿔친다
import play_mode as start_mode



# game loop13
open_canvas() 
game_framework.run(start_mode)
close_canvas()
 