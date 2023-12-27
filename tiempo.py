from datetime import datetime

_now = datetime.now()

# Lunes: 1, Martes: 2, Miércoles: 3, Jueves: 4, Viernes: 5, Sábado: 6, Domingo: 7

print(_now)
print(_now.hour)
print(_now.strftime(format("%w")))
_hoy = _now.strftime(format("%w"))
_hora = _now.hour

# Verificar si no es miércoles (3) ni jueves (4)
if (_hoy not in ['3']) and (11<= _hora <= 24):
    # Verificar que esté dentro de la hora
    print("Ejecutar")
else:
    print("Hoy no")
