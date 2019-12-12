# Given an Integer (Non-Negative) as N, Generate the first N pascal's triangle
# Do you know Pascal's Triangle? if don't know, please see https://ja.wikipedia.org/wiki/%E3%83%91%E3%82%B9%E3%82%AB%E3%83%AB%E3%81%AE%E4%B8%89%E8%A7%92%E5%BD%A2

def pascals_triangle(n):
    Pas = []
    for i in range(n):
        Cal = []
        for j in range(i+1):
            if j==0 or j==i:
                Cal.append(1)
            else:
                Cal.append(Pas[i-1][j-1]+Pas[i-1][j])
        Pas.append(Cal)
    
    return Pas
