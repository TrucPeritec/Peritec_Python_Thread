# How to install
## Step 1:
Open command line terminal.

## Step 2:
Run this command to install<br/>
pip install -e git+https://github.com/TrucPeritec/Peritec_Python_Thread.git#egg=Peritec_Python_Thread<br/>

<br/>
<br/>

# How to upgrade
## Step 1:
Open command line terminal.

## Step 2:
Run these command to upgrade<br/>
echo y | pip uninstall Peritec_Python_Thread<br/>
pip install -e git+https://github.com/TrucPeritec/Peritec_Python_Thread.git#egg=Peritec_Python_Thread<br/>

<br/>
<br/>

# How to use
## Step 1:
Create the child class from PeritecThreadTemplate class.

## Step 2:
Define the "run" method. "run" method contain what the thread does.

## Step 3:
In the "run" method, specify the behavior for specific incomming message queue.

## Step 4:
Create instances (threads) from the class created in step 1.
