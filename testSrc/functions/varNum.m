func num sumNum(var<num> a, var<num> b)
{
    return a + b;
}

import console;

func calc()
{
    var a = 10;
    var b = 20;
    var c = sumNum();
    consle.print(c);
}