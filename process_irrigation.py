#!/usr/bin/env python
# coding: utf-8

# In[10]:


# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:13:03 2020

@author: landry
"""
#import des modules necessaires pour ce projet.lecture du fichier json ,/n manipulation et analyse des donneés avec pendas,/n numpy notamment pour la valeur np.nan qui servira /n rendu graphique avec maatplotlib
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# variables 
title='irrigation August 2020'
start_date = '2020-08-01'
end_date = '2020-08-30'
filename='irrigation_graph_2020-08.png'

def clean_data(data):
    "fonction permettant de remplacer les valeur 200(saturé) par np.nan"
    data[data==200]=np.nan  
    return data

def save_plot_to_file(dataframe,title, labels, start_date, end_date, filename):
    "sauvegarde et renvoie un graprisme exploitant les données indiquées /n le dataframe etant de Type pandas.core.frame.DataFrame"
    fig, ax = plt.subplots(3,figsize=(10,10),sharex=True) #genere un graphe à 3 niveaux(lignes) avec des parametres : taille de la figure(figsize), et partage de l'axe des abscisse(sharex).Notons que ax et ax[i] ne sont pas de meme type et donc n'ont pasles meme arguments
    ax[0].text(0.5, 0.5, "top",color="green",fontsize=18, ha='center')
    ax[1].text(0.5, 0.5, "bottom",color="green",fontsize=18, ha='center')
    ax[2].text(0.5, 0.5, "dernier",color="green",fontsize=18, ha='center')
    #variables necessaires au graphe , absices et ordonnées de chaque niveau(ligne)
    x=values
    y0=values0
    y1=values1
    y2=values2
    #definition du graphe a l'aide de matplotlib.pyplot ici plt
    ax[0].plot(x,y0,label=label0)
    ax[1].plot(x,y1,label=label1)
    ax[2].plot(x,y2,label=label2)
    #Nous parametrons non pas un seul graphe a 1 niveu mais un graphe a 3 niveau donc il y'a un besoin d'utiliser une bouble parcourant le nombre de niveau a parametrer 
    for i in range(3):
        ax[i].fill_between(x, 0, 15,facecolor='red', alpha=0.2)#ax[i].fill_between(x,..) permettant de delimiter l'axe x par des parametres tels que la couleur , etc
        ax[i].fill_between(x, 15, 30,facecolor='orange', alpha=0.2)
        ax[i].fill_between(x, 30, 60,facecolor='green', alpha=0.2)
        ax[i].fill_between(x, 60, 100,facecolor='yellow', alpha=0.2)
        ax[i].fill_between(x, 100, 200,facecolor='red', alpha=0.2)
        ax[i].set_yticks([15, 30, 60, 100, 200]) #modifier les valeurs par defaut et afficher uniquement les intervalles qui nous interessent
        ax[i].yaxis.set_ticklabels(['saturated', 'too wet', 'perfect', 'plan to water', 'dry'], rotation = 0, color = 'black', fontsize = 10, verticalalignment = 'center') #labeliser ou nommer les differentes delimitations(definies ci dessus ) , biensur avec des parametres
        ax[i].set_ylim([0, 200]) #limiter l'axe y 
        ax[i].legend(loc='upper left') #permet d'afficher comme legende le label defini dans le graphe)
    ax[0].set_title(title) #titre particulierement au dessus du premier niveau sinon utilser plt.title("") ou fig.suptitle('').
    ax[0].set_xlim([values[0],values[len(values)-1]]) #limiter l'abscise       
    fig.autofmt_xdate() #mise en forme automatique des valeurs de l'axe x
    return plt.savefig(filename, dpi=100) #filename est le nom de limage , variable a preciser avecle format

if __name__ == '__main__':
        with open('eco-sensors_irrigation_2020-06-01_2020-08-31.json', "r") as Read_file:
             fichierlu =json.load(Read_file) #ouverture et lecture du fichier en dictionnaire
        vujson=pd.read_json('eco-sensors_irrigation_2020-06-01_2020-08-31.json') #pas obligatoire mais permet à ce stade de visionner le fichier 
        #Nous commençons a eliminer ce qui nous interresse pas , precisé dans l'enoncé
        del fichierlu[3]
        for i in range(3):
            del fichierlu[i].get("datasets")['yAxisID']
            del fichierlu[i].get("datasets")['type']
            del fichierlu[i].get("datasets")['borderWidth']
            del fichierlu[i].get("datasets")['borderColor']
            del fichierlu[i].get("datasets")['pointRadius']
            del fichierlu[i].get("datasets")['showLine']
            del fichierlu[i].get("datasets")['pointStyle']
            del fichierlu[i].get("datasets")['fill']
            del fichierlu[i].get("datasets")['backgroundColor']
            del fichierlu[i].get("datasets")['pointHoverRadius']
        for x in range(3):
            del fichierlu[x]['chartContainer']
        #definition et recuperation des données utiles pour la suite
        datatime=fichierlu[2].get('labels')
        label0=fichierlu[0].get('datasets').get('label') 
        label1=fichierlu[1].get('datasets').get('label')
        label2=fichierlu[2].get('datasets').get('label')
        data0=fichierlu[0].get('datasets').get('data')
        data1=fichierlu[1].get('datasets').get('data')
        data2=fichierlu[2].get('datasets').get('data')
        #dictinnaire en dataframe
        humidity_dataframe = pd.DataFrame(
           data={
            label0: data0,
            label1: data1,
            label2: data2,},
           index=datatime,
            dtype='float')
        humidity_dataframe.index = pd.to_datetime(humidity_dataframe.index)
        #recuperation des données issues du dataframe , utiles pour le graphe 
        values = humidity_dataframe[start_date:end_date].index #toutes les valeurs comprises(ordonneés).il faut donc les recuperer pour chaque niveau
        values0 = humidity_dataframe[start_date:end_date][label0].values
        values1 = humidity_dataframe[start_date:end_date][label1].values
        values2 = humidity_dataframe[start_date:end_date][label2].values
        #Appel de la fonction clean_data pour travailler avec les np.nan au lieu des données saturées
        data=humidity_dataframe
        clean_data(data)
        dataframe=humidity_dataframe
        labels=datatime
        save_plot_to_file(dataframe,title, labels, start_date, end_date, filename)




        
        
        


# In[ ]:




