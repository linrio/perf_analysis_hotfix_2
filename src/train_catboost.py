
import os
import pickle
import numpy as np
import pandas as pd
import catboost
from sklearn.model_selection import train_test_split

class TRAIN_CatBoost(object):
    def __init__(self):
        self.a = None
        self.data_path = 'F:/linlingfeng/codes/python/perf_DATA/result/big_table'
        self.algorithm_name = 'MinMax_PregelOperation'


    def train_catboost(self):
        algorithm = str(self.algorithm_name + '.csv')
        algorithm = os.path.join(self.data_path, algorithm)
        data = pd.read_csv(algorithm)

        X = data.iloc[:, 1:61]
        y = data.iloc[:, 61]
        #X = X[:500]
        #y = y[:500]
        events_name = X.columns
        X = np.array(X)

        Err = []
        Importances = []
        Indices = []
        Events_Name = []
        Itera = 10
        for _ in range(Itera):
            print('the %s th training' % (_ + 1))
            assert len(X) == len(y)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            # forest = catboost.CatBoostRegressor(iterations=500,
            #                             learning_rate=0.01,
            #                             depth=10,
            #                             l2_leaf_reg=0.3,
            #                             rsm=None,
            #                             loss_function='RMSE')
            forest = catboost.CatBoostRegressor()

            y_train = np.array(y_train)
            forest.fit(X_train, y_train)
            predicted = forest.predict(X_test)

            assert len(predicted) == len(y_test)
            y_test = np.asarray(y_test).astype(float)
            predicted = np.asarray(predicted).astype(float)
            err = np.mean(np.abs(y_test - predicted)/y_test)
            importances = forest.get_feature_importance(X=X_train, y=y_train)
            indices = np.argsort(importances)[::-1]

            Err.append(err)
            Indices.append(indices)
            events_Name = []
            importanceS = []
            print("Feature ranking:")
            for f in range(X.shape[1]):
                events_Name.append(events_name[indices[f]])
                importanceS.append(importances[indices[f]])
                print("%d. feature %d  %s (%f)" % (f + 1, indices[f], events_name[indices[f]], importances[indices[f]]))
            Events_Name.append(events_Name)
            Importances.append(importanceS)
            if _ < Itera-1:
                """ 每一轮训练，删除最不重要的10个事件"""
                X = pd.DataFrame(X)
                X[X.columns[indices[-6*(_+1):]]] = 0
                X = np.array(X)
            print('Error: ', err*100, '%')

        # Min_index = Err.index(min(Err))
        # for f in range(X.shape[1]):
        #     print("%d. lowest error feature %d  %s (%f)" % (f + 1, Indices[Min_index][indices[f]],
        #                                        events_name[Indices[Min_index][f]], Importances[Min_index][f]))

        res = {}
        res['result'] = [Err, Indices, Events_Name, Importances]
        output = open('result_'+self.algorithm_name+'_CatBoost.pkl', 'wb')
        pickle.dump(res, output)
        return res

    def build(self):
        self.train_catboost()

if __name__ == '__main__':
    Train_CatBoost_ = TRAIN_CatBoost()
    Train_CatBoost_.__init__()
    Train_CatBoost_.build()