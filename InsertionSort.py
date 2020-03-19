class InsertionSort:
    def insertion_sort(self, arr):
        """
        :param arr:list[int]
        :return: list[int]
        """

        def swap(i, j):
            return j,i

        for i in range(0, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j],arr[j-1]=swap(arr[j], arr[j - 1])
        return arr

so = InsertionSort()
a = [10, 7, 8, 7, 6, 5, 3, 2, 1]
print(so.insertion_sort(a))
