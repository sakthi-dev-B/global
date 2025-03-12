# importing packages 
import tensorflow as tf 
# creating two tensors 
matrix = tf.constant([[1, 2], [3, 4]]) 
matrix1 = tf.constant([[2, 4], [6, 8]]) 
# addition of two matrices 
print(matrix+matrix1) 
 # importing packages 
import tensorflow as tf 
# create a vector 
vector1 = tf.constant([10, 10]) 
vector2 = tf.constant([20, 20]) 
# checking the dimensions of vector 
print(vector1+vector2) 
 x = [1, 2, 3, 4, 5] 
y = 1 
 tf.add(x, y) 
 x = tf.convert_to_tensor([1, 2, 3, 4, 5]) 
 y = tf.convert_to_tensor(1) 
x + y 
x = [1, 2, 3, 4, 5] 
y = tf.constant([1, 2, 3, 4, 5]) 
tf.add(x, y) 
x = tf.constant([1, 2], dtype=tf.int8) 
y = [2**7 + 1, 2**7 + 2] 
tf.add(x, y) 
 import numpy as np 
x = np.ones(6).reshape(1, 2, 1, 3) 
y = np.ones(6).reshape(2, 1, 3, 1) 
tf.add(x, y).shape.as_list()