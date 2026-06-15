class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i, result = 0, []
        for i in range(len(operations)):
            cur = operations[i]
            if cur not in ["+", "D", "C"]:
                result.append(int(cur))

            elif cur == '+':
                sums = result[-1] + result[-2]
                result.append(sums)

            elif (cur == 'C'):
                result.pop()
            
            elif (cur == 'D'):
                product = result[-1] * 2
                result.append(product)
        
        return sum(result)
        