import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

<<<<<<< HEAD
=======
DYJetsToLL_M5to50 = creator.makeMCComponent(
    name    = 'DYJetsToLL_M5to50',
    dataset = '/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', 
    user    = 'CMS', 
    pattern = '.*root',
    xSec    = 71310.0, 
    useAAA  = True
)
# .sigma = 71310 \pm 70 pb
DYJetsToLL_M5to50.nGenEvents = DYJetsToLL_M5to50.dataset_entries


DYJetsToLL_M50 = creator.makeMCComponent(
    name    = 'DYJetsToLL_M50',
    dataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 1921.8*3, 
    useAAA  = True
)
DYJetsToLL_M50.nGenEvents = DYJetsToLL_M50.dataset_entries

>>>>>>> vstampf/rm-94-patch-3

ZZZ = creator.makeMCComponent(
    name    = 'ZZZ', 
    dataset = '/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.01398, 
    useAAA  = True
)

ZZZ .nGenEvents = ZZZ.dataset_entries 


WZZ = creator.makeMCComponent(
    name    = 'WZZ', 
    dataset = '/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.05565, 
    useAAA  = True
)

WZZ .nGenEvents = WZZ.dataset_entries 


WWZ = creator.makeMCComponent(
    name    = 'WWZ', 
    dataset = '/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.1651, 
    useAAA  = True
)

WWZ .nGenEvents = WWZ.dataset_entries 


WWW = creator.makeMCComponent(
    name    = 'WWW', 
    dataset = '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.2086, 
    useAAA  = True
)

WWW .nGenEvents = WWW.dataset_entries 


WWTo2L2Nu = creator.makeMCComponent(
    name    = 'WWTo2L2Nu', 
    dataset = '/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.1729, 
    useAAA  = True
)

WWTo2L2Nu .nGenEvents = WWTo2L2Nu.dataset_entries 


WGGJets = creator.makeMCComponent(
    name    = 'WGGJets', 
    dataset = '/WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.03711, 
    useAAA  = True
)

WGGJets .nGenEvents = WGGJets.dataset_entries 


TTWJetsToLNu = creator.makeMCComponent(
    name    = 'TTWJetsToLNu', 
    dataset = '/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.2043, 
    useAAA  = True
)

TTWJetsToLNu .nGenEvents = TTWJetsToLNu.dataset_entries 


TTZToLLNuNu = creator.makeMCComponent(
    name    = 'TTZToLLNuNu', 
    dataset = '/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 0.2529, 
    useAAA  = True
)

TTZToLLNuNu .nGenEvents = TTZToLLNuNu.dataset_entries 


TTZToLL = creator.makeMCComponent(
    name    = 'TTZToLL', 
    dataset = '/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
<<<<<<< HEAD
    xSec    = 0.05324, #from Christian Veelken
=======
    # xSec    = #FIXME 
>>>>>>> vstampf/rm-94-patch-3
    useAAA  = True
)

TTZToLL .nGenEvents = TTZToLL.dataset_entries 


ST_s_channel_4f_leptonDecays = creator.makeMCComponent(
<<<<<<< HEAD
    name    = 'ST_s_channel_4f_leptonDecays', 
=======
    name    = 'ST_s-channel_4f_leptonDecyas', 
>>>>>>> vstampf/rm-94-patch-3
    dataset = '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 3.68, 
    useAAA  = True
)

ST_s_channel_4f_leptonDecays .nGenEvents = ST_s_channel_4f_leptonDecays.dataset_entries 


ST_t_channel_antitop_4f_inclusiveDecays = creator.makeMCComponent(
<<<<<<< HEAD
    name    = 'ST_t_channel_antitop_4f_inclusiveDecays', 
=======
    name    = 'ST_t-channel_antitop_4f_inclusiveDecays', 
>>>>>>> vstampf/rm-94-patch-3
    dataset = '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 26.23, 
    useAAA  = True
)

ST_t_channel_antitop_4f_inclusiveDecays .nGenEvents = ST_t_channel_antitop_4f_inclusiveDecays .dataset_entries 


ST_t_channel_top_4f_inclusiveDecays = creator.makeMCComponent(
<<<<<<< HEAD
    name    = 'ST_t_channel_top_4f_inclusiveDecays', 
=======
    name    = 'ST_t-channel_top_4f_inclusiveDecays', 
>>>>>>> vstampf/rm-94-patch-3
    dataset = '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 44.07, 
    useAAA  = True
)

ST_t_channel_top_4f_inclusiveDecays .nGenEvents = ST_t_channel_top_4f_inclusiveDecays.dataset_entries 


ST_tW_antitop_5f_inclusiveDecays = creator.makeMCComponent(
    name    = 'ST_tW_antitop_5f_inclusiveDecays', 
    dataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 35.6, 
    useAAA  = True
)

ST_tW_antitop_5f_inclusiveDecays .nGenEvents = ST_tW_antitop_5f_inclusiveDecays.dataset_entries 


ST_tW_top_5f_inclusiveDecays = creator.makeMCComponent(
    name    = 'ST_tW_top_5f_inclusiveDecays', 
    dataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 35.6, 
    useAAA  = True
)

ST_tW_top_5f_inclusiveDecays .nGenEvents = ST_tW_top_5f_inclusiveDecays.dataset_entries 

<<<<<<< HEAD
DY1JetsToLL_M50 = creator.makeMCComponent(
    name    = 'DY1JetsToLL_M50', 
    dataset = '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 1016, 
    useAAA  = True
)

DY2JetsToLL_M50 = creator.makeMCComponent(
    name    = 'DY2JetsToLL_M50', 
    dataset = '/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 331.4,
    useAAA  = True
)

