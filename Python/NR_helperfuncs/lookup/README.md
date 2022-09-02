# Lookup-funksjon
Helperfunction lookup of industry, recipient or product codes (nærings-, mottaker- og produktkoder) in the national accounts system.

### Required libraries
- Pandas
- pprint

### Inputs, outputs and functionality

Imports correspondence files, identifies industry/product and yields
corresponding names and pubagg aggregate. Uses correspondences from current
reference year (basisår) in the national accounts.

Parameters
----------
code : str
    Input industry/product code.
    
lookup_table : str
    Which reference file to look in.    

    produkt = Corresponds to product in NR.
        kildefil: X_PRODUKT_HR2019
    naering = Corresponds to industries and recipients  in NR.
        kildefil: X_NAERING_HR2019

Returns
-------
Print : str
    NR-code, corresponding industry/recipient/product name, pubagg.