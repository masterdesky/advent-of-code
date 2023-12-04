### Day 3: Gear Ratios

You can find the original task description at the [official site](https://adventofcode.com/2023/day/3).

### Caveats and Solution
Advent of Parsing 2023, day 3. First thoughts: wtf? Can I regex my way out of this? Or should I just use my physicist linalgebra/image processing/neural networks skills? I guess I'll try the latter here instead of regex.

#### First part solution
Since we're code golfing here, notice that our puzzle input is a rectangular matrix. It actually doesn't really matter, this solution could easily work for a non-rectangular matrix too with the correct zero-padding, but now I won't detail that, because my solution is good enough for this puzzle. And we're code golfing here if I haven't mentioned that already.

First step is to encode every character in the original matrix of characters. First, assign `1` to every digit, creating a matrix is `1`s and other characters. Then, assign `0` for every useless character, namely only `.`s in this puzzle. Finally, assign `9` to every non-numeric characters, like `#` or `@` or etc., whatever they are. Now we have a matrix of only digits. Let's call it `M`. Additionally, pad our input matrix `M` with all `0`s on all sides. (It's a surprise tool that will help us later.)

In the second step, select a $3 \times3$ window function with all `1`s with a single `0` in the middle and call it `C` (as in convolution). You know what will happen next...

Convolve the `M` matrix with the `C` window function and call the result `R`. Now `R` is a matrix of numbers of the same size as `M`. However, the numbers in `R` represent exactly the neighbourhood relations of the corresponding cells in `M`.

#### Second part solution