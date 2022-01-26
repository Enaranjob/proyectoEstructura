class Empleado:
  secuencia=1
  Empleados=[ {"codigo":1,"nombre":"Erlyn","cedula":"09541921182","cargo":1,"departamento":1,"sueldo":"500.00"}]
  def __init__ (self,nombre,cedula,codCargo,codDepartamento,sueldo):
    Empleado.secuencia +=1
    self.codigo = Empleado.secuencia
    self.nombre = nombre
    self.cedula = cedula
    self.cargo = codCargo
    self.departamento= codDepartamento
    self.sueldo = sueldo
   
  def registro(self):
    return {"codigo":self.codigo,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"deprtamento":self.departamento,"sueldo":self.sueldo} 
    