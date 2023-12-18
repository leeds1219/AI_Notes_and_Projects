import nn

class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        score = nn.DotProduct(x, self.get_weights())
        return score

    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        return 1 if nn.as_scalar(self.run(x)) >= 0 else -1

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        batch_size = 1
        converged = False

        while not converged:
            converged = True  # Assume convergence initially
            for x, y in dataset.iterate_once(batch_size) :
                prediction = self.get_prediction(x)
                actual = nn.as_scalar(y)
                if prediction != actual :
                    self.w.update(x, actual)
                    converged = False  # Model hasn't converged yet
                    break  # Break after updating weights for this batch_size

class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # Hidden layer size 512
        self.w1 = nn.Parameter(1,512)
        self.w2 = nn.Parameter(512,1)
        self.b1 = nn.Parameter(1,512)
        self.b2 = nn.Parameter(1,1)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        # One hidden layer (2 linear layers in total)
        input_layer = nn.Linear(x, self.w1)
        input_layer = nn.AddBias(input_layer, self.b1)
        input_layer = nn.ReLU(input_layer)
        output_layer = nn.Linear(input_layer, self.w2)
        output_layer = nn.AddBias(output_layer, self.b2)

        return output_layer

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        prediction = self.run(x)
        ground_truth = y
        loss = nn.SquareLoss(prediction, ground_truth)

        return loss

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        # Batch size 200
        # Learning rate 0.05
        batch_size = 200
        learning_rate = 0.05
        epochs = 10000

        for epoch in range(epochs) :
            for x, y in dataset.iterate_once(batch_size) :
                
                # Compute Gradients
                gradient_w1, gradient_b1, gradient_w2, gradient_b2 = nn.gradients(self.get_loss(x,y), [self.w1, self.b1, self.w2, self.b2])
                
                # Update weights and biases
                self.w1.update(gradient_w1, -learning_rate)
                self.b1.update(gradient_b1, -learning_rate)
                self.w2.update(gradient_w2, -learning_rate)
                self.b2.update(gradient_b2, -learning_rate)


class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # Hidden layer size 200
        # Your final test set accuracy (96.540000%) must be at least 97% to receive full points for this question
        self.w1 = nn.Parameter(784,200)
        self.w2 = nn.Parameter(200,10)
        self.b1 = nn.Parameter(1,200)
        self.b2 = nn.Parameter(1,10)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        # Your final test set accuracy (96.540000%) must be at least 97% to receive full points for this question
        # One hidden layer (2 linear layers in total)
        # First hidden layer with ReLU activation
        input_layer = nn.Linear(x, self.w1)
        input_layer = nn.AddBias(input_layer, self.b1)
        input_layer = nn.ReLU(input_layer)
        
        # Output layer (no activation for logits)
        output_layer = nn.Linear(input_layer, self.w2)
        output_layer = nn.AddBias(output_layer, self.b2)
        
        return output_layer

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        # Your final test set accuracy (96.540000%) must be at least 97% to receive full points for this question
        prediction = self.run(x)
        ground_truth = y
        loss = nn.SoftmaxLoss(prediction, ground_truth)

        return loss
    
    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        # Your final test set accuracy (96.540000%) must be at least 97% to receive full points for this question
        # Batch size 100
        # Learning rate 0.5
        batch_size = 100
        learning_rate = 0.05
        epochs = 20 # 12 epochs gave 96.54% make more training or give a threshold

        for epoch in range(epochs) :
            for x, y in dataset.iterate_once(batch_size) : 
                
                # Compute Gradients
                gradient_w1, gradient_b1, gradient_w2, gradient_b2 = nn.gradients(self.get_loss(x,y), [self.w1, self.b1, self.w2, self.b2])
                
                # Update weights and biases
                self.w1.update(gradient_w1, -learning_rate)
                self.b1.update(gradient_b1, -learning_rate)
                self.w2.update(gradient_w2, -learning_rate)
                self.b2.update(gradient_b2, -learning_rate)

