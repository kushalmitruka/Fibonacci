"""
To derive nth fibonacci we will use the matrix mutiplication algorithm which give O(logn) time complexity

Fn = a*Fn-1 + b*Fn-2 + c*Fn-3 				for n > 3
f0 = 0
f1 = 1
f2 = 1

On solving we get
| F(n)   |  =  [ | a b c | ] ^ (n-2)   *  | F(2) |
| F(n-1) |     [ | 1 0 0 | ]              | F(1) |
| F(n-2) |     [ | 0 1 0 | ]              | F(0) |

where a = b = c = 1
"""

# TODO: Test the function
# TODO: Validate for all the corner cases

from datetime import datetime


# def matrix_multiply(matrix_a, matrix_b):
# 	""" Both the input matrix must be 3x3
# 	"""
# 	_m = []
# 	for i in range(3):
# 		_n = []
# 		for j in range(3):
# 			elem_ij = 0
# 			for k in range(3):
# 				elem_ij += matrix_a[i][k]*matrix_b[k][j]

# 			_n.append(elem_ij)
# 		_m.append(_n.copy())

# 	matrix_a = _m.copy() 


# def power_add_matrix(matrix, seqindex):

# 	_matrix = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]

# 	if seqindex == 1:
# 		return matrix[0][0] + matrix[0][1]

# 	power_add_matrix(matrix, seqindex//2)

# 	if seqindex % 2 != 0:
# 		matrix_multiply(matrix, _matrix)

# 	return matrix[0][0] + matrix[0][1]


# def calculate_and_return_n_fib(seqindex):

# 	matrix = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]

# 	if seqindex <= 2:
# 		if seqindex == 0:
# 			return 0
# 		else:
# 			return 1
# 	else:
# 		return power_add_matrix(matrix, seqindex-2)


class MatrixFibonacci:
    Q = [[1, 1],
         [1, 0]]

    def __init__(self):
        self.__memo = {}

    def __multiply_matrices(self, M1, M2):
        """Matrices miltiplication
        (the matrices are expected in the form of a list of 2x2 size)."""

        a11 = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
        a12 = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
        a21 = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
        a22 = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
        r = [[a11, a12], [a21, a22]]
        return r

    def __get_matrix_power(self, M, p):
        """Matrix exponentiation (it is expected that p that is equal to the power of 2)."""

        if p == 1:
            return M
        if p in self.__memo:
            return self.__memo[p]
        K = self.__get_matrix_power(M, int(p / 2))
        R = self.__multiply_matrices(K, K)
        self.__memo[p] = R
        return R

    def get_number(self, n):
        """Getting the nth Fibonacci number
        (a non-negative integer number is expected as n)."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Factoring down the passed power into the powers that are equal to the power of 2), 
        # i.e. 62 = 2^5 + 2^4 + 2^3 + 2^2 + 2^0 = 32 + 16 + 8 + 4 + 1.
        powers = [int(pow(2, b))
                  for (b, d) in enumerate(reversed(bin(n - 1)[2:])) if d == '1']
        # The same, but less pythonic: http://pastebin.com/h8cKDkHX

        matrices = [self.__get_matrix_power(MatrixFibonacci.Q, p)
                    for p in powers]
        while len(matrices) > 1:
            M1 = matrices.pop()
            M2 = matrices.pop()
            R = self.__multiply_matrices(M1, M2)
            matrices.append(R)
        return matrices[0][0][0]


mfib = MatrixFibonacci()


def return_fibonacci_and_time(seqindex):
    before = datetime.now()
    value = mfib.get_number(seqindex)
    after = datetime.now()

    time_taken = after - before

    seconds_str = '{}'.format(time_taken.seconds)
    microseconds_str = '0' * (6 - len(str(time_taken.microseconds))) + '{}'.format(time_taken.microseconds)
    try:
        return '{:,.0f}'.format(value), '{}.{} Seconds'.format(seconds_str, microseconds_str)
    except OverflowError:
        return '{}'.format(value), '{}.{} Seconds'.format(seconds_str, microseconds_str)
