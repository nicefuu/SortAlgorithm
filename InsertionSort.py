class InsertionSort:
    def insertion_sort(self, arr):
        """
        :param arr:list[int]
        :return: list[int]
        """
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j] = arr[j - 1] + arr[j]
                    arr[j - 1] = arr[j] - arr[j - 1]
                    arr[j] = arr[j] - arr[j - 1]
        return arr


so = InsertionSort()
a = [10, 9, 8, 7, 6, 5, 3, 2, 1]
print(so.insertion_sort(a))
