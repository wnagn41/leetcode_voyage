class InsertionSort:
    def __init__(self, items_to_sort):
        self.items = items_to_sort
        self.sorted_items=[]
        for i in range(1, len(items_to_sort)):
            key = items_to_sort[i]
            j = i - 1
            while j >= 0 and key < items_to_sort[j]:
                items_to_sort[j + 1] = items_to_sort[j]
                j -= 1
            items_to_sort[j + 1] = key
        self.sorted_items = items_to_sort  

       ### your implementation for insertion sort goes here 

    def get_sorted(self,):
        return self.sorted_items


                
### Insertion sort experiment code goes here

solution = InsertionSort([67, 83, 22, 91, 62, 87, 12, 6, 52, 65, 30, 81, 70, 52, 73, 24, 30, 91, 97, 53, 42, 42, 85, 66, 57, 20, 12, 69, 45, 61, 100, 34, 84, 10, 73, 16, 73, 44, 43, 31, 55, 13, 27, 15, 65, 92, 51, 33, 57, 26, 54, 52, 98, 91, 12, 60, 21, 87, 37, 80, 62, 39, 100, 94, 32, 51, 7, 20, 77, 8, 9, 14, 10, 36, 93]
)
solution.__init__([1, 83, 22, 91, 62, 87, 12, 6, 52, 65, 30, 81, 70, 52, 73, 24, 30, 91, 97, 53, 42, 42, 85, 66, 57, 20, 12, 69, 45, 61, 100, 34, 84, 10, 73, 16, 73, 44, 43, 31, 55, 13, 27, 15, 65, 92, 51, 33, 57, 26, 54, 52, 98, 91, 12, 60, 21, 87, 37, 80, 62, 39, 100, 94, 32, 51, 7, 20, 77, 8, 9, 14, 10, 36, 93]
)
tiem = solution.get_sorted()
           
print(tiem)