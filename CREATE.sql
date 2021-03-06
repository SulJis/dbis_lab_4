CREATE TABLE ZNO_STATS(
    OUTID varchar(36) PRIMARY KEY,
    Birth smallint,
    SEXTYPENAME varchar(15),
    REGNAME varchar(100),
    AREANAME varchar(100),
    TERNAME varchar(100),
    REGTYPENAME varchar(100),
    TerTypeName varchar(10),
    ClassProfileNAME varchar(50),
    ClassLangName varchar(20),
    EONAME varchar(200),
    EOTYPENAME varchar(100),
    EORegName varchar(100),
    EOAreaName varchar(100),
    EOTerName varchar(100),
    EOParent varchar(200),
    UkrTest varchar(100),

    UkrTestStatus varchar(50),
    UkrBall100 real,
    UkrBall12 smallint,
    UkrBall smallint,
    UkrAdaptScale smallint,
    UkrPTName varchar(200),
    UkrPTRegName varchar(100),
    UkrPRAreaName varchar(100),
    UkrPTTerName varchar(100),

    HistTest varchar(100),
    HistLang varchar(50),
    HistTestStatus varchar(50),
    HistBall100 real,
    HistBall12 smallint,
    HistBall smallint,
    HistPTName varchar(200),
    HistPTRegName varchar(100),
    HistPRAreaName varchar(100),
    HistPTTerName varchar(100),

    MathTest varchar(100),
    MathLang varchar(50),
    MathTestStatus varchar(50),
    MathBall100 real,
    MathBall12 smallint,
    MathBall smallint,
    MathPTName varchar(200),
    MathPTRegName varchar(100),
    MathPRAreaName varchar(100),
    MathPTTerName varchar(100),

    PhysTest varchar(100),
    PhysLang varchar(50),
    PhysTestStatus varchar(50),
    PhysBall100 real,
    PhysBall12 smallint,
    PhysBall smallint,
    PhysPTName varchar(200),
    PhysPTRegName varchar(100),
    PhysPRAreaName varchar(100),
    PhysPTTerName varchar(100),

    ChemTest varchar(100),
    ChemLang varchar(50),
    ChemTestStatus varchar(50),
    ChemBall100 real,
    ChemBall12 smallint,
    ChemBall smallint,
    ChemPTName varchar(200),
    ChemPTRegName varchar(100),
    ChemPRAreaName varchar(100),
    ChemPTTerName varchar(100),

    BioTest varchar(100),
    BioLang varchar(50),
    BioTestStatus varchar(50),
    BioBall100 real,
    BioBall12 smallint,
    BioBall smallint,
    BioPTName varchar(200),
    BioPTRegName varchar(100),
    BioPRAreaName varchar(100),
    BioPTTerName varchar(100),

    GeoTest varchar(100),
    GeoLang varchar(50),
    GeoTestStatus varchar(50),
    GeoBall100 real,
    GeoBall12 smallint,
    GeoBall smallint,
    GeoPTName varchar(200),
    GeoPTRegName varchar(100),
    GeoPRAreaName varchar(100),
    GeoPTTerName varchar(100),

    EngTest varchar(100),
    EngTestStatus varchar(50),
    EngBall100 real,
    EngBall12 smallint,
    EngDPALevel varchar(50),
    EngBall smallint,
    EngPTName varchar(200),
    EngPTRegName varchar(100),
    EngPRAreaName varchar(100),
    EngPTTerName varchar(100),

    FraTest varchar(100),
    FraTestStatus varchar(50),
    FraBall100 real,
    FraBall12 smallint,
    FraDPALevel varchar(50),
    FraBall smallint,
    FraPTName varchar(200),
    FraPTRegName varchar(100),
    FraPRAreaName varchar(100),
    FraPTTerName varchar(100),

    DeuTest varchar(100),
    DeuTestStatus varchar(50),
    DeuBall100 real,
    DeuBall12 smallint,
    DeuDPALevel varchar(50),
    DeuBall smallint,
    DeuPTName varchar(200),
    DeuPTRegName varchar(100),
    DeuPRAreaName varchar(100),
    DeuPTTerName varchar(100),

    SpaTest varchar(100),
    SpaTestStatus varchar(50),
    SpaBall100 real,
    SpaBall12 smallint,
    SpaDPALevel varchar(50),
    SpaBall smallint,
    SpaPTName varchar(200),
    SpaPTRegName varchar(100),
    SpaPRAreaName varchar(100),
    SpaPTTerName varchar(100)
)