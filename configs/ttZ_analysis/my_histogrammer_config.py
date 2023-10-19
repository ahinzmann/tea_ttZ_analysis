nEvents = -1
printEveryNevents = 1000

inputFilePath = "../samples/background_dy.root"
histogramsOutputFilePath = "../samples/histograms/background_dy.root"

#extraEventCollections = {
#    "GoodLeptons": {
#        "inputCollections": ("Muon", "Electron"),
#        "pt": (30., 9999999.),
#        "eta": (-2.4, 2.4),
#    },
#}

defaultHistParams = (
#  collection      variable          bins    xmin     xmax     dir
  #("Event"       , "nMuon"         , 50,     0,       50,      ""  ),
  ("Electron"        , "pt"            , 400,    0,       200,     ""  ),
  ("Electron"        , "eta"           , 100,    -2.5,    2.5,     ""  ),
  #("Event"       , "nGoodLeptons"  , 50,     0,       50,      ""  ),
  #("GoodLeptons" , "pt"            , 400,    0,       200,     ""  ),
  #("GoodLeptons" , "eta"           , 100,    -2.5,    2.5,     ""  ),
)

weightsBranchName = "genWeight"
