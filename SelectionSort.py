class SelectionSort:
    def selection_sort(self, arr):
        """
        :param arr:list[int]
        :return: list[int]
        """
        for i in range(len(arr) - 1):
            min_index=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index=j
            if i!=min_index:
                arr[i]=arr[i]+arr[min_index]
                arr[min_index]=arr[i]-arr[min_index]
                arr[i]=arr[i]-arr[min_index]
        return arr
so = SelectionSort()
a=[7,5,4,3,7,5,5,7,8,8,9,9]
print(so.selection_sort(a))

