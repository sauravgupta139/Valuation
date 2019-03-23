from DCF import DCF
from Pabrai import Pabrai
from BenjaminGraham import BenjaminGraham
import sys

#Discount Rate - Avg Return of index say NIFTY50
DR=12.3
#Terminal Growth Rate - 0 for stable and 2 for unstable companies
TGR=2
#EXIT Rate - Industry PE for this sector
ER=float(sys.argv[4])
#Free Cash Flow
FCF=float(sys.argv[1])

#FCF Growth Rate1 for 1-5 years
FCFGR1=float(sys.argv[2])
#FCF Growth Rate2 for 6-10 years
FCFGR2=FCFGR1-2.0
#FCF Growth Rate3 for 7-10 years for Pabrai Method
FCFGR3=FCFGR2-2.0

#Total shares Outstanding
TSO=float(sys.argv[3])

#margin of Safety - for Stable company = 2.5/3.0, to be more safe - 2.0/3.0
MOS1=2.0/3.0
MOS2=2.5/3.0

#EPS
EPS=float(sys.argv[5])

#EPS Growth Rate
EPSGR=float(sys.argv[6])

#Repo Rate
RR=float(sys.argv[7])
#10 Year Bond Yield
Y=float(sys.argv[8])

#Current Market Price
CMP=float(sys.argv[9])

if FCF > 0.0:
	if FCFGR1 > 15:
		intrinsicValuePerShareDCF=DCF(FCF,FCFGR1,FCFGR2,DR,TGR,TSO)
		intrinsicValuePerSharePabrai=Pabrai(FCF,FCFGR1,FCFGR2,FCFGR3,DR,ER,TSO)
		entryPrice1D=intrinsicValuePerShareDCF*MOS1
		entryPrice2D=intrinsicValuePerShareDCF*MOS2
		entryPrice1P=intrinsicValuePerSharePabrai*MOS1
		entryPrice2P=intrinsicValuePerSharePabrai*MOS2
		print ("\n")
		print ("FCF and FCF Growth Taken: ",FCF,FCFGR1)
		print ("Based on Discounted Cash Flow Method")
		print ("Intrinsic Value Per Share Unrealistic: ", intrinsicValuePerShareDCF)
		print ("Entry Price Safe: ",entryPrice1D)
		print ("Entry Price Relaxed: ",entryPrice2D)
		print ("\n")
		print ("Based on Pabrai valuation Method")
		print ("Intrinsic Value Per Share Unrealistic: ", intrinsicValuePerSharePabrai)
		print ("Entry Price Safe: ",entryPrice1P)
		print ("Entry Price Relaxed: ",entryPrice2P)
		print ("\n")
		FCFGR1 = 15
		FCFGR2=FCFGR1-2.0
		FCFGR3=FCFGR2-2.0
	intrinsicValuePerShareDCF=DCF(FCF,FCFGR1,FCFGR2,DR,TGR,TSO)
	intrinsicValuePerSharePabrai=Pabrai(FCF,FCFGR1,FCFGR2,FCFGR3,DR,ER,TSO)
	entryPrice1D=intrinsicValuePerShareDCF*MOS1
	entryPrice2D=intrinsicValuePerShareDCF*MOS2
	entryPrice1P=intrinsicValuePerSharePabrai*MOS1
	entryPrice2P=intrinsicValuePerSharePabrai*MOS2
	print ("\n")
	print ("FCF and FCF Growth Taken: ",FCF,FCFGR1)
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
	print ("\n")
	print ("Free Cash Flow Negative - Can't Perform DCF and Pabrai Valuation")
if EPS > 0.0:
	if EPSGR > 13:
		print ("\n")
		print ("EPS and EPS Growth Rate Taken: ",EPS,EPSGR)
		print ("Based on Banjamin Graham valuation Method")
		intrinsicValuePerShareBenjaminUnrealistic=BenjaminGraham(EPS,EPSGR,RR,Y)
		EPSGR=13
		print ("Intrinsic Value Per Share Unrealistic: ", intrinsicValuePerShareBenjaminUnrealistic)
	intrinsicValuePerShareBenjamin=BenjaminGraham(EPS,EPSGR,RR,Y)
	print ("\n")
	print ("EPS and EPS Growth Rate Taken: ",EPS,EPSGR)
	print ("Based on Banjamin Graham valuation Method")
	print ("Intrinsic Value Per Share: ", intrinsicValuePerShareBenjamin)
else:
	print ("\n")
	print ("EPS Negative - Can't Perform Benjamin Graham Valuation")
print ("\n")

if FCF > 0 and EPS > 0:
	if CMP < entryPrice1D and CMP < entryPrice1P and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: OUTRIGHT BUY")
	elif CMP < entryPrice1D and CMP < entryPrice2P and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: OUTRIGHT BUY")
	elif CMP < entryPrice1D and CMP < entryPrice1P and CMP > intrinsicValuePerShareBenjamin :
		print ("MSG: BUY with Caution")
	elif CMP < entryPrice1D and CMP < entryPrice2P and CMP > intrinsicValuePerShareBenjamin :
		print ("MSG: BUY with Caution")
	elif CMP < entryPrice1D and CMP > entryPrice1P and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: BUY with Caution")
	elif CMP < entryPrice1D and CMP > entryPrice2P and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: BUY with Caution")
	elif CMP < intrinsicValuePerShareDCF and CMP < intrinsicValuePerSharePabrai and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: HOLD")
	elif CMP < intrinsicValuePerShareDCF and CMP < intrinsicValuePerSharePabrai and CMP > intrinsicValuePerShareBenjamin :
		print ("MSG: HOLD with caution")
	elif CMP < intrinsicValuePerShareDCF and CMP > intrinsicValuePerSharePabrai and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: HOLD")
	elif CMP < intrinsicValuePerShareDCF and CMP > intrinsicValuePerSharePabrai and CMP > intrinsicValuePerShareBenjamin :
		print ("MSG: HOLD with Caution")
	elif CMP > intrinsicValuePerShareDCF and CMP > intrinsicValuePerSharePabrai and CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: Hold with Caution or Sell")
	elif CMP > intrinsicValuePerShareDCF and CMP > intrinsicValuePerSharePabrai and CMP > intrinsicValuePerShareBenjamin :
		print ("MSG: Sell")
	else:
		print ("MSG: Sell")
elif FCF < 0 and EPS > 0:
	if CMP < intrinsicValuePerShareBenjamin :
		print ("MSG: BUY only Banks and NBFC else Sell")
	elif EPSGR > 13 :
		if CMP < intrinsicValuePerShareBenjaminUnrealistic :
			print ("MSG: Hold only Banks and NBFC else Sell")
	else:
		print ("MSG: Sell")
elif FCF > 0 and EPS < 0:
	if CMP < entryPrice1D and CMP < entryPrice1P :
		print ("MSG: BUY with Caution")
	elif CMP < entryPrice1D and CMP < entryPrice2P :
		print ("MSG: Hold or Sell")
	else:
		print ("MSG: Sell")
else:
	print ("MSG: Sell")
print ("******************************************")
