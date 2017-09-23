
VENV := /opt/extpython/python3.6/bin/virtualenv
SERVER_HOST := 127.0.0.1
SERVER_PORT := 7100
.DEFAULT_GOAL := run


virtualenv: testenv


testenv:
	rm -rf testenv
	$(VENV) testenv
	. testenv/bin/activate && pip3 install -r requirements.txt


.PHONY: circus.ini
circus.ini: virtualenv
	. testenv/bin/activate && ./genconf.py $(SERVER_HOST) $(SERVER_PORT) > circus.ini


.PHONY: run
run: circus.ini
	. testenv/bin/activate && circusd circus.ini


.PHONY: daemon
daemon: circus.ini
	. testenv/bin/activate && circusd --daemon circus.ini


.PHONY: kill
kill:
	pkill circusd


clean:
	rm -rf testenv circus.ini
