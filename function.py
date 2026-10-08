def formatted_fullName (firstName, lastName):
  fullname = f"{firstName} {lastName}"
  return fullname.title()

result = formatted_fullName("hamid", "Latifa")
print(result)

def format_fullName (firstName, lastName, middleName= ''):
  if middleName:
    fullName = f"{firstName} {lastName} {middleName}"

  else:
    fullName = f"{firstName} {lastName} "

  return fullName.title()

name = format_fullName("latifa","hamid")
name2 = format_fullName("latifa","hamid","abdul")

print(name)
print(name2)