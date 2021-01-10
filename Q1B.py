avg_weight = int(input("Enter the average weight: "))
sum_weight = int(input("Enter the sum of known weight: "))

total_missed_weight =  ( 10 * avg_weight) - (sum_weight)
avg = total_missed_weight / 3

print("Weight of the fish that was not recorded:", round(avg,2)) 
