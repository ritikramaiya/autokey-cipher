
import sys
import os

# Encrypting/decrypting function
def encrypt(inputfile,outputfile,key,en):
    if not os.path.exists(inputfile):
        print("Input file does not exist!!!")
    else:
        ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        fin=open(inputfile,"r")
        fout=open(outputfile,"w")
        s=fin.readline()
        note=""
        # For encryption
        newk=key+s
        new_k=newk[0:len(s)]
        for i in range(0,len(s)):
            
            a=s[i]
            b=new_k[i]
            for k in range(len(ll)):
                if ll[k]==a:
                    si=k
                    break
            for j in range(len(ll)):
                if ll[j]==b:
                    ki=j
                    break
        
        
            v= (si + ki)%26
            for m in range(len(ll)):
                if m==v:
                    ciph=ll[m]
                    break
            note+=ciph
        

        fout.write(note)
        fin.close()
        fout.close()


def decrypt(inputfile,outputfile,key,en):
   if not os.path.exists(inputfile):
       print("Input file does not exist!!!")
   else:
       ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
       fin=open(inputfile,"r")
       fout=open(outputfile,"w")
       s=fin.readline()
       note=""
       for i in range(len(s)):
           c=s[i]
           ki=0
           k=key[i]
           for j in range(len(ll)):
               if c==ll[j]:
                   ci=j
                   break
           for kpp in range(len(ll)):
               if k==ll[kpp]:
                   ki=kpp
                   break
           v=(ci-ki)%26
           for m in range(len(ll)):
               if m==v:
                   pt=ll[m]
                   break
           note+=pt
           key+=pt
       
       fout.write(note)
       fin.close()
       fout.close()


def main():
    # Checking command line arguments if not 5, direct user
    if len(sys.argv)!=5:
        print("Invalid number of arguments")
        print("Usage: auto.py <inputfile> <outputfile> <key> <1/0>")
        print("1: encryption")
        print("0: decryption")
    # If command line arguments are 5, proceed with 1/0
    else:
        inputfile=sys.argv[1]       # Allocating index of the input file
        outputfile=sys.argv[2]       # Allocating index of the output file
        key=sys.argv[3]              # Allocating index of the key
        en=int(sys.argv[4])         # Allocating index of the action (either 1 or 0)
        if en==1:
            
            encrypt(inputfile,outputfile,key,en)
        else:
            decrypt(inputfile,outputfile,key,en)

if __name__=="__main__":
    main()