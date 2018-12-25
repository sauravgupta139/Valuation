#!/bin/bash
SYMBOL=$1
CFO=$(w3m https://in.finance.yahoo.com/quote/${SYMBOL}.NS/cash-flow?p=${SYMBOL}.NS | grep "from" | head -1)
Capex=$(w3m https://in.finance.yahoo.com/quote/${SYMBOL}.NS/cash-flow?p=${SYMBOL}.NS | grep -i "capital ")
TOS=$(w3m https://in.finance.yahoo.com/quote/${SYMBOL}.NS/key-statistics?p=${SYMBOL}.NS | grep "Shares outstanding")
PE=$(w3m "https://in.finance.yahoo.com/quote/${SYMBOL}.NS?p=${SYMBOL}.NS&.tsrc=fin-srch-v1" | grep "PE ratio" | awk '{print $4}')
#EPS=$(w3m "https://in.finance.yahoo.com/quote/${SYMBOL}.NS?p=${SYMBOL}.NS&.tsrc=fin-srch-v1" | grep "EPS" | awk '{print $3}')
PG=$(w3m https://www.screener.in/company/${SYMBOL}/ | grep "TTM" | head -3 | tail -1 | awk '{print $2}')
EPSLast=$(w3m https://www.screener.in/company/${SYMBOL}/ | grep "EPS" | awk '{print $NF}')
EPSPrev=$(w3m https://www.screener.in/company/${SYMBOL}/ | grep "EPS" | awk '{print $(NF-1)}')
EPSPrevPrev=$(w3m https://www.screener.in/company/${SYMBOL}/ | grep "EPS" | awk '{print $(NF-2)}')
EPSPrevPrevPrev=$(w3m https://www.screener.in/company/${SYMBOL}/ | grep "EPS" | awk '{print $(NF-3)}')
CashFlowLast=$(w3m https://www.screener.in/company/${SYMBOL} | grep "Operating" | awk '{print $NF}'| tail -1)
CashFlowPrev=$(w3m https://www.screener.in/company/${SYMBOL} | grep "Operating" | awk '{print $(NF-1)}'| tail -1)
CashFlowPrevPrev=$(w3m https://www.screener.in/company/${SYMBOL} | grep "Operating" | awk '{print $(NF-2)}'| tail -1)
CashFlowPrevPrevPrev=$(w3m https://www.screener.in/company/${SYMBOL} | grep "Operating" | awk '{print $(NF-3)}'| tail -1)
w3m https://www.screener.in/company/${SYMBOL}/ | grep "Current Price"
w3m https://www.screener.in/company/${SYMBOL}/ | grep "Market Cap"

cfo=${CFO//,}
cfoTTM=$(echo $cfo | grep -o '[-][0-9]*\|[0-9]*' | head -1)
cfolast=$(echo $cfo | grep -o '[-][0-9]*\|[0-9]*' | head -2 | tail -1)
cfolast2=$(echo $cfo | grep -o '[-][0-9]*\|[0-9]*' | head -3 | tail -1)
cfolast3=$(echo $cfo | grep -o '[-][0-9]*\|[0-9]*' | head -4 | tail -1)
#echo $cfoTTM, $cfolast, $cfolast2, $cfolast3

#Remove commas
capex=${Capex//,}
capexTTM=$(echo $capex |  grep -o '[-][0-9]*\|[0-9]*' | head -1)
capexlast=$(echo $capex | grep -o '[-][0-9]*\|[0-9]*' | head -2 | tail -1)
capexlast2=$(echo $capex | grep -o '[-][0-9]*\|[0-9]*' | head -3 | tail -1)
capexlast3=$(echo $capex | grep -o '[-][0-9]*\|[0-9]*' | head -4 | tail -1)
#echo $capexTTM, $capexlast, $capexlast2, $capexlast3

OS=$(awk '{print $4}' <<< $TOS)
#echo $OS

IFS='%' read -a pg <<< "$PG"
Pg=${pg[0]}

epsLast=${EPSLast#0}
epsPrev=${EPSPrev#0}
epsPrev2=${EPSPrevPrev#0}
epsPrev3=${EPSPrevPrevPrev#0}
#Figure out Handling divide by zero - GNFC
EPSGR1=$(bc -l <<< "($epsLast-$epsPrev)*100/$epsPrev")
EPSGR2=$(bc -l <<< "($epsPrev-$epsPrev2)*100/$epsPrev2")
EPSGR3=$(bc -l <<< "($epsPrev2-$epsPrev3)*100/$epsPrev3")
EPSGR=$(bc -l <<< "($EPSGR1+$EPSGR2+$EPSGR3)/3")
#echo $EPSGR

CFLast=${CashFlowLast//,}
CFPrev=${CashFlowPrev//,}
CFPrev2=${CashFlowPrevPrev//,}
CFPrev3=${CashFlowPrevPrevPrev//,}
CFLast=${CFLast#0}
CFPrev=${CFPrev#0}
CFPrev2=${CFPrev2#0}
CFPrev3=${CFPrev3#0}
#echo $CFLast, $CFPrev, $CFPrev2, $CFPrev3

CFG1=$(bc -l <<< "($CFLast-1*$CFPrev)*100/${CFPrev#-}")
CFG2=$(bc -l <<< "($CFPrev-1*$CFPrev2)*100/${CFPrev2#-}")
CFG3=$(bc -l <<< "($CFPrev2-1*$CFPrev3)*100/${CFPrev3#-}")
CFGR=$(bc -l <<< "($CFG1+$CFG2+$CFG3)/3")

if [[ $OS == *M* ]]; then
	IFS='M' read -a Tos <<< "$OS"
	os=$(bc -l <<< ${Tos[0]#0}/10)
elif [[ $OS == *B* ]]; then
	IFS='B' read -a Tos <<< "$OS"
	os=$(bc -l <<< ${Tos[0]#0}*100)
fi

#Free Cash Flow=Cash Flow from Operating Activities - CAPEX (already in -ve)
FCFTTM=$((${cfoTTM#0}+${capexTTM#0}))
FCFlast=$((${cfolast#0}+${capexlast#0}))
FCFlast2=$((${cfolast2#0}+${capexlast2#0}))
FCFlast3=$((${cfolast3#0}+${capexlast3#0}))

#Avg free cash flow in crores
FCF=$(((FCFTTM+FCFlast+FCFlast2+FCFlast3)/40000))
#echo $FCFTTM, $FCFlast, $FCFlast2, $FCFlast3
#echo $FCF
#echo $os

#Repo Rate
RR=6.5
#10 year Bind Yield
Y=7.5
#EPS Growth Rate
epsGR=${EPSGR#0}
#Exit Rate - Industry PE
ER=20
EPS=$EPSLast
#echo $EPS
python3 src/valuation.py $FCF $CFGR 13.0 11.0 $os $ER $EPS $epsGR $RR $Y
