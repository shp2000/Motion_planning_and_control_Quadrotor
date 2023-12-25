import numpy as np

def Ab_i1(i, n, d, dt_i, w_i, w_ip1):
  '''
  Ab_i1(i, n, d, dt_i, w_i, w_ip1) computes the linear equality constraint
  constants that require the ith polynomial to meet waypoints w_i and w_{i+1}
  at it's endpoints.
  Parameters:
     i - index of the polynomial.
     n - total number of polynomials.
     d - the number of terms in each polynomial.
     dt_i - Delta t_i, duration of the ith polynomial.
     w_i - waypoint at the start of the ith polynomial.
     w_ip1 - w_{i+1}, waypoint at the end of the ith polynomial.
  Outputs
     A_i1 - A matrix from linear equality constraint A_i1 v = b_i1
     b_i1 - b vector from linear equality constraint A_i1 v = b_i1
  '''
    
  A_i1 = np.zeros((4, 2*d*n))
  b_i1 = np.zeros((4, 1))

# TODO: fill in values for A_i1 and b_i1
# for j in range(n):
#     for k in range(d):
#         if(j==i and k==0):
#             A_i1[i][j] = w_i

  A_i1[0, 2*i * d] = 1
  A_i1[2, 1+ 2*i * d] = 1
  b_i1[0,0] = w_i[0]
  b_i1[1,0] = w_ip1[0]
  A_i1[1, 2*i*d:2*d*(i+1):2] = np.array([dt_i**(k) for k in range(d)])
  A_i1[3, 1+2*i*d:1+2*d*(i+1):2] = np.array([dt_i**(k) for k in range(d)])

# Constraint 2: The ith polynomial must end at w_ip1 (γ_i(Δt_i) = w_ip1)
#   for k in range(d):
#       A_i1[1, 2*i * d + k] = (dt_i ** k)
#       A_i1[3, 1+2*i * d + k] = (dt_i ** k)
  print(w_ip1)
  b_i1[2,0] = w_i[1]
  b_i1[3,0] = w_ip1[1]


# for k in range(2, 4):
#     A_i1[k, i * d] = np.math.factorial(k) / np.math.factorial(k - 2) * (dt_i ** (k - 2))
#     A_i1[k, (i + 1) * d] = -np.math.factorial(k) / np.math.factorial(k - 2)


  return A_i1, b_i1