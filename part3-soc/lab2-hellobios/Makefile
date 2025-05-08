.PHONY: build_ng build_gw

build_ng:
	python3 soc-base.py 							\
	--integrated-main-ram-size 0x4000	\
	--no-compile-gateware

build_gw:
	python3 soc-base.py 							\
	--integrated-main-ram-size 0x4000	\
	--ram-init=demo/demo.bin
