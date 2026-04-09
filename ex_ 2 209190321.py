
''' Exercise #2. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_even_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            sum = sum + digit
        n = n//10
    return sum
#########################################
# Question 2 - do not delete this comment
#########################################
def mult_residuals_of_k(lst, k):
    res2 = 1.0
    for i in range(len(lst)):
        if type(lst[i]) == float or type(lst[i]) == int:
            if lst[i] % k != 0:
                res2 = res2 * (lst[i] % k)
    return res2
#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    if c not in s:
        return 0
    counter = 1
    max_counter = 0
    prev= ''
    for curr in s:
        if curr.lower() == c.lower():
            if curr.lower() == prev.lower():
                counter = counter + 1
        else:
            counter = 1
        if counter > max_counter:
            max_counter = counter
        prev = curr
    return max_counter

#########################################
# Question 4.a - do not delete this comment
#########################################
def dict_residuals_of_k(lst, k):
    dict = {}
    for i in range(len(lst)):
        if type(lst[i]) == float or type(lst[i]) == int:
            dict[lst[i]] = (lst[i] % k)
    return dict
#########################################
# Question 4.b - do not delete this comment
#########################################
def mult_residuals_of_k_with_dict(lst, k):
    res4 = 1.0
    dict = dict_residuals_of_k(lst, k)
    for s in dict:
        if s % 2 == 0:
            if dict[s] != 0:
                res4 = res4 * dict[s]
    return res4
#########################################
# Question 5.a - do not delete this comment
#########################################
def dict_longest_repetition(s):
    dict = {}
    for c in s:
     #if c not in s:
     #       return 0
        counter = 1
        max_counter = 0
        prev = ''
        for curr in s:
            if curr.lower() == c.lower():
                if curr.lower() == prev.lower():
                    counter = counter + 1
                else:
                    counter = 1
            if counter > max_counter:
                max_counter = counter
            prev = curr
            dict[c.lower()] = (max_counter)
    return dict
#########################################
# Question 5.b - do not delete this comment
#########################################
def count_longest_repetition_with_dict(s,c):
    dict = dict_longest_repetition(s)
    if c not in s:
        return 0
    return dict[c]

#########################################
# Question 5.c - do not delete this comment
#########################################    
def find_longest_repetitions_with_dict(d):
    lst1 = list(d.keys())
    lst2 = list(d.values())
    a = max(lst2)
    b = lst2.index(a)
    return lst1[b]
#########################################
# Question 6.a - do not delete this comment
#########################################
def find_substring_locations(s, k):
    dict = {}

    for i in range(len(s)-1):
        sub = s[i:(i+k)]
        if sub in dict.keys():
            dict[sub].append(i)
        else:
            dict[sub] = [i]
    return dict
#########################################
# Question 6.b - do not delete this comment
#########################################
def count_substring_locations(substr_dict):
    for key,value in substr_dict.items():
        substr_dict[key] = len(value)

#########################################
# Question 7 - do not delete this comment
#########################################
def mult_mat_by_scalar(mat, alpha):
    mat_new = []
    mat_lst = []
    for i in mat:
        for j in i:
            num = alpha * j
            mat_lst.append(num)
        mat_new.append(mat_lst)
        mat_lst = []
    return mat_new
#########################################
# Question 8 - do not delete this comment
#########################################
def mat_transpose(mat):
    new_mat = []
    mat_lst = []
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            num = mat[j][i]
            mat_lst.append(num)
        new_mat.append(mat_lst)
        mat_lst = []
    return new_mat
#########################################
# Question 9.a - do not delete this comment
#########################################
def mat_transpose_sparse(m):
    dict = {}
    for key in m.keys():
        trans = key[-1::-1]
        dict[trans] = m.get(key, 0)
    return dict


#########################################
# Question 9.b - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    dict = lst.pop(0)
    dict_final = dict
    for i in lst:
        for key in i.keys():
            dict_final[key] = dict.get(key,0) - i.get(key,0)
            if dict_final[key] == 0:
                dict_final.remove(key)
    return dict_final
    
#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == '__main__':  # Do not delete this line!

    print("### Q1 ###")
    print(sum_even_digits(5638) == 14)
    print(sum_even_digits(137) == 0)
    print(sum_even_digits(54984127) == 18)
    print(sum_even_digits(6) == 6)

    print("### Q2 ###")
    print(mult_residuals_of_k([3, 6, 4, "hello", 11, 9], 3) == 2.0 )
    print(mult_residuals_of_k([45.5, 60, "3", 74, 48], 4) == 3.0)


    print("### Q3 ###")
    print(count_longest_repetition('eabbAaaacccaaddd', 'a') == 4)
    print(count_longest_repetition('cccccc','c') == 6)
    print(count_longest_repetition('abcdee', 'z') == 0)
    print(count_longest_repetition('', 'z') == 0)


    print("### Q4.a ###")
    print(dict_residuals_of_k([3, 6, 4, "hello", 11, 9], 3)=={3: 0, 6: 0, 4: 1, 11: 2, 9: 0})
    print(dict_residuals_of_k([45.5, 60, "3", 74, 50], 4)=={45.5: 1.5, 60: 0, 74: 2, 50: 2})

    print("### Q4.b ###")
    print(mult_residuals_of_k_with_dict([3, 6, 4, "hello", 11, 9], 3)==1)
    print(mult_residuals_of_k_with_dict([45.5, 60, "2", 74, 50], 4)==4)    

    print("### Q5.a ###")
    d1=dict_longest_repetition('eabbAaaacccaaddd')
    print(d1=={'e': 1, 'a': 4, 'b': 2, 'c': 3, 'd': 3})
    d2=dict_longest_repetition('cccccc')
    print(d2=={'c': 6})
    d3=dict_longest_repetition('abcdee')
    print(d3=={'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2})

    print("### Q5.b ###")
    print(count_longest_repetition_with_dict('eabbAaaacccaaddd', 'a') == 4)
    print(count_longest_repetition_with_dict('cccccc','c') == 6)
    print(count_longest_repetition_with_dict('abcdee', 'z') == 0)

    print("### Q5.c ###")
    print(find_longest_repetitions_with_dict(d1) == 'a')
    print(find_longest_repetitions_with_dict(d2) == 'c')
    print(find_longest_repetitions_with_dict(d3) == 'e')

    print("### Q6.a ###")
    expected_6a={'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]}
    result_6a=find_substring_locations('TTAATTAGGGGCGC', 2)
    print(expected_6a == result_6a)

    print("### Q6.b ###")
    input_6b=expected_6a.copy()
    expected_6b={'TT': 2, 'TA': 2, 'AA': 1, 'AT': 1, 'AG': 1, 'GG': 3, 'GC': 2, 'CG': 1}
    count_substring_locations(input_6b)
    print(input_6b==expected_6b)
    
    
    print("### Q7 ###")
    mat1 = [[2, 5], [6, 9]]
    mat2 = mult_mat_by_scalar(mat1, 2)
    print(mat1 == [[2, 5], [6, 9]])
    print(mat2 == [[4, 10], [12, 18]])

    print(mult_mat_by_scalar([[10,15], [-3,6]], -5) == [[-50, -75], [15, -30]])
    

    print("### Q8 ###")
    mat = [[1,2],[3,4],[5,6]]
    mat_T = mat_transpose(mat)
    print(mat == [[1, 2], [3, 4], [5, 6]])
    print(mat_T == [[1, 3, 5], [2, 4, 6]])

    mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    mat2_T = mat_transpose(mat2)
    print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])


    print("### Q9.a ###")
    print(mat_transpose_sparse({(2,9):2, (3,4):4})=={(9, 2): 2, (4, 3): 4})

    print("### Q9.b ###")
    print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})
    print(diff_sparse_matrices(([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6, (9, 10): 7}, {(2, 7): 0.5, (4, 2): 10}])) == {(1, 3): -4, (2, 7): 0.5, (9, 10): -7, (4,2): -10})

# ============================== END OF FILE =================================
