# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:05:37 2020

@author: marcelo.silva
"""
import pandas as pd

base = pd.read_csv('census.csv')


""" Dividir a base de dados em Atributos PREVISORES e em CLASSE """
previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

""" transformação de dados categóricos em dados numéricos """
from sklearn.preprocessing import LabelEncoder
labelEncoderPrevisores = LabelEncoder()

#labels = labelEncoderPrevisores.fit_transform(previsores[:,1]) #transformando a coluna workClass da base

#todas as linhas na posição  serão alteradas
previsores[:, 1]  = labelEncoderPrevisores.fit_transform(previsores[:, 1])  #transformando as a variáveis categóricas em numéricas (worckclass)
previsores[:, 3]  = labelEncoderPrevisores.fit_transform(previsores[:, 3])  #transformando as a variáveis categóricas em numéricas (education)
previsores[:, 5]  = labelEncoderPrevisores.fit_transform(previsores[:, 4])  #transformando as a variáveis categóricas em numéricas (marital-status)
previsores[:, 6]  = labelEncoderPrevisores.fit_transform(previsores[:, 6])  #transformando as a variáveis categóricas em numéricas (occupation)
previsores[:, 7]  = labelEncoderPrevisores.fit_transform(previsores[:, 7])  #transformando as a variáveis categóricas em numéricas (relationship)
previsores[:, 8]  = labelEncoderPrevisores.fit_transform(previsores[:, 8])  #transformando as a variáveis categóricas em numéricas (race)
previsores[:, 9]  = labelEncoderPrevisores.fit_transform(previsores[:, 9])  #transformando as a variáveis categóricas em numéricas (sex)
previsores[:, 13] = labelEncoderPrevisores.fit_transform(previsores[:, 13]) #transformando as a variáveis categóricas em numéricas (native-country)
