SYMBOL=
all: run

run:
	@bash src/run.sh ${SYMBOL}

search:
	@grep -i "${SYMBOL}" data/EQUITY_L.csv
