python3 -c "import pytest" ; if [ $? -eq 1 ]; then pip3 install -r requirements.txt; fi; ipython3 -i init.ipy
