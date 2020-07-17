# -*- coding: utf-8 -*-
"""select_channels.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c1cC3K28LQ-TCVU22YfCGMz70PIxGSkA
"""

import pickle

nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 32, 32, 8064
no_of_users=32
def select_32ch():
    print("Program started"+"\n")
    fout_data = open("data/32/features_raw.dat",'w')
    fout_labels0 = open("data/32/labels_0.dat",'w')
    fout_labels1 = open("data/32/labels_1.dat",'w')
    fout_labels2 = open("data/32/labels_2.dat",'w')
    fout_labels3 = open("data/32/labels_3.dat",'w')
    for i in range(no_of_users):  
        if(i%1 == 0):
            if i < 10:
                name = '%0*d' % (2,i+1)
            else:
                name = i+1
        fname = "data/32/s"+str(name)+".dat"     
        f = open(fname, 'rb')                 
        x = pickle.load(f, encoding='latin1')
        print(fname)                          
    	
        for tr in range(nTrial):
            if(tr%1 == 0):
                for dat in range(nTime):
                    if(dat%32 == 0):
                        for ch in range(nChannel):
                            fout_data.write(str(x['data'][tr][ch][dat]) + " ");
                fout_labels0.write(str(x['labels'][tr][0]) + "\n");
                fout_labels1.write(str(x['labels'][tr][1]) + "\n");
                fout_labels2.write(str(x['labels'][tr][2]) + "\n");
                fout_labels3.write(str(x['labels'][tr][3]) + "\n");
                fout_data.write("\n");
    fout_labels0.close()
    fout_labels1.close()
    fout_labels2.close()
    fout_labels3.close()
    fout_data.close()
    print("\n"+"Print Successful")

if __name__ == '__main__':
    select_32ch()



