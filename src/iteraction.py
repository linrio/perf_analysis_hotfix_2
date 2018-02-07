
import os
import numpy as np
import pandas as pd

class Iteraction(object):
    def __init__(self):
        self.a = None
        self.algorithm_name = 'SVDPlusPlus'

        self.importanceRank_path = 'F:/linlingfeng/codes/python/perf_DATA/result/10itera_xlsx'
        self.big_table_path = 'F:/linlingfeng/codes/python/perf_DATA/result/big_table'

        self.importanceRank_data = 'result_10itera_MinMax_' + self.algorithm_name + '.xlsx'
        self.big_table_data = 'MinMax_' + self.algorithm_name + '.csv'

    def split_dataFrame(self):
        importanceRank_data = os.path.join(self.importanceRank_path, self.importanceRank_data)
        big_table_data = os.path.join(self.big_table_path, self.big_table_data)

        """ 指定需要那个 Sheet 的数据"""
        importanceRank_data = pd.read_excel(importanceRank_data, sheetname='Sheet4')
        sub_IR_data = importanceRank_data[:10]
        sub_IR_event = sub_IR_data[sub_IR_data.columns[2]].tolist()
        #print(sub_IR_data)
        #print(sub_IR_event)

        big_table_data = pd.read_csv(big_table_data)
        IPC = big_table_data['IPC']
        big_table_data = big_table_data[sub_IR_event]
        assert len(IPC) == len(big_table_data)
        """To do"""
        big_table_data['IPC'] = IPC
        return big_table_data

    def colMeans_nozero(self, data):
        """ 计算每一列中非零元的均值 """
        nozero_mean = []
        for i in range(len(data.columns)):
            col_val = data[data.columns[i]]
            nozero = [x for x in col_val if x != 0]
            nozero_mean.append(np.mean(nozero))
        #nozero_mean = nozero_mean
        return nozero_mean

    def data_cleaning(self, data):
        """ 剔除 inf 异常值"""
        data_cp = data
        bedrop = []
        for index, row in data.iterrows():  # 获取每行的index、row
            for ind, col_name in enumerate(data.columns):
                if row[col_name] > 1:
                    print('row:  %s and rol: %s.' % (index, ind))
                    bedrop.append(index)
        data_cp.drop(bedrop, inplace=True)
        return data_cp

    def top10Event_denseMatrix(self, data, col_mean):
        """ 用 (均值+随机值) 填充 0
        :param data:
        :return:
        """
        for index, row in data.iterrows():  # 获取每行的index、row
            for ind, col_name in enumerate(data.columns):
                if row[col_name] == 0:
                    #continue
                    row[col_name] = col_mean[ind] + np.random.random()*1e-5  # 把结果返回给data
        return data


    def iteraction(self):
        data = self.split_dataFrame()
        data = self.data_cleaning(data)
        col_mean = self.colMeans_nozero(data)
        data = self.top10Event_denseMatrix(data, col_mean)
        data.to_csv('top10_0matrix_MinMax_'+self.algorithm_name+'.csv')
        '''to do'''
        #print(data)
        print(col_mean)

        self.a = None



    def build(self):
        self.iteraction()

if __name__ == '__main__':
    iteraction = Iteraction()
    iteraction.__init__()
    iteraction.build()