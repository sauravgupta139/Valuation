from DCF import DCF
from Pabrai import Pabrai
from BenjaminGraham import BenjaminGraham
import sys

#Discount Rate - Avg Return of index say NIFTY50
DR=12.3
#Terminal Growth Rate - 0 for stable and 2 for unstable companies
TGR=2
#EXIT Rate - Industry PE for this sector
ER=float(sys.argv[6])
#Free Cash Flow
FCF=float(sys.argv[1])

#FCF Growth Rate1 for 1-5 years
FCFGR1=float(sys.argv[2])
if FCFGR1 > 30:
	FCFGR1 = 30

#FCF Growth Rate2 for 6-10 years
FCFGR2=float(sys.argv[3])
#FCF Growth Rate3 for 6-10 years
FCFGR3=float(sys.argv[4])
#Total shares Outstanding
TSO=float(sys.argv[5])
#margin of Safety - for Stable company = 2.5/3.0, to be more safe - 2.0/3.0
MOS1=2.0/3.0
MOS2=2.5/3.0
#EPS
EPS=float(sys.argv[7])
#EPS Growth Rate
EPSGR=float(sys.argv[8])
#Repo Rate
RR=float(sys.argv[9])
#10 Year Bond Yield
Y=float(sys.argv[10])

if FCF > 0.0:
	intrinsicValuePerShareDCF=DCF(FCF,FCFGR1,FCFGR2,DR,TGR,TSO)
	intrinsicValuePerSharePabrai=Pabrai(FCF,FCFGR1,FCFGR2,FCFGR3,DR,ER,TSO)
	entryPrice1D=intrinsicValuePerShareDCF*MOS1
	entryPrice2D=intrinsicValuePerShareDCF*MOS2
	entryPrice1P=intrinsicValuePerSharePabrai*MOS1
	entryPrice2P=intrinsicValuePerSharePabrai*MOS2
	print ("Based on Discounted Cash Flow Method")
	print ("Intrinsic Value Per Share: ", intrinsicValuePerShareDCF)
	print ("Entry Price Safe: ",entryPrice1D)
	print ("Entry Price Relaxed: ",entryPrice2D)
	print ("\n")
	print ("Based on Pabrai valuation Method")
	print ("Intrinsic Value Per Share: ", intrinsicValuePerSharePabrai)
	print ("Entry Price Safe: ",entryPrice1P)
	print ("Entry Price Relaxed: ",entryPrice2P)
	print ("\n")
else:
	print ("Free Cash Flow Negative - Can't Perform DCF and Pabrai Valuation")
if EPS > 0.0:
	intrinsicValuePerShareBenjamin=BenjaminGraham(EPS,EPSGR,RR,Y)
	print ("Based on Banjamin Graham valuation Method")
	print ("Intrinsic Value Per Share: ", intrinsicValuePerShareBenjamin)
else:
	print ("EPS Negative - Can't Perform Benjamin Graham Valuation")
