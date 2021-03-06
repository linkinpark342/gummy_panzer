
PATTERN_STRAIGHT = [(-1,0)]
PATTERN_WAVE_MID_DOWN = [(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0),(-4,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5),(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0),(-4,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4)]
PATTERN_WAVE_MID_UP = [(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0),(-4,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0),(-4,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5)]
PATTERN_WAVE_TOP = [(-4,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0),(-2,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5),(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0)]
PATTERN_WAVE_BOTTOM = [(-4,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5),(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0),(-4,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0)]
PATTERN_DIAG_DOWN = [(-2,1)]
PATTERN_DIAG_UP = [(-2,-1)]
PATTERN_CIRCLE_BOTTOM = [(-4,0),(-4,-2),(-3,-2),(-3,-3),(-2,-3),(-2,-4),(0,-4),(2,-4),(2,-3),(3,-3),(3,-2),(4,-2),(4,0),(4,2),(3,2),(3,3),(2,3),(2,4),(0,4),(-2,4),(-2,3),(-3,3),(-3,2),(-4,2)]
PATTERN_CIRCLE_TOP = [(-3,0),(-3,1),(-2,1),(-2,2),(-1,2),(-1,3),(0,3),(1,3),(1,2),(2,2),(2,1),(3,1),(3,0),(3,-1),(2,-1),(2,-2),(1,-2),(1,-3),(0,-3),(-1,-3),(-1,-2),(-2,-2),(-2,-1),(-3,-1)]

SPRITE_ONE = 'fred.png'
SPRITE_TWO = 'gertrude01.png'
SPRITE_THREE = 'bernard.png'

SPRITE_ONE_HEALTH = 2
SPRITE_TWO_HEALTH = 1
SPRITE_THREE_HEALTH = 6

STATE_MOVING = 0
STATE_SHOOTING = 1
STATE_DYING = 2

STATE_MOVING_FRAMES = [1]
STATE_SHOOTING_FRAMES = [1]
STATE_DYING_FRAMES = [1]
ANIMATION_FRAMES = (STATE_MOVING_FRAMES, STATE_SHOOTING_FRAMES,
                                                    STATE_DYING_FRAMES)

STATE_W = [101,138,150]
STATE_H = [116,78,53]
