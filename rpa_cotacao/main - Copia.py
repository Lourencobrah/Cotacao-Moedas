import requests
import json
import pandas as pd
import openpyxl

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,CAD-BRL,GBP-BRL,ARS-BRL,BTC-BRL')

cotacoes = cotacoes.json()

#cotação dolar americano
cotacao_dolar_americano_code = cotacoes['USDBRL']['code']
cotacao_dolar_americano_codein = cotacoes['USDBRL']['codein']
cotacao_dolar_americano_name = cotacoes['USDBRL']['name']
cotacao_dolar_americano_high = cotacoes['USDBRL']['high']
cotacao_dolar_americano_low = cotacoes['USDBRL']['low']
cotacao_dolar_americano_pctchange = cotacoes['USDBRL']['pctChange']
cotacao_dolar_americano_bid = cotacoes['USDBRL']['bid']
cotacao_dolar_americano_ask = cotacoes['USDBRL']['ask']
cotacao_dolar_americano_create_date = cotacoes['USDBRL']['create_date']

#cotacao euro
cotacao_euro_code = cotacoes['EURBRL']['code']
cotacao_euro_codein = cotacoes['EURBRL']['codein']
cotacao_euro_name = cotacoes['EURBRL']['name']
cotacao_euro_high = cotacoes['EURBRL']['high']
cotacao_euro_low = cotacoes['EURBRL']['low']
cotacao_euro_pctchange = cotacoes['EURBRL']['pctChange']
cotacao_euro_bid = cotacoes['EURBRL']['bid']
cotacao_euro_ask = cotacoes['EURBRL']['ask']
cotacao_euro_create_date = cotacoes['EURBRL']['create_date']

#cotacao dolar canadense
cotacao_dolar_canadense_code = cotacoes['CADBRL']['code']
cotacao_dolar_canadense_codein = cotacoes['CADBRL']['codein']
cotacao_dolar_canadense_name = cotacoes['CADBRL']['name']
cotacao_dolar_canadense_high = cotacoes['CADBRL']['high']
cotacao_dolar_canadense_low = cotacoes['CADBRL']['low']
cotacao_dolar_canadense_pctchange = cotacoes['CADBRL']['pctChange']
cotacao_dolar_canadense_bid = cotacoes['CADBRL']['bid']
cotacao_dolar_canadense_ask = cotacoes['CADBRL']['ask']
cotacao_dolar_canadense_create_date = cotacoes['CADBRL']['create_date']

#cotacao libra
cotacao_libra_code = cotacoes['GBPBRL']['code']
cotacao_libra_codein = cotacoes['GBPBRL']['codein']
cotacao_libra_name = cotacoes['GBPBRL']['name']
cotacao_libra_high = cotacoes['GBPBRL']['high']
cotacao_libra_low = cotacoes['GBPBRL']['low']
cotacao_libra_pctchange = cotacoes['GBPBRL']['pctChange']
cotacao_libra_bid = cotacoes['GBPBRL']['bid']
cotacao_libra_ask = cotacoes['GBPBRL']['ask']
cotacao_libra_create_date = cotacoes['GBPBRL']['create_date']

#cotacao peso argentino
cotacao_peso_arg_code = cotacoes['ARSBRL']['code']
cotacao_peso_arg_codein = cotacoes['ARSBRL']['codein']
cotacao_peso_arg_name = cotacoes['ARSBRL']['name']
cotacao_peso_arg_high = cotacoes['ARSBRL']['high']
cotacao_peso_arg_low = cotacoes['ARSBRL']['low']
cotacao_peso_arg_pctchange = cotacoes['ARSBRL']['pctChange']
cotacao_peso_arg_bid = cotacoes['ARSBRL']['bid']
cotacao_peso_arg_ask = cotacoes['ARSBRL']['ask']
cotacao_peso_arg_create_date = cotacoes['ARSBRL']['create_date']

#cotacao bitcoin
cotacao_bitcoin_code = cotacoes['BTCBRL']['code']
cotacao_bitcoin_codein = cotacoes['BTCBRL']['codein']
cotacao_bitcoin_name = cotacoes['BTCBRL']['name']
cotacao_bitcoin_high = cotacoes['BTCBRL']['high']
cotacao_bitcoin_low = cotacoes['BTCBRL']['low']
cotacao_bitcoin_pctchange = cotacoes['BTCBRL']['pctChange']
cotacao_bitcoin_bid = cotacoes['BTCBRL']['bid']
cotacao_bitcoin_ask = cotacoes['BTCBRL']['ask']
cotacao_bitcoin_create_date = cotacoes['BTCBRL']['create_date']

tabela_cotacoes = pd.DataFrame(
    {
        'Cotação Dolar Americano':
         [
             cotacao_dolar_americano_code,
             cotacao_dolar_americano_codein,
             cotacao_dolar_americano_name,
             cotacao_dolar_americano_high,
             cotacao_dolar_americano_low,
             cotacao_dolar_americano_pctchange,
             cotacao_dolar_americano_bid,
             cotacao_dolar_americano_ask,
             cotacao_dolar_americano_create_date
         ],
        'Cotação Euro':
        [
            cotacao_euro_code,
            cotacao_euro_codein,
            cotacao_euro_name,
            cotacao_euro_high,
            cotacao_euro_low,
            cotacao_euro_pctchange,
            cotacao_euro_bid,
            cotacao_euro_ask,
            cotacao_euro_create_date
        ],
        'Cotação Dólar Canadense':
        [
            cotacao_dolar_canadense_code,
            cotacao_dolar_canadense_codein,
            cotacao_dolar_canadense_name,
            cotacao_dolar_canadense_high,
            cotacao_dolar_canadense_low,
            cotacao_dolar_canadense_pctchange,
            cotacao_dolar_canadense_bid,
            cotacao_dolar_canadense_ask,
            cotacao_dolar_canadense_create_date
        ],
        'Cotação Libra':
        [
            cotacao_libra_code,
            cotacao_libra_codein,
            cotacao_libra_name,
            cotacao_libra_high,
            cotacao_libra_low,
            cotacao_libra_pctchange,
            cotacao_libra_bid,
            cotacao_libra_ask,
            cotacao_libra_create_date
        ],
        'Cotação Peso Argentino':
        [
            cotacao_peso_arg_code,
            cotacao_peso_arg_codein,
            cotacao_peso_arg_name,
            cotacao_peso_arg_high,
            cotacao_peso_arg_low,
            cotacao_peso_arg_pctchange,
            cotacao_peso_arg_bid,
            cotacao_peso_arg_ask,
            cotacao_peso_arg_create_date
        ],
        'Cotação Bitcoin':
        [
            cotacao_bitcoin_code,
            cotacao_bitcoin_codein,
            cotacao_bitcoin_name,
            cotacao_bitcoin_high,
            cotacao_bitcoin_low,
            cotacao_bitcoin_pctchange,
            cotacao_bitcoin_bid,
            cotacao_bitcoin_ask,
            cotacao_bitcoin_create_date
        ],
    }
    , index=['MOEDA PRINCIPAL', 'MOEDAS SECUNDARIA', 'DE/PARA', 'VALOR MÁXIMO', 'VALOR MÍNIMIO', 'VARIAÇÃO', 'VALOR DE COMPRA', 'VALOR DE VENDA', 'DATA DE ATUALIZAÇÃO'])

print(tabela_cotacoes)

tabela_cotacoes.to_excel('cotacoes-moedas.xlsx', sheet_name='cotacoes-moedas')
