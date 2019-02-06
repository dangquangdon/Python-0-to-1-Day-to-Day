
# Introduction to NumPy

**Numpy stands for Numerical Python**
- Use for Quantitative Analysis
- It should be installed with Python, if you do not have it for some reason, run ```pip install numpy```
- Numpy is use for fast data generation and handling


## NumPy Arrays
- Numpy arrays is being used a lot in data analysis and visualization
- Numpy arrays has two kinds:
    - Vectors : a one dimensional array, basically it's like a list
    - Matrixes: two dimensional array


```python
import numpy as np
```


```python
# Create numpy array
list1 = [1,2,3,4]
arr_1 = np.array(list1)
arr_1
```




    array([1, 2, 3, 4])




```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
arr_2 = np.array(matrix)
arr_2
# Numpy can understand automatically this is a two dimensional array (maxtrix)
# If there are two square brackets, it's two dimentions

```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])



### Built-in methods to generate arrays


```python
#built-in range() of python
list(range(1,10))
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
# numpy version
np.arange(1,10)
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
# with steps
np.arange(1,10,2)
```




    array([1, 3, 5, 7, 9])




```python
# Quickly create a numpy array filled with 0s
np.zeros(3)
```




    array([0., 0., 0.])




```python
np.zeros(4)
```




    array([0., 0., 0., 0.])




```python
# To create a two dimensional 
np.zeros((3,3))
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
np.zeros((3,6))
```




    array([[0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0.]])




```python
# Similar to np.zeros, np.ones fills the array with 1s
np.ones((2,6))
```




    array([[1., 1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1., 1.]])




```python
np.ones(5)
```




    array([1., 1., 1., 1., 1.])




```python
# linspace take into the first argument as a start, and the second as a stop
# The third one is to specify how many numbers in between the start and the stop
# The distance between numbers are equal
np.linspace(0, 10, 20)
```




    array([ 0.        ,  0.52631579,  1.05263158,  1.57894737,  2.10526316,
            2.63157895,  3.15789474,  3.68421053,  4.21052632,  4.73684211,
            5.26315789,  5.78947368,  6.31578947,  6.84210526,  7.36842105,
            7.89473684,  8.42105263,  8.94736842,  9.47368421, 10.        ])




```python
# Identity matric (square matrix) is the one that has the same number of rows and colums
# the diagonal is 1s and the rest is 0s
np.eye(4)
```




    array([[1., 0., 0., 0.],
           [0., 1., 0., 0.],
           [0., 0., 1., 0.],
           [0., 0., 0., 1.]])




```python
np.eye(6)
```




    array([[1., 0., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0., 0.],
           [0., 0., 1., 0., 0., 0.],
           [0., 0., 0., 1., 0., 0.],
           [0., 0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 0., 1.]])



### Numpy Random modules


```python
# np.random + Tab to see all available module
# generate an array with a given shape, and fill it with 
# a random value between 0 and 1, all of the values has
# equal chances of being generated
np.random.rand(2)
```




    array([0.242888  , 0.84048197])




```python
np.random.rand(3,4)
```




    array([[0.91237886, 0.42909773, 0.88808083, 0.73705348],
           [0.39383563, 0.05622965, 0.65677902, 0.77912483],
           [0.5240108 , 0.93614157, 0.51035479, 0.33074298]])




```python
# same like random.rand but the values are in standard distribution
# mean is 0 and variance is 1
np.random.randn(3)
```




    array([-0.44942016,  1.14866351, -0.92087012])



#### Standard distribution
Standard distribution looks like this, where the mean is 0 and the closer to 0 the higher possibility of being picked
![normaldist.gif](attachment:normaldist.gif)


```python
np.random.randn(3,5)
```




    array([[-1.58000227,  1.39279769, -1.00034973,  0.62200105,  0.44349476],
           [-0.03758117, -0.55609952,  0.83439426, -0.99640164, -0.7802519 ],
           [-0.96589199, -0.33405863,  0.63787802,  1.30925298,  1.03782796]])




```python
# Random integer from low to high
np.random.randint(1,20)
```




    2




```python
np.random.randint(1,100, 10)
```




    array([17, 21, 71, 42, 39, 12, 58, 36,  3, 67])




```python
# Reshape an array
arr = np.arange(10)
```


```python
arr.reshape(2,5)
```




    array([[0, 1, 2, 3, 4],
           [5, 6, 7, 8, 9]])




```python
arr.shape
```




    (10,)




```python
rand_arr = np.random.randint(1,30,10)
```


```python
rand_arr
```




    array([14, 19,  7, 16, 23, 17, 25, 10, 16, 22])




```python
reshape_arr = rand_arr.reshape(2,5)
reshape_arr
```




    array([[14, 19,  7, 16, 23],
           [17, 25, 10, 16, 22]])




```python
# return a max, min element
print(reshape_arr.max())
print(reshape_arr.min())
```

    25
    7



```python
# return the index of max element
reshape_arr.argmax()
```




    6




```python
reshape_arr.argmin(axis=1)
```




    array([2, 2])



## NumPy Operations

We can have a lot of mathematic operations with numpy, sin, cos, tag, cotag, exp, logarit, ...


```python
arr2 = np.arange(0, 20)
arr3 = np.arange(0,10)
```


```python
arr2
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])




```python
# Arithmetic
# It will be element by element
arrith_arr = arr2 + arr2
arrith_arr
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
           34, 36, 38])




```python
arrit_arr2 = arr2*arr2
arrit_arr2
```




    array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121, 144,
           169, 196, 225, 256, 289, 324, 361])




```python
arr_22 =  arr2.reshape(4,5)
```


```python
arr_22 * arr_22
```




    array([[  0,   1,   4,   9,  16],
           [ 25,  36,  49,  64,  81],
           [100, 121, 144, 169, 196],
           [225, 256, 289, 324, 361]])



## NumPy Indexing and Selection

- For a flat array, the indexing and slicing is the same as for lists


```python
arr_ind = np.arange(0, 20)
```


```python
arr_ind[2]
```




    2




```python
arr_ind2 = arr_ind.reshape(4,5)
arr_ind2
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])




```python
arr_ind2[2,3]
```




    13




```python
arr_ind2[:2,3:]
```




    array([[3, 4],
           [8, 9]])



**Broadcasting is not applicable for normal python lists**


```python
arr_ind[1:5]
```




    array([1, 2, 3, 4])




```python
arr_ind[1:5] = 100
arr_ind
```




    array([  0, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10,  11,  12,
            13,  14,  15,  16,  17,  18,  19])




```python
arr_ind[6:10] = [200,300,400,500]
```


```python
arr_ind
```




    array([  0, 100, 100, 100, 100,   5, 200, 300, 400, 500,  10,  11,  12,
            13,  14,  15,  16,  17,  18,  19])



**Conditional selection**


```python
cond_arr = np.arange(1,20)
cond_arr
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19])




```python
cond_arr[cond_arr > 5]
```




    array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])




```python
cond_arr[cond_arr > 5]
```




    array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])



**Exercise in the Exercise notebook**


```python

```
