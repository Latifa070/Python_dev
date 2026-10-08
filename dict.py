person1_info ={"first-name":"Latifa",
              "last-name": "Hamid",
              "age": 26,
              "city" : "winneba"
              }

person2_info ={"first-name":"Assia",
              "last-name": "Hamid",
              "age": 22,
              "city" : "Accra"
              }
person3_info ={"first-name":"Rahamatu",
              "last-name": "salam",
              "age": 50,
              "city" : "Bawku"
              }

#storing the dictionaries in a list

people = [person1_info, person2_info, person3_info ]
for person in people:
    print(f"{person}")

cities = {"accra":["capital city of Ghana","southen part of ghana","full of job opportunities"],
          "temale":["capital town of northrn region","full of good people","its okay"],
          "bolga":["good ","okay so far", "last"]}

for key, value in cities.items():
    print(f"{key}\n {value}")