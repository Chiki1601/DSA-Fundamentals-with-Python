#tower of hanoi

def TowerofHanoi(n, from_rod, to_rod , aux_rod):
    if n == 1:
        print("Move Dsik 1 from rod", from_rod,"to rod",to_rod)
        return
    TowerofHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerofHanoi(n - 1, aux_rod, to_rod, from_rod)
    
    
n = int(input("Enter the number: "))
TowerofHanoi(n,"A","C","B")
