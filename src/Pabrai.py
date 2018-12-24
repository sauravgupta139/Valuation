import math

def Pabrai(FCF,FCFGR1,FCFGR2,FCFGR3,DR,ER,TSO):
	FCFi=FCF
	PV=0.0
	for i in range(1,4):
		FCFi=FCFi*(1+FCFGR1/100.0)
		PVi=FCFi/(1+DR/100.0)**i
		PV+=PVi
		#print (FCFi,PVi,"Rate 1")
	for i in range(4,7):
		FCFi=FCFi*(1+FCFGR2/100.0)
		PVi=FCFi/(1+DR/100.0)**i
		PV+=PVi
		#print (FCFi,PVi,"Rate 2")
	for i in range(7,11):
		FCFi=FCFi*(1+FCFGR3/100.0)
		PVi=FCFi/(1+DR/100.0)**i
		PV+=PVi
		#print (FCFi,PVi,"Rate 3")
	#Exit Value
	EV=FCFi*ER/(1+DR/100.0)**10
	Intrinsic=(PV+EV)/TSO
	return Intrinsic
