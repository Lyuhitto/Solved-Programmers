import re


def solution(dartResult):
    score = re.findall(r'\d+[SDT][*#]?', dartResult)
    score_arr = []
    for idx, val in enumerate(score):
        num = int(re.findall(r'\d+', val)[-1])
        if 'S' in val:
            score_arr.append(num)
        elif 'D' in val:
            score_arr.append(num**2)
        elif 'T' in val:
            score_arr.append(num**3)
        if '*' in val:
            if idx == 0:
                score_arr[idx] *= 2
            else:
                score_arr[idx] *= 2
                score_arr[idx - 1] *= 2
        if '#' in val:
            score_arr[idx] *= -1
    answer = sum(score_arr)
    return answer
