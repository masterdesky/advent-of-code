### Day 1: Trebuchet?!

You can find the original task description at the [official site](https://adventofcode.com/2023/day/1).

### Caveats and Solution
Advent of Parsing 2023, day 1. As people [mentioned](https://www.reddit.com/r/adventofcode/comments/189s2wr/day_3_2023_for_3_days_ive_just_been_using_regex/) on the [subreddit](https://www.reddit.com/r/adventofcode/), this problem was really easy to solve using regex, especially in Python with the `re` library.

#### First part solution
In the first part of the problem you had to use a simple regex to delete every character from every line that wasn't a digit. I used the regex

```python
re.sub('[^\d]', '', line)
```

where `line` is a line of the input file. This regex replaces every character that isn't a digit with an empty string, effectively deleting it. Here, the `\d` operator enclosed in `[]` brackets denotes the set of digits from `0-9`, while the `^` symbol negates the expression. Now you could simply merge the first and last digits of the string and then sum them up.

#### Second part solution
Now, the second part of the problem was much trickier. Although the example input silently hinted about the trickery that was to come, it wasn't entirely honest about it. You could easily find a naive solution that gave the right answer for the example input, but it would fail for the actual input!

The trickery was that some spelled out numbers were "merged" together in the input and you had to carefully parse them out. For example, the number `21` could be written as `twone`, or `18` as `oneight`.

The first step of my solution involved looking for the substrings `zero`, `one`, `two`, etc. in the input and replacing them with their corresponding digits based on a dictionary:

```python
n = 'zero one two three four five six seven eight nine'
return {w: n for n, w in enumerate(n.split())}
```

However, given a naive regex

```python
re.sub('|'.join(m.keys()), lambda x: str(m[x.group()]), line)
```

that I tried to use first, only the first digit in these problematic, "merged" substrings would be parsed out, and the second one would be left out. For example `twone` would be parsed out as `2ne`, instead of `21` and `oneight` as `1ght`, instead of `18`.

This was especially problematic, because there were lines in the puzzle input, where the last two digits were intentionally merged together. This would result us in missing the true last digit "hidden" in the string, giving us the wrong answer.

I was able to overcome this problem by **reading each line twice: once from left to right, then, from right to left**. On the first pass, I apply the naive regex normally, parsing out the very first digit from the problematic substrings. However, on the second pass, I reverse the input line and also apply the regex in reverse! Instead of looking for the substrings `zero`, `one`, `two`, etc. as in the first pass, I look for their reversed counterparts: `orez`, `eno`, `owt`, etc. from reading the line from right to left. This way, I'm still parsing "first digit" of the substrings, however this time, it's actually the last digit in the merged numbers!

This would ensure that on the first pass, the very first digits and on the second pass, the very last digits of the numbers would be always parsed out correctly.

The only thing left to do was to is to strip all remaining characters from the line that aren't digits and sum them up, just like in the first part of the problem. This time however, we have to merge **the first digit from the first pass** and **also the first digit from the second pass** of the same line, because the second pass started by parsing out the very last digits in each line.