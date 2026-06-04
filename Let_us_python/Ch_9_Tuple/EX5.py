n = int(input("Enter the number of Shares: "))

portfolio = []

for i in range(n):
    print(f"share no.{i+1}")

    name = input("name of the share: ")
    date = input("Enter the date of purchase(yyyy mm dd): ")
    cost = float(input("Enter the cost of per share: ")) 
    num_shares = int(input("enter the number of shares: "))
    selling_price = float(input("Enter the selling price share: "))

    portfolio.append((name,date,cost,num_shares,selling_price))

    total_cost = int(0)
    total_selling = int(0)

    for share in portfolio:
        total_cost += share[2]*share[3]
        total_selling += share[4]*share[3]

        gain_loss= total_selling - total_cost
        percentage=(gain_loss/total_cost)*100

        print("\n--------------------Portflio Summary----------------------")
        print("Total cost of portfolio = ",total_cost)
        print("Total selling value = ",total_selling)

        if gain_loss>0:
            print("Total Gain: ",abs(gain_loss))
        elif gain_loss<0:
            print("Total loss: ",abs(gain_loss))
        else:
            print("No loss No gain")

