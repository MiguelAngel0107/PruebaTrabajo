from ..models import ConfigVariable
import numpy as np


class Bacteria():

    def __init__(self, name_config, array_init) -> None:
        if not isinstance(array_init, list):
            raise Exception("set_init debe ser un arreglo")
        try:
            configvariable = ConfigVariable.objects.filter(
                name_config=name_config).first()
        except ConfigVariable.DoesNotExist:
            # Manejar la excepción cuando no se encuentra ninguna instancia de ConfigVariable
            raise Exception("ConfigVariable no encontrada")
        except Exception as e:
            # Manejar otras excepciones inesperadas
            raise Exception(
                "Error al buscar ConfigVariable: {}".format(str(e)))

        self.days_maduration = configvariable.days_maduration
        self.days_reproduction = configvariable.days_reproduction
        self.number_divisions = configvariable.number_divisions
        self.age_start = self.days_reproduction + self.days_maduration

        self.array_init = array_init

    def search_and_change(self):
        # Convertir la lista a un arreglo de numpy
        array_init = np.array(self.array_init)

        # Obtener los elementos cero del arreglo principal
        zero_elements = array_init[array_init == 0]

        # Obtener los índices donde los elementos son cero en el arreglo original
        zero_indices = np.where(array_init == 0)[0]

        # Crear un arreglo con self.number_divisions repeticiones de self.age_start
        age_start_arr = np.full(self.number_divisions, self.age_start)

        if zero_elements.size > 0:
            # Crear un arreglo repetido de [4, 4]
            repeated_arr = np.tile(age_start_arr, zero_elements.size)

            # Insertar el arreglo repetido en los índices encontrados
            zero_elements = np.insert(zero_elements, np.repeat(np.arange(zero_elements.size), 2) + 1, repeated_arr)

            # Reemplazar los elementos iguales a 0 por self.days_reproduction
            zero_elements[zero_elements == 0] = self.days_reproduction

            # Reemplazar los elementos iguales a 0 por self.days_reproduction
            zero_elements[zero_elements == 0] = self.days_reproduction

        # Eliminar los ceros del arreglo original
        array_init = np.delete(array_init, zero_indices)

        # Restar 1 a todos los elementos
        array_init -= 1

        array_init = np.append(array_init, zero_elements)

        # Convertir el arreglo de numpy de vuelta a lista
        self.array_init = array_init.tolist()

        print(self.array_init)
