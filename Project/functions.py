#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:23:16 2020

@author: cp
"""
import json
import zlib, base64
from datetime import datetime
from additional import AdditionalFunctions
from encryptor import Encryptor

class Functionalities:
    additional = AdditionalFunctions()
    encryptor = Encryptor()
    def checkEfficiency(self):
        k = list()
        with open('./network/encryptor/network.json') as data_file:
            network = json.load(data_file)
        n = self.encryptor.getAsciiData()
        dataset = list()
        for i in n:
            i = list(i)
            i = list(map(int,i))
            i.append(0)
            dataset.append(i)
            
        for i in range(100):
            k.append(self.encryptor.predict(network, dataset[i], 0))
            k[i].append(dataset[i][:-1])
            
        c = list()
        for i in k:
            s = ""
            i = list(map(str,i))
            c.append(s.join(i))
            
        s = "Network is {}% efficient".format(len(list( dict.fromkeys(c))))
        return s
        
    def beginEncryption(self, file_path):
        with open('./network/encryptor/network.json') as data_file:
            network = json.load(data_file)
        data = list()
        f=open(file_path,"r")
        line=f.readline()
        while line!='':
            data.append(line)
            line=f.readline()
        bit_data = list()
        for i in data:
            bit_data.append(self.additional.text_to_bits(i))
        flag = 1
        for i in range(len(bit_data)):
            if ((len(bit_data[i]))%8) != 0:
                print("data corrupted")
                flag = 0
                break
        if flag:
            input_data = list()
            for i in bit_data:
                l = len(i)
                k = int(l/8)
                c = 0
                for j in range(k):
                    s = i[c:c+8]
                    input_data.append(s)
                    c += 8
                    
            c = 0
            for i in bit_data:
                l = len(i)
                c += int(l/8)
            
            if c == len(input_data):
                print("data input is ready")
                
            bit_data = list()
            for i in input_data:
                a = list(i)
                b = list(i)
                a = list(map(int,a))
                b = list(map(int,b))
                a.append(b)
                bit_data.append(a)
                
            input_data = list()
            for i in bit_data:
                input_data.append(self.encryptor.predict(network,i,0))
                
            bit_data = list()
            for i in input_data:
                s = ""
                i = list(map(str,i))
                bit_data.append(s.join(i))
                
            s = ""
            for i in bit_data:
                s += i
                
            code =  base64.b64encode(zlib.compress(s.encode('utf-8'),9))
            code = code.decode('utf-8')
            now = datetime.now()
            d1 = "./data/encrypted/"+now.strftime("%Y_%m_%d_%H%M%S")+".txt"
            f=open(d1,'w')
            f.write(code)
            f.close()
            
            s = "Encrypting the file \n{} \nis successfully completed".format(file_path.split("/")[-1])
            s += "\nEncrypted file stored at: \n{}".format(d1)
            
            return s

    def beginDecryption(self, file_path):
        with open('./network/decryptor/network_bit_2.json') as data_file:
            network2 = json.load(data_file)
        with open('./network/decryptor/network_bit_3.json') as data_file:
            network3 = json.load(data_file)
        with open('./network/decryptor/network_bit_4.json') as data_file:
            network4 = json.load(data_file)
        with open('./network/decryptor/network_bit_5.json') as data_file:
            network5 = json.load(data_file)
        with open('./network/decryptor/network_bit_6.json') as data_file:
            network6 = json.load(data_file)
        with open('./network/decryptor/network_bit_7.json') as data_file:
            network7 = json.load(data_file)
        with open('./network/decryptor/network_bit_8.json') as data_file:
            network8 = json.load(data_file)
        
        print("Enter path to encrypted file")
        file = open(file_path,'r')
        text = file.read()
        file.close()
        
        decoded_txt = zlib.decompress(base64.b64decode(text))
        output = decoded_txt.decode()
        
        if len(output)%8 != 0:
            print("corrupted data")
        else:
            c = 0
            l = len(output)
            k = int(l/8)
            s = ""
            for i in range(k):
                word = list(output[c:c+8])
                word = list(map(int,output[c:c+8]))
                word.append(0)
                s += "0"
                s += self.encryptor.predict(network2,word,2)
                s += self.encryptor.predict(network3,word,3)
                s += self.encryptor.predict(network4,word,2)
                s += self.encryptor.predict(network5,word,2)
                s += self.encryptor.predict(network6,word,2)
                s += self.encryptor.predict(network7,word,2)
                s += self.encryptor.predict(network8,word,2)
                c += 8
                
            
            c = 0
            l = len(output)
            k = int(l/8)
            o = ""
            for i in range(k):
                u = self.additional.text_from_bits(s[c:c+8])
                o += u
                c += 8
            
            now = datetime.now()
            d1 = "./data/decrypted/"+now.strftime("%Y_%m_%d_%H%M%S")+".txt"
            f=open(d1,'w')
            f.write(o)
            f.close()
                
            s = "Decrypting the file \n{} \nis successfully completed".format(file_path.split("/")[-1])
            s += "\nDecrypted file stored at \n{}".format(d1)
            
            return s
            