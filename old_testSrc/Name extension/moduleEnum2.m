// test.m
module test;

enum TestEnum
{
    one = 1,
    two = 2,
    three = 3
}

enum TestEnumBinary
{
    one = 1,
    two = 10,
    three = 11
}

enum Inittype
{
    bin,
    dec
}

#@enum = InitType; // Forward name extension to init function

// # - means reference outside meta space
// @param - means special keyword
// @param is default parameter for module
if(#@param == InitType.dec)
{
    // First @ - reference local meta space
    // Second @ - reference special keyword
    @@enum = TestEnum;
    // Equal to another example with same name
}
else if(#@param == InitType.bin)
{
    @@enum = TestEnumBinary;
}

// main.m
module main;
use std;
use test(::bin); // Initialize the module with a parameter, bin is InitType

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
// INPUT
//11
// OUTPUT
//three