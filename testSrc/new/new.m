import console
use console.*

func main()
{
    // var a = new::@gc(int);
    var<ptr> $a = new(int);
    input(a);
    print(a);
    if ($a)
        $a.delete();
}