from JackTokenizer import JackTokenizer

tokenizer = JackTokenizer('foo')
while tokenizer.hasMoreTokens():
    tokenizer.advance()
