def make_car ( manufacturer, model, **car_info):

    car_info ["manufacturer"] = manufacturer
    car_info ["model"] = model

    return car_info

cars1 = make_car( "Toyota",
                "Camry",
                color = "Green",
                tow_package=True
                  
                )


cars2 = make_car ( "Toyota",
            "corrolla",
                  color = "white",
                  tow_package=False
)

print(cars1)
print(cars2)

