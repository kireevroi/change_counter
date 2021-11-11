#Change counter v 0.1

#Coin values, in cents

COIN_VALUES = [1, 5, 10, 25]

#change counting function
def count_change(change):
    return_dict = {}
    sorted_values = COIN_VALUES
    sorted_values.sort(reverse = True)
    whole_change = int()
    for i in sorted_values:
        whole_change = change//i
        return_dict[str(i)+' cents'] = whole_change
        change -= i*(whole_change)
    return return_dict

#testing the result
print(count_change(130))
