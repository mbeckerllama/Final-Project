
# coding: utf-8

# ## Sample Specifications and Annealing Data
# 
# 
# The mirror coating samples were not scanned in time to plug in real data for analysis. From predictions of previous sample studies, we may assume the following to create theoretical data:
# 
# 1. Thick and homogenous layers (only one layer of coating, not alternating with others to decrease crystal growth space) may already show crystals formed from the initial deposition. To show this, the thickness will be divided by the number of layersx10.
# 
# 2. Increasing annealing temperature is thought to increase crystal formation and will show as increased amplitude within an XRD scan. We can show this by multiplying the initial amplitude by e^n where n=deltaT/50 degrees C.
# 
# 3. The constant, non annealed samples are subjected to XRD scan to have a reference sample for XRD machine calibration and to know the location of peaks in our other samples. Therefore, we can assume that accurate samples will maintain the same peak locations.
# 
# 4. The ideal component for mirror sample coatings has not been determined at this time. With future collection of real data, we hope to determine this. For now, the "ideal" component will be designated as the TiO2 samples with the amplitudes of TiO2/ZiO2 and ZiO2 measuring an increased theoretical amplitude of 2x and 3x respectively.
# 
# 5. The two sample substrates used within this experiment are glass slides and silicon. The coating facility reported that the mirror coatings deposited on glass slides showed "beading" on the surface. Therefore, we can also assume that an increased amplitude is possible. We can estimate that the glass slides will experience 2x the amplitude of silicon substrates.
# 
# The initial amplitude for every sample will be "2" before the previous adjustments according to theory are applied.
# 
# 

# In[35]:


import pandas

sample_specifications=pandas.read_csv(r'C:\Users\mbeck\Documents\Modified_Sample_Specifications.csv')
print(sample_specifications)


# ## Categorize Sample Mirror Coatings
# 
# Mirror Coatings should be categorized by thickness, components, number of layers, and the mirror substrates.

# In[27]:


#Thickness of sample in angstrom

sample_thickness=sample_specifications.loc[:,"Total Thickness Ang"]
print(sample_thickness)

#samples with thickness of 2048 angstrom
angstrom_2048=sample_thickness==2048
samples_2048=sample_thickness[angstrom_2048]


#samples with thickness of 1952 angstrom
angstrom_1952=sample_thickness==1952
samples_1952=sample_thickness[angstrom_1952]


#samples with thickness of 1000 angstrom
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


# ## Substrate Value Adjustments

# In[ ]:


#Annealing Temperature One
def annealing_temperature_one(thickness,layers,components,substrate):
    if thickness==samples_Si
        return 

