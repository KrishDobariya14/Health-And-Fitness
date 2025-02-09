import tkinter as tk
from tkinter import messagebox

class HealthAndWellnessTracker:
    def __init__(self):
        self.water_intake = 0  # in liters
        self.exercise_minutes = 0  # in minutes
        self.sleep_hours = 0  # in hours
        self.height = 0  # in meters
        self.weight = 0  # in kilograms

    def log_water(self, liters):
        self.water_intake += liters

    def log_exercise(self, minutes):
        self.exercise_minutes += minutes

    def log_sleep(self, hours):
        self.sleep_hours += hours

    def log_height_and_weight(self, height, weight):
        self.height = height
        self.weight = weight

    def assess_health(self):
        if self.height > 0 and self.weight > 0:
            bmi = self.weight / (self.height ** 2)
            assessment = f"Your BMI is {bmi:.2f}!\n"

            if bmi < 18.5:
                assessment += "You are underweight. Consider a nutritious diet.\n"
                recommendation = "Diet: High-calorie meals including nuts, dairy, lean meats, and whole grains."
            elif 18.5 <= bmi < 24.9:
                assessment += "You have a normal weight. Maintain your lifestyle!\n"
                recommendation = "Exercise: 30 minutes of moderate workouts like jogging or yoga."
            elif 25 <= bmi < 29.9:
                assessment += "You are overweight. Consider regular exercise and a balanced diet.\n"
                recommendation = "Exercise: Cardio workouts like running, cycling, or swimming for 45 minutes daily."
            else:
                assessment += "You are obese. Consult a healthcare professional.\n"
                recommendation = "Gym: 3 days a week focusing on cardio and light weight training."

            return assessment + recommendation
        else:
            return "Height and weight must be set to assess health."

    def check_recommendations(self):
        recommendations = ""
        if self.water_intake >= 2:
            recommendations += f"Water Intake: {self.water_intake}L (Goal Met!)\n"
        else:
            recommendations += f"Water Intake: {self.water_intake}L (Drink more water!)\n"

        if self.exercise_minutes >= 30:
            recommendations += f"Exercise: {self.exercise_minutes} minutes (Goal Met!)\n"
        else:
            recommendations += f"Exercise: {self.exercise_minutes} minutes (Add more activity!)\n"

        if self.sleep_hours >= 7:
            recommendations += f"Sleep: {self.sleep_hours} hours (Goal Met!)\n"
        else:
            recommendations += f"Sleep: {self.sleep_hours} hours (Get more rest!)\n"

        return recommendations

class HealthApp:
    def __init__(self, root):
        self.tracker = HealthAndWellnessTracker()
        self.root = root
        self.root.title("Health & Wellness Tracker")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Log Water Intake (L):").grid(row=0, column=0, padx=10, pady=5)
        self.water_entry = tk.Entry(self.root)
        self.water_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Log Water", command=self.log_water).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.root, text="Log Exercise (Minutes):").grid(row=1, column=0, padx=10, pady=5)
        self.exercise_entry = tk.Entry(self.root)
        self.exercise_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Log Exercise", command=self.log_exercise).grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self.root, text="Log Sleep (Hours):").grid(row=2, column=0, padx=10, pady=5)
        self.sleep_entry = tk.Entry(self.root)
        self.sleep_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Log Sleep", command=self.log_sleep).grid(row=2, column=2, padx=10, pady=5)

        tk.Label(self.root, text="Height (Meters):").grid(row=3, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Weight (Kg):").grid(row=4, column=0, padx=10, pady=5)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=4, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Set Height & Weight", command=self.set_height_and_weight).grid(row=4, column=2, padx=10, pady=5)

        tk.Button(self.root, text="Assess Health", command=self.assess_health).grid(row=5, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Check Recommendations", command=self.check_recommendations).grid(row=6, column=0, columnspan=3, pady=10)

    def log_water(self):
        try:
            liters = float(self.water_entry.get())
            self.tracker.log_water(liters)
            messagebox.showinfo("Success", f"Logged {liters}L of water.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def log_exercise(self):
        try:
            minutes = int(self.exercise_entry.get())
            self.tracker.log_exercise(minutes)
            messagebox.showinfo("Success", f"Logged {minutes} minutes of exercise.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def log_sleep(self):
        try:
            hours = float(self.sleep_entry.get())
            self.tracker.log_sleep(hours)
            messagebox.showinfo("Success", f"Logged {hours} hours of sleep.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def set_height_and_weight(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            self.tracker.log_height_and_weight(height, weight)
            messagebox.showinfo("Success", f"Height and weight set to {height}m and {weight}kg.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for height and weight.")

    def assess_health(self):
        assessment = self.tracker.assess_health()
        messagebox.showinfo("Health Assessment", assessment)

    def check_recommendations(self):
        recommendations = self.tracker.check_recommendations()
        messagebox.showinfo("Recommendations", recommendations)

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthApp(root)
    root.mainloop()