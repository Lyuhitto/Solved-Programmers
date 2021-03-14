import re


def solution(dartResult):
    answer = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    score = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    print(score)
    for idx, val in enumerate(score):
        if val[2] == '*' and idx > 0:
            answer[idx - 1] *= 2
        answer.append(int(val[0]) ** bonus[val[1]] * option[val[2]])
    return sum(answer)
