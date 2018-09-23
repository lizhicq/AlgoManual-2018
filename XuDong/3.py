### Solution 3 

import pandas as pd
class FileChecker(object):
    
    def __init__(self, file):
        self.df = pd.read_csv(file, sep="|")
        
    def check1(self):
        '''
        Check if file column num is constant 
        '''
        return any(self.df.isnull())
    
    def check2(self, num):
        '''
        Check if file col num is num
        '''
        return self.df.shape[1] == num
    
    def check3(self, num=100):
        '''
        Check if file row num is greater num
        '''
        return self.df.shape[0] > num
    
    def check4(self, num):
        '''
        Check if file row num is num
        '''
        return self.df.shape[1] == num
    
    def check5(self, col_num, string):
        '''
        Check if a column contains string
        '''
        return any(self.df.iloc[:,col_num-1].str.contains(string))
    
    
    def check6(self, col_num=1, string='SSE'):
        '''
        Check if a column not contains string
        '''
        return not any(self.df.iloc[:,col_num-1].str.contains(string))
    
    def check7(self, col_num, value):
        '''
        Check if a column has some value
        '''
        s = self.df.iloc[:,col_num-1]
        return len(s[s == value]) > 0 
    
    
    def check7(self, col_num, a, b):
        '''
        Check if a column is in range(a,b)
        '''
        s = self.df.iloc[:,col_num-1]
        return len(s[s>a][s<b]) > 0 
    
    
if __name__ == "__main__":
    from sys import argv

    sample = list(map(str, range(1,7)))
    for v in argv[1:]:
        if v not in sample:
            print ('Please check input, only, support 1 ~ 6 check')

    s = FileChecker('3.quotes.txt')
    check = {'1':s.check1, 
             '2':s.check2,
             '3':s.check3,
             '4':s.check4,
             '5':s.check5,
             '6':s.check6,}
    
    flag = True
    for v in argv[1:]:
        if check[v]():
            flag = False
            break
    
    print(flag)
        

