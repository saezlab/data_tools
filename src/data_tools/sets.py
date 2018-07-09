# -*- coding: utf-8 -*-

'''
data_tools.sets
===============

Set operations module.
'''

__all__ = ['bit_or', 'find_min', 'in_all', 'subsets']

import itertools


def bit_or(a, b):
    '''
    Returns the bit operation OR between two bit-strings *a* and *b*.
    NOTE: *a* and *b* must have the same size.

    * Arguments:
        - *a* [tuple]: Or any iterable type.
        - *b* [tuple]: Or any iterable type.

    * Returns:
        - [tuple]: OR operation between *a* and *b* element-wise.

    * Examples:
        >>> a, b = (0, 0, 1), (1, 0, 1)
        >>> bit_or(a, b)
        (1, 0, 1)
    '''

    if a == b:
        return a

    else:
        return tuple([el_a | el_b for (el_a, el_b) in zip(a, b)])


def find_min(A):
    '''
    Finds and returns the subset of vectors whose sum is minimum from a
    given set *A*.

    * Arguments:
        - *A* [set]: Set of vectors ([tuple] or any iterable).

    * Returns:
        - [set]: Subset of vectors in *A* whose sum is minimum.

    * Examples:
        >>> A = {(0, 1, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)}
        >>> find_min(A)
        set([(0, 1, 0), (1, 0, 0)])
    '''

    A = list(A)
    sums = map(sum, A)
    idx_mins = np.where(sums == min(sums))[0]

    return {A[i] for i in idx_mins}


def in_all(x, N):
    '''
    Checks if a vector *x* is present in all sets contained in a list
    *N*.

    * Arguments:
        - *x* [tuple]: Or any hashable type as long as is the same
          contained in the sets of *N*.
        - *N* [list]: Or any iterable type containing [set] objects.

    * Returns:
        - [bool]: ``True`` if *x* is found in all sets of *N*, ``False``
          otherwise.

    * Examples:
        >>> N = [{(0, 0), (0, 1)}, # <- set A
        ...      {(0, 0), (1, 1), (1, 0)}] # <- set B
        >>> x = (0, 0)
        >>> in_all(x, N)
        True
        >>> y = (0, 1)
        >>> in_all(y, N)
        False
    '''

    for s in N:
        if x in s:
            pass

        else:
            return False

    return True


def subsets(N):
    '''
    Function that computes all possible logical relations between all
    sets on a list *N* and returns all subsets. This is, the subsets
    that would represent each intersecting area on a Venn diagram.

    * Arguments:
        - *N* [list]: Or any iterable type containing [set] objects.

    * Returns:
        - [dict]: Collection of subsets according to the logical
          relations between the sets in *N*. The keys are binary codes
          that denote the logical relation (see examples below).

    * Examples:
        >>> N = [{0, 1, 2}, {2, 3, 4}]
        >>> subsets(N)
        {'11': set([2]), '10': set([0, 1]), '01': set([3, 4])}
        >>> N = [{0, 1}, {2, 3}, {1, 3, 4}]
        >>> subsets(N)
        {'010': set([2]), '011': set([3]), '001': set([4]), '111': set([
        ]), '110': set([]), '100': set([0]), '101': set([1])}
    '''

    combinations = list(itertools.product(['0', '1'], repeat=len(N)))[1:]

    result = dict()

    for c in combinations:
        intersect = [N[n] for n in [i for i, v in enumerate(c) if v == '1']]
        unite = [N[n] for n in [i for i, v in enumerate(c) if v == '0']]

        lhs = reduce(set.intersection, intersect)
        rhs = reduce(set.union, unite) if unite else set()

        result[''.join(c)] = lhs.difference(rhs)

    return result
