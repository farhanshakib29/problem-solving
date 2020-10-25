# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

n_leaderboard = 0
a_leaderboard = []
a_leaderboard_clean = []

n_alice = 0
a_alice = []

last_pos = -1

def input_leaderboard():
    global n_leaderboard
    global a_leaderboard
    global a_leaderboard_clean
    global last_pos

    n_leaderboard = int(input())
    a_leaderboard[0:n_leaderboard] = input().split()

    prev = ''
    for rank in a_leaderboard:
        if rank == prev:
            continue
        
        prev = rank
        rank = int(rank)
        a_leaderboard_clean.append(rank)

    last_pos = len(a_leaderboard_clean)-1

def input_alice():
    global n_alice
    global a_alice
    
    n_alice = int(input())
    a_alice[0:n_alice] = map(int, input().split())

def get_rank(alice_score):
    global a_leaderboard_clean
    global last_pos
    
    for i in range(last_pos, -1, -1):
        last_pos = i
        if alice_score < a_leaderboard_clean[i]:
            print(i+2)
            return
        elif alice_score == a_leaderboard_clean[i]:
            print(i+1)
            return
        else:
            if i > 0:
                continue
            print(i+1)
            return

input_leaderboard()
input_alice()
for alice_score in a_alice:
    get_rank(alice_score)