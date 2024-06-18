#Importaciones
from flask import Flask, render_template, request, redirect, session

#Importar la app
from flask_app import app

#Importar los modelos a utilizar
from flask_app.models.usuario import Usuario

#RUTAS