simple calculator program 

to run: 
    pip install -r requirements.txt
    python -m tkinter_calculator

built using tkinter
architecture is like MVVMC, but there's no navigation, the coordinator is just doing initialization

_ReactiveProperty.py contains a function used to wrap properties in CalculatorModel.Data and observe updates
    the observed properties aren't immutable, that's one problem with this design in python
    there's a reactive framework that uses namedtuples to achieve immutability that could be worth looking into 
