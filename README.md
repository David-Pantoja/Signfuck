# Signfuck

## Introduction

Tired of typing your code? Signfuck allows you to just move your hands around and communicate a valid Turing complete program! The interpreter converts Signfuck to Brainfuck.

## Design Principles

- Should work
- 👏 Makes it obvious you are communicating a program
- Should avoid the 🖕 action unless required by end user

## Language Concepts

Signfuck consists of 9 commands. If you are familiar with Brainfuck, the largest differences are that Signfuck must start and end with a clap and that Signfuck may be communicated directly visually. Because of the streamlined 9 commands, this makes it an incredibly easy language to sign for beginners, unlike other languages where at minimum all ASCII characters may need to be known, with ASL words possibly being required.

## Memory Array and Pointer

Similar to Brainfuck, Signfuck uses a data pointer and a one-dimensional array initialized to zero. Signfuck also uses two streams for input and output using only ASCII char encodings.

## Comments

Why use words when you can point?

## Syntax

| Symbol | Description                                                                                                                                                                       |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 👏     | All Signfuck scripts must start and end with a clap to get attention.                                                                                                             |
| 👉     | Increment the data pointer by one (to point to the next cell to the right).                                                                                                       |
| 👈     | Decrement the data pointer by one (to point to the next cell to the left).                                                                                                        |
| 👆     | Increment the byte at the data pointer by one.                                                                                                                                    |
| 👇     | Decrement the byte at the data pointer by one.                                                                                                                                    |
| 👌     | Output the byte at the data pointer.                                                                                                                                              |
| 🫵      | Accept one byte of input, storing its value in the byte at the data pointer.                                                                                                      |
| 🫸      | If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching 🫷 command. |
| 🫷      | If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching 🫸 command. |

All other characters are ignored. Do not include 👏 in the middle of written files as this would mean it is a new script when signed.

## Example

The following example can be found in test.signfuck and converted to Brainfuck with `$ python3 signfuck.py test.signfuck`

```
👏the following outputs 2x the input ascii value
🫵🫸👇👉👆👉👆👈👈🫷
👉
🫸👇👈👆👉🫷
👉
🫸👇👈👈👆👉👉🫷
👈👈
👌
👏
```
