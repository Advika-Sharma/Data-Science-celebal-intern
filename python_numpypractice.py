## 🔧 Coding Practice Takeaways
#
#1. **Array Creation & Comparison**
#
#   * Practice converting Python lists into NumPy arrays using `np.array`, and compare operations (like addition, multiplication) to list behavior—observe vectorized efficiency.
#
#2. **Vectorized Computation & Speed Test**
#
#   * Benchmark operations on arrays vs. pure Python lists. Focus on dot products and element-wise operations. Implement mini speed tests using `%timeit` to experience performance gains.
#
#3. **Multi-Dimensional Arrays**
#
#   * Create 2D arrays and index them: slicing, boolean indexing, and fancy indexing. Try tasks like extracting rows/columns or selecting elements meeting conditions.
#
#4. **Reshaping & Concatenation**
#
#   * Use methods like `.reshape()`, `np.concatenate`, `vstack`, and `hstack` to manipulate array shapes. Build exercises like stacking feature vectors or reshaping flattened data.
#
#5. **Broadcasting Exercises**
#
#   * Experiment with broadcasting by performing arithmetic between arrays of different shapes. For example, add a column vector to a 2D array to shift features.
#
#6. **Axis-Based Functions**
#
#   * Use functions like `np.sum`, `np.mean`, `np.max` along different axes. Try aggregations across rows vs. columns and replicating this behavior manually.
#
#7. **Random Array Generation**
#
#   * Generate data using `np.random.rand`, `randn`, or `randint`. Practice sampling distributions and setting seeds for reproducibility (`np.random.seed()`).
#
#8. **Linear Algebra with NumPy**
#
#   * Solve systems using `np.linalg.solve`, compute eigenvalues with `np.linalg.eig`, and experiment with matrix inversion and determinant computation.
#
#9. **File I/O with CSV Files**
#
#   * Load and save CSVs using `np.loadtxt` and `np.savetxt`. Parse data, handle delimiters, and integrate with Pandas for combined workflows if needed.
#
#---
#
### 📘 Imp Theory Concepts
#
#* **Why NumPy over Lists:**
#  Discusses how NumPy arrays are stored in contiguous memory and processed in C, leading to huge performance gains (vectorization vs. Python loops).
#
#* **Dimensionality & Shape:**
#  The concept of `ndarray` and its `shape` property, plus the importance of understanding dimensions and their alignment in operations.
#
#* **Copy vs. View:**
#  Highlights how slicing often creates views, not copies. Changing a view can modify the original array. Use `.copy()` to prevent unintended side-effects.
#
#* **Broadcasting Rules:**
#  Explains NumPy’s algorithm: aligning trailing dimensions, compatible shapes, and implicit replication—critical for high-dimensional data operations.
#
#* **Data Types (`dtype`):**
#  Covers `int64`, `float32`, etc., and their impact on memory usage and numerical precision. Good practice: explicitly define `dtype` when generating arrays.
#
#* **Axis Semantics:**
#  Understanding axes (e.g., axis=0 for rows, axis=1 for columns) is essential for correctly aggregating or transforming data in machine learning pipelines.
#
#* **Stochastic Data with Random:**
#  Data generation methods and the significance of reproducible results (via `seed`) in experiments and training ML models.
#
#---
#
### 🧩 How to Integrate into Your Practice
#
#| Concept          | Practice Task                                               |
#| ---------------- | ----------------------------------------------------------- |
#| Array operations | Implement array-based linear regression or vector norms.    |
#| Broadcasting     | Normalize each feature in a dataset with broadcasting.      |
#| Linear algebra   | Use `linalg.solve` for parameter estimation in equations.   |
#| CSV I/O          | Import real-world datasets and apply NumPy transformations. |


import numpy as np
print(np.__version__)

a = np.array([1, 2, 3]) #list to array conversion
print(a)
print(a.shape) #shape of the array
print(a.dtype) #data type of the array
print(a.ndim) #number of dimensions
print(a.size) #number of elements in the array
print(a.itemsize) #size of each element in bytes
print(a.nbytes) #total bytes consumed by the array

print(a[0]) #accessing the first element
a[0] = 10 #modifying the first element
print(a) #printing the modified array
print(a + 5) #adding 5 to each element
print(a[1:3]) #slicing the array
print(a[-1]) #accessing the last element
print(a[1:]) #slicing from the second element to the end
print(a[:2]) #slicing from the start to the second element

b=a*np.array([2,0,2]) #element-wise multiplication
print(b) #printing the result of element-wise multiplication

#diff between list and array
l= [1, 2, 3]
a=np.array(l)

l.append(4) #appending to list
#or 
l= l + [4] #appending to list
l=l*2 #repeating the list
a = np.append(a, 4) #appending to array
a = a * 2 #repeating the array
print(l)
print(a)

