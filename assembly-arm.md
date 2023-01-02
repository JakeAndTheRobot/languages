# ARM assembly

ARM assembly is a low-level programming language used to write code for microprocessors that use the ARM architecture. It is an assembly language, which means that it is a set of mnemonic codes that represent the underlying machine code that a processor can understand and execute. ARM assembly is used to write code for a variety of applications, including operating systems, device drivers, and firmware. It is a relatively simple and easy-to-learn language, but it can be time-consuming to write and debug programs in, since the code is closely tied to the underlying hardware.

**Registers:**

- r0-r12: General-purpose registers
- sp: Stack pointer
- lr: Link register
- pc: Program counter

**Instructions:**

- mov: Move data
- add: Add two values
- sub: Subtract one value from another
- mul: Multiply two values
- ldr: Load a word from memory
- str: Store a word in memory
- cmp: Compare two values
- b: Unconditional branch
- bl: Branch with link
- bx: Branch and exchange

**Directives:**

- .data: Declare initialized data
- .text: Declare code
- .global: Make a symbol visible to other files

**Assembler directives:**

- @: Start of a comment
- @’: Start of a multiline comment
- @’: End of a multiline comment
