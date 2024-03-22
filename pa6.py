'''
import copy
from structures import Matrix, Vec
""" ----------------- PROBLEM 1 ----------------- """


def norm(p : int, v : Vec):
  """
  returns the p-norm of Vec v
  INPUT:
      p - an integer determining the norm to be calculated
      v - the Vec object for which the norm will be applied
  OUTPUT:
      the norm as a float
  """
  # TODO: implement this function
  pass


""" ----------------- PROBLEM 2 ----------------- """


def _ref(A : Matrix):
  """
    returns the Row Echelon Form of the Matrix A
    INPUT: Matrix A
    OUTPUT: distinct Matrix object that is the
            Row-Echelon Form of A
    """
  matrix = Matrix(copy.deepcopy(A.rowsp))
  m, n = matrix.dim()
  # TODO: Finish implementation for this function
  return matrix


""" ----------------- PROBLEM 3 ----------------- """


def rank(A : Matrix):
  """
  returns the rank of the given Matrix object
  as an integer
  """
  # TODO: implement this function
  pass


""" ----------------- PROBLEM 4 ----------------- """


def gauss_solve(A : Matrix, b : Vec):
  """
  returns the solution to the system Ax = b 
  if the system has a solution.  If the system
  does not have a solution, None is returned.
  If the system has infinitely-many solutions,
  the number of free variables as an 'int' is returned
  INPUT:
      A - a Matrix object
      b - a Vec object

  OUTPUT:
      Vec object if the system has a unique solution
      None if the system has no solution
      int if the system has infinitely-many solutions
  """
  # TODO: Implement this function
  pass


""" ----------------- PROBLEM 5 ----------------- """


def gram_schmidt(S : set):
  """
  returns the orthonormal basis of given set S
  INPUT: S - a set of linearly independent 'Vec' objects
  OUTPUT: An orthonormal set of 'Vec' objects
  """
  # TODO: Implement this function
  pass
'''
import copy
from structures import Matrix, Vec
""" ----------------- PROBLEM 1 ----------------- """


def norm(v : Vec, p: int):
  """
  returns the p-norm of Vec v
  INPUT:
      p - an integer determining the norm to be calculated
      v - the Vec object for which the norm will be applied
  OUTPUT:
      the norm as a float
  """
  # TODO: implement this function
  result = 0.0
  for value in v:
    result += abs(value) ** p

  result = result ** (1/p)

  return result

""" ----------------- PROBLEM 2 ----------------- """


def _ref(A : Matrix):
  """
    returns the Row Echelon Form of the Matrix A
    INPUT: Matrix A
    OUTPUT: distinct Matrix object that is the
            Row-Echelon Form of A
    """
  matrix = Matrix(copy.deepcopy(A.rowsp))
  m, n = matrix.dim()
  # TODO: Finish implementation for this function
  pivot_row = 0

  for j in range(n):
      # Find a pivot row with a non-zero entry in the current column
      pivot_found = False
      for i in range(pivot_row, m):
          if matrix.get_entry(i + 1, j + 1) != 0:
              # Swap rows to make the pivot row the current row
              matrix.set_row(i + 1, matrix.get_row(pivot_row + 1))
              matrix.set_row(pivot_row + 1, matrix.get_row(i + 1))  # Fix: Swap rows correctly
              pivot_found = True
              break

      if pivot_found:
          # Make the pivot element 1
          pivot_value = matrix.get_entry(pivot_row + 1, j + 1)

          # Check if the pivot value is zero before division
          if pivot_value != 0:
              for col_index in range(1, n + 1):
                  matrix.set_entry(pivot_row + 1, col_index, matrix.get_entry(pivot_row + 1, col_index) / pivot_value)

              # Eliminate below the pivot
              for i in range(pivot_row + 1, m):
                  factor = matrix.get_entry(i + 1, j + 1)
                  if factor != 0:  # Check if the factor is not zero before elimination
                      for col_index in range(1, n + 1):
                          matrix.set_entry(i + 1, col_index, matrix.get_entry(i + 1, col_index) - factor * matrix.get_entry(pivot_row + 1, col_index))

              # Move to the next pivot row
              pivot_row += 1

          else:
              # If pivot value is zero, skip to the next column
              continue

  return matrix



""" ----------------- PROBLEM 3 ----------------- """


def rank(A: Matrix):
  ref_matrix = _ref(A)

  # Count the number of non-zero rows in the reduced row echelon form
  rank = sum(1 for row in ref_matrix.rowsp if any(entry != 0 for entry in row))

  return rank


""" ----------------- PROBLEM 4 ----------------- """


def gauss_solve(A: Matrix, b: Vec):
  """
  returns the solution to the system Ax = b 
  if the system has a solution. If the system
  does not have a solution, None is returned.
  If the system has infinitely-many solutions,
  the number of free variables as an 'int' is returned
  INPUT:
      A - a Matrix object
      b - a Vec object

  OUTPUT:
      Vec object if the system has a unique solution
      None if the system has no solution
      int if the system has infinitely-many solutions
  """
  # TODO: Implement this function
  augmented_matrix = [
      [A.get_entry(i + 1, j + 1) for j in range(len(A.colsp))] + [b.elements[i]] for i in range(len(A.rowsp))
  ]

  # Perform Gaussian elimination
  ref_matrix = _ref(Matrix(augmented_matrix))

  # Check for inconsistency
  for row in ref_matrix.rowsp:
      if all(entry == 0 for entry in row[:-1]) and row[-1] != 0:
          return None  # Inconsistent system, no solution

  # Count the number of non-zero rows in the row echelon form
  rank = sum(1 for row in ref_matrix.rowsp if any(row[:-1]))

  # Check for underdetermined system (infinitely-many solutions)
  if rank < len(A.colsp):
      return len(A.colsp) - rank  # Number of free variables

  # Back-substitution to find the solution
  solution = [0] * len(A.colsp)
  for i in range(rank - 1, -1, -1):
      row_entries = ref_matrix.rowsp[i][i+1:rank]
      solution[i] = (ref_matrix.rowsp[i][-1] - sum(row_entries[j-i-1] * solution[j] for j in range(i+1, rank))) / ref_matrix.rowsp[i][i]

  return Vec(solution)




""" ----------------- PROBLEM 5 ----------------- """


def gram_schmidt(S : set):
  """
  returns the orthonormal basis of given set S
  INPUT: S - a set of linearly independent 'Vec' objects
  OUTPUT: An orthonormal set of 'Vec' objects
  """
  # TODO: Implement this function
  Q = []
  for v in S:
      u = copy.deepcopy(v)
      for q in Q:
          u = u - ((v * q) / (q * q)) * q
      u = u / norm(u, 2)
      Q.append(u)
  return Q
