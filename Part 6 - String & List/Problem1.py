def compare(A, B):
    a = len(A)
    b =len(B)
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    max_len = 0
    end_index = 0
    
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i 
    if max_len == 0:
        return ""
    else:
        start_index = end_index - max_len
        return A[start_index:end_index]

# Example usage:
print(compare("AKA", "AKASHI"))      
print(compare("KANGOORO", "KANG"))   
print(compare("KI", "KIJANG"))
print(compare("KUPU-KUPU", "KUPU"))
print(compare("ILALANG", "ILA"))