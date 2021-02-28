shutdown(#@enum)
{
    enum shutdownType
    {
        shutdown,
        restart,
        sleep
    };
    @@enum = shutdownType;
}

main()
{
    shutdown(::sleep);
}