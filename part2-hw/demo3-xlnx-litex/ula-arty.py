from migen import *
from litex.gen import LiteXModule
from litex.soc.integration.builder import *
from litex_boards.platforms import digilent_arty

# Clock/Reset Generator
class _CRG(LiteXModule):
    def __init__(self, platform):
        # Declare clock domains "a" and "b":
        self.cd_a = ClockDomain("a")
        self.cd_b = ClockDomain("b")

        # Request "buttons" from (Arty) platform:
        btn_0 = platform.request("user_btn", 0)
        btn_1 = platform.request("user_btn", 1)

        # Connect each button to the clock signals:
        self.comb += self.cd_a.clk.eq(btn_0)
        self.comb += self.cd_b.clk.eq(btn_1)

class ula(LiteXModule):
    def __init__(self, platform):
        self.crg = _CRG(platform) # Add CRG

        # to be implemented: request necessary IOs

        # BEGIN of LOGIC -----------------------------------
        # Intern signals:
        data   = Signal(2)
        opcode = Signal(2)
        result = Signal(4)
 
        # Flip-flops:
        reg_a = Signal(2)
        reg_b = Signal(2)

        # Synchronous logic for clock domains a and b
        self.sync.a += reg_a.eq(data)
        self.sync.b += reg_b.eq(data)

        cases_dict = {}
        cases_dict[0] = result.eq(reg_a + reg_b)
        cases_dict[1] = result.eq(reg_a - reg_b)
        cases_dict[2] = result.eq(reg_a * reg_b)
        cases_dict[3] = result.eq(reg_a >> reg_b)

        self.comb += Case(opcode, cases_dict)
        # END of LOGIC -------------------------------------

        # to be implemented: connect ula and FPGA IOs...

def main(args):
    platform = digilent_arty.Platform()
    platform.add_platform_command("set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets user_btn0_IBUF]")
    dut = ula(platform)
    platform.build(dut, build_dir="build", build_name=args.build_name, run=args.run_synth)

if __name__ == "__main__":
    # Get arguments:
    parser = argparse.ArgumentParser(description="LiteX Verilog generator")
    parser.add_argument("--build_name","-n", type=str, default="ula", help="Build name")
    parser.add_argument("--run_synth", "-r", action="store_true", help="Run FPGA synthesis")
    args = parser.parse_args()
    main(args)
