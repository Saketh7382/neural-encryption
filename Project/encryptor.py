#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:14:43 2020

@author: cp
"""
from random import seed
from random import random
from math import exp
import numpy as np
import timeit
import string
import json
import io

from additional import AdditionalFunctions

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

class Encryptor:
    
    ascii_list = list()
    additional = AdditionalFunctions()
    
    def main(self):
        #creating dataset for the system
        dataset = self.getDataset()
        network = self.createEncryptor(dataset,[8,16,16,8],0.5,1000)
        self.saveEncryptor(network)
        self.saveLanguage(network)
    
    
    #initializing the network
    def initialize_network(self, parameters):
        network = list()
        for j in range(1,len(parameters)):
            layer = [{'weights':[random() for i in range(parameters[j-1] + 1)]} for i in range(parameters[j])]
            network.append(layer)
        return network
    
    # Calculate neuron activation for an input
    def activate(self, weights, inputs):
        activation = weights[-1]
        for i in range(len(weights)-1):
            activation += weights[i] * inputs[i]
        return activation
    
    # Transfer neuron activation
    def transfer(self, activation):
        return 1.0 / (1.0 + exp(-activation))
    
    # Forward propagate input to a network output
    def forward_propagate(self, network, row, getEncryption):
       
        count = 0
        inputs = row
        for layer in network:
            new_inputs = []
            for neuron in layer:
                activation = self.activate(neuron['weights'], inputs)
                neuron['output'] = self.transfer(activation)
                new_inputs.append(neuron['output'])
            if count == 1 and getEncryption == 1:
                print("io")
                return new_inputs
            inputs = new_inputs
            count += 1
     
        return inputs
    
    # Calculate the derivative of an neuron output
    def transfer_derivative(self, output):
        return output * (1.0 - output)
    
    # Backpropagate error and store in neurons
    def backward_propagate_error(self, network, expected):
        
        for i in reversed(range(len(network))):
            layer = network[i]
            errors = list()
            if i != len(network)-1:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in network[i + 1]:
                        error += (neuron['weights'][j] * neuron['delta'])
                    errors.append(error)
            else:
                for j in range(len(layer)):
                    neuron = layer[j]
                    errors.append(expected[j] - neuron['output'])
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * self.transfer_derivative(neuron['output'])
                
    # Update network weights with error
    def update_weights(self, network, row, l_rate):
        
        for i in range(len(network)):
            inputs = row[:-1]
            if i != 0:
                inputs = [neuron['output'] for neuron in network[i - 1]]
            for neuron in network[i]:
                for j in range(len(inputs)):
                    neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
                neuron['weights'][-1] += l_rate * neuron['delta']
    
    # Train a network for a fixed number of epochs
    def train_network(self, network, train, l_rate, n_epoch, n_outputs):
        count = 1
        print("Training began")
        for epoch in range(n_epoch):
            sum_error = 0
            for row in train:
                count += 1
                outputs = self.forward_propagate(network, row, 0)
                expected = row[-1]
                sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
                self.backward_propagate_error(network, expected)
                self.update_weights(network, row, l_rate)
            if count % 100 == 0:
                print('> epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
            count += 1
            
    # Make a prediction with a network
    def predict(self, network, row, encr):
        outputs = self.forward_propagate(network, row, encr)
        k = [round(i) for i in outputs]
        if encr == 0:
            return k
        else:
            s = ""
            k = list(map(str,k))
            k = s.join(k)
            return k
            
    def getAsciiData(self):
        a = string.printable
        ascii_list = list()
        for i in a:
            ascii_list.append(self.additional.text_to_bits(i))
        self.ascii_list = ascii_list
        return ascii_list
    
    def getDataset(self):
        ascii_list = self.getAsciiData()
        encrypted = list()
        c = 1
        for i in ascii_list:
            t = np.random.randint(2, size= 8)
            "".join(map(str, t))
            t = "".join([str(a) for a in t])
            if t in encrypted or t in ascii_list:
                flag = 1
                while flag:
                    t = np.random.randint(2, size= 8)
                    "".join(map(str, t))
                    t = "".join([str(a) for a in t])
                    if t in encrypted or t in ascii_list:
                        flag = 1
                    else:
                        encrypted.append(t)
                        flag = 0
            else:
                encrypted.append(t)           
        #testing new random dataset
        flag = 1
        for i in encrypted:
            if i in ascii_list:
                flag = 0
                print("dataset compromised")
                break
        l = len(encrypted)
        c = len(list( dict.fromkeys(encrypted)))
        if flag == 1 and l == c:
            print("dataset clean")
            
        count = 0
        dataset = list()
        for i in ascii_list:
            k = list(i)
            k = list(map(int,k))
            j = list(encrypted[count])
            j = list(map(int,j))
            count += 1
            k.append(j)
            dataset.append(k)
            
        return dataset
    
    def createEncryptor(self,dataset,layers,l_rate,epochs):
        seed(1)
        #initializing network for encryption
        network = self.initialize_network(layers)
        n_outputs = len(dataset[0][-1])
        start = timeit.default_timer()
        self.train_network(network, dataset, l_rate, epochs, n_outputs)
        stop = timeit.default_timer()
        print("Encryptor Training Completed in = {} seconds".format(stop - start))
        return network
    
    def saveEncryptor(self, network):
        with io.open('./network/encryptor/network.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(network,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))
        
    def saveLanguage(self,network):
        new_data =list()
        for i in self.ascii_list:
            new_data.append(list(map(int,list(i))))
            
        for i in new_data:
            i.append(0)
        
        en = list()
        for i in range(len(new_data)):
            en.append(self.predict(network,new_data[i],0))
            
        for i in range(len(new_data)):
            en[i].append(new_data[i][:-1])
            
        with io.open('./data/languageDecryptor.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(en,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

