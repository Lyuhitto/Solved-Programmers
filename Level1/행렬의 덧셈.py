def solution(arr1, arr2):
    answer = [[x + y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer


'''
두 리스트의 길이가 같으므로
zip()을 이용하면 편리하게 해결할 수 있다
단, 2차원 함수를 다루므로 for을 두번 써야한다
또한 zip()은 zip 오브젝트를 리턴하므로
리스트로 다시 바꿔줘야 한다
'''
