class BubbleSort:
    def __init__(self, items_to_sort):
        self.items = items_to_sort
        self.sorted_items=[]
        for i in range(len(items_to_sort)-1,0,-1):
            a = 0
            for j in range(i):
                if items_to_sort[j] > items_to_sort[j+1]:
                    a = items_to_sort[j]
                    items_to_sort[j] = items_to_sort[j+1]
                    items_to_sort[j+1] = a
        self.sorted_items = items_to_sort   

       ### your implementation for bubble sort goes here 

    def get_sorted(self,):
        return self.sorted_items


                
                    
### your implementation for bubble sort goes here
solution = BubbleSort([16,586,1,31,354,43,3])
solution.__init__([16,586,1,31,354,43,3])
tiem = solution.get_sorted()
           
print(tiem)

