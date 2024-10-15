import pytest
from classes import Simulador

class TestClass:
    
    def test_programa_en_local(self):
        simulador = Simulador()
        simulador.definir_programa("fibonacci", "LOCAL")
        es_ejecutable = simulador.ejecutable("fibonacci")
        assert es_ejecutable == True
    
    def test_mismo_nombre(self):
        simulador = Simulador()
        simulador.definir_programa("fibonacci", "LOCAL")
        with pytest.raises(ValueError):
            simulador.definir_programa("fibonacci", "LOCAL")

    def test_no_existe_programa(self):
        simulador = Simulador()
        with pytest.raises(ValueError):
            simulador.ejecutable("fibonacci")
    
    def test_varios_interpretes(self):
        simulador = Simulador()
        simulador.definir_interprete("LOCAL", "Java")
        simulador.definir_interprete("Java", "Python")
        simulador.definir_programa("fibonacci", "Python")
        es_ejecutable = simulador.ejecutable("fibonacci")
        assert es_ejecutable == True
    
    def test_traduccion(self):
        simulador = Simulador()
        simulador.definir_programa("fibo", "Python")
        simulador.definir_traductor("LOCAL", "Python", "LOCAL")
        es_ejecutable = simulador.ejecutable("fibo")
        assert es_ejecutable == True


    def test_programa_en_java0(self):
        simulador = Simulador()
        simulador.definir_programa("factorial", "Java")
        es_ejecutable = simulador.ejecutable("factorial")
        assert es_ejecutable == False

    def test_programa_en_java1(self):
        simulador = Simulador()
        simulador.definir_programa("factorial", "Java")
        simulador.definir_interprete("C", "Java")
        simulador.definir_traductor("C", "Java", "C")
        es_ejecutable = simulador.ejecutable("factorial")
        assert es_ejecutable == False
    

    def test_programa_en_java2(self):
        simulador = Simulador()
        simulador.definir_programa("factorial", "Java")
        simulador.definir_interprete("C", "Java")
        simulador.definir_traductor("C", "Java", "C")
        simulador.definir_interprete("LOCAL", "C")
        es_ejecutable = simulador.ejecutable("factorial")
        assert es_ejecutable == True

    def test_programa_holamundo0(self):
        simulador = Simulador()
        simulador.definir_interprete("C", "Java")
        simulador.definir_traductor("C", "Java", "C")
        simulador.definir_interprete("LOCAL", "C")
        simulador.definir_programa("holamundo", "Python3")
        simulador.definir_traductor("wtf42", "Python3", "LOCAL")
        es_ejecutable = simulador.ejecutable("holamundo")
        assert es_ejecutable == False


    def test_programa_holamundo1(self):
        simulador = Simulador()
        simulador.definir_interprete("C", "Java")
        simulador.definir_traductor("C", "Java", "C")
        simulador.definir_interprete("LOCAL", "C")
        simulador.definir_programa("holamundo", "Python3")
        simulador.definir_traductor("wtf42", "Python3", "LOCAL")
        simulador.definir_traductor("C", "wtf42", "Java")
        es_ejecutable = simulador.ejecutable("holamundo")
        assert es_ejecutable == True


