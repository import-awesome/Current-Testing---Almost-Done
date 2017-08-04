import pygame
Q = "Q"
F = "."
D = "D"
E = "E"
B = "B"
W = "W"
WD = "W"
WL = "W"
WR = "W"
WU = "W"
WD = "W"
WRL = "W"
WRU = "W"
WUR = "W"
WRD = "W"
WLU = "W"
WLD = "W"
WLRU = "W"
WLRD = "W"
WLRUD = "W"
WUDL = "W"
WUDR = "W"
WUD = "W"
SU = "SU"
SD = "SD"
V = "V"



s1_f1 = [
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],			
[Q, Q, Q, Q, Q, Q, W, W, W, W, W, Q, W, W, W, Q, W, W, W, Q, W, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, F, F, F, W, F, F, F, D, F, F, F, D, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, F, W, F, W, F, W, F, W, W, F, F, W, F, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, D, W, W, Q, D, W, F, W, F, F, W, F, F, W, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q], 
[Q, Q, Q, Q, Q, W, F, W, F, W, F, F, F, W, F, W, Q, W, F, W, W, W, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, D, F, W, F, W, W, W, F, F, D, F, F, D, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, W, F, F, F, W, F, W, F, W, Q, W, W, W, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, W, W, W, W, W, F, W, F, F, W, F, F, W, W, W, E, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, F, F, W, W, F, W, W, W, W, F, F, W, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, W, W, W, F, D, F, F, D, F, F, F, F, F, W, W, W, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, F, F, W, F, W, W, W, W, W, W, SD, W, F, W, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, W, W, F, W, F, W, F, F, F, W, W, W, W, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, F, F, W, F, W, F, F, F, F, F, W, F, F, W, W, E, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, W, W, W, W, F, W, W, E, W, W, F, W, F, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, D, F, W, F, W, F, F, F, W, F, W, F, F, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, W, W, W, F, W, F, W, W, F, W, W, F, W, W, W, W, W, E, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, D, F, W, F, F, W, F, W, F, F, F, F, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, W, F, W, F, F, W, F, W, F, W, W, F, W, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, W, F, F, W, F, F, F, F, W, B, W, F, F, F, F, D, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, W, W, Q, W, W, W, W, Q, W, Q, W, W, W, W, Q, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q]

]

#dungeon 1, floor 2
s1_f2 = [

[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, SU, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, W, W, D, W, W, W, W, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, F, F, F, F, F, W, F, F, F, F, F, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, W, F, F, F, D, F, F, F, F, F, F, W, W, W, W, W, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, D, W, W, W, W, W, W, W, W, W, F, W, F, W, F, F, F, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, F, F, F, W, F, F, F, F, F, W, F, W, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, Q, F, F, F, F, W, F, F, W, F, W, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, F, Q, F, W, W, W, W, W, F, W, F, F, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, F, Q, F, W, F, F, F, W, W, W, W, W, D, W, W, D, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, F, F, F, W, F, F, F, F, F, F, F, W, F, F, F, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, D, W, W, W, F, W, F, W, W, F, W, W, F, W, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, D, W, F, F, W, F, W, F, F, W, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, Q, Q, Q, F, F, F, F, W, F, W, F, F, F, F, F, F, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, W, F, W, F, W, F, F, W, F, W, W, W, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, W, W, F, W, F, F, W, F, W, D, W, W, F, Q, Q, SD ,W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, W, F, D, F, F, W, F, F, F, F, W, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, W, W, W, W, W, W, W, F, F, F, W, F, Q, Q, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, W, W, F, F, F, F, F, W, W, W, F, W, F, F, F, F, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, W, F, F, F, F, F, W, F, F, F, W, W, W, W, W, W, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, D, F, F, F, F, F, D, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, W, W, W, D, W, W, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, W, W, Q, W, F, W, Q, W, W, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q] ]

