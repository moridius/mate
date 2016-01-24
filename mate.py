#!/usr/bin/env python3

import sys

### Konfiguration ###
# Pfad zur Kontostand-Datei
mate_file = None
# Preis für eine Mate
mate_price = 1.2
#####################

def ReadFile():
    try:
        with open( mate_file, 'r' ) as f:
            return float( f.read() )
    except:
        return 0.0

def WriteFile( deposit ):
    with open( mate_file, 'w' ) as f:
        f.write( str( deposit ) )

def ModDeposit( deposit, change ):
    deposit += val
    print( ("{:.2f}€ ".format( abs(val) )).replace('.', ','), end='' )
    if val < 0:
        print( "abgezogen." )
    else:
        print( "eingezahlt." )
    return deposit

def PrintDeposit( deposit ):
    print( ("Kontostand: {:+.2f}€ ".format( deposit )).replace('.', ',') )

def PrintHelp():
    print( "mate - ein Skript um meinen Kontostand in der Getränkekasse unseres Club-Hauses zu speichern.\n" )
    print( "Beispiele:" )
    print( "  $ mate" )
    print( "  > Kontostand: 2,30€\n" )
    print( "  $ mate +3" )
    print( "  > 3,00€ eingezahlt.\n" )
    print( "  $ mate -1,5" )
    print( "  > 1,50€ abgezogen.\n" )
    print( "  $ mate -" )
    print( "  > 1,20€ abgezogen." )

if __name__ == "__main__":
    if not mate_file or not mate_price:
        print( "Im Skript stehen oben ein paar Settings, die du anpassen solltest. Ja, ich weiß, dass das ekelig ist. ;-)", file=sys.stderr )
        sys.exit(1)
    
    deposit = ReadFile()

    if len( sys.argv ) > 1:
        if "help" in sys.argv[1]:
            PrintHelp()
            sys.exit(0)
        elif sys.argv[1].startswith('+') or sys.argv[1].startswith('-'):
            val = 0
            if sys.argv[1] == '-':
                val = (-1) * mate_price
            else:
                try:
                    val = float( sys.argv[1].replace(',', '.') )
                except ValueError:
                    print( "Parameter-Fehler.", file=sys.stderr )
                    sys.exit(2)

            deposit = ModDeposit( deposit, val )

            WriteFile( deposit )

    PrintDeposit( deposit )
