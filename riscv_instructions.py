# !/user/bin/env Python3
# -*- coding:utf-8 -*-

class Insts:
    R_insts = [
        'add', 'sll', 'slt', 'sltu', 
        'xor', 'srl', 'or', 'and', 
        'sub', 'sra'
    ]
    R_opcodes = [0b0110011] * 10
    R_funct3s = range(8) + [0b000, 0b101]
    R_funct7s = [0b0000000] * 8 + [0b0100000] * 2

    I_insts = [
        'addi', 'slli', 'slti', 'sltiu', 
        'xori', 'srli', 'ori', 'andi', 
        'srai', 
        'lb', 'lh', 'lw', 'lbu', 'lhu', 
    ]
    I_opcodes = [0b0010011] * 9 + [0b0000011] * 5
    I_funct3s = range(8) + [0b101] + [0b000, 0b001, 0b010, 0b100, 0b101]
    
    S_insts = [
        'sb', 'sh', 'sw'
    ]
    S_opcodes = [0b0100011] * 3
    S_funct3s = range(3)

    B_insts = [
        'beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu'
    ]
    B_opcodes = [0b1100011] * 6
    B_funct3s = [0b000, 0b001, 0b100, 0b101, 0b110, 0b111]

    U_insts = [
        'lui', 'auipc'
    ]
    U_opcodes = [
        0b110111, 0b0010111
    ]

    J_insts = [
        'jal', 'jalr'
    ]
    J_opcodes = [
        0b1101111, 0b1100111
    ]

    Pseudo_insts = [
        'mv', 'nop', 'not', 
        'beqz', 'bnez', 
        'li', 'la', 
        'j', 'ret'
    ]

    def __init__(self, asmcode):
        self.inst_code = asmcode

    def legal(self):
        inst = self.inst_code[0]
        