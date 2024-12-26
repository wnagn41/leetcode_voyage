class SelectionSort:
    def __init__(self, items_to_sort):
        self.items = items_to_sort
        self.sorted_items=1*len(items_to_sort)
        for i in range(0,len(items_to_sort)):
            max = i
            for j in range(i,len(items_to_sort)):
                # print(i,j)
                if items_to_sort[j] < items_to_sort[max]:
                    max = j
                
            items_to_sort[max],items_to_sort[i] = items_to_sort[i],items_to_sort[max]
            
            # print("/n")
        
        self.sorted_items = items_to_sort   
        # return(sorted_items)       ### your implementation for selection sort goes here 

    def get_sorted(self,):
        return self.sorted_items

                
                    
### your implementation for bubble sort goes here


solution = SelectionSort([16,586,1,31,354,43,3])
solution.__init__([37, 77, 0, 80, 78, 97, 87, 81, 20, 40, 76, 100, 67, 66, 18, 77, 78, 36, 41, 60, 86, 96, 67, 41, 51, 10, 12, 41, 80, 71, 89, 22, 1, 55, 9, 34, 24, 52, 21, 94, 47, 5, 44, 86, 41, 9, 21, 34, 35, 59, 40, 24, 31, 84, 50, 21, 82, 37, 69, 77, 76, 73, 91, 63, 26, 92, 11, 19, 43, 27, 97, 62, 19, 97, 76]
)
tiem = solution.get_sorted()
           
print(tiem)

