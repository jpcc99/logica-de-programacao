votes = [int(i) for i in input("").split(",")]
total_of_votes = len(votes)
votes_per_canditate = [0] * 6


def calc_percentage_of(votes, total):
    return int((votes * 100) / total)


for vote in votes:
    votes_per_canditate[vote - 1] += 1


c1 = calc_percentage_of(votes_per_canditate[0], total_of_votes)
c2 = calc_percentage_of(votes_per_canditate[1], total_of_votes)
c3 = calc_percentage_of(votes_per_canditate[2], total_of_votes)
c4 = calc_percentage_of(votes_per_canditate[3], total_of_votes)
null_votes = calc_percentage_of(votes_per_canditate[4], total_of_votes)
blank_votes = calc_percentage_of(votes_per_canditate[5], total_of_votes)


print(f"VOTOS = {total_of_votes}")
print(f"C#1 = {c1}%")
print(f"C#2 = {c2}%")
print(f"C#3 = {c3}%")
print(f"C#4 = {c4}%")
print(f"NULOS = {null_votes}%")
print(f"BRANCOS = {blank_votes}%")
