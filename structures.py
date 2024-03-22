class Vec:

  def __init__(self, contents=[]):
    """constructor defaults to empty vector
         accepts list of elements to initialize a vector object with the
         given list
      """
    self.elements = contents
    return

  def __abs__(self):
    """Overloads the built-in function abs(v)
          returns the Euclidean norm of vector v
      """
    return sum([e**2 for e in self.elements])**0.5

  def __add__(self, other):
    """Overloads the + operation to support Vec + Vec
       raises ValueError if vectors are not same length
      """
    if len(self.elements) == len(other.elements):
      return Vec([
          self.elements[i] + other.elements[i]
          for i in range(len(self.elements))
      ])
    else:
      raise ValueError("ERROR: Vectors must be same length")


  def __mul__(self, other):
    """Overloads the * operator to support
          - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
          - Vec * float (component-wise product)
          - Vec * int (component-wise product)

      """
    if type(other) == Vec:  # define dot product
      if len(self.elements) == len(other.elements):
        return sum([
            self.elements[i] * other.elements[i]
            for i in range(len(self.elements))
        ])
      else:
        raise ValueError("ERROR: Vectors must be same length")
    elif type(other) == float or type(
        other) == int:  # scalar-vector multiplication
      return Vec([other * self.elements[i] for i in range(len(self.elements))])

  def __rmul__(self, other):
    """Overloads the * operation to support
          - float * Vec
          - int * Vec
      """
    if type(other) == float or type(other) == int:
      return Vec([other * self.elements[i] for i in range(len(self.elements))])
    else:
      raise ValueError("ERROR: Incompatible types.")

  def __str__(self):
    """returns string representation of this Vec object"""
    return str(self.elements)  # does NOT need further implementation

  def __sub__(self, other):
    if type(other) == Vec and len(self.elements) == len(other.elements):
      return Vec([
          self.elements[i] - other.elements[i]
          for i in range(len(self.elements))
      ])
    elif type(other) == Vec:
      raise ValueError("ERROR: Vectors must be same length")
    else:
      raise ValueError("ERROR: Incompatible types.")

  def __truediv__(self, other):
    if type(other) == float or type(other) == int:
      return Vec([x / other for x in self.elements])

  def __iter__(self):
    return iter(self.elements)

  def __getitem__(self, i):
    return self.elements[i]

  def __len__(self):
    return len(self.elements)



class Matrix:
  # TODO: Copy-paste your Matrix class from pa5.py here
  pass
  