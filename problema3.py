from datetime import datetime
import MetaTrader5 as mt5



mt5.initialize(
#  path,                     // path to the MetaTrader 5 terminal EXE file
   login=5501309,              #// account number
   password="iZqfSq3L",      #// password
   server="FxPro-MT5",          #// server name as it is specified in the terminal
#  timeout=TIMEOUT,          #// timeout
#  portable=False            #// portable mode
   )

print(mt5.terminal_info())

symbols=mt5.symbols_total()
symbols
#mt5.shutdown()