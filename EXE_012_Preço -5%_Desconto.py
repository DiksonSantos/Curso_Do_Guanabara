P_ = float(input('Preço do Produto:'))
Desconto = ((P_ / 100)*5)
Total = P_ - Desconto
print('Total Da Compra{}R$ \n Com Desconto {:.0f}% \n É: {:.2f}R$'.format(P_, Desconto, Total))
