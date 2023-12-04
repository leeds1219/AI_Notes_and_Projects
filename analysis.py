# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2a():
    """
      Prefer the close exit (+1), risking the cliff (-10).
    """
    answerDiscount = 0.5 # low discounting for close exit
    answerNoise = 0 # 
    answerLivingReward = -2 # negative living reward to encourages short path
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# python gridworld.py -g DiscountGrid -a value --discount [YOUR_DISCOUNT] --noise [YOUR_NOISE] --livingReward [YOUR_LIVING_REWARD]

def question2b():
    """
      Prefer the close exit (+1), but avoiding the cliff (-10).
    """
    answerDiscount = 0.2 # low discount to avoid +10
    answerNoise = 0.2 # nosie to avoid close cliff
    answerLivingReward = -1 # negative for close exit
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2c():
    """
      Prefer the distant exit (+10), risking the cliff (-10).
    """
    answerDiscount = 0.99 # high 
    answerNoise = 0 # 
    answerLivingReward = -0.1 # negative but low
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2d():
    """
      Prefer the distant exit (+10), avoiding the cliff (-10).
    """
    answerDiscount = 0.99 # high 
    answerNoise = 0.1 # 
    answerLivingReward = -0.1 # negative
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2e():
    """
      Avoid both exits and the cliff (so an episode should never terminate).
    """
    answerDiscount = 0.99 # high discount for future
    answerNoise = 0.0 # noise possible
    answerLivingReward = 1 # not negative or 0 for livining
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
