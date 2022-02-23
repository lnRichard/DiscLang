# ------------------------------------------------------------
# lex.py
#
# tokenizer for the language
# ------------------------------------------------------------
import ply
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'EXP',
   'UNEXP',
   'PTR',
   'DEFBY',
   'SEP',
   'EXPRREF',
   'VAR',
)

# Regular expression rules for simple tokens
t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_TIMES    = r'\*'
t_DIVIDE   = r'\/'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_EXP      = r'\$'
t_UNEXP    = r'\@'
t_PTR      = r'\&'
t_DEFBY    = r'\:\='
t_SEP      = r'\:'
t_EXPRREF  = r'\;'
t_VAR      = r'[a-zA-Z_]'

# A regular expression rule with some action code
def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

# Define a rule so we can track line numbers
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
   # Test it out
   data = '''
   x := 2
   g := $;x + 1$
   '''

   # Give the lexer some input
   lexer.input(data)

   # Tokenize
   for tok in lexer:
      print(str(tok.lineno) + "} " + str(tok.type) + " (VAL " + str(tok.value) + ") (POS " + str(tok.lexpos) + ")")
