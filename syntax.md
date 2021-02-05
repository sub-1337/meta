# Meta Languge
## Introduction
In meta languge you are not boud to a specific realizations that may occur in your path.
Meta language is a template language, it does not tell you how you should write code, and you has no real bounds in a way of writing portable and clear code.
You potentially could express with your code exactly what you wanted to express, just pure logic.

Realization of endline execution is no matter either, you can for example write different parts of your project with different programmers and different code styles, and then use these different modules that may vary much in their design: one part will be platform specific and C code extended, other be written purely on meta language and create just an interface, and third will be most slow but feature rich that be responsible for buisness logic. So you get most perfomance on bottlenecks and write simpler code on the top level of your project logic.

Code translation is everything: you could write some library once and use it in different applications and platforms. You may still want to enchance optimization, but you do not need to complitely rewrite all of the code, only parts of it.

One of the main ideologies is a late bounding.

Hello world:
```
use console;
main()
{
    print("hello world!");
}
```
## Test

Изменения переменных функциями

Изменения копированием: множество a -> преобразуется в множество a', множество а забываем, множество a мы принимаем за a'


Определим виртуальную машину на коротких инструкциях:
```
x = константа // присвоить а константе
x = func(y) // присвоить x функцию от y
delete x // забыть x
```

У нас получилось 3 операции для чистых функций:
- 1) выделить память, присвоить константу
- 2) выделить память, присвоить значение функции
- 3) освободить память

Тогда код

```
a = 1
a = func(a)
```

Станет

```
a = значение 
// существует а == значению
a' = func(a)
// существует а == значению, и a' == func(a)
delete a
// существует значение a' == func(a)
a = a'
// существует значение а == func(a0) и a' == func(a0)
delete a'
// существует значение а == func(a0)
```

## Operators

**Operational space:**

There is local operational space that part of global operational space, local operational space is divided by left operational space and right operational space.

```
global space
|(local space)   left space  =  rigt space   |
```

Some operations may create subspace, then current  local space will be global for them.


**Syntax:**

`//` - commentary untill end of the line

`/* */` - multiline commentary

`(...)` - subspace creation then execute with it's content



Examples:
```
func(); // execute function
```

**Multyrhreaded instructions**

All instructions splitted by `;` considered **ordered**
All instructions splitted by `,` considered **unordered**

Example 

Ordered code
```
int a = 0;
int b = 10;
a = a + 1;
a = a + b;
println(a); // 11
```

Unordered code
```
new arr[8] = {0,1,2,3,4,5,6,7};
new n = 2;
for i [0;arr.size] @step = 4
{
    arr[i] = arr[i] * n,
    arr[i + 1] = arr[i] * n,
    arr[i + 2] = arr[i] * n,
    arr[i + 3] = arr[i] * n;
}
println(str(arr)); // will print `0 2 4 6 10 12 14`
```

This will result to multyple permutation instructions genereted and SSE optimization on compilation.

**Binary:**

`=` - set equality. Set left operation space equal to rigth operation space, and then reurn left operaton space into global space

Examples:
```
int b = int a = func(5);
```




## Types
## Functions
### Basics
Functions in meta language is much the same as in C and C++.
By default you get _something_ that may be _called_ and do somechanges to a variables.
Basic function look:
```
func(number a)
{
    return a + 5;
}
```
That function just returns the same value plus 5.
### Return types
You can not relay on static analysis and specify implicitly return type.
```
number : sum(number num1, number num2)
{
    return num1 + num2;
}
```
### Multiple return
You can return multiple variables as tuple and as named tuple.
```
number, number : retValue(number num1, number num2)
{
    return [num1,num2];
}

main()
{
    number num1, num2 = retValue(1,5);
    print(num1,"\n"); // 1
    print(num2,"\n"); // 5
}
```
Named tuple
```
number num1, number num2 : retValue(number numArg1, number numArg2)
{
    return [num1 : numArg1,num2 : numArg2];
}

main()
{
    number number1 : num1, number number2 : num2 = retValue(1,5);
    print(number1,"\n"); // 1
    print(number2,"\n"); // 5
} 
```
## Data types
### Iterators
You can easily mark some iterable data with iterators.
There is a single access iterator `[N]` (regular) and `[N!]` (poked, like an point in math, it does not refers to any specific point but may be used to set ranges) and _range_ iterator such as:
```
[0:N]  // 0, 1, 2, ... , N
[0:N!] // 0, 1, 2, ... , N - 1
[K!:N] // K + 1, K + 2, ... , N
```
After simplifying operation, all these lines will be equal to the first line `[0:N]`
```
[[0]:[N]]
[[0:N]]
[[0:K!] + [K:N]]
```

`[]` Empty statement, does not refers to any single iterator

`[NaN]` Empty iterator, do not point just consuming space. If you iterate this iterator you get 1 cycle spin.

TODO: Empty iterators, think about it

First includes entire range, seconds and third discludes right and left numbers appropriately.

There is also operations on iterators, such a:

- Splitting 
- Including
- Excluding
- Reversing/setting orientation
- Checking if a single access iterator is in range
- Simplifying
- Type casts into numbers/between iterators

**Splitting**

```
let iteratorBasic = [0:N]
let iteratorNew1, iteratorNew2 = iterator.split([K!]) // Split at K 
```
This is basically the same as `[0:K!]` and `[K:N]`

```
let iteratorBasic = [0:N]
let iteratorNew1, iteratorNew2 = iterator.split([K]) // Split at K
```
This is basically the same as `[0:K]` and `[K!:N]`

```
let iteratorBasic = [0:128!]
let array iterators @= iterator.splitOctet(4)
```
This will split iterator to `[0:8!], [8;16!], ... [120;128]`

**Including**

```
let includedIterator1 = [0:N!] + [N + K] // Same as [0:K]
let includedIterator2 = [0:5] + [3:10] + [12:15] // Same as [[0:10] + [12:15]]
```

**Excluding**

```
let iteratorBasic = [0:N]
let iteratorWithoutPoint = iteratorBasic.exclude([K]) // Excludes K point from the range
let iteratorWithoutRange = iteratorBasic.exclude([5:10]) // Same as [[0:5!]:[10!:N]]
```

**Reversing/setting orientation**

This topic comes with loop realization, which seems the most important thing in all this mess.

First of all, there is

```
for i in [0;10] * 10
{
    print(i);
}
```

Will print out 0, 10, 20, ... , 100 (with a default orientation from 0 to 10).

```
for i in [10;0]
{
    print(i);
}
```
```
for i in [0;10].reverse()
{
    print(i);
}
```

Example with poked element.

```
for i in [10!;0]
{
    print(i);
}
```

Print 9, 8, 7, ... , 0


**Limitations**

TODO: think about this

You can not use several times included parts of iterators, so be carefull. If you need some ranges of numbers included several times see _Unions_.
## Integrated tests

There is integrated test suit, static and runtime checks.

```

```