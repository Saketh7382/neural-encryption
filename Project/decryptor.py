#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:44:02 2020

@author: cp
"""

from additional import AdditionalFunctions
import json
import io

from additional import AdditionalFunctions
from encryptor import Encryptor
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
    
class Decryptor:
    encryptor = Encryptor()
    
    def main(self):
        #creating dataset for the system
        network = list()
        dataset = self.getDataset()
        for i in range(7):
            print("Training Decryptor for bit {} initiated".format(i+2))
            if i == 0 or i == 1 or i == 2:
                layers = [8,9,7,1]
            elif i == 3 or i == 4 or i == 6:
                layers = [8,10,9,1]
            else:
                layers = [8,9,3,1]       
            l_rate = 1.0
            epochs = 10000
            network = self.encryptor.createEncryptor(dataset[i],layers,l_rate,epochs)
            name = './network/decryptor/network_bit_'+str(i+2)+'.json'
            with io.open(name, 'w', encoding='utf8') as outfile:
                str_ = json.dumps(network,
                                  indent=4, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))
            self.checkEfficiency(network,dataset[i])
        
    def getDataset(self):
        final_temp = list()
        with open('./data/languageDecryptor.json') as data_file:
            temp1 = json.load(data_file)
            
        with open('./data/languageDecryptor.json') as data_file:
            temp2 = json.load(data_file)
            
        with open('./data/languageDecryptor.json') as data_file:
            temp3 = json.load(data_file)
            
        with open('./data/languageDecryptor.json') as data_file:
            temp4 = json.load(data_file)
            
        with open('./data/languageDecryptor.json') as data_file:
            temp5 = json.load(data_file)
            
        with open('./data/languageDecryptor.json') as data_file:
            temp6 = json.load(data_file)
            
        with open('./data/languageDecryptor.json') as data_file:
            temp7 = json.load(data_file)
            
        
        for i in range(100):
            temp1[i][-1] = temp1[i][-1][1:2]
            temp2[i][-1] = temp2[i][-1][2:3]
            temp3[i][-1] = temp3[i][-1][3:4]
            temp4[i][-1] = temp4[i][-1][4:5]
            temp5[i][-1] = temp5[i][-1][5:6]
            temp6[i][-1] = temp6[i][-1][6:7]
            temp7[i][-1] = temp7[i][-1][7:]
        
        print(temp1)
        final_temp.append(temp1)
        final_temp.append(temp2)
        final_temp.append(temp3)
        final_temp.append(temp4)
        final_temp.append(temp5)
        final_temp.append(temp6)
        final_temp.append(temp7)
        return final_temp
    
            
    def checkEfficiency(self,network,dataset):
        c = 0
        for j in dataset:
            k = self.encryptor.predict(network,j,0)
            s = ""
            k = list(map(str,k))
            k = s.join(k)
            p = j[-1]
            s = ""
            p= list(map(str,p))
            p = s.join(p)
            if(k != p):
                c += 1
        print("Efficiency of this decryptor is "+str(c)+" %")
 
