# Interview Questions

This document has some interview questions from "The Algorithm Design Manual" as well as answer code. Please note the code is not perfect nor the best solution for each question. The following code was written by me during my studies.

## 1-28
Write a function to perform integer division without using either the / or * operators. Find a fast way to do it.

### Answer

```py
def div(n,d):
    c = 0
    while d > 0:
        d -= n
        c += 1
    return c
```

## 1-29
There are 25 horses. At most, 5 horses can race together at a time. You must determine the fastest, second fastest, and third fastest horses. Find the minimum number of races in which this can be done

### Answer
Six. Five races will test every horse. The last race will be between the fastest of the previous five races.

## 1-30

How many piano tuners are there in the entire world?

### Answer



## 1-31
How many gas stations are there in the United States?

### Answer

Roughly 110,000.

## 1-32

How much does the ice in a hockey rink weigh?

### Answer

Around 57 pounds per cubic foot.

## 1-33

How many miles of road are there in the United States?

### Answer

z