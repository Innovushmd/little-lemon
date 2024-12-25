from django.test import TestCase
from.models import Reserva, Mesa

class ReservaTestCase(TestCase):
    def test_reserva_creada(self):
        mesa = Mesa.objects.create(numero=1, capacidad=4)
        reserva = Reserva.objects.create(fecha='2024-12-25', hora='19:00', mesa=mesa, nombre='Juan')
        self.assertEqual(reserva.nombre, 'Juan')

class MesaTestCase(TestCase):
    def test_mesa_creada(self):
        mesa = Mesa.objects.create(numero=1, capacidad=4)
        self.assertEqual(mesa.numero, 1)