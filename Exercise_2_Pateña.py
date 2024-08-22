
input_grades=int(input("Enter your grades for validation: "))

if input_grades >= 75:
 print('passed!')
  
elif input_grades == 74:
    print('Remedial')
    
elif input_grades < 74 and input_grades >=0 :
    print('failed')

else:
    print('You entered an invalid input!')


      
    
