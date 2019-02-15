from django.shortcuts import render
from django.http import HttpResponse
from blockcypher import get_blockchain_overview, get_address_overview, get_address_details, from_satoshis


# Create your views here.

def homepage(request):

    #deveria estar em outro local
    def total_balance(address):
        total_details = get_address_details(address,coin_symbol='btc-testnet',confirmations=2)
        return from_satoshis(total_details['balance'], 'btc')

    def history(address):
        total_details = get_address_details(address,coin_symbol='btc-testnet')
        
        transaction_history = []
        if (total_details['unconfirmed_balance'] != 0):
            for tx in total_details['unconfirmed_txrefs']:
                transaction = {}
                transaction['tx_hash'] = tx['tx_hash']
                transaction['data'] = tx['received']
                transaction['confirmations'] = tx['confirmations']
                transaction['value'] = from_satoshis(tx['value'], 'btc')

                transaction_history.append(transaction)
            
        for tx in total_details['txrefs']:
            transaction = {}
            transaction['tx_hash'] = tx['tx_hash']
            transaction['data'] = tx['confirmed']
            transaction['confirmations'] = tx['confirmations']
            transaction['value'] = from_satoshis(tx['value'], 'btc')
        
            transaction_history.append(transaction)
            
        return transaction_history   
    
    endereco = 'mtHshtv1SwLAiCYaVT6gYe8c4LFFKRHovk'
    history = history(endereco)
    total = total_balance(endereco)
    return render(request = request,
                template_name = "main/home.html",
                context={"endereco":endereco, "history":history,"total":total})


def balance_api(request):
    
    total_details = blockcypher.get_address_details('mhAwG2W3WuGF27oxx58GuwqXpY1hjQLiXz',coin_symbol='btc-testnet',confirmations=2)
    return blockcypher.from_satoshis(total_details['balance'], 'btc')

