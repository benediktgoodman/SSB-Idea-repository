# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:00:20 2022

@author: Benedikt Goodman
"""

import pandas as pd
import pprint

def code_dictionary(*codes, lookup_table):
    """
    Function for lookup of industry, recipient or product codes (nærings-, 
    mottaker- og produktkoder) in the national accounts system.
    
    Imports correspondence files, identifies industry/product and yields
    corresponding names and pubagg aggregate. Uses correspondences from current
    reference year (basisår) in the national accounts.
    
    Still in development.
    
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

    """
    pd.options.display.max_colwidth = 100
    
    def dictionary_import(lookup_table):
        
        if lookup_table == 'produkt':
            filename = 'X_PRODUKT_HR2019.csv'
            
        elif lookup_table == 'naering':
            filename = 'X_NAERING_HR2019.csv'
        try:
            # Import df
            df = pd.read_csv(filename, encoding='ANSI')
            df.iloc[:,0] = df.iloc[:,0].astype(str)
            
            return df
        
        except:
            print("Error: valid inputs for lookup_table are 'produkt' or 'naering'.")
            
        
    # Define df to lookup codes from
    lookup_df = dictionary_import(lookup_table)
    
    # Create boolean variables to test for datatypes against
    is_df1 = type(lookup_df).__name__ == 'DataFrame'
    is_str = all(isinstance(n, str) for n in codes) # checks that codes are strings
    
    # Store test-booleans as list
    input_test_list = [is_df1, is_str]
    
    # If user inputs conforms to allowed, run lookup routine
    if False not in input_test_list:
        
        # Make list of codes present in lookup df
        approved_codes = list(lookup_df.iloc[:,0])
        
        # Make list of input codes present in lookup df
        input_codes_present = [ele for ele in approved_codes if(ele in codes)]
        
        # Checks if amount of input codes are the same as input codes
        # present in correspondence file
        if len(codes) != len(input_codes_present):
            print('Error: One or more input codes not in reference file')
            return
        
        # Runs function if file present
        else:
            
            # Define loop variables
            i = 0 
            output_df = pd.DataFrame() # what will be output of function
            
            for code in codes: 
            
                # Extracts corresponding and codes and pubagg
                # then writes it to the output to df
                if lookup_table == 'naering':
                    # output_df.columns = lookup_df.columns[[0, 4, 11]]
                    row = lookup_df.loc[lookup_df.iloc[:,0] == codes[i]].iloc[:,[0, 4, 11]]
                    output_df = pd.concat([output_df, row]) 
                    i += 1
                    
                elif lookup_table == 'produkt':
                    row = lookup_df.loc[lookup_df.iloc[:,0] == codes[i]].iloc[:,[0, 5, 13]]
                    output_df = pd.concat([output_df, row])
                    
                    i += 1
            
            # Print output
            return pprint.pprint(output_df)
    
    # If user input does not conform to allowed inputs
    elif False in input_test_list:
        
        print("Error: Wrong input. Input code must be string. valid inputs for \n"
              "lookup_table are 'naering' and 'produkt'.")
        return
    