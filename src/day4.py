#!/usr/bin/python3

print("hello day 4")

txt = "../data/day4.txt"

sum=0

def update(score):
  if score==0:
    return 1
  else:
    return 2*score

with open(txt) as f:
  grid = f.readlines()


cards=0
winners_total=0
ours_total=0
for line in grid:
  cards+=1
  print(f"line: {line}")
  score = 0
  winners = line.strip().split("|")[0].split()[2:]
  wset = set()
  
  for w in winners:
    wset.add(int(w))
  ours = line.strip().split("|")[1].split()
  print(f"winners: {wset}, ours: {ours}")
  for o in ours:
    if int(o) in wset:
      score = update(score)
  print(f"\tadding {score}")
  winners_total+=len(wset)
  ours_total+=len(ours)
  sum+=score 

print(f"Processed {cards} cards")
print(f"Winners total: {winners_total}, Ours total: {ours_total}")

print(f"Sum: {sum}\nGoodbye")






