shutdown(#@enum)
{
    enum shutdownType
    {
        shutdown,
        restart,
        sleep
    };
    @@enum = shutdownType;

    // (here goes actual code)
}

main()
{
    shutdown(::sleep);
}