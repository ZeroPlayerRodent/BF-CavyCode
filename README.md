# BF-CavyCode
Is a classic 8-bit [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter implemented in [CavyCode](https://github.com/ZeroPlayerRodent/cavycode).

## How to use
You can compile or run [bf-interpreter.cavy](https://github.com/ZeroPlayerRodent/BF-CavyCode/blob/main/bf-interpreter.cavy) from source, or you can run the pre-compiled [bf-interpreter.lisp](https://github.com/ZeroPlayerRodent/BF-CavyCode/blob/main/bf-interpreter.lisp).

(Note that this interpreter is only confirmed to work on [CLISP](https://clisp.sourceforge.io/))

After starting the interpreter, input a Brainfuck program with an exclamation point (!) marking the end of the program and press enter.

You can also load a Brainfuck program from a file by typing `cat filename.bf | clisp bf-interpreter.lisp` in the terminal. When doing this you must include your input in the same file as the program, just after the exclamation point.

## Why you shouldn't use
This implementation was only created for fun, and should not be used as a practical interpreter if you just want to run Brainfuck programs.

This implementation is not ideal to use because it is VERY slow and does not support dynamic memory. As of right now it only uses the traditional 30 kilobytes of memory and wraps around when it reaches the end of the memory tape. I may implement dynamic memory in the future, though.
