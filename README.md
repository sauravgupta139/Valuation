This code should be run in unix/linux

It fetches data from yahoo.com and screener.in for Indian Bourses.
If someone wants to use it for other stock exchanges then alternative
 of screener.in has to be found to get the datas such as EPS and Cash Flow.
Edit the file run.sh and make necessary changes.

Prerequisites-  
1. Python 3
2. Bash Shell (else use method 3)
3. Install w3m
	sudo apt-get install w3m

Info
1. Data Picked from - https://in.finance.yahoo.com/
	and https://www.screener.in/dash/


#To run
go to Terminal
1. Method 1
bash run.sh <SCRIP> 
for eg bash run.ch HDFC

2. Method 2
make SYMBOL=<SCRIP>
for eg make SYMBOL=HDFC

3. Method 3
python3 valuation.py <Free Cash Flow>  <Cash Flow Growth Rate> <Cash Flow Growth Rate 1> <Cash Flow Growth Rate2> <outstanding shares> <Exit Rate> <EPS> <EPS Growth Rate> <Repo Rate> <10 year Govt. Bond Yield>

