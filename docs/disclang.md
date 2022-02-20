# DiscLang

Sources: <https://www.maths.usyd.edu.au/u/UG/JM/MATH1901/r/PDF/cheat-sheet.pdf>
Operators: +, -, *, /, ^, %, =, :=, =>, <=>, {}, [], (), $ (Completed expression), @ (Partial expression), !, \, :, ->, ; (Variable reference in $$ or @@)

```py
a = @x + x^2@ // Valid
b = @x^3@ // Valid

// Allow construction
c = $;a + ;b = 3$ // c = 1
```
