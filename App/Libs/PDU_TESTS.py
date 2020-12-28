import unittest
from PDUs import PDU

class Test_PDU(unittest.TestCase):

    def test_init(self):

        pdu = PDU(PDU.PDU_PERSON, "1;gabe;0")

        self.assertEqual(pdu.pdu_data, "1;gabe;0")
        self.assertEqual(pdu.pdu_type, PDU.PDU_PERSON )

    def test_eq_ne(self):

        pdu = PDU(PDU.PDU_PERSON, "1;gabe;0")
        pdu2 = PDU(PDU.PDU_PERSON, "1;gabe;0")

        self.assertTrue(pdu == pdu2)
        self.assertFalse(pdu != pdu2)

    def test_serial(self):
        pdu = PDU(PDU.PDU_PERSON, "1;gabe;0")

        self.assertEqual(PDU.serialize(pdu), "P,1;gabe;0")


    def test_unserial(self):
        pdu = PDU.unserialize("P,1;gabe;0")

        self.assertEqual(pdu.pdu_data, "1;gabe;0")
        self.assertEqual(pdu.pdu_type, PDU.PDU_PERSON)


if __name__ == "__main__":
    unittest.main()

