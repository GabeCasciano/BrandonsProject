from __future__ import annotations
from enum import Enum


class PDU:
    PDU_IDENTIFY = 'I'
    PDU_PERSON = 'P'
    PDU_ORGANIZATION = 'O'
    PDU_ACK = 'A'
    PDU_ERROR = 'E'

    ERR_NO_ID = 1
    ERR_NO_NAME = 2

    def __init__(self, pdu_type: str = None, pdu_data: str = None):
        self.pdu_type = ""
        self.pdu_data = ""

        if pdu_type is not None and pdu_data is not None:
            self.pdu_type = pdu_type
            self.pdu_data = pdu_data

    def __eq__(self, other) -> bool:
        if isinstance(other, PDU):
            return self.pdu_type == other.pdu_type and self.pdu_data == other.pdu_data
        
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def serialize(pdu: PDU) -> str:
        return pdu.pdu_type + "," + pdu.pdu_data

    def unserialize(data: str) -> PDU:
        in_list = data.split(",")
        if in_list.__len__() == 2:
            return PDU(in_list[0], in_list[1])
        else:
            return PDU()

    def make_pdu_ack() -> PDU:
        return PDU(PDU.PDU_TYPES.PDU_ACK, "")

    def make_pdu_error(err_code: PDU.PDU_ERRORS) -> PDU():
        return PDU(PDU.PDU_TYPES.PDU_ERROR, )


