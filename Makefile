# Setup
IMAGE          = gvillanovanm/dk-riscv-wshop-vday
CONTAINER_NAME = dk-riscv-wshop-vday
HOST_PATH      = $(PWD)
CONTAINER_PATH = /workspace
HOSTNAME       = dk-riscv-wshop-vday

# Docker cmds
dk_run:
	docker run -h $(HOSTNAME) -it --rm --name $(CONTAINER_NAME) -v $(HOST_PATH):$(CONTAINER_PATH) $(IMAGE) /bin/bash -c "cd $(CONTAINER_PATH) && /bin/bash"

dk_run_eyes:
	docker run -h $(HOSTNAME) -it --rm -e DISPLAY=host.docker.internal:0 -v $(HOST_PATH):$(CONTAINER_PATH) $(IMAGE) /bin/bash -c "cd $(CONTAINER_PATH) && /bin/bash"
