# DiscLang

Sources: <https://www.maths.usyd.edu.au/u/UG/JM/MATH1901/r/PDF/cheat-sheet.pdf>

Tokens: ```+, -, *, /, ^, %, =, :=, =>, <=>, {}, [], (), $, @, !, \, :, ->, ;```

## Normal Operations

```js
x := 2
y := 4
$x + y$ // 6
```

## Discrete Operations

```js
P := true
Q := false
$Q => P$ // True
$P => Q$ // False
```

## Expression Building

```js
a := @x + x^2@ // Valid
b := @x^3@ // Valid

// Allow construction
c := $;a + ;b = 3$ // c = 1
```

## Contextual Spaces

```js
// Create a space
space:open
   P := if a student their score becomes greater than 90
      then the student has passed // Rule

   s := a student with a score greater than 95 // Definition
   $s has passed$ // True
space:close
```

## Mathematical Functions

```js
f(x) := @x@
g(x) := @x + 1@
$f(1) + g(1)$ // 3
h(x) := f(x) + g(x) // @x + (x + 1)@
$h(1)$ // 3
```

## Logical Functions

```js
F(x):open
   // x is now a global in this space
   y := $;x + 1$
   z := 1
F(y, z):close

a, b := $F(1)$ // 2, 1
```

## Early Stopping

```js
F(x):open
   x := $x + 1$
   if x < 10 then F:close // Early stop
   x := $x + 1$
F(x):close
```

## Async Spaces

```js
#define "print" from "std::print"

F(x):open
   x := x + 1
F(x):close

G(x):async
   await x := F(2) + x // Await resolve
G(x):close

// Chain Existing Function
H(x):open
   print("Resolved")
H(x):close

x := G(1):H

// One-Time Function
x := G(1):H(x):open
   print("Resolved")
H(x):close
```

## Advanced Chaining

```js
F(x):async
   x := x + 1
F(x):close

G(x):open
   x := x + 1
G(x):close

H(x, y):open
   x := x + y
H(x):close

x := F(1):(...G, 1):H
```

## Looping Functionality

```js
x := 1

<<START
$;x + 1$
x := x + 1
if x < 10 then >>START
```

## Looping Library

### Iterative Loop

```js
#define "iloop" from "std::loop"

F(x /*Incrementer*/, y):open
   y := $x + 1$
F(y):close

// iloop(execute, min, max, step, arguments)
// x: incrementer, rf: return values of F
y := iloop(f(x, rf) := @F(x, ...rf)@, 1, 3, 1, (1))
// 0 + 2 + 4 + 6 = 12
```

### Conditional Loop

```js
#define "cloop" from "std::loop"

F(y):open
   y := $y + 1$
F(y):close

G(y):open
   if y < 6 then c := $true$ and G:close
   c := $false$
G(c):close

// cloop(execute, condition, arguments)
// rf: return values of F
y := cloop(f(rf) := @F(...rf)@, g(rf) := @G(...rf)@, (1))
// 1 + 3 + 5 + 7
```

## Printing Rules

```js
x := 2
f(x) := @;x = x@ // Comparison ;x and x
$f(3)$ // Does not print, as 'x' is caught by ';x ='
$;x$ // Does print (3), 'x;' is caught by nothing

#define "print" from "std::print"
print($x + 1 = 2$) // Print the outcome
print(f) // Print a function
```

## Documenting Code

```js
"""
:open
  x {0...\INF}: Value that will get 1 added to it
:close
  x {0...\INF}: Value that has gotten 1 added to it
"""
F(x):open
   x := $x + 1$
F(x):close
```

## Using Pointers

```js
x := 4
y := &x
y := 2
$x$ // 2
```
