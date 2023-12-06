import os
import sys
sys.path.append(os.path.abspath(".."))

import pytest
from fastapi.testclient import TestClient
from confluent_kafka.admin import AdminClient

from src import crearApp
from src.kafka.config import SERVIDOR

@pytest.fixture()
def app():

	app=crearApp()

	return app

@pytest.fixture()
def cliente(app):

	return TestClient(app)

@pytest.fixture()
def admin():

	return AdminClient({"bootstrap.servers":SERVIDOR})