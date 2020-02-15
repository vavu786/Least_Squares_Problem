import numpy as np
from RREF_Calculator import rrefMatrix

def main():
    degree = int(input("What degree is the polynomial? "))
    pair_or_matrix = input("Ordered pairs (P) or a coefficient matrix? (M)? ")
    while pair_or_matrix.lower() != 'p' and pair_or_matrix.lower() != 'm':
        pair_or_matrix = input("Please enter a 'p' or an 'm': ")
    
    if pair_or_matrix.lower() == 'p':
        num = int(input("How many points are there? "))
        points = input("Please enter each coordinate and each point separated by a space.\nFor example, (2,3), (3,1), and (0,3) will go in as 2 3 3 1 0 3\n")
        # points_matrix is the matrix of the ordered pairs
        points_matrix = np.asarray(points.split(" ")).astype(float).reshape(num, 2)
        # points_matrix_x_coords is the matrix of only the x coordinates
        points_matrix_x_coords = np.delete(points_matrix, 1, 1)
        # coeff_matrix is the coefficient matrix, without the ones
        coeff_matrix = np.around(np.empty([num, degree], dtype=float))
        for i in range(degree):
            coeff_matrix[:,i] = np.power(np.transpose(points_matrix_x_coords), i+1)
        # A connects a matrix of ones to coeff_matrix to form the final matrix
        A = np.concatenate((np.ones((num, 1), dtype=float), coeff_matrix), axis=1)
        for i in range(1, degree):
            np.power(A[:,i], i)
        # b is the matrix of the y coordinates
        b = points_matrix[:,1].reshape(num, 1)
        print("A is: \n{}".format(A))
        print("b is: \n{}".format(b))
        
        
    if pair_or_matrix.lower() == 'm':
        rows = int(input("How many rows are there? "))
        cols = int(input("How many columns are there? "))
        A_values = input("Enter the values of the coefficient matrix in one line, separated by spaces:\n")
        A = np.asarray(A_values.split(" ")).astype(float).reshape(rows, cols)
        b_values = input("Enter the values of vector b: ")
        b = np.asarray(b_values.split(" ")).astype(float).reshape(rows, 1)
        print("A is: \n{}".format(A))
        print("b is: \n{}".format(b))

    A_trans = np.transpose(A)
    A = np.dot(A_trans, A)
    b = np.dot(A_trans, b)
    
    augmented_coeff_matrix = np.concatenate((A, b), axis=1)
    rrefMatrix(augmented_coeff_matrix)
    solution_col_num = augmented_coeff_matrix.shape[1]-1
    solution = augmented_coeff_matrix[:,solution_col_num]
    print("The solution for the least squares problem is:\n{}".format(solution))
if __name__ == '__main__':
    main()

