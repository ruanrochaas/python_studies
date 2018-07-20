qtd_cesta = float(raw_input())
qtd_bananas = float(raw_input())
qtd_goiabas = float(raw_input())
qtd_mangas = float(raw_input())

qtd_tot_frutas = qtd_bananas + qtd_goiabas + qtd_mangas

tempo = qtd_tot_frutas/qtd_cesta

if qtd_tot_frutas%qtd_cesta != 0:
    tempo += 1

print("%d" %tempo)