s1_f3 = [
[Q, Q, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, Q, Q],
[Q, Q, W, F, W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W, F, W, Q, Q],
[Q, W, W, F, W, F, W, F, W, F, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, F, W, F, W, F, W, F, W, Q, Q],
[W, F, W, F, F, F, W, F, W, F, W, F, F, F, F, F, F, F, F, F, F, F, F, F, W, F, W, F, W, F, F, F, W, F, W],
[W, F, F, F, W, F, W, F, W, F, W, F, F, F, W, W, W, W, W, W, W, F, F, F, W, F, W, F, W, F, W, F, F, F, W],
[W, W, F, W, W, W, W, F, W, F, W, F, F, F, W, F, F, F, F, F, W, F, F, F, W, F, W, F, W, W, W, W, W, W, W],
[W, F, F, F, F, F, W, F, W, F, W, F, F, F, W, F, W, SD, W, F, W, F, F, F, W, F, W, F, W, F, F, F, F, F, W],
[W, F, F, W, F, W, W, F, W, F, W, F, F, F, W, F, W, F, W, F, W, F, F, F, W, F, W, F, W, W, F, W, F, F, W],
[W, F, F, W, F, F, W, F, W, F, W, F, F, F, W, F, F, F, F, F, W, F, F, F, W, F, W, F, W, F, F, W, F, F, W],
[W, F, F, W, F, F, W, F, W, F, W, F, F, F, F, F, F, F, F, F, F, F, F, F, W, F, W, F, W, F, F, W, F, F, W],
[W, F, F, W, F, F, W, F, W, W, W, W, W, W, W, W, W, D, W, W, W, W, W, W, W, W, W, F, W, F, F, W, F, F, W],
[W, F, F, W, F, F, W, F, F, F, F, F, F, F, W, F, F, F, F, F, W, F, F, F, F, F, F, F, W, F, F, W, F, F, W],
[W, F, W, W, W, W, W, W, W, W, W, W, F, W, W, F, F, F, F, F, W, W, F, W, W, W, W, W, W, F, F, W, W, F, W],
[W, F, W, F, F, F, W, F, F, F, F, F, F, F, W, F, F, F, F, F, W, F, F, F, F, F, F, F, F, F, F, F, W, F, W],
[W, F, W, W, W, W, W, W, W, W, W, W, W, W, W, F, F, F, F, F, W, W, W, W, W, W, W, W, W, W, W, W, W, F, W],
[W, F, W, W, F, F, F, F, F, F, F, F, F, F, W, F, F, F, F, F, W, F, F, F, F, F, F, F, F, F, F, W, W, F, W],
[W, F, W, W, F, W, W, W, W, W, W, W, W, F, W, F, F, F, F, F, W, F, W, W, W, W, W, W, W, W, F, W, W, F, W],
[W, F, F, F, F, W, F, F, F, F, F, F, F, F, W, F, F, F, F, F, W, F, F, F, F, F, F, F, F, W, F, F, F, F, W],
[W, W, W, W, W, W, W, W, F, W, W, W, W, W, W, F, F, F, F, F, W, W, W, W, W, W, F, W, W, W, W, W, W, W, W],
[W, F, F, F, F, F, F, F, F, F, W, F, F, F, W, F, F, F, F, F, W, F, F, F, W, F, F, F, F, F, F, F, F, F, W],
[W, W, F, W, W, W, W, W, W, W, W, F, W, F, W, F, F, F, F, F, W, F, W, F, W, W, W, W, W, W, W, W, F, W, W],
[W, F, F, F, F, F, F, F, W, F, W, F, W, F, W, F, F, F, F, F, W, F, W, F, W, F, W, F, F, F, F, F, F, F, W],
[W, W, W, W, W, W, W, F, W, F, W, F, W, F, W, F, F, F, F, F, W, F, W, F, W, F, W, F, W, W, W, W, W, W, W],
[W, F, F, F, F, F, W, F, W, F, F, F, W, F, W, F, F, F, F, F, W, F, W, F, F, F, W, F, W, F, F, F, F, F, W],
[W, W, W, W, W, F, W, F, W, F, W, F, W, F, W, F, F, F, F, F, W, F, W, F, W, F, W, F, W, F, W, W, W, W, W],
[W, F, F, F, W, F, W, F, W, F, W, F, W, F, W, F, F, F, F, F, W, F, W, F, W, F, W, F, W, F, W, F, F, F, W],
[W, F, W, F, W, F, F, F, W, F, W, F, W, F, W, F, F, F, F, F, W, F, W, F, W, F, W, F, F, F, W, F, W, SU, W],
[W, W, W, F, F, F, W, W, W, F, W, W, W, F, W, F, F, F, F, F, W, F, W, W, W, F, W, W, W, F, F, F, W, W, W],
[Q, Q, W, F, W, F, F, F, F, F, W, F, F, F, F, F, F, F, F, F, W, F, F, F, W, F, F, F, F, F, W, F, W, Q, Q],
[Q, Q, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, Q, Q]]

#dungeon 1, floor 4
boss = [
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, W, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, V, V, V, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, V, V, V, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, V, V, V, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, F, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, D, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, F, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, B,W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q] ]

allmaps = [
[
	[s1_f1, 0], [s1_f2, 0], [s1_f3, 0], [boss, 0]
],
	
	[
		[boss, 0]
	]
]