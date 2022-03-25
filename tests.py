import pytest
import funciones as tf

def obtener_datos_suma():
  return [(1,1,2),("1/4",2,2.25), (0.5,"1/4", 0.75)]

@pytest.mark.parametrize("numero1,numero2,resultado",obtener_datos_suma())
def test_suma(numero1, numero2, resultado):
  assert tf.suma(numero1,numero2) == resultado


def obtener_datos_resta():
  return [(8,"4/5",7.2),(2,-2,4),("1/2","1/2",0)]

@pytest.mark.parametrize("minuendo,sustraendo,resultado", obtener_datos_resta())
def test_resta(minuendo, sustraendo, resultado):
  assert tf.resta(minuendo, sustraendo) == resultado


def obtener_datos_multiplicacion():
  return [("1/2",2,1.0),(2,4,8),(-1,2,-2)]

@pytest.mark.parametrize("numero1,numero2,resultado", obtener_datos_multiplicacion())
def test_multiplicacion(numero1,numero2,resultado):
  assert tf.multiplicacion(numero1,numero2) == resultado

def obtener_datos_division():
  return [("5","1/5",25.0),(10,"4/2",5),(10,1,10)]

@pytest.mark.parametrize("numerador,denominador,resultado", obtener_datos_division())
def test_division(numerador,denominador,resultado):
  assert tf.division(numerador,denominador) == resultado

import pytest
import funciones as tf

def obtener_datos_integracion():
  return [(5,5,1.25,0.75,5),(8,"7/5",15,"3/8",137.475)]

@pytest.mark.parametrize("num_suma1, num_suma2, num_resta1, num_resta2, resultado", obtener_datos_integracion())
def test_integracion(num_suma1, num_suma2, num_resta1, num_resta2, resultado):
  assert tf.multiplicacion(tf.suma(num_suma1,num_suma2),tf.resta(num_resta1,num_resta2)) == resultado

