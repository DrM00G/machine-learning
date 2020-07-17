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
assert result.test_show()==Matrix([[1, 0], [0, 1]]).test_show(), "Test  failed: output "+result.test_show()+ " expected to be "+Matrix([[1, 0], [0, 1]]).test_show()
print("Test  passed")


# assert result.test_show() == , "Test  failed: output "+result.test_show()+ " expected to be "+{expected}
# print("Test  passed")