DY2JetsToLL_M50_ext = creator.makeMCComponent(
    name    = 'DY2JetsToLL_M50_ext', 
    dataset = '/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 331.4,
    useAAA  = True
)

DY3JetsToLL_M50 = creator.makeMCComponent(
    name    = 'DY3JetsToLL_M50', 
    dataset = '/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 96.36,
    useAAA  = True
)

DY3JetsToLL_M50_ext = creator.makeMCComponent(
    name    = 'DY3JetsToLL_M50_ext', 
    dataset = '/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',
    user    = 'CMS', 
    pattern = '.*root', 
    xSec    = 96.36,
    useAAA  = True
)
=======
>>>>>>> vstampf/rm-94-patch-3


# LINK for crosssections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns

##########################################################################################
# assign to each sample its own PU profile file. For 2017 it is important to do it per-sample
##########################################################################################
<<<<<<< HEAD
ZZZ                                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ZZZ.root' # derived manually 
WZZ                                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WZZ.root' # derived manually 
WWZ                                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WWZ.root' # derived manually 
WWW                                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WWW.root' # derived manually 
WWTo2L2Nu                                 .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WWTo2L2Nu.root' # derived manually 
WGGJets                                   .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WGGJets.root' # derived manually 
TTWJetsToLNu                              .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTWJetsToLNu.root' # derived manually 
TTZToLLNuNu                               .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTZToLLNuNu.root' # derived manually 
TTZToLL                                   .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTZToLL.root' # derived manually 
ST_s_channel_4f_leptonDecays              .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_s-channel_4f_leptonDecays.root' # derived manually 
ST_t_channel_antitop_4f_inclusiveDecays   .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_t-channel_antitop_4f_inclusiveDecays.root' # derived manually 
ST_t_channel_top_4f_inclusiveDecays       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_t-channel_top_4f_inclusiveDecays.root' # derived manually 
ST_tW_antitop_5f_inclusiveDecays          .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_tW_antitop_5f_inclusiveDecays.root' # derived manually 
ST_tW_top_5f_inclusiveDecays              .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_tW_top_5f_inclusiveDecays.root' # derived manually 
DY1JetsToLL_M50                           .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DY1JetsToLL_M50.root' # derived manually   
DY2JetsToLL_M50                           .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DY2JetsToLL_M50.root' # derived manually     
DY2JetsToLL_M50_ext                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DY2JetsToLL_M50_ext.root' # derived manually 
DY3JetsToLL_M50                           .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DY3JetsToLL_M50.root' # derived manually     
DY3JetsToLL_M50_ext                       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DY3JetsToLL_M50_ext.root' # derived manually 


=======
DYJetsToLL_M5to50 .puFileMC= os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJetsToLL_M5to50.root' 
DYJetsToLL_M50    .puFileMC= os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_DYJetsToLL_M50.root' 
ZZZ  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ZZZ.root' # derived manually 
WZZ  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WZZ.root' # derived manually 
WWZ  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WWZ.root' # derived manually 
WWW  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WWW.root' # derived manually 
WWTo2L2Nu  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WWTo2L2Nu.root' # derived manually 
WGGJets    .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_WGGJets.root' # derived manually 
TTWJetsToLNu  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTWJetsToLNu.root' # derived manually 
TTZToLLNuNu   .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTZToLLNuNu.root' # derived manually 
TTZToLL       .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_TTZToLL.root' # derived manually 
ST_s_channel_4f_leptonDecays             .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_s_channel_4f_leptonDecays.root' # derived manually 
ST_t_channel_antitop_4f_inclusiveDecays  .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_t_channel_antitop_4f_inclusiveDecays.root' # derived manually 
ST_t_channel_top_4f_inclusiveDecays      .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_t_channel_top_4f_inclusiveDecays.root' # derived manually 
ST_tW_antitop_5f_inclusiveDecays         .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_tW_antitop_5f_inclusiveDecays.root' # derived manually 
ST_tW_top_5f_inclusiveDecays             .puFileMC = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_ST_tW_top_5f_inclusiveDecays.root' # derived manually 
>>>>>>> vstampf/rm-94-patch-3


##########################################################################################
hnl_bkg_noskim = [
<<<<<<< HEAD
=======
    DYJetsToLL_M5to50,
    DYJetsToLL_M50,
>>>>>>> vstampf/rm-94-patch-3
    ZZZ, 
    WZZ, 
    WWZ, 
    WWW, 
    WWTo2L2Nu, 
    WGGJets, 
    TTWJetsToLNu, 
    TTZToLLNuNu, 
    TTZToLL, 
    ST_s_channel_4f_leptonDecays, 
    ST_t_channel_antitop_4f_inclusiveDecays, 
    ST_t_channel_top_4f_inclusiveDecays, 
    ST_tW_antitop_5f_inclusiveDecays, 
<<<<<<< HEAD
    ST_tW_top_5f_inclusiveDecays, 
    DY1JetsToLL_M50,     
    DY2JetsToLL_M50,     
    DY2JetsToLL_M50_ext, 
    DY3JetsToLL_M50,     
    DY3JetsToLL_M50_ext, 
=======
    ST_tW_top_5f_inclusiveDecays 
>>>>>>> vstampf/rm-94-patch-3
] 


##########################################################################################
#  data PileUp profile
##########################################################################################
# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Pileup_JSON_Files_For_Run_II
# have a loo at this too, the mb cross section might be off https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/755.html
'''
pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt\
              --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PileUp/pileup_latest.txt\
              --calcMode true --minBiasXsec 69200 --maxPileupBin 200 --numPileupBins 200  pileup_data_golden_json_2017.root
'''
for ibkg in hnl_bkg_noskim:
    ibkg.puFileData = os.environ['CMSSW_BASE'] + '/src/CMGTools/HNL/data/pileup/pileup_data_golden_json_2017.root'




