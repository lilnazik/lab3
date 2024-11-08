
def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0
    
    for i in range(n):
        term = y_points[i]
        
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
                
        result += term
        
    return result

def sum_s(x):
    sum_i = 0
    for i in x:
        sum_i += i
    return sum_i

def linear_regression(x, y):
    n = len(x)
    
    m = (n * sum_s(x * y) - sum_s(x) * sum_s(y)) / (n * sum_s(x**2) - sum_s(x)**2)
    b = (sum_s(y) - m * sum_s(x)) / n
    
    return m, b