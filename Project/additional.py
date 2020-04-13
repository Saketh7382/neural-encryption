#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:52:20 2020

@author: cp
"""
import binascii

class AdditionalFunctions:
    #Funtions to calculate XOR
    def addZeros(self, strr, n): 
        for i in range(n): 
            strr = "0" + strr 
        return strr 
    
    def getXOR(self, a, b): 
        aLen = len(a) 
        bLen = len(b) 
    
    
        if (aLen > bLen): 
            b = self.addZeros(b, aLen - bLen) 
        elif (bLen > aLen): 
            a = self.addZeros(a, bLen - aLen) 
     
        lenn = max(aLen, bLen); 
    
        res = "" 
        for i in range(lenn): 
            if (a[i] == b[i]): 
                res += "0"
            else: 
                res += "1"
        return res 
    
    #functions to convert text - bits and vice versa
    def text_to_bits(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    
    def text_from_bits(self, bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return self.int2bytes(n).decode(encoding, errors)
    
    def int2bytes(self, i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))