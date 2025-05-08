'''
==========================================================================================
 VDAY25 - Desvendando o RISC-V: Um Workshop Prático com FPGA e LiteX 
------------------------------------------------------------------------------------------
 Script   : ula-tb.py                                                              Lab: 01
 Author(s): Gabriel Villanova N. M. <gabriel.magalhaes@virtus.ufcg.edu.br>
 Author(s): Thiago M. de Oliveira <thiago.oliveira@virtus.ufcg.edu.br>
==========================================================================================
'''

from migen import *
import random as rnd
from ula import *

def test_random(dut, NBITS, TESTS):
    for i in range(TESTS):
        # input
        a = rnd.randrange(0,pow(2,NBITS))
        b = rnd.randrange(0,pow(2,NBITS))

        # stimuli
        yield dut.i_data_a.eq(a)
        yield dut.i_data_b.eq(b)
        
        yield # advance one cycle
        print(f"a[{i}] + b[{i}] = {yield dut.i_data_a} + {yield dut.i_data_b} = {yield dut.o_result}")

        # check with reference model
        assert(a+b == (yield dut.o_result))

if __name__ == "__main__":
    # Get arguments:
    parser = argparse.ArgumentParser(description="Migen ULA test-bench")
    parser.add_argument("--nbits", "-n", type=int, default=2, help="width of inputs")
    parser.add_argument("--ntest", type=int, default=10, help="num of tests")
    args = parser.parse_args()

    dut = ula(args.nbits)
    run_simulation(dut, test_random(dut, args.nbits, args.ntest), vcd_name="ula.vcd")