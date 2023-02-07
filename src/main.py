import tkinter as tk
from tkinter import ttk
from constrains import FONT_NAME, CITIES
from graph import Vertex, Edge, BellmanFord
from coinChange import MinCoinChange


def calc_cheapest_route():
    bellmanFord = BellmanFord()

    index_origin = 0
    for i in range(len(vertices)):
        if vertices[i].name == origin_city.get():
            index_origin = i
            break

    index_destination = 0
    for i in range(len(vertices)):
        if vertices[i].name == destination_city.get():
            index_destination = i
            break

    if bellmanFord.find_path(vertices[0], edges, len(vertices)):
        global cost
        cost = vertices[index_destination].distance
        path = bellmanFord.trace_path(vertices[index_origin], vertices[index_destination])
        output_string = f"O melhor percurso é pelas cidades {path}\n" \
                        f"Gastando um total de R$ {cost} com pedágios."
        result_cheapest_route.set(output_string)


def calc_coins():
    availability = []
    availability.append(int(coins_5_real.get()))
    availability.append(int(coins_2_real.get()))
    availability.append(int(coins_1_real.get()))
    availability.append(int(coins_50_cents.get()))
    availability.append(int(coins_25_cents.get()))
    availability.append(int(coins_10_cents.get()))
    availability = availability[::-1]
    coins = [10, 25, 50, 100, 200, 500]
    # print("aval, coin ",availability, coins)
    coin = MinCoinChange(coins, availability)
    total = int(cost * 100)
    # print(total)
    result = coin.solve(total)
    # print("Re: ",result)
    # print("Minimum coins required is", result[0])
    # print("Combination is", [coin / 100 for coin in result[1]])

    result_coins = [coin / 100 for coin in result[1]]
    string_coins = ''
    for i in result_coins:
        string_coins = string_coins + " R$ " + str(i)


    output_string1 = f"Voce vai precisar de {result[0]} moedas\n" \
                        f"Sendo elas: {string_coins}."
    result_min_coin.set(output_string1)






vertices = []
for city in CITIES:
    vertices.append(Vertex(city))

edges = [Edge(vertices[0], vertices[1], 3.50),
         Edge(vertices[1], vertices[2], 1.50),
         Edge(vertices[0], vertices[2], 30)]


window = tk.Tk()
window.title("Car Trip Planner 🚗")
window.geometry("900x700")
s = ttk.Style()
s.theme_use('clam')

title = tk.Label(text="Car Trip Planner 🚗", font=(FONT_NAME, 20, "bold"))
title.grid(columnspan=2, row=0, pady=30)


label_origin_city = tk.Label(text="Selecione a cidade de origem:", font=(FONT_NAME, 14, "bold"))
label_origin_city.grid(column=0, row=1, padx=80)

origin_city = tk.StringVar()
cb_origin_cities = ttk.Combobox(window, textvariable=origin_city, font=(FONT_NAME, 12))
cb_origin_cities['values'] = CITIES
cb_origin_cities['state'] = 'readonly'
cb_origin_cities.grid(column=0, row=2)


label_destination_city = tk.Label(text="Selecione a cidade de destino:", font=(FONT_NAME, 14, "bold"))
label_destination_city.grid(column=1, row=1)

destination_city = tk.StringVar()
cb_destination_cities = ttk.Combobox(window, textvariable=destination_city, font=(FONT_NAME, 12))
cb_destination_cities['values'] = CITIES
cb_destination_cities['state'] = 'readonly'
cb_destination_cities.grid(column=1, row=2)


btn_calc_cheapest_route = tk.Button(text="Calcular trajetória mais barata", highlightthickness=0,
                                    font=(FONT_NAME, 12, "bold"), command=calc_cheapest_route)
btn_calc_cheapest_route.grid(columnspan=2, row=3, pady=30)


result_cheapest_route = tk.StringVar()
label_cheapest_route = tk.Label(font=(FONT_NAME, 12))
label_cheapest_route['textvariable'] = result_cheapest_route
label_cheapest_route.grid(columnspan=2, row=4, pady=10)

label_coins = tk.Label(text="Informe a quantidade de moedas de cada valor que você possui:",
                       font=(FONT_NAME, 14, "bold"))
label_coins.grid(columnspan=2, row=5, pady=10)

label_5_real = tk.Label(text="R$ 5,00:", font=(FONT_NAME, 14))
label_5_real.grid(column=0, row=6)
coins_5_real = tk.StringVar()
coins_5_real.set("0")
text_coins_5_real = tk.Entry(window, textvariable=coins_5_real)
text_coins_5_real.grid(column=0, row=7)

label_2_real = tk.Label(text="R$ 2,00:", font=(FONT_NAME, 14))
label_2_real.grid(column=1, row=6)
coins_2_real = tk.StringVar()
coins_2_real.set("0")
text_coins_2_real = tk.Entry(window, textvariable=coins_2_real)
text_coins_2_real.grid(column=1, row=7)

label_1_real = tk.Label(text="R$ 1,00:", font=(FONT_NAME, 14))
label_1_real.grid(column=0, row=8)
coins_1_real = tk.StringVar()
coins_1_real.set("0")
text_coins_1_real = tk.Entry(window, textvariable=coins_1_real)
text_coins_1_real.grid(column=0, row=9)

label_50_cents = tk.Label(text="R$ 0,50:", font=(FONT_NAME, 14))
label_50_cents.grid(column=1, row=8)
coins_50_cents = tk.StringVar()
coins_50_cents.set("0")
text_coins_50_cents = tk.Entry(window, textvariable=coins_50_cents)
text_coins_50_cents.grid(column=1, row=9)

label_25_cents = tk.Label(text="R$ 0,25:", font=(FONT_NAME, 14))
label_25_cents.grid(column=0, row=10)
coins_25_cents = tk.StringVar()
coins_25_cents.set("0")
text_coins_25_cents = tk.Entry(window, textvariable=coins_25_cents)
text_coins_25_cents.grid(column=0, row=11)

label_10_cents = tk.Label(text="R$ 0,10:", font=(FONT_NAME, 14))
label_10_cents.grid(column=1, row=10)
coins_10_cents = tk.StringVar()
coins_10_cents.set("0")
text_coins_10_cents = tk.Entry(window, textvariable=coins_10_cents)
text_coins_10_cents.grid(column=1, row=11)

btn_calc_coins = tk.Button(text="Calcular quantidade de moedas", highlightthickness=0,
                                    font=(FONT_NAME, 12, "bold"), command=calc_coins)
btn_calc_coins.grid(columnspan=2, row=12, pady=30)

result_min_coin = tk.StringVar()
label_min_coin = tk.Label(font=(FONT_NAME, 12))
label_min_coin['textvariable'] = result_min_coin
label_min_coin.grid(columnspan=2, row=14, pady=10)



window.mainloop()

