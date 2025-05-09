'''
==========================================================================================
 VDAY25 - Desvendando o RISC-V: Um Workshop Prático com FPGA e LiteX 
------------------------------------------------------------------------------------------
 Script   : ula-tb.py                                                              Lab: 02
 Author(s): Gabriel Villanova N. M. <gabriel.magalhaes@virtus.ufcg.edu.br>
 Author(s): Thiago M. de Oliveira <thiago.oliveira@virtus.ufcg.edu.br>
==========================================================================================
'''

from migen import *
import random as rnd
from ula import *

def toggle(clk):
    yield 
    yield clk.eq(1)
    yield 
    yield clk.eq(0)

def test_random(dut, NBITS, TESTS):
    # Test Add:
    yield dut.i_data.eq(1)
    yield dut.i_opcode.eq(0)
    yield from toggle(dut.cd_a.clk)
    print(f"TEST ADD: {yield dut.i_data} + {yield dut.i_data} = {yield dut.o_result}")
    yield 

    # Test Subtraction:
    yield dut.i_data.eq(2)
    yield dut.i_opcode.eq(1)
    yield from toggle(dut.cd_b.clk)
    print(f"TEST SUB: {yield dut.i_data} - {yield dut.i_data} = {yield dut.o_result}")
    yield

    # Test Multiplication:
    yield dut.i_data.eq(3)
    yield dut.i_opcode.eq(2)
    yield from toggle(dut.cd_a.clk)
    print(f"TEST MUL: {yield dut.i_data} * {yield dut.i_data} = {yield dut.o_result}")
    yield

    # Test Shift:
    yield dut.i_data.eq(3)
    yield dut.i_opcode.eq(3)
    yield from toggle(dut.cd_a.clk)
    print(f"TEST SHIFT: {yield dut.i_data} >> {yield dut.i_data} = {yield dut.o_result}")
    yield

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Migen ULA dual-clock testbench")
    parser.add_argument("--nbits", "-n", type=int, default=2)
    parser.add_argument("--ntest", type=int, default=10)
    args = parser.parse_args()

    dut = ula(args.nbits)

    run_simulation(dut,
                   test_random(dut, args.nbits, args.ntest),
                   clocks={"sys":10, "a":10, "b":10},
                   vcd_name="ula.vcd")
