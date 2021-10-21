.PHONY: create-kernel
create-kernel: ## Install required tool for installing packages
	pip install pipenv;\
	pipenv install;\
	/opt/dapla/pipenv_kernel.sh create pipenvtest1 /opt/conda/share/jupyter/kernels/python3
    
.PHONY: activate-kernel
activate-kernel: ## Activate existing kernel
	/opt/dapla/pipenv_kernel.sh activate pipenvtest1

.PHONY: install-packages
install-packages: ## install all packages project requires
	pip install pipenv;\
	pipenv install toml python-highcharts