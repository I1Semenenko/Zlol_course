from collections import defaultdict

logfile = open("LogFile.txt") # Open file with logs
ip_list = defaultdict(int)	
url_list = defaultdict(int)

# Add ip and url to dict and count them
for i in logfile:
    ip_list[i.split(" ")[0]] += 1
    url_list[i.split(" ")[8]] += 1
    

# Sort dictionary function
def print_sorted(dict):
    sorted_ = {k: v for k, v in sorted(dict.items(), reverse = True, key=lambda item: item[1])}
    for item in sorted_:
        print(f" {item} used {sorted_[item]} time(s)")

print_sorted(ip_list)
print()
print_sorted(url_list)