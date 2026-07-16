# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency, locale, entries):
    if locale == 'en_US':
        # Generate Header Row
        table = 'Date'
        for _ in range(7):
            table += ' '
        table += '| Description'
        for _ in range(15):
            table += ' '
        table += '| Change'
        for _ in range(7):
            table += ' '

        entries = sorted(entries, key=lambda e: (e.date, e.change, e.description))
        for entry in entries:
            table += '\n'

            # Write entry date to table
            date_str = entry.date.strftime('%m/%d/%Y')
            table += date_str
            table += ' | '
            
            # Write entry description to table
            # Truncate if necessary
            if len(entry.description) > 25:
                description = entry.description[:22] + '...'
            else:
                description = entry.description.ljust(25)
            table += description
            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                table += format_change(entry.change, '$')
            elif currency == 'EUR':
                table += format_change(entry.change, '€')
        return table            
    elif locale == 'nl_NL':
        # Generate Header Row
        table = 'Datum'
        for _ in range(6):
            table += ' '
        table += '| Omschrijving'
        for _ in range(14):
            table += ' '
        table += '| Verandering'
        for _ in range(2):
            table += ' '

        entries = sorted(entries, key=lambda e: (e.date, e.change, e.description))
        for entry in entries:
            table += '\n'
        
            # Write entry date to table
            date_str = entry.date.strftime('%d-%m-%Y')
            table += date_str
            table += ' | '
            
            # Write entry description to table
            # Truncate if necessary
            if len(entry.description) > 25:
                description = entry.description[:22] + '...'
            else:
                description = entry.description.ljust(25)
            table += description
            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                table += format_change_nl(entry.change, '$')
            elif currency == 'EUR':
                table += format_change_nl(entry.change, '€')
        return table
def format_change(change, symbol):
    amount = abs(change) / 100
    formatted = f"{symbol}{amount:,.2f}"
    if change < 0:
        formatted = '(' + formatted + ')'
    else:
        formatted += ' '
    return formatted.rjust(13)

def format_change_nl(change, symbol):
    amount = abs(change) / 100
    formatted = f"{amount:,.2f}"
    formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
    formatted = symbol + ' ' + ('-' if change < 0 else '') + formatted
    formatted += ' '
    return formatted.rjust(13)



    
