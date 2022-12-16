import os
import csv

path = "/Users/christineyang/Desktop/challenge3/python-challenge/PyPoll/Resources/election_data.csv"
total = 0
c = 0 
d = 0
r = 0
c_name = "Charles Casper Stockham"
d_name = "Diana DeGette" 
r_name = "Raymon Anthony Doane"
candidate = []

print("Election Results")
print("-------------------------")
with open(path, "r") as open_file :
    reader = csv.reader(open_file, delimiter=",")
    header = next(reader)
    
    for row in reader:
        total += 1
        candidate.append(row[2])
        if row[2] == c_name:
            c += 1
        elif row[2] == d_name:
            d += 1
        else:
            r += 1
    
    c_percentage = round(c / total * 100, 3)
    d_percentage = round(d / total * 100, 3)
    r_percentage = round(r / total * 100, 3)
    
    
    print(f"Total Votes: {total}")
    print("-------------------------")
    print(f"{c_name}: {c_percentage}% ({c})")
    print(f"{d_name}: {d_percentage}% ({d})")
    print(f"{r_name}: {r_percentage}% ({r})")
    print("-------------------------")
    
    if c_percentage > d_percentage and c_percentage > r_percentage:
        a = f"Winner: {c_name}"
        print(f"Winner: {c_name}")
    elif d_percentage > c_percentage and d_percentage > r_percentage:
        a = f"Winner: {d_name}"
        print(f"Winner: {d_name}")

    elif r_percentage > c_percentage and r_percentage > d_percentage:
        a = f"Winner: {r_name}"
        print(f"Winner: {r_name}")
    
    print("-------------------------")


analysis = "/Users/christineyang/Desktop/challenge3/python-challenge/PyPoll/analysis"
path2 = os.path.join(analysis, "PyPoll.txt")
with open(path2, "w") as f:
    lines = ["Election Results","-------------------------",f"Total Votes: {total}",
    "-------------------------", f"{c_name}: {c_percentage}% ({c})",
    f"{d_name}: {d_percentage}% ({d})",f"{r_name}: {r_percentage}% ({r})",
    "-------------------------", a, "-------------------------"]
    
    f.write("\n".join(lines))
    f.close()






