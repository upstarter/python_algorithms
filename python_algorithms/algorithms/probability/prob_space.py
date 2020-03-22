# A probability space consists of a sample space of possible outcomes and a
# probability measure which specifies how to assign probabilities to related
# events.

# The first step in creating a probability space is to define a function that
# explains how to draw one outcome.

# Example. Probability of drawing cards from a 52-card standard deck.

# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (float(event_outcomes) / float(sample_space)) * 100
    print(probability)
    return round(probability, 1)


# Sample Space
cards = 52

# Determine the probability of drawing a heart
hearts = 13
heart_probability = event_probability(hearts, cards)

# Determine the probability of drawing a face card
face_cards = 12
face_card_probability = event_probability(face_cards, cards)

# Determine the probability of drawing the queen of hearts
queen_of_hearts = 1
queen_of_hearts_probability = event_probability(queen_of_hearts, cards)

# Print each probability
print(str(heart_probability) + "%")
print(str(face_card_probability) + "%")
print(str(queen_of_hearts_probability) + "%")
