### Day 2: Cube Conundrum

You can find the original task description at the [official site](https://adventofcode.com/2023/day/2).

### Caveats and Solution
Advent of Parsing 2023, day 2. This problem was much easier, than day 1. Although again, it consisted of two parts, the difference between the code required was minuscule and the second part felt even easier, than the first one. "Literally calculate the same thing as in the first part, but now calculate the product of the numbers too before adding them together". Well, okay then. I guess I'll just do that.

No complicated regex in sight, just one pattern to find every instances of numbers followed by a name of color using `re.findall(rf'(\d+)\s*{c}', l)`, where `c` was either `red`, `green` or `blue`. No tricky puzzle input to `twone` our entire day and cause sleepless nights for the rest of the month. But really, I just keep using regex and lambda functions and it keeps working. (I'm not sure if that's a good sign though.)