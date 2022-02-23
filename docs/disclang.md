# DiscLang

Sources: <https://www.maths.usyd.edu.au/u/UG/JM/MATH1901/r/PDF/cheat-sheet.pdf>

Operational Order: Evaluations, Sets, then Mathematical order

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

## Conditional Logic

```js
// Logical 'If-Then'
if $1 = 1$ then $"Hello World!"$ // Hello World!
if ¬$1 = 2$ then $"Bye World!"$ // Bye World!

// Logical 'If-Then' Shorthand
$1 = 1$ |=> $"Welcome Back!"$ // Welcome Back!
```

## Contextual Spaces

```js
// Create a space
space:open
   P := $if a student their score becomes greater than 90
      then the student has passed$ // Rule

   s := $a student with a score greater than 95$ // Definition
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
F(y, z):close // Returns an ordered set by default

a, b := $F(1)$ // 2, 1
```

## Early Stopping

```js
F(x):open
   x := $;x + 1$
   if $;x < 10$ then F:close // Early stop
   x := $;x + 1$
F(x):close
```

## Async Spaces

```js
#define "print" from "std::print"

F(x):open
   x := $;x + 1$
F(x):close

G(x):async
   await x := $F(2) + ;x$ // Await resolve
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
   x := $;x + 1$
F(x):close

G(x):open
   x := $;x + 1$
G(x):close

H(x, y):open
   x := $;x + y$
H(x):close

x := F(1):(...G, 1):H
```

## Looping Library

### Iterative Loop

```js
#define "iloop" from "std::loop"

F(x /*Incrementer*/, y):open
   y := $;x + 1$
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
   y := $;y + 1$
F(y):close

G(y):open
   if $;y < 6$ then c := $true$ then G:close
   // $y < 6$ => c := $true$ => G:close
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
  x {n | n ∈ of \N}: Value that will get 1 added to it
:close
  x {nx | n ∈ \N}: Value that has gotten 1 added to it
"""
F(x):open
   x := $;x + 1$
F(x):close
```

## Complex Space

```js
#define "print" from "std::print"

print($x^2 + 1 = 0$) // {sqrt(-1), -sqrt(-1)}
space:open
   #define "def::complex"
   print($x^2 + 1 = 0$) // {i, -i}
space:close
```

## Undefined Operations

```js
#define "print" from "std::print"

// There are no runtime errors, only undefined
print($0 / 0$) // {\UNDEFINED}
print($0 / 0 + 1$) // {\UNDEFINED}
print($0 / 0 = \UNDEFINED$) // True
```

## Set manipulation

```js
#define "print" from "std::print"

x := {1, 2, 3, 4}
y := {1, 2}
z := &x

// ? Everything evaluates to true

// Subset
print($;y ⊆ ;x$)
print($;y <subset>of ;x$)

print($∅ = {}$)
print($∅ <value>is {}$) // Same as '='
print(${1, 2} <type>is {}$)
print($;x <addr>is ;z$)

// Infinity
print($1 ∈ ℕ$)
print($1 <elem>of \N$)
```

## Mathematical order

```js
// '$' are not actually needed
x := 1 + 2
x := $1 + 2$

// However they are standart, because of possible ambiguity
if true = 1 = 1 then "WHAT!" // Evaluates from left to right

// Could mean:
if $true = 1$ = 1 then "WHAT!"
if true = $1 = 1$ then "WHAT!" // WHAT!

// Which could also be represented by ordered set of length 1:
if (true = 1) = 1 then "WHAT!"
if true = (1 = 1) then "WHAT!" // WHAT!

// $$, Evaluate before ordered sets (), while ordered sets (), evaluate before what is outside
// Mathematical order goes from inside to outside, from left to right, following mathematical order
```

## Disclang Algorithms

### FizzBuzz

```js
F(n):open
   // FizzBuzz
   if $n % 3 = 0$ then fb :+ "Fiz"
   if $n % 5 = 0$ then fb :+ "Buz"
F(fb := ""):close

fb = [F(n) | n <elem>of {n | 11 > n > 0 & n <elem>of \N}]
```

## Fibonacci

```js
F(n):open
   // Compiler automatically detects similar negation, and uses the same result
   if $n <elem>of {1, 2}$ then fib := n
   if ¬$n <elem>of {1, 2}$ then fib := F(n - 1) + F(n - 2)
F(fib := n):close

fib = F(10)
```

## 99 Bottles of Beer

```js
#define "print" from "std::print"
F(n := 99):open
   print($n + " bottles of beer on a wall"$, 
         $n + " bottles of beer"$,
         "Take one down, pass it around",
         $n := n - 1$,
         n = " bottles of beer on a wall")
   if n > 0 then F(n)
F(n):close

// 99 bottles of beer on a wall
F(99)
```

## Even Numbers

```js
F(n):open
   // Voids all non-even numbers
   if ¬$n % 2 = 0$ then n := void // Void is nothing, go eat a pancake
F(n):close

e = [F(n) | n <elem>of {n | 11 > n > 0 & n <elem>of \N}]
```
