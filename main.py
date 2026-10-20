from pyscript import document

citizen_biringan = ["Guia Suarez", "Loriz Santos", "Maynard Lee", "Kandice Villanueva", "Gil Dessert", "Robert Pattinson"]

def verify_citizen(event=None):
   first_name = document.getElementById("first_name").value.strip()
   last_name = document.getElementById("last_name").value.strip()
   full_name = f"{first_name} {last_name}".title().strip()

   is_citizen = full_name in citizen_biringan
   result_element = document.getElementById("result")

   messages = {
       True: f"Welcome, {full_name}! You are a citizen of Biringan City.",
       False: f"ERROR: {full_name} is not a citizen of Biringan City."
   }
   document.getElementById("result").innerHTML = messages[is_citizen]