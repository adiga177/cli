def main_cli():
    #k1 encryption string k2 decryption string
    k1 ,k2 ="" , ""
    while True:
        new_cmd = input('prompt>')
        if new_cmd == "done":
            break
        elif new_cmd != "":
            promtcomnd=new_cmd.split(' ')
            if promtcomnd[0] == "newkey":
                print("Enter k1:")
                k1 = input('k1>')
                print("Enter k2:")
                k2 = input('k2>')
            elif promtcomnd[0] == "load":
                if len(promtcomnd)==2:
                    k1, k2=load_key_file(promtcomnd[1])
                else:
                    print("missing file name to load")
            elif promtcomnd[0] == "save":
                if len(promtcomnd)==2:
                    save_key_file(promtcomnd[1],k1,k2)
                else: 
                    print("missing file name to save")
            elif promtcomnd[0] == "info":
                print_info(promtcomnd[0],k1,k2)
            elif promtcomnd[0] == "enc":
                if len(promtcomnd)==3:
                    encryption_file(promtcomnd[1],promtcomnd[2],k1,k2)
                else: 
                    print("missing file source or destination")
            elif promtcomnd[0] == "dec":
                if len(promtcomnd)==3:
                    decryption_file(promtcomnd[1],promtcomnd[2],k1,k2)
                else: 
                    print("missing file source or destination")
            elif promtcomnd[0] == "k1":
                print(k1)
            elif promtcomnd[0] == "k2":
                print(k2)

def decryption_file(decfile,fileclear,k1,k2):
    try:
        f= open(decfile, 'r')
    except OSError:
        print ("Could not open/read file:")
    else:
        Lines = f.read()
        temp=""
        Lines= Lines.upper()
        for x in Lines:
            for y in x:
                if k2.find(y) != -1:
                    temp+=k1[k2.find(y)]
                else: 
                    temp+=y
        print(temp)
        try:        
            f=open(fileclear, 'w')
        except OSError:
            print ("Could not open/read file:")
        else:    
            f.write(temp) 
            f.close()    

def encryption_file(fileclear,encfile,k1,k2):
    try:        
        f= open(fileclear, 'r')
    except OSError:
        print ("Could not open/read file:")
    else:
        Lines = f.readlines()
        temp=""
        for x in Lines:
            for y in x: 
                if k1.find(y) != -1:
                    temp+=k2[k1.find(y)]
                else: 
                    temp+=y
        print(temp)
        try:
            f=open(encfile, 'w')
        except OSError:
            print("Could not open/read file:")
        else:
            f.write(temp)
            f.close()     

def save_key_file(Fname,key1,key2):
    try:
        f=open(Fname, 'w')
    except OSError:
        print ("Could not open/read file:")  
    else:  
        f.write(key1)
        f.write('\n')
        f.write(key2)

def load_key_file(Fname):
    try:
        f= open(Fname, 'r')
    except OSError:
        print ("Could not load file")   
        return "" ,""
    else:
        Lines = f.readlines()
        k1=Lines[0]
        k2=Lines[1]
        f.close()
        return k1 ,k2
    
def print_info(Fname,key1,key2):
    print('Current key: ' + Fname)
    print('Clear: \n' + key1)
    print('Encryption: \n' + key2)

main_cli()
