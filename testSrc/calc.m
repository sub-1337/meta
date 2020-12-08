use types, arrays, errors;
use appType;

// Set app type to standart console
appType.type = ~.stdConsole;
// Set every error fatal - stop execution of program at them
error.fatality.default = ~.fatal;

doTask(A,operation,B)
{
    let A,B = number(A and B) #@exeption: suppress
    if (A and B is type.number)
    {
        switch(operation)
        {
            case "*":
                return A * B;
            case "/":
                return A / B;
            case "-":
                return A - B;
            case "+":
                return A + B;
            default:
                error("Invalid operation")
        }
    }
    else
        error("Invalid args")
}

main(console.args: arguments)
{
    if (arguments.size <= 1)
    {
        print("input strings:\n");
        var taskStr = input();
    }
    else
    {
        if (arguments.size != 4)
            error("Too much/less arguments");
        let taskStr = arguments.exept([0]);
    }
    print(doTask(@args = taskStr);)
}