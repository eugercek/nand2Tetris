(LOOP)
    @i
    M=0

    @SCREEN
    D=A
    @now
    M=D
    M=M-1

	@KBD
    D=M
	    @WHITE
        D;JEQ
    
	    @BLACK
        0;JMP

(WHITE)
    @now
    M=M+1
    A=M
    M=0
    @8192
    D=A

    @i
    M=M+1
    D=D-M//8192-i
    @WHITE
    D;JGT

    @LOOP
    0;JMP

(BLACK)
    @now
    M=M+1
    A=M
    M=-1
    @8192
    D=A

    @i
    M=M+1
    D=D-M//8192-i
    @BLACK
    D;JGT

    @LOOP
    0;JMP

