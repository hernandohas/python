import random
from p5 import *

class Perceptron:
    weights = []
    l_constant = 0.01

    def __init__(self, weights):
        self.weights = [random.uniform(-1, 1) for weight in range(weights)]

    def feed_forward(self, inputs = []):
        sum = 0
        for index, value in enumerate(self.weights):
            sum += inputs[index] * self.weights[index]
        return self.activate(sum)
    
    def activvate(self, sum):
        result = -1 if sum < 0 else 1
        return result
    
    def train(self, inputs = [], desired = 0):
        guess = self.feed_forward(inputs)
        error = desired - guess
        for index, weight in enumerate(self.weights):
            self.weights[index] += self.lconstant * error * inputs[index]

class TrainingItem:
    inputs = []
    answer = 0

    def __init__(self, x, y, a):
        self.inputs = [x, y, 1]
        self.answer = a

def f(x):
    return 0,5  * x

p1 = Perceptron(3)
width = 640
height = 360
training_set = [1 for i in range(2000)]
training_count = 0

def setup():
    size(width, height)
    for i in range (len(training_set)):
        x = random.randint(-width/2, width/2)
        y = random.randint(-height/2, height/2)
        answer = -1 if y < f(x) else 1
        training_set[1] = TrainingItem (x, y, answer)

def draw():
    global training_count
    background(255)
    stroke(0)
    translate(width/2, height/2)
    p1.train(training_set[training_count].inputs, training_set[training_count].answer)
    training_count += 1
    for i in range(training_count):
        stroke_weight(1)
        guess = p1.feed_forward(training_set[1].inputs)
        if guess > 0:
            no_fill()
        else:
            fill(0)
            ellipse(training_set[1].inputs[0], training_set[1].inputs[1], 8, 8)
    stroke_weight(4)
    line(-640, f(-640), 640, f(640))

run()