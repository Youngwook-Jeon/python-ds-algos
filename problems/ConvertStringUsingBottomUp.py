# s1 문자열을 s2 로 바꾸기 위한 최소한의 연산 횟수 구하기
# 연산은 delete, insert, replace 만 허용됨
def findMinOperationBU(s1, s2, tempDict):
    # TODO
    for i in range(len(s1) + 1):
        key = str(i) + "0"
        tempDict[key] = i
    for i in range(len(s2) + 1):
        key = "0" + str(i)
        tempDict[key] = i
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                key = str(i) + str(j)
                prev_key = str(i - 1) + str(j - 1)
                tempDict[key] = tempDict[prev_key]
            else:
                key = str(i) + str(j)
                prev_s1_to_s2 = str(i - 1) + str(j)
                s1_to_prev_s2 = str(i) + str(j - 1)
                prev_s1_to_prev_2 = str(i - 1) + str(j - 1)
                tempDict[key] = 1 + min(tempDict[prev_s1_to_s2], min(tempDict[s1_to_prev_s2], tempDict[prev_s1_to_prev_2]))
    final_key = str(len(s1)) + str(len(s2))
    return tempDict[final_key]