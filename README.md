# 100-days-of-py
Write a simple, complete program every day for 100 days.

Day 1:
* Wrote `dotproduct.calculate` to calculate a dot product 
of two n-dimentional vectors.

Day 2:
* Wrote `crossproduct.calcuate` to calculate a cross product
of two 3-dimentional vectors (cross product only defined
for 3-D vectors).

Day 3:
* Wrote `sequences.fibonacci` to calculate the n-th term in
the fibonacci sequence.

* Wrote `dotproduct.orthogonal` to calculate a vector
orthogonal to an n-dimensional input vector.

Day 4:
* Refactored `sequence.fibonacci` and `dotproduct.orthogonal`.

Day 5:
* Was too tired, didn't write anything :(.

Day 6:
* Wrote a simple class `func.Poly` that implements n-th order 
polynomial functions. They are constructed using a list of floats,
where the index of the element of the list corresponds to the
order of the polynomial term that that element is the coefficient
of.

Day 7:
* Was too tired/watched anime.

Day 8:
* Refactor the polynomial implementation to construct individual
polynomial terms as instances of the class `func.Pterm` using
tuples of `(order, coeficient)` as construction arguments. The 
`func.Poly` class instances are essentially sets of PTerms, and
are intended to provide a standard interface for operators
on polynomials, such as derivatives, and root finders that will
be implemented later.