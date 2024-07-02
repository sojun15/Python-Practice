loop_count = 1
while loop_count <= 5:
    loop_count+=1
    email = input('Enter an email address:')
    #check first character is small letter or not
    if(not(email[0]>='a' and email[0]<='z')):
        print('wrong!,please enter valid email address')
    else:
        #check the length of string is less than six or not
        if(len(email)<6):
            print('wrong!,please enter valid email address')
        else:
            #check number of @, dot, space and sequence of @ and dot
            if((email.count('@')!=1) or (email.count('.')!=1) or (email.count(' ')>0) or (email.find('@')>email.find('.'))):
                print('wrong!,please enter valid email address')
            else:
                #check all the character are small letter or not except dot and @
                count_letter = 0
                for x in email:
                    if((x>='a' and x<='z') or (x>='0' and x<='9')):
                        count_letter = count_letter + 1
                if(count_letter!=(len(email)-2)):
                    print('wrong!,please enter valid email address')
                else:
                    print("your email is corrct.")
                    break