a=np.sqrt(a) #square root of each element in the array
print(a)

#dot product
l1 = [1, 2, 3]
l2 = [4, 5, 6]
dot=0
for i in range(len(l1)):
    dot += l1[i] * l2[i]  # calculating dot product manually
print(dot)  # printing the dot product calculated manually

##or using numpy
a1 = np.array(l1)
a2 = np.array(l2)
dot_product = np.dot(a1, a2)  # dot product of two arrays
print(dot_product)  # printing the dot product
dot=np.sum(a1 * a2)  # another way to calculate dot product
print(dot)  # printing the dot product calculated using sum
dot=a1@a2  # using @ operator for dot product
print(dot)  # printing the dot product using @ operator


import numpy as np
from timeit import default_timer as timer

# speed test
a = np.random.randn(1000)
b = np.random.randn(1000)

A=list(a)
B=list(b)

T=1000

def dot1():
    dot =0
    for i in range(len(A)):
        dot += A[i] * B[i]
        return dot
def dot2():
    return np.dot(a, b)

start=timer()
for i in range(T):
    dot1()
end=timer()
t1 = end - start

start=timer()
for i in range(T):
    dot2()
end=timer()
t2 = end - start

print('list calculation', t1)
print('np.dot',t2)
print('ratio', t1/t2)

c=np.array([[1,2],[3,4]]) #creating a 2D array
print(c)
print(c.shape) #shape of the 2D array
print(c[0])

print(np.linalg.inv(c)) #inverse of a matrix
print(np.diag(c)) #diagonal elements of a matrix

bool_idx=c>2
print(bool_idx) #boolean indexing
print(c[bool_idx]) #selecting elements greater than 2

z=np.array([10,20,30,40,50])
print(z)
y=np.array([1,2,3])
print(z[y])

even=np.argwhere(z%2==0).flatten()  # finding indices of even elements
print(a[even])  # printing indices of even elements

w=np.arange(1, 7)  # creating an array with a step of 2
print(w)  # printing the array with a step of 2
print(w.shape)  # printing the shape of the array with a step of 2
p=w.reshape([2,3])
print(p)  # printing the reshaped array
p=w.reshape([3,2])
print(p)  # printing the reshaped array

f=np.array([[1,2],[4,5]])
print(f)
g=np.array([[3,4],[6,7]])
print(g)
h=np.concatenate((f,g.T), axis=1)  # concatenating arrays along axis 1
print(h)  # printing the concatenated array along axis 1

j=np.array([1,2,3,4])
k=np.array([5,6,7,8])
#hstack , vstack
v=np.vstack((j,k))  # stacking arrays vertically
print(v)  # printing the vertically stacked array
h=np.hstack((j,k))  # stacking arrays horizontally
print(h)  # printing the horizontally stacked array

d=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(d)
print(d.sum(axis=0))  # summing along axis 0 (columns)
print(d.sum(axis=1))  # summing along axis 1 (rows)
print(d.mean(axis=0))  # mean along axis 0 (columns)
print(a.min(axis=0))  # minimum along axis 0 (columns)  
print(a.max(axis=0))  # maximum along axis 1 (rows)
print(d.std(axis=None))  # standard deviation along axis 0 (columns)


#generating arrays 
e=np.zeros((2,3))  # creating an array of zeros with shape (2,3)
print(e)  # printing the array of zeros
f=np.ones((2,3))  # creating an array of ones with shape (2,3)
print(f)  # printing the array of ones

e=np.full((2,3), 5.0)  # creating an array filled with 5s with shape (2,3)
print(e)  # printing the array filled with 5s
f=np.eye(3)  # creating an identity matrix of size 3
print(f)  # printing the identity matrix

e=np.arange(20)
print(e)  # printing the array with values from 0 to 19
e=np.linspace(0, 10, 5)  # creating an array with 5 evenly spaced values between 0 and 10
print(e)  # printing the array with evenly spaced values

#random arrays
a=np.random.rand(2,3)  # creating a random array with shape (2,3)
print(a)  # printing the random array

a=np.random.randn(1000)  # creating a random array with 1000 elements from a normal distribution
print(a)  # printing the random array from a normal distribution

a=np.random.randint(0, 10, (2,3))  # creating a random array with shape (2,3) with values between 0 and 10
print(a)  # printing the random array with values between 0 and 10

a=np.random.choice(5,size=10)  # creating a random array with 10 elements chosen from the range 0 to 5
print(a)  # printing the random array with elements chosen from the range 0 to 5

#numpy in ml
a=np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)  # calculating eigenvalues and eigenvectors
print("Eigenvalues:", eigenvalues)  # printing the eigenvalues
print("Eigenvectors:", eigenvectors)  # printing the eigenvectors