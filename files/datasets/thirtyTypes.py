where = '/Users/magdalenas/Downloads/textmining (2)/'

fileNames = [
    'BeyondEntitiesAndRelationships.txt',
    'bigdata.txt',
    'ConditionsOverCauses.txt',
    'EmergentDesignInEnterpriseIT.txt',
    'FromInformationToKnowledge.txt',
    'FromTheCoalface.txt',
    'HeraclitusAndParmenides.txt',
    'IroniesOfEnterpriseIT.txt',
    'MakingSenseOfOrganizationalChange.txt',
    'MakingSenseOfSensemaking.txt',
    'ObjectivityAndTheEthicalDimensionOfDecisionMaking.txt',
    'OnTheInherentAmbiguitiesOfManagingProjects.txt',
    'OrganisationalSurprise.txt',
    'ProfessionalsOrPoliticians.txt',
    'RitualsInInformationSystemDesign.txt',
    'RoutinesAndReality.txt',
    'ScapegoatsAndSystems.txt',
    'SherlockHolmesFailedProjects.txt',
    'SixHeresiesForBI.txt',
    'SixHeresiesForEnterpriseArchitecture.txt',
    'TOGAFOrNotTOGAF.txt',
    'TheArchitectAndTheApparition.txt',
    'TheCloudAndTheGrass.txt',
    'TheConsultantsDilemma.txt',
    'TheDangerWithin.txt',
    'TheDilemmasOfEnterpriseIT.txt',
    'TheEssenceOfEntrepreneurship.txt',
    'ThreeTypesOfUncertainty.txt',
    'UnderstandingFlexibility.txt',
    'sherlockHolmesMgmtFetis.txt'
]

def getFilenames(isTrain = True):
    castFiles = []
    for fileName in fileNames:
        castFiles.append(where + fileName)
    return castFiles