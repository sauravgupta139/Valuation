#!/bin/bash
SYMBOL=$1
CFO=$(w3m https://in.finance.yahoo.com/quote/${SYMBOL}.NS/cash-flow?p=${SYMBOL}.NS | grep "from" | head -1)
Capex=$(w3m https://in.finance.yahoo.com/quote/${SYMBOL}.NS/cash-flow?p=${SYMBOL}.NS | grep -i "capital ")
TOS=$(w3m https://in.finance.yahoo.com/quote/${SYMBOL}.NS/key-statistics?p=${SYMBOL}.NS | grep "Shares outstanding")
PE=$(w3m "https://in.finance.yahoo.com/quote/${SYMBOL}.NS?p=${SYMBOL}.NS&.tsrc=fin-srch-v1" | grep "PE ratio" | awk '{print $4}')
EPS=$(w3m "https://in.finance.yahoo.com/quote/${SYMBOL}.NS?p=${SYMBOL}.NS&.tsrc=fin-srch-v1" | grep "EPS" | awk '{print $3}')

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
EPSGR=12
#Exit Rate - Industry PE
ER=20

python3 src/valuation.py $FCF 12.7 11.0 10.0 $os $ER $EPS $EPSGR $RR $Y
