def generate_combinations(nums, k):
    def backtrack(start, combination):
        if len(combination) == k:  # 종료 조건
            result.append(combination[:]) # 종료조건에 맞는 결과 값을 result변수에 넣는다.
            return

        for i in range(start, len(nums)):# 가지치기 why? 범위를 start - n까지로 정하고 반복시킴으로 중복가능성을 배재했다?
            
            combination.append(nums[i])  # 선택
            print(f'start: {start}, i: {i}, combination: {combination}, nums[i]{nums[i]}')
            backtrack(i + 1, combination)  # 다음 선택으로 이동
            combination.pop()  # 선택 취소

    result = []
    backtrack(0, [])
    return result

# 실행 예시
nums = [1, 2, 3]
k = 2
print(generate_combinations(nums, k))  # 출력: [[1, 2], [1, 3], [2, 3]]