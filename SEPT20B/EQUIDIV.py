# Quesition Link :  https://www.codechef.com/SEPT20A/problems/EQDIV
# My Solution : https://www.codechef.com/viewsolution/37728115
# My profile : https://www.codechef.com/users/navdeep_15

import math
# cook your dish her
k=int(input())
for t in range(int(input())):
    n=int(input())
    if k==1:
        if(n%4==1 or n%4==2):
            print(1)
        else:
            print(0)
        ts=(n*(n+1))//4
        s=['0']*n
        sum=0
        for i in range(n,0,-1):
            if sum+i<=ts:
                s[i-1]="1"
                sum+=i
            else:
                s[ts-sum-1]="1"
                break
        s=''.join(x for x in s)
        print(s)
    if k==2:
        ts=(n*(n+1)*(2*n+1))//6
        a=[int(x**2) for x in range(1,n+1)]
        s=["1", "01", "001", "0001", "10001", "001001", "1101001", "01101001", "001101001", "0100100101", "01000111010", "000000001101", "0001000010011"]
        if n<6:
            sum1=ts
            sum2=0
            minx=ts
            x=y=c=0
            for i in range(n-1,-1,-1):
                    x=sum1-a[i]
                    y=sum2+a[i]
                    if abs(x-y)<minx:
                        sum1-=a[i]
                        sum2+=a[i]
                        minx=abs(x-y)
            print(min(abs(sum1-sum2),minx))
        elif n==6:
            print(1)
        else:
            if n%4==3 or n%4==0:
                print(0)
            elif n%4==1 or n%4==2:
                print(1)
        c=0
        while(n>13):
            n-=8
            c+=1
        s2=''.join(x for x in s[n-1])
        s2+=''.join(x for x in s[7]*c)
        print(s2)
    if k==3:
        s=["1","01","001","0001","00001","010001","1110001","11001001","100101001","1111111010","00001101001","001011100110","0000111011010","01011001101001","001111010111100","0110100110010110","10010110111110010","010011010101011010","1100110110100111100","01011111110111111000","110101100000000101101","0001000111111101111000","01110000010000001000111","101011110110111110111000","0001111011111111111110000","01111111001101111111101000","011101101111111011111110000"]
        a=[1,7,18,28,25,7,26,4,5,1,12]
        if(n<12):
            print(a[n-1])
        else:
            if n%4==3 or n%4==0:
                print(0)
            elif n%4==1 or n%4==2:
                print(1)
        c=0
        while(n>27):
            n-=16
            c+=1
        s2=''.join(x for x in s[n-1])
        s2+=''.join(x for x in s[15]*c)
        print(s2)
    if k==4:
        s=["1","01","001","0001","00001","000001","0000001","00101110","000001110","0101001001","00000101001","001101010110","0010110101001","00000001111010","011110001010110","0000111000001110","00101000011111100","000000110100001110","1000010010110111100","00001010110111011100","000000000100100100011","1101001111011111110100","00001000100110111101100","000010011110110111110100","0101110101111110111111000","00010100000100010000110101","001111000000011110111111000","0001011111000101111011111000","01010100010001011111010101010","010110010011011011111111011000","1111111111110100000010000101011","01101001100101101001011001101001","111111111101110101000011110101010","1111101111111011111010101111100010","11111111110101010011110100101101010","111111111111011110000100000101000111","1111111110101111111111101001101000101","11111111111111010001100001010110010101","111111111111111001010100010111010100110","1111111111111101010110100001000101000111","11111111111111110001010101100100010111010","111111111111111111101101111111111001101000","1111111111111111010000010000000001111001110","11111111111111111000001001010001010011010101","111111111111111111101011011111111001101100100","1111111111111111110001100000010000010111010101","11111111111111111101010100100001000101010110110","111111111111111111011101000100010101100110010101","1111111111111111111101010101000001110100010111010","11111111111111111111111111111111101101010011100100","111111111111111111110001010111000111010101010101001","1111111111111111111101010000001000010101011001000111","11111111111111111111111111111110001101011010100101001","111111111111111111111101000110000001001101010101010101","1111111111111111111111010100110101110100110101010101010","00000001000001000011110111111111011111111111111110000000","010001011101010111010111110111111111011111111111110000000","0010111101100111110111111111111111111111111011111110000000","00000101000100010111010111111111111111111111101111110000000","000100010101010000110101111111111111111111111111011110000000","1110100011011010101010110010111100111110011011111011011010000"]
        a=[1,15,64,158,271,317,126,34,253,13,92,30,47,31,2,0,1,13,0,0,9,1,0,0,1,5,0,0,5]
        if(n<30):
            print(a[n-1])
        else:
            if n%4==3 or n%4==0:
                print(0)
            elif n%4==1 or n%4==2:
                print(1)
        c=0
        while(n>61):
            n-=32
            c+=1
        s2=''.join(x for x in s[n-1])
        s2+=''.join(x for x in s[31]*c)
        print(s2)
