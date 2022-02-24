# Meta Languge
## Introduction
In meta languge you are not boud to a specific realizations that may occur in your path.
Meta language is a template language, it does not tell you how you should write code, and you has no real bounds in a way of writing portable and clear code.
You potentially could express with your code exactly what you wanted to express, just pure logic.

Realization of endline execution is no matter either, you can for example write different parts of your project with different programmers and different code styles, and then use these different modules that may vary much in their design: one part will be platform specific and C code extended, other be written purely on meta language and create just an interface, and third will be most slow but feature rich that be responsible for buisness logic. So you get most perfomance on bottlenecks and write simpler code on the top level of your project logic.

Code translation is everything: you could write some library once and use it in different applications and platforms. You may still want to enchance optimization, but you do not need to complitely rewrite all of the code, only parts of it.

One of the main ideologies is a late bounding (may be not)

Hello world:
```
use console;
main()
{
    print("hello world!");
}
```


## TODO
deciminal

1) Механизм "членов" в интерфейсах - определять не только функции, необходимые для реализации, но и помечать что для них должны быть _абстрактные_ данные.

2) Стирание границы между наследованием и инкапсуляцией.

Что-то типа такого:

```
           [Animal]
           ||    ||
         \/       \/
  [(Mammal) Dog] [(NonMammal) Frog]
```

```
interface Animal
{
    virtual printData() {};
    var type;
};

class Mammal
{
    int legs = 4;
    int temperature = 36.0;
};

class Dog : Animal
{
    @override printData = Mammal printData
    {
        println("Dog legs %d, temperature %f", data.legs, data.temperature);
    };
    @override type = Mammal data;
};

class NonMammal // Do not remember how this called
{
    int legs = 4;
    bool hibernation = false;    
}

class Frog : Animal
{
    @override printData = NonMammal printData
    {
        println("Frog legs %d, hibernation %b", data.legs, data.hibernation);
    };
    @override type = NonMammal data;
};

int main()
{
    Dog sharik = new; // Syntax shugar, equal to new Dog
    Frog alice = new;

    Animal[] = [sharik, alice];

    foreach(entity in Animal)
    {
        entity.printData();
    }    
}
```

Этот код выведет:
```
Dog legs 4, temperature 36.0
Frog legs 4, hibernation false
```

Писать реализацию функционала в _базовом классе_, строить интерфейсы, которые допускают _отключение_ вызова функций и доступа к членам 
## Test 0

Циклы как функции

```  
fn func(@iterator A)
{
    pint ((int)A.iterator)
} 
for ({count i = 0 | i < 1 | i++},code=func) 

```



```   
for ({count i = 0 | i < 1 | i++},name='A',code=func#goNext)
fn func
{
    pint ((int)A.iterator)
}
```


```   
for ({count i = 0 | i < 1 | i++},name='A') 
{
    pint ((int)A.iterator)
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

### Operational space

There is local operational space that part of global operational space, local operational space is divided by left operational space and right operational space.

```
global space
|(local space)   left space  =  rigt space   |
```

Some operations may create subspace, then current  local space will be global for them.


### Syntax

`//` - commentary untill end of the line
```
// This is a commentary
```

`/* */` - multiline commentary
```
/*
This is a multiline commentary
*/
```

`@` - dynamic space extension.

```
func()
{
@
}
```

`#` - static space extension, everything that logically needs be foreseen before current operators otherwise it's behavior unpredictable.

```
func()
{
    #function.body = #assembly.x86{pop eax; pop cx; add cx;}; // not sure what it does
}
```

`(...)` - subspace creation then execute with it's content

```
func(); // execute function
call(mem[0xffffffff], @~.stdcall)(); // execute function at 0xffffffff as stdcall
```



### Naming

There are basic and additional keywords. All names such as
```
for, while, if, ...
```
Are 1st rank keywords. You can not use them for naming. If you need to reference them use underscore before `_for`. Sometime you will need it, for exaple when you writing you own code generation patch.

Additional or 2nd rank keywords are context-specific. For example in for it
```
@step, @iterator, @name
```

You can reference them with a special meta symbol.

Meta characters lets you modify basic control flow of a program. There are basic conception on which every code has internal instructions, such as runtime _loops_, _control flow_, _variable modification_ and purely static operations for example _linkage_ and _preprocessor_ in C/C++, but they better integrated and more hi level.

### Name extension

In meta you can extend a name with `::` symbols

Extending name may leak some definition, but this is good for not specifing all the time enums and use them for extending functionality of function calling (even constructor, even constructor of a module)

This is usefull when when you need to pass a enum to a function that declared inside this function (1), or when you writing your own class that is used as enum (2).

Extending package refers to default package global scoping variables (3) 

1)
```
shutdown(#@enum)
{
    enum shutdownType
    {
        shutdown,
        restart,
        sleep
    };
    @#enum = shutdownType;
}

main()
{
    shutdown(::sleep);
}
```

2)

```
class Variable
{
    var data;
    enum VariableType
    {
        integer,
        string     
    };
    VariableType type;
    #@enum = VariableType;

    init(#@param)
    {
        #  
        if (type(@param) == int)
        {
            data = new int(@param);
            type = ::int;
        }
        else if(type(@param) == string)
        {
            data = new string(@param);
            type = ::string;
        }
        else
        {
            throw Exeption(::wrongParam, @param = @param);
        }
    }
    
}

main()
{
    Variable a(10);
    print(a.@enum); // will print integer
    Variable b("10");

}
```

P.S. declaring an enum inside function isn't necessary to 

3.

```

```

**Repeat symbol**

`~` - Lets you repeat nearest name

```
debug.logLevel = ~.::All;
```

is equivalent to

```
debug.logLevel = debug.logLevel::All;
```

**Meta characters**

`@` - universal inner symbol. It can:

1) When written before name consider _name_ a keyword.
```
for i = 0 to 10 @step = 2 // @step is a keyword
    ...
```
2) When written inside subspace gives you control over it.
```
func()
```

**Set equality**

`#` - universal static symbol

`=` inner set

`:` static set

`:=` auto set

`let` lazy binding, set equality to the epression but later

**Other**

`swap` swap a variables

`copy` low level copy operation


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
    return [num1,num2]#tuple;
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
## Keywords
### Functions
`fn` - function
```
fn func()
{

}
```
`#static` - as typical C function. Pre-defined types
```
fn int:func(int: a,int: b)#static
{
    return b + a;
}

func(1,4) // 5
```
`#dynamic` - dinamically enterpret body of a function.
```
fn func(a, b)#dynamic
{
    return b + a;
}

func(1,4) // 5
func("a","b") // "ab"

`#template` - template as in c++.
```
fn func(a, b)#template
{
    return b + a;
}

func(1,4) // error
func(int:1,int:4) // 5
func(str:"a",str:"b") // "ab"
```


`#auto` - find best match for a function from #static, #dynamic and #template (due to highest possible type guessing)

## Functions
