# takes in a price without GST, calcutate GST, and adds it to the
def calc_gst(net_price):
    return net_price * 1.15

# Main routine
net_price_ = float(input("Enter the net price $"))
print(f"${calc_gst(net_price_):.2f}")
