#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np

__all__ = [ 'frdist' ]

def _c(ca,i,j,p,q):

    if ca[i,j] > -1:
        return ca[i,j]
    elif i == 0 and j == 0:
        ca[i,j] = np.linalg.norm(p[i]-q[j])
    elif i > 0 and j == 0:
        ca[i,j] = max( _c(ca,i-1,0,p,q), np.linalg.norm(p[i]-q[j]) )
    elif i == 0 and j > 0:
        ca[i,j] = max( _c(ca,0,j-1,p,q), np.linalg.norm(p[i]-q[j]) )
    elif i > 0 and j > 0:
        ca[i,j] = max(                                                     \
            min(                                                           \
                _c(ca,i-1,j,p,q),                                          \
                _c(ca,i-1,j-1,p,q),                                        \
                _c(ca,i,j-1,p,q)                                           \
            ),                                                             \
            np.linalg.norm(p[i]-q[j])                                            \
            )                                                          
    else:
        ca[i,j] = float('inf')
    
    return ca[i,j]


def frdist(p,q):
    """ 
    Computes the discrete Fréchet distance between
    two curves. The Fréchet distance between two curves in a
    metric space is a measure of the similarity between the curves.
    The discrete Fréchet distance may be used for approximately computing
    the Fréchet distance between two arbitrary curves, 
    as an alternative to using the exact Fréchet distance between a polygonal
    approximation of the curves or an approximation of this value.
    
    This is a Python 3.* implementation of the algorithm produced
    in Eiter, T. and Mannila, H., 1994. Computing discrete Fréchet distance. Tech. 
    Report CD-TR 94/64, Information Systems Department, Technical University 
    of Vienna.
    http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf

    Function dF(P, Q): real;
        input: polygonal curves P = (u1, . . . , up) and Q = (v1, . . . , vq).
        return: δdF (P, Q)
        ca : array [1..p, 1..q] of real;
        function c(i, j): real;
            begin
                if ca(i, j) > −1 then return ca(i, j)
                elsif i = 1 and j = 1 then ca(i, j) := d(u1, v1)
                elsif i > 1 and j = 1 then ca(i, j) := max{ c(i − 1, 1), d(ui, v1) }
                elsif i = 1 and j > 1 then ca(i, j) := max{ c(1, j − 1), d(u1, vj ) }
                elsif i > 1 and j > 1 then ca(i, j) :=
                max{ min(c(i − 1, j), c(i − 1, j − 1), c(i, j − 1)), d(ui, vj ) }
                else ca(i, j) = ∞
                return ca(i, j);
            end; /* function c */

        begin
            for i = 1 to p do for j = 1 to q do ca(i, j) := −1.0;
            return c(p, q);
        end.

    Parameters
    ----------
    P : Input curve - two dimensional array of points
    Q : Input curve - two dimensional array of points

    Returns
    -------
    dist: float64
        The discrete Fréchet distance between curves `P` and `Q`.

    Examples
    --------
    >>> from frechetdist import frdist
    >>> P=[[1,1], [2,1], [2,2]]
    >>> Q=[[2,2], [0,1], [2,4]]
    >>> frdist(P,Q)
    >>> 2.0
    >>> P=[[1,1], [2,1], [2,2]]
    >>> Q=[[1,1], [2,1], [2,2]]
    >>> frdist(P,Q)
    >>> 0
    """
    p = np.array(p, np.float64)
    q = np.array(q, np.float64)

    len_p = len(p)
    len_q = len(q)

    if len_p == 0 or len_q == 0:
        raise ValueError('Input curves are empty.')

    if len_p != len_q or len(p[0]) != len(q[0]):
        raise ValueError('Input curves do not have the same dimensions.')

    ca    = ( np.ones((len_p,len_q), dtype=np.float64) * -1 ) 

    dist = _c(ca,len_p-1,len_q-1,p,q)
    return dist
