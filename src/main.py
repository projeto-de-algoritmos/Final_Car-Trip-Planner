import tkinter as tk
from tkinter import ttk
from constrains import FONT_NAME, CITIES
from graph import Vertex, Edge, BellmanFord

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
        cost = vertices[index_destination].distance
        path = bellmanFord.trace_path(vertices[index_origin], vertices[index_destination])
        output_string = f"O melhor percurso é pelas cidades {path}\n" \
                        f"Gastando um total de R$ {cost} com pedágios."
        result_cheapest_route.set(output_string)

def calc_coins():
    pass


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



window.mainloop()

