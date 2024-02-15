car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
car["year"] = 2020
print(car.get("brand"), car.get("model"), car.get("year"), car.get("color"), sep="\n")
