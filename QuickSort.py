class QuickSort:
    def quick_sort(self,arr):
        """
        :param arr:list{int]
        :return: list[int]
        """
        if len(arr)<=1:
            return arr
        elif len(arr)==2:
            if arr[0]<=arr[1]:
                return arr
            else:
                return arr[::-1]
        def f(a,left,right):
            base=left
            

