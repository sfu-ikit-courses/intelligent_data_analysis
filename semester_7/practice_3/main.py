import numpy as np


class MyBackPropagation:
    def __init__(self, layers, activations, verbose=False):
        self.layers = layers
        self.activations = activations
        self.verbose = verbose
        self.weights = []
        self.biases = []

    def initialize_weights(self):
        np.random.seed(42)
        for i in range(1, len(self.layers)):
            w = np.random.uniform(0.1, 1, size=(self.layers[i - 1], self.layers[i]))
            b = np.random.uniform(0.1, 1, size=(1, self.layers[i]))
            self.weights.append(w)
            self.biases.append(b)

    def forward(self, x):
        x = x.reshape(1, -1)
        a_s = [x]
        z_s = []

        for i in range(len(self.weights)):
            z = x @ self.weights[i] + self.biases[i]
            a = self.activations[i]["func"](z)
            z_s.append(z)
            a_s.append(a)
            x = a

        return a_s, z_s

    def only_forward(self, x):
        x = x.reshape(1, -1)
        for i in range(len(self.weights)):
            z = x @ self.weights[i] + self.biases[i]
            x = self.activations[i]["func"](z)
        return x

    def backward(self, y, a_s, z_s):
        dW = [np.zeros_like(w) for w in self.weights]
        db = [np.zeros_like(b) for b in self.biases]

        delta = (a_s[-1] - y.reshape(1, -1)) * self.activations[-1]["deriv"](z_s[-1])

        for l in reversed(range(len(self.weights))):
            dW[l] = a_s[l].T @ delta
            db[l] = delta.copy()

            if l > 0:
                delta = (delta @ self.weights[l].T) * self.activations[l - 1]["deriv"](
                    z_s[l - 1]
                )

        return dW, db

    def update_weights(self, dW, db, lr):
        for l in range(len(self.weights)):
            self.weights[l] -= lr * dW[l]
            self.biases[l] -= lr * db[l]

    def fit(self, X, y, epochs=1000, lr=0.1, verbose=None):

        if verbose is None:
            verbose = self.verbose

        if len(self.weights) == 0:
            self.initialize_weights()

        for epoch in range(epochs):
            total_loss = 0
            for j in range(X.shape[0]):
                a_s, z_s = self.forward(X[j])
                dW, db = self.backward(y[j], a_s, z_s)
                self.update_weights(dW, db, lr)
                total_loss += np.mean((a_s[-1] - y[j].reshape(1, -1)) ** 2)
            if verbose and epoch % 100 == 0:
                print(f"Эпоха {epoch:5d} | Среднеквадратичная ошибка: {total_loss:.6f}")

    def predict(self, X):
        predictions = []
        for i in range(X.shape[0]):
            y_pred = self.only_forward(X[i])
            predictions.append(y_pred.flatten())
        return np.array(predictions)

    def get_loss(self, X, y):
        y_pred = self.predict(X)
        return np.mean((y_pred - y) ** 2)


np.random.seed(42)

X = np.random.uniform(0.1, 1.0, size=(3, 3))
y = np.random.uniform(0.1, 1.0, size=(3, 2))

k = 0.6

activations = [
    {"func": lambda z: k * z, "deriv": lambda z: k},
    {"func": lambda z: k * z, "deriv": lambda z: k},
]

nn = MyBackPropagation(layers=[3, 3, 2], activations=activations)

nn.fit(X=X, y=y, lr=0.1)

loss = nn.get_loss(X, y)
predictions = nn.predict(X)

print("="*50)
print("РЕЗУЛЬТАТЫ ОБУЧЕНИЯ СЕТИ")
print("="*50)
print(f"Количество обучающих примеров: {X.shape[0]}")
print(f"Количество входов: {X.shape[1]}, количество выходов: {y.shape[1]}")
print("-"*50)

for i in range(X.shape[0]):
    print(f"Пример {i+1}:")
    print(f"  Вход:             {X[i]}")
    print(f"  Ожидаемый выход:  {y[i]}")
    print(f"  Предсказание сети:{predictions[i]}")
    print("-"*50)

print(f"Итоговая среднеквадратичная ошибка (MSE): {loss:.6f}")
print("="*50)
