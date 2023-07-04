from ..models import ConfigVariable, Lote
import numpy as np
import gc


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

    def split_and_evaluate(self, iter):
        array_init = np.array(self.array_init)

        # Obtener el tamaño actual del arreglo
        array_size = len(array_init)

        if array_size <= 1000000:  # 800000000 #6
            next(self.search_and_change_generator())
        else:
            sub_arrays = np.array_split(
                array_init, array_size // 10000)  # 800000 #4
            first_array = sub_arrays.pop(0)

            print('Entre a la Base')

            self.storage_lotes(sub_arrays, iter)
            print("\n")
            print('Sali de La Base')

            self.array_init = first_array
            next(self.search_and_change_generator())

    def storage_lotes(self, sub_arrays, iter):
        for index, sub_array in enumerate(sub_arrays):
            # print(sub_array)
            # print(type(sub_array))
            Lote.objects.create(
                id_lote="ABC1234",
                id_collection=str(index),
                nivel_iter=iter,
                array=sub_array.tolist(),
                status=False,
                size=len(sub_array)
            )

            print(f"\rSe guardo el Array {index+1}: Success", end="")

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
            zero_elements = np.insert(zero_elements, np.repeat(
                np.arange(zero_elements.size), 2) + 1, repeated_arr)

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

        # print(self.array_init)

    def search_and_change_generator(self):
        # print("==========================================================")
        # print(type(self.array_init))
        # Convertir la lista a un arreglo de numpy
        array_init = np.array(self.array_init)
        print("SizeStart: ", len(array_init))

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
            zero_elements = np.insert(zero_elements, np.repeat(
                np.arange(zero_elements.size), 2) + 1, repeated_arr)

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
        self.array_init = array_init

        print(array_init)
        # print(self.array_init)
        print("SizeEnd:   ", len(array_init))
        yield len(array_init)

    def control_interactor(self):
        Lote.objects.create(
            id_lote="ABC1234",
            id_collection=0,
            nivel_iter=0,
            array=self.array_init,
            status=False,
        )

        # for i in range(10):
        #    print("==========================================================")
        #    print("Serie", i,)
        #    self.split_and_evaluate(i)
        #    # print(len(self.array_init))

        #    # print(next(self.search_and_change_generator()))

        while True:
            try:
                #gc.collect()
                raw_list = Lote.objects.filter(status=False).first()

                iterador = int(raw_list.nivel_iter)
                id_collection = int(raw_list.id_collection)
                rango = 60 - iterador
                self.array_init = raw_list.array
                for i in range(int(rango)):
                    print("==========================================================")
                    print("Serie:", i, "|   Nivel:",
                          iterador, "|   Id:", id_collection)
                    print("==========================================================")
                    self.split_and_evaluate(i)
                    print("\n")

                raw_list.size_end = len(self.array_init)
                raw_list.status = True
                raw_list.save()

            except:
                break
