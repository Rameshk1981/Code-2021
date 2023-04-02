"""  
 

#******Inclusion: Creates 25 CIRCULAR Inclusions ************************************************************************************************** 
"""  


#Import Abaqus-related (Python) Object files 
from abaqus import * 
from abaqusConstants import * 
import __main__ 
import section 
import regionToolset 
import displayGroupMdbToolset as dgm 
import part 
import material 
import assembly 
import step 
import interaction 
import load 
import mesh 
import job 
import sketch 
import visualization 
import xyPlot 
import displayGroupOdbToolset as dgo 
import connectorBehavior 

#**************************************************** 
# CREATE MATRIX AND FIBRE MATERIALS/SECTIONS HERE 
#**************************************************** 
mdb.models['Model-1'].Material(name='matrix') 
mdb.models['Model-1'].Material(name='fibre') 
mdb.models['Model-1'].HomogeneousSolidSection(name='matrixSection', material='matrix', thickness=None) 
mdb.models['Model-1'].HomogeneousSolidSection(name='fibreSection', material='fibre', thickness=None) 

#Create Viewport 
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF) 
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(meshTechnique=OFF) 

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=360) 
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints 
s.setPrimaryObject(option=STANDALONE) 
session.viewports['Viewport: 1'].view.setValues(width=30, height=15) 

#**************************************************** 
# REINFORCING INCLUSIONS SECTION 
#**************************************************** 

# ------------------------------------------------------------------- 
#Create Fibre circles at specified centre coordinates(XYAll) and defined radius, R 
s.CircleByCenterPerimeter(center=(85.6289, 74.2005), point1=(95.6289, 74.2005)) 
s.CircleByCenterPerimeter(center=(41.1945, 112.3233), point1=(51.1945, 112.3233)) 
s.CircleByCenterPerimeter(center=(14.9729, 87.6702), point1=(24.9729, 87.6702)) 
s.CircleByCenterPerimeter(center=(77.5773, 99.9782), point1=(87.5773, 99.9782)) 
s.CircleByCenterPerimeter(center=(47.7939, 89.9787), point1=(57.7939, 89.9787)) 
s.CircleByCenterPerimeter(center=(100.2265, 38.6952), point1=(110.2265, 38.6952)) 
s.CircleByCenterPerimeter(center=(65.917, 39.6508), point1=(75.917, 39.6508)) 
s.CircleByCenterPerimeter(center=(114.5009, 3.8307), point1=(124.5009, 3.8307)) 
s.CircleByCenterPerimeter(center=(33.7802, 27.646), point1=(43.7802, 27.646)) 
s.CircleByCenterPerimeter(center=(5.7066, 41.8542), point1=(15.7066, 41.8542)) 
s.CircleByCenterPerimeter(center=(69.892, 8.4821), point1=(79.892, 8.4821)) 
s.CircleByCenterPerimeter(center=(110.7293, 96.0447), point1=(120.7293, 96.0447)) 
s.CircleByCenterPerimeter(center=(34.3136, 65.2396), point1=(44.3136, 65.2396)) 
s.CircleByCenterPerimeter(center=(2.5867, 67.1809), point1=(12.5867, 67.1809)) 
s.CircleByCenterPerimeter(center=(62.0389, 66.8034), point1=(72.0389, 66.8034)) 
s.CircleByCenterPerimeter(center=(20.8624, 3.1329), point1=(30.8624, 3.1329)) 
s.CircleByCenterPerimeter(center=(-5.4991, 3.8307), point1=(4.5009, 3.8307)) 
s.CircleByCenterPerimeter(center=(125.7066, 41.8542), point1=(135.7066, 41.8542)) 
s.CircleByCenterPerimeter(center=(-9.2707, 96.0447), point1=(0.72935, 96.0447)) 
s.CircleByCenterPerimeter(center=(122.5867, 67.1809), point1=(132.5867, 67.1809)) 
s.CircleByCenterPerimeter(center=(41.1945, -7.6767), point1=(51.1945, -7.6767)) 
s.CircleByCenterPerimeter(center=(114.5009, 123.8307), point1=(124.5009, 123.8307)) 
s.CircleByCenterPerimeter(center=(69.892, 128.4821), point1=(79.892, 128.4821)) 
s.CircleByCenterPerimeter(center=(20.8624, 123.1329), point1=(30.8624, 123.1329)) 
s.CircleByCenterPerimeter(center=(-5.4991, 123.8307), point1=(4.5009, 123.8307)) 
# ------------------------------------------------------------------- 
 
