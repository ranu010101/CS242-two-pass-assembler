; program to swap data between two memory locations
jmp start
MACRO jsup mem, m
swp mem, m
MEND
var db 7,4
EXTERN rishi
start: 
swp rishi[0],var[1]
jsup var[0], var[1]
hlt
