symbol=
all: run

run:
	@bash src/run.sh ${symbol}

search:
	@grep -i "${symbol}" data/EQUITY_L.csv
