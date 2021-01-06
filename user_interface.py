from feature_library import features
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tkinter as tk

# testing with custom inputs
# load the model from disk
path = r'Model\finalized_RFmodel.sav'

loaded_model = pickle.load(open(path, 'rb'))

# data used as reference to scale user input
inputs = pd.read_json('Data/model_inputs.json')


def predict_price():
    if living_space_input() < 20:
        return None

    new_features = features
    new_features['livingSpace'] = living_space_input()
    new_features['buildingAge'] = building_choice()
    new_features['newlyConst'] = newlyConst()
    new_features['balcony'] = balcony_choice()
    new_features['hasKitchen'] = kitchen_choice()
    new_features['cellar'] = cellar_choice()
    new_features['lift'] = lift_choice()
    new_features['garden'] = garden_choice()


    for key in new_features:
        if flat_choice().replace(' ', '_').lower() in key:
            print(key)
            print(new_features[key])
            new_features[key] = 1
            break

    for key in new_features:
        # print(area_choice())
        if area_choice() in key:
            print(key)
            new_features[key] = 1
            break

    print(new_features)
    new_inputs = pd.DataFrame(data=new_features, index=[0])
    new_inputs = new_inputs.append(inputs, ignore_index=True)
    scaler = StandardScaler()
    scaler.fit(new_inputs)
    new_inputs_scaled = scaler.transform(new_inputs)
    X_input = new_inputs_scaled

    pred_rf = loaded_model.predict(X_input)
    print('Approx. total rent:', round(pred_rf[0], 2))
    estimate_label2.config(text=f'{round(pred_rf[0], 2)} €/month')

    for key in new_features:
        new_features[key] = 0


# GUI
window = tk.Tk()
window.minsize(width=300, height=500)
window.title('Apartment Rental Price Estimator')

# label for space
ghost_label = tk.Label(text='', width=5)
ghost_label.grid(row=0, column=4)
# label for space2
ghost_label2 = tk.Label(text='', width=25)
ghost_label2.grid(row=11, column=1)

# Button
button = tk.Button(text='Price Estimate', command=predict_price)
button.config(width=10, height=2)
button.config(pady=10, padx=10)
button.grid(row=9, column=1)
# bind button to 'enter' key
window.bind('<Return>', lambda event=None: button.invoke())

# estimate label1
estimate_label1 = tk.Label(text='Estimated apartment\nrental price:')
estimate_label1.grid(row=10, column=0)
estimate_label1.config(pady=30, padx=20)

# estimate label2
estimate_label2 = tk.Label(text='')
estimate_label2.grid(row=10, column=1)
estimate_label2.config(pady=30, padx=20)


def living_space_input():
    while True:
        try:
            user_input = float(my_input1.get())
        except ValueError:
            return 0
        else:
            return user_input


## Living Space
# input living space
my_input1 = tk.Entry(width=10, justify='center', takefocus=1)
my_input1.grid(row=0, column=1)
# label living space
living_space_label = tk.Label(text='Living Space (min. 20m²)* :')
living_space_label.grid(row=0, column=0)
living_space_label.config(pady=10, padx=5)
# unit label
unit_label = tk.Label(text='m²', width=2)
unit_label.grid(row=0, column=2)
unit_label.config(pady=10, padx=5)




## Balcony
def balcony_choice():
    return int(radio_state1.get())


# Variable to hold on to which radio button value is checked.
radio_state1 = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Yes", value=1, variable=radio_state1, command=balcony_choice)
radiobutton2 = tk.Radiobutton(text="No", value=0, variable=radio_state1, command=balcony_choice)
radiobutton1.grid(row=2, column=1)
radiobutton2.grid(row=2, column=2)
# balcony_label
balcony_label = tk.Label(text='Balcony :', width=5)
balcony_label.grid(row=2, column=0)
balcony_label.config(pady=10, padx=5)


# Built-in_Kitchen
def kitchen_choice():
    return int(radio_state2.get())


radio_state2 = tk.IntVar()
radiobutton3 = tk.Radiobutton(text="Yes", value=1, variable=radio_state2, command=kitchen_choice)
radiobutton4 = tk.Radiobutton(text="No", value=0, variable=radio_state2, command=kitchen_choice)
radiobutton3.grid(row=3, column=1)
radiobutton4.grid(row=3, column=2)
# balcony_label
built_in_kitchen = tk.Label(text='Built-in\nKitchen :', width=5)
built_in_kitchen.grid(row=3, column=0)
built_in_kitchen.config(pady=10, padx=5)


## cellar
def cellar_choice():
    return int(radio_state3.get())


