'''
==========================================================================================
 VDAY25 - Desvendando o RISC-V: Um Workshop Prático com FPGA e LiteX 
------------------------------------------------------------------------------------------
 Script   : ula.py                                                                 Lab: 01
 Author(s): Gabriel Villanova N. M. <gabriel.magalhaes@virtus.ufcg.edu.br>
 Author(s): Thiago M. de Oliveira <thiago.oliveira@virtus.ufcg.edu.br>
==========================================================================================
'''

from migen import Module, Signal
from migen.fhdl import verilog
import argparse
 
class ula(Module):
    def __init__(self, NBITS):
        self.i_data_a = Signal(NBITS)
        self.i_data_b = Signal(NBITS)
        self.o_result = Signal(2*NBITS)
        self.comb += self.o_result.eq(self.i_data_a + self.i_data_b)
 
def generate(dut, filename):

    # get dut-obj (ConvOutput)
    dut_obj = verilog.convert(
        dut,
        name="ula",
        ios={dut.i_data_a,
             dut.i_data_b,
             dut.o_result
             }
    )
    # write verilog
    verilog_text = str(dut_obj)
    with open(filename, "w") as f:
        f.write(verilog_text)
    print(f"{filename} succesfully generated.")
 
if __name__ == "__main__":

    # Get arguments:
    parser = argparse.ArgumentParser(description="Migen ULA Verilog generator")
    parser.add_argument("--nbits",  "-n", type=int, default=2, help="width of inputs")
    parser.add_argument("--output", "-o", default="ula.v", help="output .v file")
    args = parser.parse_args()

    # DUT instanciation
    dut = ula(args.nbits)

    # Write verilog
    generate(dut, args.output)
