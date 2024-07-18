
# array is a collection of elements of the same type. 
# The elements of an array are stored in contiguous memory locations.
# The array elements can be accessed using an index.
# The index of the first element in the array is 0, the index of the second element is 1, and so on.
# The elements of the array can be accessed using the subscript operator [].
# The subscript operator [] is also called an index operator.


from array import *

array1 = array('i', [10, 20, 30, 40, 50])

for x in array1:
    print(x)

print(array1[0])
print(array1[-1])
 
    # Type codes for array elements in Python
    # Type code	C Type	Python Type	Minimum size in bytes
    # 'b'	        signed char	int	1
    # 'B'	        unsigned char	int	1
    # 'u'	        Py_UNICODE	Unicode character	2
    # 'h'	        signed short	int	2
    # 'H'	        unsigned short	int	2
    # 'i'	        signed int	int	2
    # 'I'	        unsigned int	int	2
    # 'l'	        signed long	int	4
    # 'L'	        unsigned long	int	4
    # 'q'	        signed long long	int	8
    # 'Q'	        unsigned long long	int	8
    # 'f'	        float	float	4
    # 'd'	        double	float	8

