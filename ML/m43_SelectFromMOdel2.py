#실습
#1 . 상단ㄷ모델에 그리드서치 또는 래덤서치로 튜닝한 모델구성
#최적의 R2값과 피처임포턴스 구할것

#2. 위쓰레드 값으로 SelectFromModel 을 구해서
#최적의 피처 개수를 구할것

#3.위 피처 갯수로 데이터를 수정해서
#그리드서치 또는 랜덤서치 적용하여
#최적의 r2 값을 구할것

#1번값과 2번값 비교
from xgboost import XGBClassifier, XGBRFRegressor

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split,RandomizedSearchCV,GridSearchCV

import numpy as np
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import r2_score, accuracy_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

x, y = load_boston(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, shuffle=True, random_state =66
)

xgb = XGBRFRegressor()

#파라미터 튜닝
parameters = [
    {"n_estimators":[100,200]},
    {"max_depth":[4,5,6]},
    {"n_jobs":[8]}
]
#모델링
model = RandomizedSearchCV(xgb, param_distributions=parameters,cv=5)

model.fit(x_train, y_train, eval_metric='logloss', verbose= True,
           eval_set=[(x_train, y_train),(x_test, y_test)])
score = model.score(x_test, y_test)
print("R2:", r2_score)

thresholds = np.sort(model.best_estimator_feture_importances_)
print(thresholds)

#0으로 비워주기
tmp = 0
tmp2 = [0,0]

for thresh in thresholds :
    selection = SelectFromModel(model, threshold= thresh, prefit =True)

    select_x_train = selection.transform(x_train)
    print(select_x_train.shape)

    selection_model = XGBRFRegressor(n_jobs=8)
    selection_model.fit(select_x_train, y_train)

    select_x_test = selection.transform(x_test)
    y_predict = selection_model.predict(select_x_test)

    score = r2_score(y_test, y_predict)
    if score > tmp :
        tmp = score
        tmp2[0] = thresh
        tmpe[1] = select_x_train.shape[1]


    print("Thresh=%.3f, n=%d, R2: %.2f%%" %(thresh, select_x_train.shape[1], score*100))
    print("BEST SCORE SO FAR", tmp)
    print('Best Threshold:', tmp2[0])

print("===========================================")

selection = SelectFromModel(model.best_estimator_threshold = tmp2[0], prefit=True)

select_x_train = selection.transform(x_train)

selection_model = RandomizedSearchCV(xgb, Parameters, cv=5)
selection_model.fit(select_x_train, y_train)

select_x_test = selection_model.predict(select_x_test)

score = r2_score(y_test, y_predict)

print("=====================================================")
print(f'최종 R2 score: {score*100}% n = {tmp2[1]일떄!!')