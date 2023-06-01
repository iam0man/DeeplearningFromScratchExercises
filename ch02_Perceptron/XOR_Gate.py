import and_gate_2
def xor_gate(x1,x2):
    s1 = and_gate_2.nand_gate(x1, x2)
    s2 = and_gate_2.or_gate(x1, x2)
    y = and_gate_2.and_gate_2(s1, s2)
    return y


