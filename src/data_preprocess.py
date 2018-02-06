#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
=================================
preprocessing data. Lingfeng Lin
=================================
"""

import os
import re
import xlwt
import xlrd
import errno
import numpy as np
import pandas as pd

class DataPreprocess(object):
    def __init__(self):
        self.a = None
        self.init_data_path = '../data/DecisionTree_new/'
        self.csv_data_path = '../data/DecisionTree_new_csv/'
        self.init_data_path = '../data/LogisticRegression-128MB/'
        self.csv_data_path = '../data/LogisticRegression-128MB_csv/'

        self.init_data_path = '../data/mini/PageRank-32MB-18slavers-1000ms'
        self.csv_data_path = '../data/mini/PageRank-32MB-18slavers-1000ms_xls'

        self.init_data_path = 'F:/linlingfeng/codes/python/perf_DATA/IPC/submit/cppVSjava_DecisionTree'
        self.csv_data_path = 'F:/linlingfeng/codes/python/perf_DATA/IPC/submit/cppVSjava_DecisionTree_xls'

        self.init_data_path = 'F:/linlingfeng/codes/python/perf_DATA/IPC/1000ms/LogisticRegression-128MB-18slavers-1000ms'
        self.csv_data_path = 'F:/linlingfeng/codes/python/perf_DATA/IPC/1000ms/LogisticRegression-128MB-18slavers-1000ms_xls'

        self.txt_file_path = None
        self.csv_file_path  =None

    def data_preprocess(self):
        print("***lol*** data preprocess ***lol***")
        data_path = self.init_data_path
        for dirpath, dirnames, filenames in os.walk(data_path):
            for filename in filenames:
                filename = os.path.join(dirpath, filename)
                print(filename)
                filename = open(filename)
                txtDF = pd.DataFrame(filename)
                txtDF.to_csv('file.csv', index=False)
                break
        print(data_path)
        a = None
        return a


    def txt_to_scv2(self):
        pattern_file_path = re.compile('ms-(\w*)events')
        '''特例所用：cpp VS Java'''
        #pattern_file_path = re.compile('archi_(\w*)')
        event_series = pattern_file_path.findall(self.txt_file_path)[0]
        '''特例所用：cpp VS Java'''
        #event_series = str(self.txt_file_path).strip().split('\\')[1]
        #print(event_series)
        f_data = xlwt.Workbook()
        data_sheet = f_data.add_sheet('config_perf', cell_overwrite_ok=True)
        arch_params = ['TIME', 'INS', 'CYC', '00', '01', '02', '03', '04']
        arch_params_1 = ['TIME', 'INS', 'CYC', 'SW_INCR', 'L1I_CACHE_REFILL', 'L1I_TLB_REFILL', 'L1D_CACHE_REFILL']
        arch_params_2 = ['TIME', 'INS', 'CYC', 'L1D_CACHE', 'L1D_TLB_REFILL', 'LD_RETIRED', 'ST_RETIRED']
        arch_params_3 = ['TIME', 'INS', 'CYC', 'EXC_TAKEN', 'EXC_RETURN', 'CID_WRITE_RETIRED', 'PC_WRITE_RETIRED']
        arch_params_4 = ['TIME', 'INS', 'CYC', 'BR_IMMED_RETIRED', 'PRD_FN_RET', 'UNALIGNED_LDST_RETIRED', 'BR_MIS_PRED']
        arch_params_5 = ['TIME', 'INS', 'CYC', 'BR_PRED', 'JAVA_BC_EXEC', 'JAVA_SFTBC_EXEC', 'JAVA_BB_EXEC']
        arch_params_6 = ['TIME', 'INS', 'CYC', 'CO_LF_MISS', 'CO_LF_HIT', 'IC_DEP_STALL', 'DC_DEP_STALL']
        arch_params_7 = ['TIME', 'INS', 'CYC', 'STALL_MAIN_TLB', 'STREX_PASS', 'STREX_FAILS', 'DATA_EVICT']
        arch_params_8 = ['TIME', 'INS', 'CYC', 'ISS_NO_DISP', 'ISS_EMPTY', 'DATA_LF', 'PREFETCHER_LF']
        arch_params_9 = ['TIME', 'INS', 'CYC', 'HITS_PRE_CAL', 'INS_MAIN_EXEC', 'INS_SND_EXEC', 'INS_LSU']
        arch_params_10 = ['TIME', 'INS', 'CYC', 'INS_FP_RR', 'INS_NEON_RR', 'STALL_PLD', 'STALL_WRITE']
        arch_params_11 = ['TIME', 'INS', 'CYC', 'STALL_INS_TLB', 'STALL_DATA_TLB', 'STALL_INS_UTLB', 'STALL_DATA_ULTB']
        arch_params_12 = ['TIME', 'INS', 'CYC', 'STALL_DMB', 'CLK_INT_EN', 'CLK_DE_EN', 'CLK_NEONS_EN']
        arch_params_13 = ['TIME', 'INS', 'CYC', 'INS_TLB_ALLO', 'DATA_TLB_ALLO', 'INS_ISB', 'INS_DSB']
        arch_params_14 = ['TIME', 'INS', 'CYC', 'INS_DMB', 'EXT_IRQ', 'PLE_CL_REQ_CMP', 'PLE_CL_REQ_SKP']
        arch_params_15 = ['TIME', 'INS', 'CYC', 'PLE_FIFO_FLSH', 'PLE_REQ_COMP', 'PLE_FIFO_OF', 'PLE_REQ_PRG']


        if event_series == 'archi_1':
            arch_params = arch_params_1
        elif event_series == 'archi_2':
            arch_params = arch_params_2
        elif event_series == 'archi_3':
            arch_params = arch_params_3
        elif event_series == 'archi_4':
            arch_params = arch_params_4
        elif event_series == 'archi_5':
            arch_params = arch_params_5
        elif event_series == 'archi_6':
            arch_params = arch_params_6
        elif event_series == 'archi_7':
            arch_params = arch_params_7
        elif event_series == 'archi_8':
            arch_params = arch_params_8
        elif event_series == 'archi_9':
            arch_params = arch_params_9
        elif event_series == 'archi_10':
            arch_params = arch_params_10
        elif event_series == 'archi_11':
            arch_params = arch_params_11
        elif event_series == 'archi_12':
            arch_params = arch_params_12
        elif event_series == 'archi_13':
            arch_params = arch_params_13
        elif event_series == 'archi_14':
            arch_params = arch_params_14
        elif event_series == 'archi_15':
            arch_params = arch_params_15

        #创建csv的表头
        j = 1
        m = 0
        for index, param in enumerate(arch_params):
            data_sheet.write(0, index, param)

        txt_file = open(self.txt_file_path, "r")
        for line in txt_file.readlines():
            line = line.strip().split(' ')
            if line[0] == '' or line[0] == '#':
                continue
            time = line[0]
            count = None
            event = None

            for jj in range(1, len(line)):
                if line[jj] != '':
                    count = line[jj]
                    try:
                        event = line[jj+1]
                    except IndexError:
                        event = None
                    break
            if time == None or count == None or event == None:
                continue
            time = str(time.strip().split('.')[0])
            count = str(count)
            event = str(event[1:])
            m+=1
            if m > 6:
                j += 1
                m = 1
            data_sheet.write(j, 0, time)
            if '68' in event:
                data_sheet.write(j, 1, count)
            if 'FF' in event:
                data_sheet.write(j, 2, count)
            if '00' in event or '04' in event or '09' in event or '0D' in event or '12' in event or '50' in event or '62' in event or '66' in event or '6B' in event or '73' in event or '82' in event or '86' in event or '8D' in event or '92' in event or 'A2' in event:
                data_sheet.write(j, 3, count)
            elif '01' in event or '05' in event or '0A' in event or '0E' in event or '40' in event or '51' in event or '63' in event or '67' in event or '70' in event or '74' in event or '83' in event or '8A' in event or '8E' in event or '93' in event or 'A3' in event:
                data_sheet.write(j, 4, count)
            elif '02' in event or '06' in event or '0B' in event or '0F' in event or '41' in event or '60' in event or '64' in event or '69' in event or '71' in event or '80' in event or '84' in event or '8B' in event or '90' in event or 'A0' in event or 'A4' in event:
                data_sheet.write(j, 5, count)
            elif '03' in event or '07' in event or '0C' in event or '10' in event or '42' in event or '61' in event or '65' in event or '6A' in event or '72' in event or '81' in event or '85' in event or '8C' in event or '91' in event or 'A1' in event or 'A5' in event:
                data_sheet.write(j, 6, count)

        f_data.save(self.csv_file_path)
        return self.a

    def read_path(self):
        rootdir = self.init_data_path  # 指明被遍历的文件夹
        csvdir = self.csv_data_path

        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            print(parent)
            for filename in filenames:  # 输出文件信息
                self.txt_file_path = os.path.join(parent, filename)
                csv_parent = parent.strip().replace(rootdir, csvdir)
                csv_filename = filename.strip().replace(".txt", '.xls')
                self.csv_file_path = str(os.path.join(csv_parent, csv_filename)).strip().replace('\\', '/')
                #print("the full name of txt file is: " + self.txt_file_path)  # 输出文件路径信息
                #print("the full name of xls file is: " + self.csv_file_path)  # 输出文件路径信息
                self.mkdir_p(csv_parent)
                self.a = self.txt_to_scv2()
        print('read_path', rootdir)
        return self.a

    def mkdir_p(self, csv_parent):
        #创建文件夹
        try:
            os.makedirs(csv_parent, exist_ok=False)
        except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
            if exc.errno == errno.EEXIST and os.path.isdir(csv_parent):
                pass
            else:
                raise

    def test_txtTocsv(self):
        txt_file = open('slaver3.txt', "r")
        i = 0
        TIME = []
        INS = []
        CYC = []
        SW_INCR= []
        L1I_CACHE_REFILL = []
        L1I_TLB_REFILL = []
        L1D_CACHE_REFILL = []

        for line in txt_file.readlines():
            line = line.strip().split(' ')
            if line[0] == '' or line[0] == '#':
                continue
            time = line[0]
            count = None
            event = None
            for j in range(1,len(line)):
                if line[j] != '':
                    count = line[j]
                    event = line[j+1]
                    break
            if time == None or count ==None or event == None:
                continue
            time = str(time.strip().split('.')[0])
            count = str(count)
            event = str(event[1:])


            if event == '68':
                TIME.append(time)
                INS.append(count)
            if event == 'FF':
                CYC.append(count)
            if event == '82':
                SW_INCR.append(count)
            if event == '83':
                L1I_CACHE_REFILL.append(count)
            if event == '84':
                L1I_TLB_REFILL.append(count)
            if event == '85':
                L1D_CACHE_REFILL.append(count)
        print(len(TIME),len(INS))
        f_data = xlwt.Workbook()
        data_sheet = f_data.add_sheet('config_perf', cell_overwrite_ok=True)
        arch_params = ['TIME', 'INS', 'CYC', 'SW_INCR', 'L1I_CACHE_REFILL', 'L1I_TLB_REFILL', 'L1D_CACHE_REFILL']
        dataframe = [TIME, INS, CYC, SW_INCR, L1I_CACHE_REFILL, L1I_TLB_REFILL, L1D_CACHE_REFILL]
        k = 0
        for param in arch_params:
            data_sheet.write(0, k, param)
            for i in range(len(TIME)):
                data_sheet.write(i+1, k, dataframe[k][i])
            k += 1
        f_data.save('eggs.xls')


        """
        import csv
        with open('eggs.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['time', 'instructions', 'cycle','SW_INCR', 'L1I_CACHE_REFILL', 'L1I_TLB_REFILL', 'L1D_CACHE_REFILL'])
            for i in range(len(TIME)):
                tobewrite = [TIME[i], INS[i], CYC[i], SW_INCR[i], L1I_CACHE_REFILL[i], L1I_TLB_REFILL[i], L1D_CACHE_REFILL[i]]
                spamwriter.writerows(tobewrite)
        """


    def build(self):
        print("***lol*** build ***lol***")
        a = self.read_path()
        #a = self.data_preprocess()
        #self.test_txtTocsv()
        a = None
        return a

if __name__ == '__main__':
    data_preprocess = DataPreprocess()
    data_preprocess.__init__()
    data_preprocess.build()