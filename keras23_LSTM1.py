#1. 데이터
import numpy as np

x = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
y = np.array([4,5,6,7])

print("x.shape: ",x.shape)
print("y.shape: ",y.shape)

x = x.reshape(4, 3, 1) # 데이터를 1개씩 잘라서 사용
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM # RNN에서 가장 대표적인 모델, RNN은 Y가 없는 데이터

model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(3,1)))# LSTM(10 ->(앞에있는 숫자는 아웃풋노드)/(4,3,1)에서 가장앞에서 쳐내기(=행무시)
#LSTM 레이어를 쓰려면 데이터가 3차원(N1, N2, N3)이되어야한다(+Dense는 2차원 , CNN은 4차원)]
model.add(Dense(20))
model.add(Dense(10))
model.add(Dense(1))

model.summary()

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=100,batch_size=1)


#4.평가 ,예측
loss = model.evaluate(x,y)
print("loss:",loss)

x_pred = np.array([5,6,7])#(3,) - > (1,3,1)
x_pred = x_pred.reshape(1, 3, 1) #1행 3개 1개씩 잘라서 작업할것

result = model.predict(x_pred)
print("result:", result)
