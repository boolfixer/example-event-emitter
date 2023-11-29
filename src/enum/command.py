from enum import Enum


class Command(Enum):
    BA = 'BA'
    BO = 'BO'
    ANT_SET = 'RXA'
    BAUD_S = 'baud_s'
    BAUD_T = 'baud_t'
    CH_SET = 'FC'
    INIT_S = 'INITS'
    INIT_T = 'INITT'
    MOD_EN = 'mod_en'
    OPER_SET = 'RXO'
    POW_SET = 'FP'
    SN = 'SN'
    STATUS = 'status'
    TA = 'TA'
    TO = 'TO'
    RXO = 'RXO'
    ATS = 'ATS'
    ATS_B = 'ATS+B****'
    ATS_C = 'ATS+C***'
    ATS_FUx = 'ATS+FUx'
    ATS_Px = 'ATS+Px'
    ATS_Ry = 'ATS+Ry'
    ATS_Udps = 'ATS+Udps'
    ATS_V = 'ATS+V'
    ATS_SLEEP = 'ATS+SLEEP'
    ATS_DEFAULT = 'ATS+DEFAULT'
    ATS_UPDATE = 'ATS+UPDATE'
    ATT = 'ATT'
    ATT_B = 'ATT+B****'
    ATT_C = 'ATT+C***'
    ATT_FUx = 'ATT+FUx'
    ATT_Px = 'ATT+Px'
    ATT_Ry = 'ATT+Ry'
    ATT_Udps = 'ATT+Udps'
    ATT_V = 'ATT+V'
    ATT_SLEEP = 'ATT+SLEEP'
    ATT_DEFAULT = 'ATT+DEFAULT'
    ATT_UPDATE = 'ATT+UPDATE'
