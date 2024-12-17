import random
import pandas

name = ["alex", "betty", "andreas", "annabelle", "lucifer"]

name_scores = {n : random.randint(1, 100) for n in name}
dic = pandas.DataFrame([name_scores])
passed_student = {student : name_scores[student] for student in name_scores if name_scores[student] > 60}
dic_passed = pandas.DataFrame([passed_student])
print(dic)
print(dic_passed)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key : (value * 9/5 + 32) for (key, value) in weather_c.items()}

print(weather_f)