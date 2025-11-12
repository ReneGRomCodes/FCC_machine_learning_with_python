# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago.
# It is not a very good player so you will need to change the code to pass the challenge.
import random

"""Original function."""
#def player(prev_play, opponent_history=[]):
#    opponent_history.append(prev_play)

#    guess = "R"
#    if len(opponent_history) > 2:
#        guess = opponent_history[-2]

#    return guess


"""Work in Progress function."""
def player(prev_play, opp_hist_list=[], opp_hist_markov={}):
    guess = ""
    opp_hist_list.append(prev_play)

    # Perform Markov analysis to map patterns in opponents plays.
    depth = 2

    if len(opp_hist_list) > depth:
        last_chain = tuple(opp_hist_list[-(depth+1):-1])
        last_play = opp_hist_list[-1]

        if last_chain not in opp_hist_markov:
            opp_hist_markov[last_chain] = [last_play]
        else:
            opp_hist_markov[last_chain].append(last_play)

        prediction = max(opp_hist_markov[last_chain], key=opp_hist_markov[last_chain].count)
    else:
        prediction = random.choice(("R", "P", "S"))

    # Choose 'guess' to counter predicted play.
    if prediction == "R":
        guess = "P"
    elif prediction == "P":
        guess = "S"
    elif prediction == "S":
        guess = "R"

    return guess
