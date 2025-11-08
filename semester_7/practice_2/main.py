import numpy as np

X = np.array([[0, 1], [1, 0], [1, 1]])

y = np.array(
    [
        [1, 0],  # 0 OR 1 = 1, 0 XNOR 1 = 0
        [1, 0],  # 1 OR 0 = 1, 1 XNOR 0 = 0
        [1, 1],  # 1 OR 1 = 1, 1 XNOR 1 = 1
    ]
)

k_tanh = 2
k_linear = 0.8


def tanh(x, k=1):
    return np.tanh(x / k)


def linear(x, k=1):
    return k * x


def activation(z):
    a1 = tanh(z[:, [0]], k=k_tanh)
    a2 = linear(z[:, [1]], k=k_linear)
    return np.concatenate([a1, a2], axis=1)


def train_delta_rule(X, y, learning_rate=0.7, e=1e-2, max_iter=10000):
    np.random.seed(42)
    n_inputs = X.shape[1]
    n_neurons = y.shape[1]

    W = np.random.rand(n_inputs, n_neurons)
    bias = np.random.rand(1, n_neurons)

    for iteration in range(max_iter):
        achieved_accuracy = True
        for k in range(X.shape[0]):
            x = X[k:k + 1]
            target = y[k:k + 1]

            z = np.dot(x, W) + bias
            output = activation(z)

            delta = target - output

            if not np.allclose(output, target, atol=e):
                achieved_accuracy = False

            for i in range(n_neurons):
                for j in range(n_inputs):
                    W[j, i] += learning_rate * delta[0, i] * x[0, j]
                bias[0, i] += learning_rate * delta[0, i]

        if achieved_accuracy:
            print(f"Сеть обучена на {iteration} итерации")
            break

    outputs = activation(np.dot(X, W) + bias)
    return W, bias, outputs


W_final, bias_final, outputs_final = train_delta_rule(X, y)

np.set_printoptions(precision=3, suppress=True)

print("Итоговые веса W:")
print(W_final)
print("\nИтоговые смещения (bias):")
print(bias_final)
print("\nВыход сети для всех входов:")

print("\n  X1  X2  |  OR(tanh)   XNOR(linear)")
print(" ——— ——— ————————— ———————————")
for (x1, x2), (o1, o2), (t1, t2) in zip(X, outputs_final, y):
    print(f"  {x1:>2}  {x2:>2}  |   {o1:6.3f} ({t1})     {o2:6.3f} ({t2})")
