JMP $14
DB  7,4
DS  8
DB  25

LDA $3
MOV B, A
LDA $4
STA $3
MOV A, B
STA $4
LDA $3
MOV B, A
LDA  $4
STA $3
MOV A, B
STA  $4
HLT