import numpy as np

def calculate(list):
    """
    Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean,
    variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

    The input of the function should be a list containing 9 digits. The function should convert 
    the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, 
    standard deviation, max, min, and sum along both axes and for the flattened matrix.

    The returned dictionary should follow this format:

    {
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
    }

    If a list containing less than 9 elements is passed into the function, it should raise a ValueError
    exception with the message: "List must contain nine numbers." The values in the returned dictionary
    should be lists and not Numpy arrays.

    For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

    {
    'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
    'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
    'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
    'max': [[6, 7, 8], [2, 5, 8], 8],
    'min': [[0, 1, 2], [0, 3, 6], 0],
    'sum': [[9, 12, 15], [3, 12, 21], 36]
    }
    """
    calculations = {}   #Create a placeholder for final result
    
    if len(list) != 9:  #Check if the list contains 9 elements
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3,3)   #Reshape the list into a 3x3 array
    arr_flat = np.array(list)   #Flattened array
    
    #Calculate the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
    calculations['mean'] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr_flat.mean()]
    calculations['variance'] = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr_flat.var()]
    calculations['standard deviation'] = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr_flat.std()]
    calculations['max'] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr_flat.max()]
    calculations['min'] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr_flat.min()]
    calculations['sum'] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr_flat.sum()]

    return calculations