#Name the part model and associate it 
p = mdb.models['Model-1'].Part(name='RVE2DFibre', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY) 
p = mdb.models['Model-1'].parts['RVE2DFibre'] 
 
#Fibre Extrusion 
p.BaseShell(sketch=s) 
s.unsetPrimaryObject() 
p = mdb.models['Model-1'].parts['RVE2DFibre'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
del mdb.models['Model-1'].sketches['__profile__'] 
 
#**************************************************** 
# MATRIX SECTION 
#**************************************************** 

#Create Viewport 
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF) 
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(meshTechnique=OFF) 

s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=360) 
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints 
s1.setPrimaryObject(option=STANDALONE) 
session.viewports['Viewport: 1'].view.setValues(width=30, height=15) 

#Sketch RVE Rectangle 
s1.rectangle(point1=(0.0,0.0), point2=(120, 120)) 
 
#Name the part model and associate it 
p = mdb.models['Model-1'].Part(name='RVE2DMatrix', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY) 
p = mdb.models['Model-1'].parts['RVE2DMatrix'] 
 
#Matrix Extrusion 
p.BaseShell(sketch=s1)  
s1.unsetPrimaryObject() 
p = mdb.models['Model-1'].parts['RVE2DMatrix'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
del mdb.models['Model-1'].sketches['__profile__'] 
 
#**************************************************** 
#ASSEMBLY INSTANCES AND MERGE THE TWO INSTANCES 
#**************************************************** 
a = mdb.models['Model-1'].rootAssembly 
a.DatumCsysByDefault(CARTESIAN) 
p = mdb.models['Model-1'].parts['RVE2DFibre'] 
a.Instance(name='RVE2DFibre-1', part=p, dependent=ON) 
p = mdb.models['Model-1'].parts['RVE2DMatrix'] 
a.Instance(name='RVE2DMatrix-1', part=p, dependent=ON) 
a = mdb.models['Model-1'].rootAssembly 
a.InstanceFromBooleanMerge(name='RVE2DComposite', instances=( 
    a.instances['RVE2DFibre-1'], a.instances['RVE2DMatrix-1'], ), 
    keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY) 
mdb.models['Model-1'].rootAssembly.features.changeKey( 
    fromName='RVE2DComposite-1', toName='RVE2DComposite') 
 
#**************************************************** 
# EXTRUDE-CUT SECTION TO TRIM BOUNDARY FIBRES 
#**************************************************** 
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,engineeringFeatures=OFF) 
p1 = mdb.models['Model-1'].parts['RVE2DComposite'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p1) 
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=360) 
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints 
s.setPrimaryObject(option=SUPERIMPOSE) 
p = mdb.models['Model-1'].parts['RVE2DComposite'] 
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES) 
s.rectangle(point1=(0 ,0), point2=(120 ,120)) 
s.rectangle(point1=(-240 ,-240), point2=(240 ,240)) 
session.viewports['Viewport: 1'].view.fitView() 
p = mdb.models['Model-1'].parts['RVE2DComposite'] 
p.Cut(sketch=s) 
s.unsetPrimaryObject() 
mdb.models.changeKey(fromName='Model-1', toName='RVE4_120X120' )
session.viewports['Viewport: 1'].setValues(displayedObject=None) 
 
mdb.Model(name='Model-1') 
#************************************************************************ 
#                               END OF SCRIPT                             
#************************************************************************ 
# ------------------------------------------------------------------- 
