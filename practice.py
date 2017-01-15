"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # Returning a set passes all the doc tests, but since line 9 
    # says "return list" I converted the set to a list

    return list(set(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # Wasn't sure if we want to return a set or a list, but if we want a list, 
    # I'd wrap the return statement in list().

    return set(items1) & set(items2)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """


    # I couldn't think of a good way to do this with sets or dictionaries...

    pairs = []

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            test_pair = sorted([numbers[i], numbers[j]])

            if numbers[i] + numbers[j] == 0 and test_pair not in pairs:
                pairs.append(test_pair)

    return pairs



def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

# I've included two solutions to this problem. The first is much more "skimmable"
# than the second. Is this just because I'm not yet 100% comfortable with list
# and dictionary comprehension? Which way is better? Does one run faster than 
# the other? My concern is that the count() function might slow things down

    # Version 1: using for loop and conditionals

    # char_counts = {}

    # for char in phrase:
    #     if char in ' .!,?':
    #         continue
    #     elif char not in char_counts:
    #         char_counts[char] = 1
    #     else:
    #         char_counts[char] += 1


    # max_count = max(char_counts.values())
    # return sorted([char for char, count in char_counts.items()
    #                if count == max_count])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Version 2: using list and dictionary comprehension
    letters = [char for char in phrase if char not in ' .!,?']

   # What is causing the PEP 8 violation in the following line?
    letters_w_counts = {char: letters.count(char) for char in set(letters)}

    max_count = max(letters_w_counts.values())

    return sorted([char for char, count in letters_w_counts.items()
                   if count == max_count])


#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
