'''
    Copyright (C) 2005-17 www.interpss.org
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

import numpy as np

from py4j.java_gateway import JavaGateway

#
# define InterPSS train/test case service 
#
gateway = JavaGateway()
ipss_app = gateway.entry_point

#
# define configuration parameters
#
learning_rate = 0.001
train_steps = 10000

# 
# function to transfer data from a tensor array to a Java double array
#
def transfer2JavaDblAry(tArray, size):
    dblAry = gateway.new_array(gateway.jvm.double, size)
    i = 0
    for x in tArray:
        dblAry[i] = float(x)
        i = i + 1
    return dblAry

#
# function to transfer a Java [[x], [y]] to two Python arrays [x], [y]
#
def transfer2PyArrays(ary) :
    x = np.array([ary[0]])[0]
    y = np.array([ary[1]])[0]
    return x, y
    
#
# Output functions
#    
def printArray(ary, msg) :
    print(msg)
    for x in ary :
        print(x)
        
def print2DArray(ary2D, msg1, msg2) :
    print(msg1)
    for ary in ary2D :
        print(msg2)
        for x in ary :
            print(x)        