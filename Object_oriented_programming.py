
class Phone:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def call(self, number):
        return f"Calling {number} from a {self.brand} phone..."

    def details(self):
        return f"Brand: {self.brand}, Color: {self.color}"


class RedmiNote15Pro(Phone):
    def __init__(self, brand, color, camera_megapixels):
        super().__init__(brand, color)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a photo with {self.camera_megapixels}MP camera 📸"

    def details(self):
        return f"{self.brand} RedmiNote15Pro in {self.color} with {self.camera_megapixels}MP camera"



phone1 = Phone("Samsung", "Black")
phone2 = RedmiNote15Pro("Xiaomi", "Blue", 200)


print(phone1.details())      
print(phone1.call("+254700000000"))

print(phone2.details())       
print(phone2.take_photo())   
print(phone2.call("+254711111111"))  


    