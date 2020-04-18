class QuickSort:
    def quick_sort(self, arr):
        """
        :param arr:list{int]
        :return: list[int]
        """
        if not arr or len(arr) <= 1:
            return arr

        def qs(arr, left, right):
            if left >= right:
                return
            i, j = left, right
            key = arr[left]
            while 1:
                while arr[i] < key:
                    i += 1
                    if i == right:
                        break
                while arr[j] > key:
                    j -= 1
                    if j == left:
                        break
                if i >= j:
                    break
                swap(arr, i, j)
            qs(arr, left, i)
            qs(arr, i + 1, right)

        def swap(arr, i, j):
            arr[i] ^= arr[j]
            arr[j] ^= arr[i]
            arr[i] ^= arr[j]

        qs(arr, 0, len(arr) - 1)
        return arr


s = QuickSort()
arr = [7, 3, 9, 5, 4, 10, 1]
print(s.quick_sort(arr))
