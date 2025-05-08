module ula_system (
      input       [3:0]  KEY,
      output      [9:0]  LEDR,
      input       [9:0]  SW	 
);

ula uu_ula(
	.i_data  (SW[1:0]  ),
	.i_opcode(SW[3:2]  ),
	.o_result(LEDR[3:0]),
	.a_clk   (KEY[0]   ),
	.b_clk   (KEY[1]   )
);
endmodule 
