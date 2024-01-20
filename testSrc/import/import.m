#import ("console")
#import ("console", ::as = "con")

// Import module logically (with no direct instructions
// how to do it 


import ("console")
import ("console", ::as = "con")

// runtime only import (when interpretating)

#import_file("console.m")
import_file("console.m")  // runtime

// insert to the document some file like include in c/c++

#import_lib("console.lib")
#import_lib::auto("console.lib")

// Link with this lib the program (automatic)

var table = {"out":"@@out_()"} // TODO: questioanable syntax
#import_lib::functions("console.lib", ::table = table)

// Link with this functions needed

import_lib::dynamic("user32.dll")

// Dynamically import some .so or .dll file