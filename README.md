[![Build Status](https://travis-ci.org/spiros/discrete_frechet.svg?branch=master)](https://travis-ci.org/spiros/discrete_frechet)

Discrete Fréchet distance
=========================

Computes the discrete Fréchet distance between
two curves. The Fréchet distance between two curves in a
metric space is a measure of the similarity between the curves.
The discrete Fréchet distance may be used for approximately computing
the Fréchet distance between two arbitrary curves, 
as an alternative to using the exact Fréchet distance between a polygonal
approximation of the curves or an approximation of this value.

This is a Python 3.* implementation of the algorithm produced
in *Eiter, T. and Mannila, H., 1994. [Computing discrete Fréchet distance](http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf). Tech. 
Report CD-TR 94/64, Information Systems Department, Technical University 
of Vienna.*


```
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
```

Parameters
----------
    P : Input curve - two dimensional array of points
    Q : Input curve - two dimensional array of points

Returns
-------
dist: float64
    The discrete Frechet distance between curves `P` and `Q`.

Examples
--------
```
>>> from frechetdist import frdist
>>> P=[[1,1], [2,1], [2,2]]
>>> Q=[[2,2], [0,1], [2,4]]
>>> frdist(P,Q)
>>> 2.0
>>> P=[[1,1], [2,1], [2,2]]
>>> Q=[[1,1], [2,1], [2,2]]
>>> frdist(P,Q)
>>> 0
```