# Variable to hold on to which radio button value is checked.
radio_state3 = tk.IntVar()
radiobutton5 = tk.Radiobutton(text="Yes", value=1, variable=radio_state3, command=cellar_choice)
radiobutton6 = tk.Radiobutton(text="No", value=0, variable=radio_state3, command=cellar_choice)
radiobutton5.grid(row=4, column=1)
radiobutton6.grid(row=4, column=2)
# cellar_label
cellar = tk.Label(text='Cellar :', width=5)
cellar.grid(row=4, column=0)
cellar.config(pady=10, padx=5)


## lift
def lift_choice():
    return int(radio_state4.get())


# Variable to hold on to which radio button value is checked.
radio_state4 = tk.IntVar()
radiobutton7 = tk.Radiobutton(text="Yes", value=1, variable=radio_state4, command=lift_choice)
radiobutton8 = tk.Radiobutton(text="No", value=0, variable=radio_state4, command=lift_choice)
radiobutton7.grid(row=5, column=1)
radiobutton8.grid(row=5, column=2)
# balcony_label
lift = tk.Label(text='Lift :', width=5)
lift.grid(row=5, column=0)
lift.config(pady=10, padx=5)


## garden
def garden_choice():
    return int(radio_state5.get())


# Variable to hold on to which radio button value is checked.
radio_state5 = tk.IntVar()
radiobutton9 = tk.Radiobutton(text="Yes", value=1, variable=radio_state5, command=garden_choice)
radiobutton8 = tk.Radiobutton(text="No", value=0, variable=radio_state5, command=garden_choice)
radiobutton9.grid(row=6, column=1)
radiobutton8.grid(row=6, column=2)
# balcony_label
garden = tk.Label(text='Garden :', width=5)
garden.grid(row=6, column=0)
garden.config(pady=10, padx=5)


## building_age
def newlyConst():
    return int(radio_state6.get())

radio_state6 = tk.IntVar()
radiobutton10 = tk.Radiobutton(text="Yes", value=1, variable=radio_state6, command=newlyConst)
radiobutton11 = tk.Radiobutton(text="No", value=0, variable=radio_state6, command=newlyConst)
radiobutton10.grid(row=2, column=1)
radiobutton11.grid(row=2, column=2)
# balcony_label
newlyConst_label = tk.Label(text='Newly built:')
newlyConst_label.grid(row=2, column=0)
newlyConst_label.config(pady=10, padx=5)


# building_age
def building_choice():
    while True:
        try:
            user_input = int(my_input7.get())
        except ValueError:
            return 0
        else:
            return user_input


## Living Space
# input living space
my_input7 = tk.Entry(width=10, justify='center', takefocus=1)
my_input7.grid(row=1, column=1)
# label living space
building_label = tk.Label(text='Building age (in years) :')
building_label.grid(row=1, column=0)
building_label.config(pady=10, padx=5)


# type of flat
def flat_choice(*args):
    return tkvar1.get()


# Create a dropdown menu for conversion options
# Create a Tkinter variable
tkvar1 = tk.StringVar()
# Tuple with options
options_flats = ('Apartment', 'Ground floor', 'Half basement', 'Loft',
                 'Maisonette', 'Penthouse', 'Raised ground floor',
                 'Roof storey', 'Terraced flat')

tkvar1.set('Apartment')  # set the default option
popupMenu1 = tk.OptionMenu(window, tkvar1, *options_flats)
# popupMenu1.config(width=10)
popupMenu1.grid(row=7, column=1)
# flat label
flat_label = tk.Label(text='Type of flat :')
flat_label.grid(row=7, column=0)
flat_label.config(pady=10, padx=10)


# Berlin area
def area_choice(*args):
    return tkvar2.get()


tkvar2 = tk.StringVar()
options_areas = ('Buchholz',
                 'Charlottenburg',
                 'Friedrichshain',
                 'Hellersdorf',
                 'Hohenschönhausen',
                 'Kreuzberg',
                 'Köpenick',
                 'Lichtenberg',
                 'Marzahn',
                 'Mitte',
                 'Neukölln',
                 'Pankow',
                 'Prenzlauer Berg',
                 'Reinickendorf',
                 'Schöneberg',
                 'Spandau',
                 'Steglitz',
                 'Tempelhof',
                 'Tiergarten',
                 'Treptow',
                 'Wedding',
                 'Weißensee',
                 'Wilmersdorf',
                 'Zehlendorf')

tkvar2.set('Mitte')  # set the default option

popupMenu2 = tk.OptionMenu(window, tkvar2, *options_areas)
# popupMenu2.config(width=15)
popupMenu2.grid(row=8, column=1)
# area label
area_label = tk.Label(text='Flat\n location :', width=5)
area_label.grid(row=8, column=0)
area_label.config(pady=10, padx=10)

window.mainloop()

