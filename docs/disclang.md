# DiscLang

Sources: <https://www.maths.usyd.edu.au/u/UG/JM/MATH1901/r/PDF/cheat-sheet.pdf>
Operators: ```+, -, *, /, ^, %, =, :=, =>, <=>, {}, [], (), $, @, !, \, :, ->, ;```

## Normal Operations

```coffee
x = 2
y = 4
print x + y // 6
```

## Discrete Operations

```coffee
P = true
Q = false
print Q => P // True
print P => Q // False
```

## Expression Building

```coffee
a = @x + x^2@ // Valid
b = @x^3@ // Valid

// Allow construction
c = $;a + ;b = 3$ // c = 1
```

## Contextual Spaces

```coffee
// Create a space
space:open
   P = if a student their score becomes greater than 90
      then the student has passed

   s = a student with a score of >95
   print $s has passed$ // True
space:close
```
