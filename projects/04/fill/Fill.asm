(LOOP)
    @i//@16
    M=0

    @SCREEN
    D=A
    @now//@17
    M=D
    M=M-1

	@KBD
    D=M
	
	@BLACK
	D;JNE
	
	//color=white
    @color//@18
	M=0
	@AFTERIF
	0;JMP
	
	(BLACK)
		@color//@18
		M=-1
	
(AFTERIF)
    @color//@18
	D=M
	@now//@17
    M=M+1
    A=M
	M=D
    @8192
    D=A
    @i//@16
    M=M+1
    D=D-M//8192-i
    @AFTERIF
    D;JGT

    @LOOP
    0;JMP
