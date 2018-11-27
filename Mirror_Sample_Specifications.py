
# coding: utf-8

# In[8]:


import pandas

sample_specifications=pandas.read_csv(r'C:\Users\mbeck\Documents\Samples_Specifications.csv')
print(sample_specifications)


# ## Categorize Sample Mirror Coatings
# 
# Mirror Coatings should be categorized by thickness, components, number of layers, and the mirror substrates.

# In[27]:


#Thickness of sample in angstrom

sample_thickness=sample_specifications.loc[:,"Total Thickness Ang"]
print(sample_thickness)

#samples with thickness of 2048 angstrom
angstrom_2048=sample_thickness>2047
samples_2048=sample_thickness[angstrom_2048]


#samples with thickness of 1952 angstrom
angstrom_1952=sample_thickness==1952
samples_1952=sample_thickness[angstrom_1952]


#samples with thickness of 1952 angstrom
angstrom_1000=sample_thickness==1000
samples_1000=sample_thickness[angstrom_1952]



# In[30]:


#Components of mirror sample coatings

sample_components=sample_specifications.loc[:,"Sample Components"]
print(sample_components)

#samples with Zirconium Dioxide and Titanium Dioxide
ZrO2_TiO2_samples=sample_components==('ZrO2/TiO2')
samples_zirconium_and_titanium=sample_components[ZrO2_TiO2_samples]
print(samples_zirconium_and_titanium)

#samples with Titanium Dioxide
TiO2_samples=sample_components==('TiO2')
samples_titanium=sample_components[TiO2_samples]
print(samples_titanium)

#samples with Zirconium Dioxide
ZrO2_samples=sample_components==('ZrO2')
samples_zirconium=sample_components[ZrO2_samples]
print(samples_zirconium)


# In[31]:


#Number of layers of mirror coating

sample_layers=sample_specifications.loc[:,"Number of Layers"]
print(sample_layers)

#samples with 128 layers
layers_128=sample_layers==128
samples_128=sample_layers[layers_128]

#samples with 122 layers
layers_122=sample_layers==122
samples_122=sample_layers[layers_122]

#samples with 64 layers
layers_64=sample_layers==64
samples_64=sample_layers[layers_64]

#samples with 32 layers
layers_32=sample_layers==32
samples_32=sample_layers[layers_32]

#samples with 16 layers
layers_16=sample_layers==16
samples_16=sample_layers[layers_16]

#samples with 8 layers
layers_8=sample_layers==8
samples_8=sample_layers[layers_8]

#samples with 1 layers
layers_1=sample_layers==1
samples_1=sample_layers[layers_1]


# In[33]:


#Mirror Coating Substrates

sample_substrate=sample_specifications.loc[:,"Substrate"]
print(sample_substrate)

#samples with glass slide substrates
glass_samples=sample_substrate==('Glass Slides')
samples_glass=sample_substrate[glass_samples]
print(samples_glass)

#samples with Silicon substrates
silicon_samples=sample_substrate==('Silicon')
samples_Si=sample_substrate[silicon_samples]
print(samples_Si)

