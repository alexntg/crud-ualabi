APP = app.py
TEST_FILES = test_unitario.py test_funcional.py test_integracion.py test_rendimiento.py test_seguridad.py
SECRETS_FILE = secrets.yaml
ENCRYPTED_SECRETS = secrets.enc.yaml
GPG_KEY_ID = FBC7B9E2A4F9289AC0C1D4843D16CEE4A27381B4

run:
	python3 $(APP)

#test:
#	pytest $(TEST_FILES)
#de momento me esta dando problemas
encrypt:
	gpg --output $(ENCRYPTED_SECRETS) --encrypt --recipient $(GPG_KEY_ID) $(SECRETS_FILE)

decrypt:
	gpg --output $(SECRETS_FILE) --decrypt $(ENCRYPTED_SECRETS)

.PHONY: run test encrypt decrypt
