def net_payment(N, K):
    fair_share = N // (K + 1)  # Calculate fair share, rounded down
    amount_paid_back = K * fair_share  # Total amount paid back by friends
    net_payment = N - amount_paid_back  # Net amount you paid
    return net_payment


T = int(input())  # Read the number of test cases
for _ in range(T):
    N, K = map(int, input().split())  # Read the bill amount and number of friends
    result = net_payment(N, K)
    print(result)  # Print the net payment

