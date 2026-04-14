class programmer:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The programmer name is {self.name}")

class language:
    def __init__(self, lang):
        self.lang = lang
    def show(self):
        print(f"The programming language is {self.lang}")

class sport:
    def __init__(self, sp):
        self.sp = sp
    def show(self):
        print(f"He is a good player of {self.sp}")

class id:
    def __init__(self, i):
        self.i = i
    def show(self):
        print(f"The programmer id is {self.i}")

class allinformation_programmer(programmer, id, language, sport):
    def __init__(self, name, i, lang, sp):
        programmer.__init__(self, name)
        id.__init__(self, i)
        language.__init__(self, lang)
        sport.__init__(self, sp)

object1 = allinformation_programmer("nitesh", 234, "python", "cricket")


print(object1.name)   # programmer name
print(object1.i)      # programmer id
print(object1.lang)   # programming language
print(object1.sp)     # sport



def test(a, b=2, c=3):
    return a + b + c

print(test(4, c=5))


from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'distance_km': [2.5, 3.0, 4.2, 1.8],
    'traffic': [1, 2, 3, 1],  # 1=low,2=medium,3=high
    'time_of_day': [9, 18, 8, 15],  # hour of day
    'weather': [0, 1, 0, 0],  # 0=clear, 1=rain
    'eta_min': [8, 15, 20, 6]  # actual travel time
})

X = data[['distance_km', 'traffic', 'time_of_day', 'weather']]
y = data['eta_min']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Predict ETA for new trip
test = [[3.0, 2, 9, 0]]  # 3 km, medium traffic, 9 AM, clear weather
print("Predicted ETA:", model.predict(test)[0], "minutes")

