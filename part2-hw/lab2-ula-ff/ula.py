'''
==========================================================================================
 VDAY25 - Desvendando o RISC-V: Um Workshop Prático com FPGA e LiteX 
------------------------------------------------------------------------------------------
 Script   : ula.py                                                                 Lab: 02
 Author(s): Gabriel Villanova N. M. <gabriel.magalhaes@virtus.ufcg.edu.br>
            Thiago M. de Oliveira <thiago.oliveira@virtus.ufcg.edu.br>
==========================================================================================
'''

from migen import Module, Signal, Case, ClockDomain
from migen.fhdl import verilog
import argparse
 
class ula(Module):
    def __init__(self, NBITS):
        self.i_data     = Signal(NBITS)
        self.i_opcode   = Signal(2)
        self.o_result   = Signal(2*NBITS)
 
        # Flip-flops
        reg_a = Signal(NBITS)
        reg_b = Signal(NBITS)

        # Setup clock domains for data sampling 
        self.clock_domains.cd_a = ClockDomain("a")
        self.clock_domains.cd_b = ClockDomain("b")

        # Synchronous logic for clock domains a and b
        self.sync.a += reg_a.eq(self.i_data)
        self.sync.b += reg_b.eq(self.i_data)

        cases_dict = {}
        cases_dict[0] = self.o_result.eq(reg_a + reg_b)
        cases_dict[1] = self.o_result.eq(reg_a - reg_b)
        cases_dict[2] = self.o_result.eq(reg_a * reg_b)
        cases_dict[3] = self.o_result.eq(reg_a >> reg_b)

        self.comb += Case(self.i_opcode, cases_dict)
 
def generate(dut, filename):

    # get dut-obj (ConvOutput)
    dut_obj = verilog.convert(
        dut,
        name="ula",
        ios={dut.i_data,
             dut.i_opcode,
             dut.cd_a.clk,
             dut.cd_b.clk,
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
