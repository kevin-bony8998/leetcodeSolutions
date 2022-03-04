class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1,1]
        currRows = 2
        oldRow = [1, 1]
        newRow = []
        while currRows < numRows:
            newRow = []
            newRow.append(oldRow[0])
            for idx in range(len(oldRow) - 1):
                first = oldRow[idx]
                second = oldRow[idx + 1]
                total = first + second
                newRow.append(total)
            newRow.append(oldRow[-1])
            oldRow = newRow.copy()
            currRows += 1
        return newRow