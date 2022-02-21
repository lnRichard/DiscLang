# DiscLang

Sources: <https://www.maths.usyd.edu.au/u/UG/JM/MATH1901/r/PDF/cheat-sheet.pdf>

Tokens: ```+, -, *, /, ^, %, =, :=, =>, <=>, {}, [], (), $, @, !, \, :, ->, ;```

## Normal Operations

```js
x = 2
y = 4
$x + y$ // 6
```

## Discrete Operations

```js
P = true
Q = false
$Q => P$ // True
$P => Q$ // False
```

## Expression Building

```js
a = @x + x^2@ // Valid
b = @x^3@ // Valid

// Allow construction
c = $;a + ;b = 3$ // c = 1
```

## Contextual Spaces

```js
// Create a space
space:open
   P = if a student their score becomes greater than 90
      then the student has passed // Rule

   s = a student with a score greater than 95 // Definition
   $s has passed$ // True
space:close
```

## Functions

```js
f(x) = @x@
g(x) = @x + 1@
$f(1) + g(1)$ // 3
h(x) = f(x) + g(x) // @x + (x + 1)@
$h(1)$ // 3
```
