import numpy as np

from sklearn.datasets import load_boston

dataset = load_boston()
x  = dataset.data
y = dataset.target
print(x.shape)   #(506, 13)
print(y.shape)   #(506,)
print("================")
print(x[:5])
print(y[:10])

print(np.max(x), np.min(x)) #최댓값과 최솟값
print(dataset.feature_names)
print(dataset.DESCR)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size= 0.6, random_state = 66
)

#2.MODEL

from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import Dense,Input

input1 = Input(shape=(13,))
dense1 = Dense(156,activation='linear')(input1)
dense1 = Dense(30)(dense1)
dense1 = Dense(60)(dense1)
dense1 = Dense(80)(dense1)
dense1 = Dense(44)(dense1)
dense1 = Dense(80)(dense1)
dense1 = Dense(50)(dense1)
dense1 = Dense(10)(dense1)
dense1 = Dense(40)(dense1)
dense1 = Dense(10)(dense1)
dense1 = Dense(66)(dense1)
dense1 = Dense(5)(dense1)
output = Dense(1)(dense1)

model = Model(inputs=input1, 
              outputs= output)
model.summary()

#3.compile
model.compile(loss = 'mse', optimizer='adam', metrics=['mae'])
model.fit(x_train, y_train, epochs=600, verbose= 3, validation_split=0.2)

#4.EVALUATE
loss, mae = model.evaluate(x_test, y_test, batch_size=8, )
print("model.metrics_names : ", model.metrics_names)
print("loss,mae:", loss, mae)

y_pred = model.predict(x_test)
print("=====================" )
#print("y_pred : ", y_pred)

from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_pred):
    return np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE: ", RMSE(y_test, y_pred))

from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_pred)
print("R2 : ", R2)