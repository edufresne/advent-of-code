# Advent of Code 2025
These are my solutions for the [Advent of Code](https://adventofcode.com/).

## Disclaimer
Right now I am aiming to just get them finished. There are definitely a bunch of optimizations 
I am going to try and retrofit into my solutions.

### My Scoreboard
| Year | Stars | Notes                                     |
| --- | --- |-------------------------------------------|
| 2024 | 30/50 ⭐ | First year!!                              |
| 2025 | 25/25 ⭐ | Hardest days were definitely day 9 and 10 |

### Notes
##### 2025 - Day 9
This one was my favourite problem of the set. The solution is that for two tiles, you have to make a rectangle and then 
figure out if the rectangle is both inside the polygon (with only horizontal/vertical lines) and each edge of the
rectangle doesn't intersect with any edges of the polygon (passing over a lake or inlet). I figured out that you had to 
count from a straight line from a given point how many edges you intersect and that even means outside the polygon and 
odd for inside. I couldn't however (without a little searching of the ray tracing algorithm) what to do when you 
intersect both a line on the same plane and a vertex. You have to ignore the horizontal liens and also treat the line as
if it's slightly above or below the vertex but be consistent. After that, line to line intersection is actually easy 
without math as you can just use min/maxing of coordinates.

##### 2025 - Day 10
This one I straight up could not do part 2 of. Part 1 didn't help me as I ended up figuring out that buttons should be 
pressed either 0 or 1 times since 2 or more times cancel each other out due to the toggling of the lights. So brute f
forcing was easy enough since the combinations are limited. Part 2 I mis-read and thought you can exceed voltage but it
had to be exact. Two ways to solves this which is a matrix of linear equations and use gaussian elimination (I forget 
linear algebra completely), or a clever solution I found on reddit which I had to copy. This one used recursion after
figuring out the unique pattern for unique buttons to get the voltages to all even. Then even is just the same buttons
`* 2` so simply just find `2 * ` the recursive function. 