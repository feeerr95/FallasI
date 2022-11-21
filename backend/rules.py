from conditions import *

rules = [
    ([problemsWithTheFirstLayer, badDefinition, bubblesExploited],
     'Baje la velocidad de impresión'),

    ([problemsWithTheFirstLayer, badDefinition, holesBetweenLayers],
     'Baje la velocidad de impresión'),

    ([problemsWithTheFirstLayer, badDefinition, tightPulleys],
     'El programa usado está mal configurado'),

    ([problemsWithTheFirstLayer, badDefinition], 'Ajuste correctamente las poleas'),

    ([problemsWithTheFirstLayer, firstLayerSeparate],
     'Nivelar correctamente la cama'),

    ([problemsWithTheFirstLayer, firstLayerSeparate, calibratedBed],
     'Configurar bien la velocidad de impresión'),

    ([problemsWithTheFirstLayer, firstLayerSeparate, calibratedBed,
     correctPrintSpeed], 'Configurar bien la temperatura de la cama'),

    ([problemsWithTheFirstLayer, firstLayerSeparate, calibratedBed,
     correctPrintSpeed, bedIsHot], 'Utilizar algún adhesivo en la cama'),

    ([problemsWithTheFirstLayer, firstLayerSeparate, calibratedBed, correctPrintSpeed,
     bedIsHot, bedWithAdhesive], 'Tu impresora no sirve para lo que necesitas realizar'),

    ([outOfPhasePiece, tightPulleys], 'Baje la velocidad de impresión'),

    ([outOfPhasePiece], 'Ajustar correctamente las poleas'),

    ([threadsInThePiece, correctTemperature, correctPrintSpeed],
     'Configura bien la velocidad de retracción'),

    ([threadsInThePiece, correctTemperature],
     'Configurar bien la velocidad de impresión'),

    ([threadsInThePiece], 'Configurar bien la temperatura'),

    ([halfPiece, excessFilament, configuratedSupports], 'Ajustar las correas'),

    ([halfPiece, excessFilament], 'Configurar los soportes'),

    ([halfPiece, restOfFilamentBetweenExtrusorAndBarrel],
     'La temperatura del barrel esta por encima de la correcta'),

    ([halfPiece, noFilament], 'Cargar el carrete con filamento'),

    ([halfPiece, blockedNozzle], 'Configurar bien la temperatura del barrel'),

    ([halfPiece, blockedNozzle, correctBarrelTemperature], 'Ajustar bien el nozzle'),

    ([halfPiece, blockedNozzle, correctBarrelTemperature,
     adjustedNozzle], 'Comprar otro nozzle'),
]
