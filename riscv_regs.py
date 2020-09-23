# !/user/bin/env Python3
# -*- coding:utf-8 -*-

class Regs:
    regids = [
        'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 
        'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 
        'x16', 'x17', 'x18', 'x19', 'x20', 'x21', 'x22', 'x23', 
        'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30', 'x31'
        ]
    names = [
        'zero', 
        'ra', 
        'sp', 
        'gp', 
        'tp', 't0', 't1', 't2', 
        's0',     # 'fp' 
        's1', 
        'a0',    # also for 'v0'
        'a1',    # also for 'v1'
        'a2', 'a3', 
        'a4', 'a5', 'a6', 'a7', 
        's2', 's3', 
        's4', 's5', 's6', 's7', 
        's8', 's9', 's10', 's11', 
        't3', 't4', 't5', 't6', 
    ]

    @classmethod
    def name_to_id(cls, name):
        i = cls.names.index(name)
        return cls.regids[i]

    @classmethod
    def id_to_name(cls, id):
        i = cls.regids.index(id)
        return cls.names[i]

    @classmethod
    def isname(cls, text):
        return text in cls.names
    
    @classmethod
    def isid(cls, text):
        return text in cls.regids
    
    @classmethod
    def getaddr(cls, text):
        if cls.isname(text):
            return cls.names.index(text)
        elif cls.isid(text):
            return cls.regids.index(text)
        raise Exception('No such register.')

def is_reg(name):
    if Regs.isid(name) or Regs.isname(name):
        return True
    return False

def get_reg_addr(name):
    return Regs.getaddr(name)