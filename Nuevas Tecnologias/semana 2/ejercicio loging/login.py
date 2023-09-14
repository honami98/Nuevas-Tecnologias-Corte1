print("------------------------------")
print("********** SIGN UP ***********")
print("------------------------------")

usu_name = input("Ingresa nombre: ")
usu_email = input("Ingresa email: ")
usu_phone = input("Ingresa número de teléfono: ")
usu_password = input("Ingresa contraseña: ")

print("------------------------------")
print("*********** LOGIN ************")
print("------------------------------")

captcha = 25

usu_validation = input("Ingrese email o número de telefono: ")
password_validation = input("Ingrese contraseña: ")
captcha_validation = input("CAPTCHA - Resuelva la siguiente ecuación: 5*5 = ?")
int_captcha = int(captcha_validation)

if usu_email == usu_validation or usu_phone == usu_validation:
    if password_validation == usu_password:
      if int_captcha == captcha:
        print("Bienvenido" , usu_name)
else:
  print("usuario o contraseña inválidos")