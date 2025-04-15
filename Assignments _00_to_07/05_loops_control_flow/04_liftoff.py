# Yeh question keh raha hai ke aik spaceship launch hone wali hai, 
# aur uske liye tumhein aik countdown program banana hai jo 10 se lekar 1 tak numbers print kare, aur uske baad "Liftoff!" likhe.

def main():
    for i in range(10,0,-1):
        print(i,end=' ')
    print("Liftoff!")

if __name__ == '__main__':
    main()