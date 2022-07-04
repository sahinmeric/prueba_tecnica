# Qualabs Technical Test

This repo contains my solutions for the technical test provided by Qualabs.

## Description

As described in pdf file [prueba_technica](https://github.com/sahinmeric/qualabs/blob/fa55471775028a1f41d50c86b7ac3b35fc12439c/Prueba%20Tecnica.pdf). Given two problems with 20 json files in the following structure.  
**JSON file structure**

    {
        "name": "User 2",
        "modulos":
                  {
                  "content_module": "authz.provider_1",
                  "auth_module": "authn.provider_2"
                  }
    }

These files indicate for each user, which modules must be loaded. In this case, the modules are authz.provider_1 and authn.provider_2.  
## Problems
**Part A** : We want to see which users are using which module.  
The result must have the following format where the each module and the user of the module are indicated.  
**Expected output format**  

    {
      'auth_module' : 
                      {
                        'authn.provider_1': ['./u1.json', './u2.json'],
                        'authn.provider_2': ['./u3.json', './u4.json', './u5.json']
                      },
      'content_module' : 
                        {
                          'authz.provider_1': ['./u1.json', './u3.json'],
                          'authz.provider_2': ['./u2.json', './u4.json'],
                          'authz.provider_3': ['./u5.json']
                        }
    }

**Part B** : We also want to know which minimum user set is needed to be able to test all modules with the following format.  
For example in the prior part u1, u4, u5 or u2, u3 ,u5 user sets will cover all present modules.  
**Expected output format**

    [‘./u1.json’, ‘./u4.json’, ‘./u5.json’]  
    [‘./u2.json’, ‘./u3.json’, ‘./u5.json’]  

## Solutions
I choose Python to write my script for solutions since I feel more comfortable with it. Each part I took some steps to reach solution and my final answer. Those steps are also included to this repo.  
**Part A steps**  
    [a1](https://github.com/sahinmeric/qualabs/blob/fa55471775028a1f41d50c86b7ac3b35fc12439c/steps/a1.py)
    [a2](https://github.com/sahinmeric/qualabs/blob/fa55471775028a1f41d50c86b7ac3b35fc12439c/steps/a2.py)
    [a3](https://github.com/sahinmeric/qualabs/blob/fa55471775028a1f41d50c86b7ac3b35fc12439c/steps/a3.py)
**Part A solution**:
    [part_a](https://github.com/sahinmeric/qualabs/blob/fa55471775028a1f41d50c86b7ac3b35fc12439c/part_a.py)

**Solution for Part A** : 
