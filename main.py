from scipy import stats     # stats and graphing module
import numpy as np      # data manipulation and management module


# questions and answers
# as well as a setup for the attempts and score list to sub in for x and y
Qs = np.array([
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
    "Q8",
    "Q9",
    "Q10"
])
As = np.array([
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "A10"
])
attempts = np.array([1])
scores = np.array([(len(Qs)+1)/2])


# plots a linear line of best fit based on the distance, std div and variance of the data
# then uses that line to predict results
def predict_out_linear(factor, x, y):
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    return slope * factor + intercept


# basically the same as its linear counterpart
# but uses a polynomial equation for the line instead of a linear ax + by = c
def predict_out_polynomial(factor, x, y):
    out = np.poly1d(np.polyfit(x, y, 3))
    return out(factor)


# quiz iterates through the answer list
# and uses the question list as an input prompt
def quiz(questions, answers):
    result = 0
    for av, bv in zip(questions, answers):
        if input(av) == bv:
            result += 1
    return result


# standardises predictions to a set min and max
def standard(lower, upper, v):
    if v > upper:
        return upper
    elif v < lower:
        return lower
    else:
        return v


# program start
while True:
    selection = input("""
would you like to:
take the quiz (type quiz):
predict your score on the quiz using a linear model (type predict lin):
predict your score on the quiz using a polynomial model (type predict poly)
type here: """)

    # adds the score to the list of scores
    # adds another attempt onto the attempt list
    # outputs score
    if selection == "quiz":
        score = quiz(Qs, As)
        scores = np.append(scores, score)
        if len(attempts) > 0:
            attempts = np.append(attempts, attempts[len(attempts) - 1] + 1)
        print(f"you got {score} out of {len(Qs)} correct")

    # outputs the linear prediction function subbing score for y and attempts for x
    # using the next attempt as its factor
    elif selection == "predict lin":
        lin = int(predict_out_linear(attempts[len(attempts) - 1] + 1, attempts, scores))
        print(standard(0, len(Qs), lin))

    # same as linear but for the polynomial prediction
    elif selection == "predict poly":
        poly = int(predict_out_polynomial(attempts[len(attempts) - 1] + 1, attempts, scores))
        print(standard(0, len(Qs), poly))
