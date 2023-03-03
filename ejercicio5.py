# Cómo determinar si un año es un año bisiesto
# Para determinar si un año es bisiesto, siga estos pasos:

# 1. Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
# 2. Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
# 3. Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
# 4. El año es un año bisiesto (tiene 366 días).
# 5. El año no es un año bisiesto (tiene 365 días).https://learn.microsoft.com/es-es/office/troubleshoot/excel/determine-a-leap-year#how-to-determine-whether-a-year-is-a-leap-year

def aniobisiesto(anio: int):
    bisiesto = False
    if anio % 4 == 0 or anio % 100 == 0 and anio % 400 == 0:
        print(f"El año {anio} es bisiesto, tiene 366 días")

    else:
        print(f"El año {anio} no es bisiesto, tiene 365 días")


aniobisiesto(2009)
aniobisiesto(2004)
aniobisiesto(2400)
aniobisiesto(2017)
