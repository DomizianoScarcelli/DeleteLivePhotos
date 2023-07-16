import os

def delete(path):
    count = 0
    for filename in os.listdir(path):
        for filenameDup in os.listdir(path):
            if filename.endswith('.MOV') and not filenameDup.endswith(".MOV") and filename.split('.')[0] == filenameDup.split('.')[0]:
                location = os.path.join(path, filename)
                if os.path.exists(location):
                    print(filename)
                    count += 1
                    os.remove(location)
    print('Removed {} files'.format(count))
       


directory = input('Insert the absolute path of the directory where the photos are: \n')
delete(directory)
input('Press a key to continue')
