# Sources Interaction with Liquid Xenon in TPC

# 
This project focuses on simulating the interactions between gamma particles emitted by radioactive sources and liquid xenon atoms within a Time Projection Chamber (TPC).

## Overview

The simulation considers idealized radioactive sources, taking into account only the main energy peaks. The positions of the sources are uniformly distributed within the volume of the TPC, with an initial approximation centered around the coordinates (0, 0, 0).

## Data Folder

The data folder in this repository contains two subfolders that store different types of data generated for the project.

### Geant4 Simulations Output

The `G4_output/` subfolder contains the output files generated from G4 simulations conducted by Andrej. The files collect the relevant data for analysing the interactions between gamma particles emitted by radioactive sources and liquid Xenon atoms within the TPC.

### Ideal Sources Data

The `ideal_sources/` subfolder contains data files representing ideal sources. These files provide valuable information about the positions and energies of the interactions between gamma particles and liquid xenon atoms in the TPC. The positions are generated using random distributions around a chosen point within the TPC, while the energies are based on the main gamma peaks of each source (reference: NuDat). 

## To do

1. Modify the source generation code (not here for now) or configuration file to allow for non-centered positions.
2. Specify the desired positions for the sources. 
3. Rerun the simulation using the updated source positions.
4. Add more relevant data from G4 simulations. 
