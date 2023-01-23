from src.controllers.controller import *
from src.controllers.error_controller import NotFoundController


routes ={
    "ola_route":"/", "ola_controller":OlaController.as_view("ola"),
    "not_found":404, "not_found_controller": NotFoundController.as_view("not_found"),
}