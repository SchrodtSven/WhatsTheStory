import json
import requests
from typing import Self


class LocationFinder:
    """  Lokations-/Geoinformation zu verschiedenen Gebieten (Objectives) finden
    
        Z.B: cty: 'Berlin' / obj: 'supermarkt' 

    """
    
    tmeot = 120 # Timeout in Sekunden
    
    lst_rsp:requests.models.Response = None # Letze Response als Objekt
    
    # API: Aggregator verschiedener Datenquellen
        
    base_url = "https://overpass-api.de/api/interpreter"
    
    
    
    # Anfrage an Overpass API
    def snd_req(self, cty:str, obj:str)  -> Self:
        """ Sendet POST Request (mit JSON Payload) zur API

        Args:
            cty (str): Gemeinde/ Stadt / Region/ etc.
            obj (str): objective of interest 

        Returns:
            requests.models.Response
        """
        
        
        
        query = self.gen_bs_q(cty=cty, obj=obj)
        self.lst_rsp =  requests.post(self.base_url, data={"data": query}, timeout=self.tmeot)
        return self
    
    
    def gen_bs_q(self, cty:str, obj:str):
        """ Generiert die Basis-Suche nach 
            - Ort (cty)  und 
            - Sachgebiet (obj)
        
        """
        
        return f"""
        [out:json];
        area["name"="{cty}"]->.searchArea;
        (
        node["shop"="{obj}"](area.searchArea);
        way["shop"="{obj}"](area.searchArea);
        relation["shop"="{obj}"](area.searchArea);
        );
        out center;
        """

    def ld(self, fn:str) -> str:
        """ Load data from file identified by fn

        Args:
            fn (str): File name

        Returns:
            string: file content
        """
        with (open(fn, 'r')) as f:
            tmp = f.read()
        return tmp
    
    def sv(self, fn:str, dta:str)->Self:
        """ Save dta string data to file  identified by fn

        Args:
            fn (str): _description_
            dta (str): _description_

        Returns:
            Self: _description_
        """
        with(open(fn, 'w')) as f:
            f.write(dta)
        return self