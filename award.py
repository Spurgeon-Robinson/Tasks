# get inputs on time to complete Tri
swim_time = int(input("How many minutes did it take you to complete your swim?:"))
ride_time = int(input("How many minutes did it take you to complete your ride?: "))
run_time = int(input("how many minutes did it take you to complete your run?: "))
# add times together, output total time for Tri
print(f"Total time taken for the triathlon: {swim_time+ride_time+run_time}")
# print what award you get based on time
if swim_time+ride_time+run_time <= 100:
    print("Award: Provincial colours")
elif swim_time+ride_time+run_time >=111:
    print("No award")
elif swim_time+ride_time+run_time >= 106: 
    print("Award: Provincial scroll")
elif swim_time+ride_time+run_time >=101:
    print("Award: Provincial half colours")