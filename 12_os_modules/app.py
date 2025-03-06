import os 

# os.makedirs('data')
#? if we create a any file or folder using os modules make sure to rape it into conditional statement bcz if you run the programme again it is giving you a duplicate error example given below
if(not os.path.exists('data')):
    os.makedirs('data')


#? for creating a multiple files in any folder
# for i in range(0,100):
#     os.mkdir(f'data/Day{i+1}')

#? for renaming file we can use this function


# for i in range(0,100):
#     os.rename(f'data/Day{i+1}', f'data/tutorial{i + 1}')
    
#? for checking number of folder
folders = os.listdir('data')
# print(folder)


# for folder in folders:
#     print(folder)
#     #* for checking file is exist or not
#     print(os.listdir(f'data/{folder}'))
 
 
#! for checking any folder is found or not

# for folder in folders:
#     print(folder)
#     # print(os.listdir(f'data/{folder}'))
#     if(os.path.exists(f'data/{folder}/readme.md')):
#         print(f'folder is found in {folder} ')
#         break
#     else:
#         print('file is not found')
#     #* for checking file is exist or not
    


#? for checking current working director 
# print(f'it is my current working directory {os.getcwd()}') 
# print(f'it is my changing working directory ') 
# os.chdir('/Users')
# os.getcwd()
