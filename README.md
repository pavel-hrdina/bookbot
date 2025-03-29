# Bookbot

A word count file analyzer writen in python.

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You only need vanilla python, no 3d party libs were used in the making. Install python from your
package manager or download the [binary](https://www.python.org/downloads/).

### Installation

1. Cone the repo
   ```sh
   git https://github.com/pavel-hrdina/bookbot.git
   ```

<!-- USAGE EXAMPLES -->

## Usage

To use this project run it as follows from the project root:

   ```sh
   python main.py <path_to_book>
   ```

example output:

   ```sh
   ...
   ============ BOOKBOT ============
   Analyzing book found at books/frankenstein.txt...
   ----------- Word Count ----------
   Found 75767 total words
   --------- Character Count -------
   e: 44538
   t: 29493
   a: 25894
   o: 24494
   i: 23927
   n: 23643
   s: 20360
   r: 20079
   h: 19176
   d: 16318
   l: 12306
   m: 10206
   u: 10111
   c: 9011
   f: 8451
   y: 7756
   w: 7450
   p: 5952
   g: 5795
   b: 4868
   v: 3737
   k: 1661
   x: 691
   j: 497
   q: 325
   z: 235
   æ: 28
   â: 8
   ê: 7
   ë: 2
   ô: 1
   ============= END ===============
   ```

## License

This project is licensed under [MIT](./LICENSE)