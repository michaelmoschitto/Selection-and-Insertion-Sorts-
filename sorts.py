import random
import time

def selection_sort(list):
    if list is None:
        raise IndexError('cannnot sort empty list')
    comps = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            comps += 1
            if list[j] < list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return comps
        
    
def insertion_sort(list):
    comparisons = 0
    for i in range(1,len(list)):
        min_val = list[i]
        j = i
        while j > 0:
            if min_val < list[j-1]:
                comparisons += 1
                list[j] = list[j-1]
        
                list[j-1] = min_val
                j=j-1
            else:    
                comparisons+=1
                break
          
    return comparisons        





   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    nums = int(input('how many random numbers would you like to generate?'))
    randoms = random.sample(range(1000000), nums)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, str(stop_time - start_time) + ' seconds')
    
    # randoms2 = random.sample(range(1000000), 16000)
    # start_time2 = time.time() 
    # comps2 = selection_sort(randoms2)
    # stop_time2 = time.time()
    # print(comps2, str(stop_time2 - start_time2) + ' seconds')

if __name__ == '__main__': 
    main()

