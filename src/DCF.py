import math

def DCF(FCF,FCFGR1,FCFGR2,DR,TGR,TSO):
	FCFi=FCF
	PV=0.0
	for i in range(1,6):
		FCFi=FCFi*(1+FCFGR1/100.0)
		PVi=FCFi/(1+DR/100.0)**i
		PV+=PVi
		#print (FCFi,PVi,"Rate 1")
	for i in range(6,11):
		FCFi=FCFi*(1+FCFGR2/100.0)
		PVi=FCFi/(1+DR/100.0)**i
		PV+=PVi
		#print (FCFi,PVi,"Rate 2")
	TV=(FCFi+1)*100.0/(DR-TGR)
	Intrinsic=(PV+TV)/TSO
	return Intrinsic
