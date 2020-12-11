import sys
sys.path.append('src')
from Matrix import Matrix


mat1 = Matrix([[1, 2], [3, 2]])
mat2 = Matrix([[3, 4], [4, 10]])

print("Testing Arithmetic Operations:")

result = Matrix.add(mat1,mat2)
assert  result.test_show()==Matrix([[4, 6], [7, 12]]).test_show(), "Test Addition failed: output "+ result.test_show() + " expected to be "+Matrix([[4, 6], [5, 12]]).test_show()
print("Test  passed")


result = Matrix.subtract(mat2,mat1)
assert  result.test_show()==Matrix([[2, 2], [1, 8]]).test_show(), "Test Subtraction failed: output "+ result.test_show() + " expected to be "+Matrix([[2, 2], [1, 8]]).test_show()
print("Test  passed")


result = Matrix.scale(mat1,2)
assert  result.test_show()==Matrix([[2, 4], [6, 4]]).test_show(), "Test Scaling failed: output "+ result.test_show() + " expected to be "+Matrix([[2, 4], [6, 4]]).test_show()
print("Test  passed")


result = Matrix.multiply(mat1,mat2)
assert  result.test_show()==Matrix([[11, 24], [17, 32]]).test_show(), "Test Matrix Mult failed: output "+ result.test_show() + " expected to be "+Matrix([[11, 24], [17, 32]]).test_show()
print("Test  passed")


result = Matrix.transpose(mat1)
assert  result.test_show()==Matrix([[1, 3], [2, 2]]).test_show(), "Test Transpose failed: output "+ result.test_show() + " expected to be "+Matrix([[1, 3], [2, 2]]).test_show()
print("Test  passed")

mat1 = Matrix([[1, 2], [3, 2]])
result = Matrix.rref(mat1)
assert result.test_show()==Matrix([[1.0, 0.0], [-0.0, 1.0]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1, 0], [0, 1]]).test_show()
print("Test  passed")

print("rref checks:")

mat1 = Matrix([[5, 4, 6, 3, 10], [5, 5, 1, 9, 9], [3, 3, 4, 10, 7]])
result = Matrix.rref(mat1)
assert result.test_show()==Matrix([[1.0, 0.0, 0.0, -11.235294117647065, 0.3529411764705874], [0.0, 1.0, 0.0, 12.764705882352946, 1.3529411764705888], [0.0, 0.0, 1.0, 1.3529411764705892, 0.47058823529411775]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1, 0, 0, -11.235294117647065, 0.3529411764705874], [0, 1, 0, 12.764705882352946,
1.3529411764705888], [0.0, 0.0, 1.0, 1.3529411764705892, 0.47058823529411775]]).test_show()
print("Test  passed")


mat1 = Matrix([[10, 10, 6], [9, 4, 7], [1, 10, 8], [1, 3, 5], [8, 2, 3]])
result = Matrix.rref(mat1)
assert result.test_show()==Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1, 0, 0], [0, 1, 0], [0.0, 0.0, 1.0], [0, 0, 0], [0, 0, 0]]).test_show()
print("Test  passed")

mat1 = Matrix([[1, 0, 0], [0, 1, 0], [0.0, 0.0, 1.0], [0, 0, 0], [0, 0, 0]])
result = Matrix.rref(mat1)
assert result.test_show()==Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1, 0, 0], [0, 1, 0], [0.0, 0.0, 1.0], [0, 0, 0], [0, 0, 0]]).test_show()
print("Test  passed")

mat1 = Matrix([[9, 1, 6, 6, 10], [1, 9, 9, 1, 7], [
            2, 4, 3, 9, 5], [1, 7, 3, 5, 0], [8, 3, 10, 7, 7]])
result = Matrix.rref(mat1)
assert result.test_show()==Matrix([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [-0.0, -0.0, -0.0, -0.0, 1.0]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [-0.0, -0.0, -0.0, -0.0, 1.0]]).test_show()
print("Test  passed")

mat1 = Matrix([[7, 10, 2, 9, 10], [4, 3, 6, 2, 5], [2, 9, 5, 9, 4]])
result = Matrix.rref(mat1)
assert result.test_show()==Matrix([[1.0, 0.0, 0.0, -0.2423208191126282, 1.1399317406143346], [0.0, 1.0, 0.0, 1.0784982935153584,0.2081911262798635], [0.0, 0.0, 1.0, -0.044368600682593795, -0.030716723549488064]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1.0, 0.0, 0.0, -0.24232081911262804, 1.1399317406143346], [0.0, 1.0, 0.0, 1.0784982935153584,0.2081911262798635], [0.0, 0.0, 1.0, -0.044368600682593795, -0.030716723549488064]]).test_show()
print("Test  passed")

print("det checks:")

mat1 = Matrix([[1, 2, 3], [1, 2, 4], [0, 0, 0]])
result = Matrix.recursive_det(mat1)
assert result == 0, "Test  failed: output "+str(result)+ " expected to be 0"
print("Test  passed")

#invertible Matrix
mat1 = Matrix([[9, 3, 8], [5, 1, 6], [10, 0, 1]])
result = Matrix.recursive_det(mat1)
assert result == 94, "Test  failed: output "+str(result)+ " expected to be 94"
print("Test  passed")
mat1 = Matrix([[9, 3, 8], [5, 1, 6], [10, 0, 1]])
result = Matrix.inverse_by_minors(mat1)
assert result == [[0.010638297872340413, -0.03191489361702121, 0.10638297872340424], [0.5851063829787235, -0.7553191489361706, -0.14893617021276595], [-0.1063829787234043, 0.3191489361702128, -0.06382978723404255]], "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[0.010638297872340413, -0.03191489361702121, 0.10638297872340424], [0.5851063829787235, -0.7553191489361706, -0.14893617021276595], [-0.1063829787234043,0.3191489361702128, -0.06382978723404255]]).test_show()
print("Test  passed")

# assert result.test_show() == , "Test  failed: output "+result.test_show()+ " expected to be "+{expected}
# print("Test  passed")