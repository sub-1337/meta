// test.m
module test;

enum ~
{
    one = 1,
    two = 2,
    three = 3
}

// main.m
module main;
use std;
use test;

int main()
{
    switch(input().toType(type(test::)))
    {
        test::one:
            print("one");
        test::two:
            print("two");
        test::three:
            print("three");
        default:
            print("default");
    }
    return 0;
}