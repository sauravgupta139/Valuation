symbol=
all: run

run:
	@cat data/EQUITY_L.csv | cut -f1 -d ',' | grep -iwq "${symbol}" && echo "SYMBOL "${symbol}" FOUND. Fetching Data from Internet" || (echo "Symbol Not Found. Showing Closest Match"; cat data/EQUITY_L.csv | grep -i "${symbol}"; exit 1;)	
	@bash src/run.sh ${symbol}

con:
	@cat data/EQUITY_L.csv | cut -f1 -d ',' | grep -iwq "${symbol}" && echo "SYMBOL "${symbol}" FOUND. Fetching Data from Internet" || (echo "Symbol Not Found. Showing Closest Match"; cat data/EQUITY_L.csv | grep -i "${symbol}"; exit 1;)	
	@bash src/run.sh ${symbol} consolidated

search:
	@grep -i "${symbol}" data/EQUITY_L.csv