class LanguageIDModel(object):
    """
    A model for language identification at a single-word granularity.

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Our dataset contains words from five different languages, and the
        # combined alphabets of the five languages contain a total of 47 unique
        # characters.
        # You can refer to self.num_chars or len(self.languages) in your code
        self.num_chars = 47
        self.languages = ["English", "Spanish", "Finnish", "Dutch", "Polish"]

        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.w1 = nn.Parameter(self.num_chars,100)
        self.b1 = nn.Parameter(1,100)
        self.w2 = nn.Parameter(100,100)
        self.b2 = nn.Parameter(1,100)
        self.w1_hidden = nn.Parameter(100,100)
        self.b1_hidden = nn.Parameter(1,100)
        self.w2_hidden = nn.Parameter(100,100)
        self.b2_hidden = nn.Parameter(1,100)
        self.w_final = nn.Parameter(100,5)
        self.b_final = nn.Parameter(1,5)


    def run(self, xs):
        """
        Runs the model for a batch of examples.

        Although words have different lengths, our data processing guarantees
        that within a single batch, all words will be of the same length (L).

        Here `xs` will be a list of length L. Each element of `xs` will be a
        node with shape (batch_size x self.num_chars), where every row in the
        array is a one-hot vector encoding of a character. For example, if we
        have a batch of 8 three-letter words where the last word is "cat", then
        xs[1] will be a node that contains a 1 at position (7, 0). Here the
        index 7 reflects the fact that "cat" is the last word in the batch, and
        the index 0 reflects the fact that the letter "a" is the inital (0th)
        letter of our combined alphabet for this task.

        Your model should use a Recurrent Neural Network to summarize the list
        `xs` into a single node of shape (batch_size x hidden_size), for your
        choice of hidden_size. It should then calculate a node of shape
        (batch_size x 5) containing scores, where higher scores correspond to
        greater probability of the word originating from a particular language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
        Returns:
            A node with shape (batch_size x 5) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        input_layer = nn.AddBias(nn.Linear(xs[0],self.w1),self.b1)
        input_layer = nn.ReLU(input_layer)
        hidden_layer = nn.AddBias(nn.Linear(input_layer,self.w2),self.b2)

        for i in range(1,len(xs)) :
            input_layer = nn.AddBias(nn.Add(nn.Linear(xs[i], self.w1), nn.Linear(hidden_layer, self.w1_hidden)),self.b1_hidden)
            input_layer = nn.ReLU(input_layer)
            input_layer = nn.AddBias(nn.Linear(input_layer,self.w2_hidden),self.b2_hidden)
            hidden_layer = nn.ReLU(input_layer)

        output_layer = nn.AddBias(nn.Linear(hidden_layer,self.w_final),self.b_final)

        return output_layer

    def get_loss(self, xs, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 5). Each row is a one-hot vector encoding the correct
        language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
            y: a node with shape (batch_size x 5)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        prediction = self.run(xs)
        ground_truth = y
        loss = nn.SoftmaxLoss(prediction, ground_truth)

        return loss

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        batch_size = 100
        learning_rate = 0.05
        # Our reference implementation takes 10-20 epochs to train
        epochs = 20

        for epoch in range(epochs) :
            for x, y in dataset.iterate_once(batch_size) :
                
                # Compute Gradients
                gradient_w1, gradient_b1, gradient_w2, gradient_b2, gradient_w1_hidden, gradient_b1_hidden, gradient_w2_hidden, gradient_b2_hidden, gradient_w_final, gradient_b_final =\
                     nn.gradients(self.get_loss(x,y), [self.w1, self.b1, self.w2, self.b2, self.w1_hidden, self.b1_hidden, self.w2_hidden, self.b2_hidden, self.w_final, self.b_final])
                
                # Update weights and biases
                self.w1.update(gradient_w1, -learning_rate)
                self.b1.update(gradient_b1, -learning_rate)
                self.w2.update(gradient_w2, -learning_rate)
                self.b2.update(gradient_b2, -learning_rate)
                self.w1_hidden.update(gradient_w1_hidden, -learning_rate)
                self.b1_hidden.update(gradient_b1_hidden, -learning_rate)
                self.w2_hidden.update(gradient_w2_hidden, -learning_rate)
                self.b2_hidden.update(gradient_b2_hidden, -learning_rate)
                self.w_final.update(gradient_w_final, -learning_rate)
                self.b_final.update(gradient_b_final, -learning_rate)

