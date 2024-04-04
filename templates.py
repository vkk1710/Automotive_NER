
TEMPLATES = [
  {
    "Sentence": """The excessive load on the rear axle can lead to the deformation of the suspension components and exacerbation of the stress on the axle housing. This increased stress may cause the fracture of bolts securing the axle housing to the chassis frame rail, or even the collapse of the axle housing support system. There is a risk of damage to brake lines and electrical wiring, potentially resulting in a fire.""",

    "Output": [{"Entity": "deformation of the suspension components", "Label": "Failure_issue"}, {"Entity": "exacerbation of the stress", "Label": "Failure_issue"}, {"Entity": "axle housing", "Label": "Component"}, {"Entity": "fracture of bolts", "Label": "Failure_issue"}, {"Entity": "chassis frame rail", "Label": "Component"}, {"Entity": "axle housing support system", "Label": "Component"}, {"Entity": "damage to brake lines", "Label": "Failure_issue"}, {"Entity": "electrical wiring", "Label": "Component"}, {"Entity": "fire", "Label": "Failure_issue"}]
  },
  {
    "Sentence": """DANA SPICER TANDEM DRIVE AXLE MODELS DS463 AND DS521 EQUIPPED WITH DANA WELDED SUSPENSION BRACKETS FOR USED WITH CHALMERS SUSPENSION MANUFACTURED BETWEEN NOVEMBER 1, 1998, AND DECEMBER 31, 2001. AN UNDERSIZED ATTACHMENT WELD MAY FRACTURE WITHOUT WARNING. THE WELD FRACTURE MAY RESULT IN A LOSS OF VEHICLE CONTROL, POSSIBLY RESULTING IN A VEHICLE CRASH WITHOUT PRIOR WARNING. DANA WILL NOTIFY PACCAR/KENWORTH'S CUSTOMERS AND INSPECT AND REPAIR THE AXLE WELDS FREE OF CHARGE.  OWNER NOTIFICATION BEGAN JULY 25, 2002.   OWNERS WHO TAKE THEIR VEHICLES TO AN AUTHORIZED DEALER ON AN AGREED UPON SERVICE DATE AND DO NOT RECEIVE THE FREE REMEDY WITHIN A REASONABLE TIME SHOULD CONTACT DANA AT 419-535-4500. ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S AUTO SAFETY HOTLINE AT 1-888-DASH-2-DOT (1-888-327-4236).""",

    "Output": [{"Entity": "UNDERSIZED ATTACHMENT WELD", "Label": "Component"}, {"Entity": "FRACTURE", "Label": "Failure_issue"}, {"Entity": "WELD FRACTURE", "Label": "Failure_issue"}, {"Entity": "LOSS OF VEHICLE CONTROL, POSSIBLY RESULTING IN A VEHICLE CRASH WITHOUT PRIOR WARNING", "Label": "Failure_issue"}, {"Entity": "PACCAR/KENWORTH", "Label": "Manufacturer"}, {"Entity": "INSPECT AND REPAIR THE AXLE WELDS FREE OF CHARGE", "Label": "Corrective_action"}, {"Entity": "JULY 25, 2002", "Label": "Recall_date"}]
  },
  {
    "Sentence": """ON CERTAIN MOTORCYCLES EQUIPPED WITH OPTIONAL BRAKE ROTOR-CARRIERS,THE ROTOR-CARRIERS CAN CRACK WHILE IN SERVICE AND POSSIBLY BREAK. THIS CAN CAUSE A PARTIAL LOSS OF THE BRAKE SYSTEM OR THE POTENTIAL FOR ROTOR-CARRIER DETACHMENT, WHICH COULD RESULT IN A CRASH. DEALERS WILL REPLACE THE ROTOR-CARRIER ASSEMBLY.  OWNER NOTIFICATION BEGAN JANUARY 26, 2004. OWNERS SHOULD CONTACT AMERICAN IRONHORSE AT 1-817-665-2045.""",

    "Output": [{"Entity": "ROTOR-CARRIERS", "Label": "Component"}, {"Entity": "CRACK", "Label": "Failure_issue"}, {"Entity": "POSSIBLY BREAK", "Label": "Failure_issue"}, {"Entity": "PARTIAL LOSS OF THE BRAKE SYSTEM", "Label": "Failure_issue"}, {"Entity": "ROTOR-CARRIER DETACHMENT", "Label": "Failure_issue"}, {"Entity": "CRASH", "Label": "Failure_issue"}, {"Entity": "DEALERS WILL REPLACE THE ROTOR-CARRIER ASSEMBLY", "Label": "Corrective_action"}, {"Entity": "JANUARY 26, 2004", "Label": "Recall_date"}]
  },
  {
    "Sentence": """PASSENGER VANS.  THESE VANS EXPERIENCE FUEL ODORS OR LEAKAGE.  FUEL LEAKAGE IN THE PRESENCE OF AN IGNITION SOURCE COULD RESULT IN A FIRE. DEALERS WILL INSTALL A REVISED EVAPORATIVE EMISSION PIPE ASSEMBLY. """,

    "Output": [{"Entity": "PASSENGER VANS", "Label": "Component"}, {"Entity": "FUEL ODORS OR LEAKAGE", "Label": "Failure_issue"}, {"Entity": "FUEL LEAKAGE", "Label": "Failure_issue"}, {"Entity": "FIRE", "Label": "Failure_issue"}, {"Entity": "DEALERS WILL INSTALL A REVISED EVAPORATIVE EMISSION PIPE ASSEMBLY", "Label": "Corrective_action"}]
  },
  {
    "Sentence": """2000 NISSAN XTERRA VEHICLES MANUFACTURED BETWEEN OCTOBER 15, 1999, AND FEBRUARY 29, 2000.  THE ALLOY WHEELS USED ON THESE VEHICLES MAY NOT HAVE BEEN PROPERLY MANUFACTURED AND COULD DEVELOP CRACKS IN THE WHEEL SPOKES. IF A SUFFICIENT NUMBER OF SPOKE CRACKS DEVELOP, THE WHEEL COULD FAIL AND SEPARATE FROM THE MOUNTING HUB, POSSIBLY RESULTING IN A VEHICLE CRASH WITHOUT PRIOR WARNING. NISSAN WILL NOTIFY ITS CUSTOMERS AND REPLACE THE FOUR ALLOY WHEELS WITH XTERRA SE MODEL BRIGHT ALLOY WHEELS FREE OF CHARGE.  THE SPARE TIRE STEEL WHEEL IS NOT AFFECTED.  OWNER NOTIFICATION BEGAN ON SEPTEMBER 15, 2003.  OWNERS WHO TAKE THEIR VEHICLES TO AN AUTHORIZED DEALER ON AN AGREED UPON SERVICE DATE AND DO NOT RECEIVE THE FREE REMEDY WITHIN A REASONABLE TIME SHOULD CONTACT NISSAN AT 1-800-647-7261.  INFORMATION CAN ALSO BE OBTAINED THROUGH NISSAN'S WEB SITE AT WWW.NISSANUSA.COM.""",

    "Output": [{"Entity": "2000 NISSAN XTERRA", "Label": "Vehicle_model"}, {"Entity": "CRACKS", "Label": "Failure_issue"}, {"Entity": "WHEEL SPOKES", "Label": "Component"}, {"Entity": "WHEEL", "Label": "Component"}, {"Entity": "SEPARATE FROM THE MOUNTING HUB", "Label": "Failure_issue"}, {"Entity": "VEHICLE CRASH", "Label": "Failure_issue"}, {"Entity": "NISSAN", "Label": "Manufacturer"}, {"Entity": "REPLACE THE FOUR ALLOY WHEELS WITH XTERRA SE MODEL BRIGHT ALLOY WHEELS FREE OF CHARGE", "Label": "Corrective_action"}, {"Entity": "SEPTEMBER 15, 2003", "Label": "Recall_date"}]
  },
  {
    "Sentence": """Altec Industries Inc. (Altec) is recalling certain model year 1999-2014 aerial devices models A65, A70, A75, A72-, A/77-T, A82-T, A72-TE88, and A77-TE93 manufactured January 1, 1999, to July 15, 2014.  The affected aerial devices may have an improperly set hydraulic pressure transducer which relieves excessive backpressure in the hydraulic tank circuit. In cooler temperatures, the improperly set hydraulic pressure transducer may result in inadvertent boom movement, increasing the risk of injury to the occupant or those nearby. Altec will notify owners, and dealers will replace and install a pressure switch, free of charge. The recall began in January 16, 2015.  Owners may contact Altec customer service at 1-205-991-7733.  Altec's number for this recall is CSN 609.""",

    "Output": [{"Entity": "Altec Industries Inc", "Label": "Manufacturer"}, {"Entity": "hydraulic pressure transducer", "Label": "Component"}, {"Entity": "inadvertent boom movement", "Label": "Failure_issue"}, {"Entity": "risk of injury", "Label": "Failure_issue"}, {"Entity": "dealers will replace and install a pressure switch, free of charge", "Label": "Corrective_action"}, {"Entity": "January 16, 2015", "Label": "Recall_date"}]
  },
  {
    "Sentence": """BMW IS RECALLING CERTAIN 2005 THROUGH 2007 R 1200 GS ADVENTURE MOTORCYCLES MANUFACTURED FROM 
    DECEMBER 7, 2005 THROUGH SEPTEMBER 26, 2007.  THE BRACKET WHICH SUPPORTS THE AUDIBLE SIGNALING DEVICE CAN BREAK, POSSIBLY ALLOWING THE SIGNALING DEVICE TO FALL FROM THE VEHICLE AND ONTO THE ROADWAY. SHOULD THE SIGNALING DEVICE FALL FROM THE MOTORCYCLE WHILE BEING DRIVEN ON THE ROADWAYS, IT COULD BECOME AN OBSTACLE FOR OTHER DRIVERS WHICH MAY RESULT IN A CRASH. BMW WILL NOTIFY OWNERS AND DEALERS WILL REPAIR MOTORCYCLES BY FURTHER SECURING THE BOLTS USING LOCTITE.  THE REPAIR WILL BE PERFORMED FREE OF CHARGE.  THE SAFETY RECALL BEGAN ON AUGUST 30, 2010.  OWNERS MAY CONTACT BMW AT 1-800-525-7417. CUSTOMERS CAN ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S AUTO SAFETY HOTLINE AT 1-888-DASH-2-DOT (1-888-327-4236).""",

    "Output": [{"Entity": "R 1200 GS ADVENTURE", "Label": "Vehicle_model"}, {"Entity": "BRACKET", "Label": "Component"}, {"Entity": "BREAK", "Label": "Failure_issue"}, {"Entity": "CRASH", "Label": "Failure_issue"}, {"Entity": "BMW", "Label": "Manufacturer"}, {"Entity": "DEALERS WILL REPAIR MOTORCYCLES BY FURTHER SECURING THE BOLTS USING LOCTITE.  THE REPAIR WILL BE PERFORMED FREE OF CHARGE.", "Label": "Corrective_action"}, {"Entity": "AUGUST 30, 2010", "Label": "Recall_date"}]
  },
  {
    "Sentence": """CRACKS DEVELOP ON HANDLEBARS BETWEEN THE HANDLEBAR STAYS (HANDLEBAR MOUNTING BRACKETS) DUE TO THE 
    SOFTNESS OF THE CUSHION SHOCK ABSORBERS OF THE HANDLEBAR STAYS. THE CRACKS MAY CAUSE LOOSENESS OF THE HANDLEBAR WHICH MAY RESULT IN LOSS OF CONTROL AND AN ACCIDENT. SUZUKI DEALERS WILL REPLACE THE HANDLEBAR STAY CUSHION RUBBERS AND THE HANDLEBAR OF THE AFFECTED VEHICLES. RECALL NO. 146.CUSTOMERS MAY CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S VEHICLE SAFETY HOTLINE AT 1-888-327-4236 (TTY: 1-800-424-9153); OR GO TO HTTP://WWW.SAFERCAR.GOV.""",

    "Output": [{"Entity": "CRACKS", "Label": "Failure_issue"}, {"Entity": "HANDLEBAR MOUNTING BRACKETS", "Label": "Component"}, {"Entity": "CRACKS", "Label": "Failure_issue"}, {"Entity": "LOOSENESS", "Label": "Failure_issue"}, {"Entity": "HANDLEBAR", "Label": "Component"}, {"Entity": "LOSS OF CONTROL AND AN ACCIDENT", "Label": "Failure_issue"}, {"Entity": "SUZUKI", "Label": "Manufacturer"}, {"Entity": "REPLACE THE HANDLEBAR STAY CUSHION RUBBERS AND THE HANDLEBAR OF THE AFFECTED VEHICLES.", "Label": "Corrective_action"}]
  },
  {
    "Sentence": """Certain Choice 3 piece reflective warning trinagle kits sold by BHC Investment Corp., 
    fail to conform to the requirements of Federal Motor Vehicle safety Standard No. 125, "Warning Devices."  The 
    measurement of the inner orange fluorescent material is smaller in width than required by the standard. As a 
    consequence, the reflective properties of the warning triangle have been deminished and may not be clearly 
    visible to oncoming traffic, increasing the risk of a crash. Notifications to BHC's distributors were mailed on September 6, 2012.  BHC will either replaced the warning triangle with a domestically purchased one or credited the customer?s account.  Owners may contact BHC at 1-704-916-3435. BHC RECALL NO. 90519.OWNERS MAY ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S VEHICLE SAFETY HOTLINE AT 1-888-327-4236 (TTY 1-800-424-9153), OR GO TO <A HREF=HTTP://WWW.SAFERCAR.GOV>HTTP://WWW.SAFERCAR.GOV</A> .""",

    "Output": [{"Entity": "crash", "Label": "Failure_issue"}, {"Entity": "BHC", "Label": "Manufacturer"}, {"Entity": "replaced the warning triangle with a domestically purchased one or credited the customer?s account", "Label": "Corrective_action"}]
  },
  {
    "Sentence": """EQUIPMENT DESCRIPTION:  PERFORMA INFANT SEATS MANUFACTURED FROM JANUARY 26, 1996 THROUGH JULY 31, 1997.    THESE MATERIAL USED IN THESE SEATS DO NOT COMPLY WITH FMVSS NO. 302, "FLAMMABILITY OF INTERIOR MATERIALS." THE MATERIAL USED IN THESE INFANT SEATS COULD POSSIBLY IGNITE BURNING AN OCCUPANT OF THE SEAT. KOLCRAFT WILL REPLACE THE MATERIAL ON THESE INFANT SEATS.""",

    "Output": [{"Entity": "INFANT SEATS", "Label": "Component"}, {"Entity": "IGNITE BURNING", "Label": "Failure_issue"}, {"Entity": "KOLCRAFT", "Label": "Manufacturer"}, {"Entity": "REPLACE THE MATERIAL ON THESE INFANT SEATS", "Label": "Corrective_action"}]
  }
]