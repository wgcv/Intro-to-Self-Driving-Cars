import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    """
        Dot product between two vectors.
        https://en.wikipedia.org/wiki/Dot_product
    """
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result

def get_row(matrix, row):
    """
        Get full row from a matrix
    """
    return matrix[row]
    
def get_column(matrix, column_number):
    """
    Get full column from a matrix
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        det = 0
        # Check if is square
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        # Check if is more than 2x2
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # For Matrix 1x1
        if (self.h * self.w) == 1:
            det = self.g[0][0]
        
        # For Matrix 2x2
        elif self.h == 2 & self.w == 2:
            det = self.g[1][1] * self.g[0][0] - self.g[0][1]*self.g[1][0]
        # In the future could implement determinant for matrix bigger
        else:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        
        for i in range(self.h):
            trace += self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = zeroes( self.h, self.w )
        # Check if exist inverse determinant for Matrices 2x2 (ad is not equal to bc)
        if self.h == 2 & self.w == 2:
            if self.determinant() == 0:
                raise(ZeroDivisionError, "This matrix is not invertible")
                
        inv_determinant = 1 / self.determinant()
        
        # For Matrix 1x1
        if((self.h * self.w) == 1):
            inverse[0][0] = inv_determinant

        # For Matrix 2x2
        elif self.h == 2 & self.w == 2:
            inverse[0][1] = -self.g[0][1] * inv_determinant
            inverse[1][0] = -self.g[1][0] * inv_determinant
            inverse[1][1] = self.g[0][0] * inv_determinant
            inverse[0][0] = self.g[1][1] * inv_determinant
        # In the future could implement determinant for matrix bigger
        else:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        return inverse
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        # The heigth is the wide and the wide be the heigth
        matrix_transpose = zeroes( self.w, self.h )
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_transpose.g[j][i] = self.g[i][j]
        return matrix_transpose
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append( self[i][j] + other[i][j])
            matrixSum.append(row)
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrixNeg = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-1 * self[i][j] )
            matrixNeg.append(row)
        return Matrix(matrixNeg)
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixSub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            matrixSub.append(row)
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        # Get dimensions of the Matrix 1 and the Matrix 2
        m_rows = self.h
        p_columns = other.w
        
        # empty list that will hold the product of AxB
        matrixMul = []
        
        for i in range(m_rows):
            row = []
            for j in range(p_columns):
                row.append(dot_product(get_row(self.g,i),get_column(other.g,j)))
            matrixMul.append(row)
        return Matrix(matrixMul)
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            matrixRmul = Matrix(self.g)
            for i in range(self.h):
                for j in range(self.w):
                    matrixRmul[i][j] = self.g[i][j] * other
            return (matrixRmul)

            