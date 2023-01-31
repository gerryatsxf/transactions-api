

class TransferPipeline(object):

    def __init__(self, items):
        self.items = items

    def run(self):
        items = self.items 
        items = self.cashDepositPipe(items)
        items = self.cashWithdrawalPipe(items)
        items = self.creditPaymentPipe(items)
        items = self.paymentFromDebitPipe(items)
        return items 

    def cashDepositPipe(self, items):
        key = 'DEPOSITO EN EFECTIVO ATM'
        newMemo = 'cash-deposit'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items

    def cashWithdrawalPipe(self, items):
        key = 'BANCO SANTANDER'
        newMemo = 'cash-withdrawal'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items

    def creditPaymentPipe(self, items):
        key = 'CARGO PAGO TARJETA CREDITO'
        newMemo = 'credit-payment'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items

    def paymentFromDebitPipe(self, items):
        key = 'PAGO POR TRANSFERENCIA'
        newMemo = 'payment-from-debit'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items