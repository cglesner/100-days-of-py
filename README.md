# 100-days-of-py
Write a simple, complete program every day for 100 days.

Day 1 (2019-06-23):
* Wrote `dotproduct.calculate` to calculate a dot product 
of two n-dimentional vectors.

Day 2 (2019-06-24):
* Wrote `crossproduct.calcuate` to calculate a cross product
of two 3-dimentional vectors (cross product only defined
for 3-D vectors).

Day 3 (2019-06-25):
* Wrote `sequences.fibonacci` to calculate the n-th term in
the fibonacci sequence.

* Wrote `dotproduct.orthogonal` to calculate a vector
orthogonal to an n-dimensional input vector.

Day 4 (2019-06-26):
* Refactored `sequence.fibonacci` and `dotproduct.orthogonal`.

Day 5 (2019-06-27):
* Was too tired, didn't write anything :(.

Day 6 (2019-06-28):
* Wrote a simple class `func.Poly` that implements n-th order 
polynomial functions. They are constructed using a list of floats,
where the index of the element of the list corresponds to the
order of the polynomial term that that element is the coefficient
of.

Day 7 (2019-06-29):
* Was too tired/watched anime.

Day 8 (2019-06-30):
* Refactor the polynomial implementation to construct individual
polynomial terms as instances of the class `func.Pterm` using
tuples of `(order, coeficient)` as construction arguments. The 
`func.Poly` class instances are essentially sets of PTerms, and
are intended to provide a standard interface for operators
on polynomials, such as derivatives, and root finders that will
be implemented later. Also implemented `__call__` methods to allow
for use that looks more naturally like algebraic functions.

Day 9 (2019-07-01):
* Implemented `__eq__` operator on Pterm class. Quick test
because it's late. The method will consider two Pterm instances
equal if both the coefficients and the powers of the terms are
equal.

Day 10 (2019-07-02):
* Implemented `operator.differentiate` method that takes a `Pterm`
instance and returns a `Pterm` instance that is its derivative.

Day 11 (2019-07-03):
* Saw fireworks at Coors Field with Family and Friends.

Day 12 (2019-07-04):
* Saw fireworks in Littleton with Family.

Day 13 (2019-07-05):
* Went back and did clean up by adding tests for 
`test_crossproduct.py`.