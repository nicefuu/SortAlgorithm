
class BubbleSort:
    def bubble_sort(self,arr):
        """
        :param arr:list[int]
        :return: list[int]
        """
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j]=arr[j+1]+arr[j]
                    arr[j+1]=arr[j]-arr[j+1]
                    arr[j]=arr[j]-arr[j+1]
        return arr
so = BubbleSort()
a=[7,5,4,3,7,5,5,7,8,8,9,9]
print(so.bubble_sort(a))