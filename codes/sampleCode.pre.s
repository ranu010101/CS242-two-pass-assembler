JMP START
VAR: DB 7,4
VAR1: DS 8
GLOBAL RISHI: DB 25
START:
LDA VAR+0
MOV B, A
LDA VAR+1
STA VAR+0
MOV A, B
STA VAR+1
LDA VAR+0
MOV B, A
LDA  VAR+1
STA VAR+0
MOV A, B
STA  VAR+1
HLT