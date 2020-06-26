// şMultiplies R0 and R1 and stores the result in R2.



@R0
D=M
@num0
M=D

@R1
D=M
@num1
M=D
D=M
@num0
D=M-D//if num0>num1 => D>0
@CONT
D;JLE

    D;JLE
    D=M
    @temp
    M=D
    @num1
    D=M
    @num0
    M=D
    @temp
    D=M
    @num1
    M=D


(CONT)
@sum
M=0
(LOOP)
@num0
D=M
@ENDISH
D;JEQ
@num1
D=M
@sum
M=D+M
@num0
M=M-1
@LOOP
0;JMP

(ENDISH)
@sum
D=M
@R2
M=D
(END)
@END
0;JMP

