import visdom
import matplotlib.pyplot as plt

from project.datasets import Simple, Split, Xor

# Visdom demo
#  vis = visdom.Visdom()

#  # Loss goes down!
#  plt.plot([2.0, 1.0, 0.0], c="blue")
#  plt.title("Model Loss")
#
#  # Send to visdom
#  vis.matplot(plt, win="loss")

# Task 0.5
N = 100

# Dataset: Simple
Simple(N, vis=True).graph("Simple")

# Dataset: Split


def classify_simple(pt):
    "Classify based on x position"
    if pt[0] < 0.2 or pt[0] > 0.8:
        return 1.0
    else:
        return 0.0


Split(N, vis=True).graph("Split", model=classify_simple)

# Dataset: XOR


def classify_xor(pt):
    "Classify based on x and y postion"
    if pt[0] < 0.5 and pt[1] < 0.5:
        return 0.0
    elif pt[0] > 0.5 and pt[1] > 0.5:
        return 0.0
    else:
        return 1.0


Xor(N, vis=True).graph("XOR", model=classify_xor)
