import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        # set columns
        self.cols = 1
        
        # create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
               
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))       
        # Add input box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Favorite pizza: "))       
        # Add input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Favorite ingredient: "))       
        # Add input box
        self.ingredient = TextInput(multiline=False)
        self.top_grid.add_widget(self.ingredient)
        
        # Add the new top grid to app
        self.add_widget(self.top_grid)
        
        
        #create Submit btn
        self.submit = Button(text="Submit", font_size=32)
        # bind the submit button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        
    def press(self, instance):
        name = self.name.text
        pizza= self.pizza.text
        ingredient= self.ingredient.text
        
        # print(f"Hello {name}, you like {pizza} pizza with {ingredient} ingredient")
        # print it to the screen
        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza with {ingredient} ingredient"))  
        # clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.ingredient.text = ""
        
        
        
        
        
        
        
    
    


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()
    
