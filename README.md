## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

##  Rationale
2.1) The refactoring sign (code smells) Dead code suggests this since after invoking the PriceStrategy objects directly
in Rental, Movie has no use for the PriceStrategy classes, and therefore they go unused in Movie. Dead code suggests
that we remove any unused code so that we reduce code size.
2.2) The design principle that suggests this refactoring is Strive for loosely coupled objects.
Since price_code in Movie is a different class of objects we don't want to change Movie if we change
the PriceStrategy objects.

