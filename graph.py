import os
import numpy as np
import matplotlib.pyplot as plt
import re

path='F:\\卒論プログラム３\\forgraph保存\\'
forgraph=re.compile(r'forgraph')
shs=re.compile(r'shs')
fovar=re.compile(r'fovar')
total=re.compile(r'total')
two=re.compile(r'2-3')
three=re.compile(r'3-3')
p90=re.compile(r'90.010.0')
p95=re.compile(r'95.05.0')
p99=re.compile(r'99.01.0')

for filename in os.listdir(path):
    if forgraph.search(filename):
        textfile=filename
        if shs.search(filename):
            ylabel='調波構造検出可能時間率'
        elif fovar.search(filename):
            ylabel='基本周波数連続時間率'
        elif total.search(filename):
            ylabel='周波数特性総合時間率'

        if two.search(filename):
            labelname='none'
            marker='^'
            fillstyle='full'
        elif three.search(filename):
            labelname='25-30'
            marker='x'
            fillstyle='none'
        elif p90.search(filename):
            labelname='none'
            marker='o'
            fillstyle='full'
        elif p95.search(filename):
            labelname='none'
            marker='o'
            fillstyle='none'
        elif p99.search(filename):
            labelname='none'
            marker='^'
            fillstyle='none'


        #ファイル読み込み、リストの取得
        z=open(path+textfile,'r',encoding='UTF-8')
        all_list=np.array(z.readlines())
        snr_list=np.array(all_list[0].split(' ')[:-1]).astype(float)
        mean_list=np.array(all_list[1].split(' ')[:-1]).astype(float)
        sd_list=np.array(all_list[2].split(' ')[:-1]).astype(float)

        fig,ax=plt.subplots(figsize=(9,5))
        ax.errorbar(snr_list,mean_list,yerr=sd_list,\
                    label=labelname,\
                    marker=marker,markersize=13,\
                    fillstyle=fillstyle,\
                    ecolor='black',color='black',\
                    capsize=8,linestyle='None')
        ax.tick_params(direction='in',labelsize=25,length=8)
        ax.set_xlabel('SN比(dB)',fontname='Yu Gothic',fontsize=25)
        ax.set_ylabel(ylabel,fontname='Yu Gothic',fontsize=25)
        plt.tight_layout()
        pngfile=textfile.replace('.txt','.png').replace('forgraph_','')
        dirname='グラフ保存先/'
        os.makedirs(dirname,exist_ok=True)
        filename=dirname+f'{pngfile}'
        plt.savefig(filename)