# English Scoring Function
import random

def english_rally(p_server, r):
    # Return whether the server won the rally
    win_rally = False

    if (r < p_server):
        win_rally = True
    else:
        win_rally = False

    return win_rally

def check_score_is_eight(score, player):
    if (score == 8):
        return player
    else:
        return None

def get_new_win_score(server, player_to_eight_first, pa):
    pb = 1 - pa
    pass

def english_game(ra, rb, server = "a"):
    pa = ra / (ra + rb)

    win_score = 9
    a_score = 0
    b_score = 0
    # Stores the most recent player to get to a score of eight
    got_to_eight = None
    print("b")

    while (a_score < win_score) and (b_score < win_score):
        r = random.random()

        if (server == "a"):
            if (english_rally(pa, r)):
                #print("a1:", a_score)
                a_score += 1
                #print("a2:", a_score)
                got_to_eight = check_score_is_eight(a_score, "a")
            else:
                server = "b"
        else:
            if (english_rally(1 - pa, r)):
                b_score += 1
                got_to_eight = check_score_is_eight(b_score, "b")
            else:
                server = "a"

        if (a_score == 8 and b_score == 8):
            # As got_to_eight stores the most recent player
            # the other player must be the one who got to eight first
            if (got_to_eight == "b"):
                got_to_eight = "a"
            else:
                got_to_eight = "b"

            # Decide whether to play to 9 or 10
            win_score = 10 #get_new_win_score(server, got_to_eight, pa)

    return [a_score, b_score]


print(english_game(60, 40))