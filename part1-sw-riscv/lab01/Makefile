c2asm:
	riscv64-unknown-elf-gcc -march=rv32i -mabi=ilp32 -O0 -S main.c -o main.s

asm2instructions: main.s
	riscv64-unknown-elf-as -march=rv32i -mabi=ilp32 $< -o main.o
	riscv64-unknown-elf-objdump -d main.o > main.dump
