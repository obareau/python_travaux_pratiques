
o_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print (o_list[0 : 2])   #! [10, 20]
print (o_list[:3])      #! [10, 20, 30]

print (o_list[-1])      #! 90
print (o_list[2:])

print (o_list[::2]) # take every elements with a step of 2
print (o_list[1::2]) # take every 2 step beginig at pos 1

print (o_list[::-1]) # reverse !!!!

print (o_list[-2::-1]) # reverse  from  end -1
       
print (o_list[-2:1:-1]) #! [80, 70, 60, 50, 40, 30]

