S="0123456789"
print(S[2:8:1]) #234567
print(S[2:8:-1]) #empty output 
#print(S[2:8:0])# slice step value cannot be 0
print(S[-1:-6:-1])#98765
print(S[2:-5:1])#234
print(S[1:6:-2])#empty string
print(S[0:-5:-5])#empty	


s='0123456789'
print(s[0:7:1]) #0123456
print(s[0:7:2]) #0246
print(s[0:7]) #0123456 because by default step value is 1
print(s[0:]) #0123456789
print(s[::]) #0123456789 default begin value is 0
print(s[::-1])# 9876543210  reverse value
