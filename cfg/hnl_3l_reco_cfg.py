import os
from collections import OrderedDict
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.config     import printComps
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
from CMGTools.RootTools.utils.splitFactor import splitFactor

# import Heppy analyzers:
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer      import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.SkimAnalyzerCount import SkimAnalyzerCount
from PhysicsTools.Heppy.analyzers.core.EventSelector     import EventSelector
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer    import PileUpAnalyzer
from PhysicsTools.Heppy.analyzers.gen.GeneratorAnalyzer  import GeneratorAnalyzer
from PhysicsTools.Heppy.analyzers.gen.LHEWeightAnalyzer  import LHEWeightAnalyzer

from CMGTools.H2TauTau.proto.analyzers.TriggerAnalyzer   import TriggerAnalyzer
from CMGTools.H2TauTau.proto.analyzers.JetAnalyzer       import JetAnalyzer

# import HNL analyzers:
from CMGTools.HNL.analyzers.HNLAnalyzer           import HNLAnalyzer
from CMGTools.HNL.analyzers.HNLTreeProducerSignal import HNLTreeProducerSignal
from CMGTools.HNL.analyzers.HNLTreeProducerData   import HNLTreeProducerData
from CMGTools.HNL.analyzers.HNLGenTreeAnalyzer    import HNLGenTreeAnalyzer
from CMGTools.HNL.analyzers.RecoGenAnalyzer       import RecoGenAnalyzer
from CMGTools.HNL.analyzers.CheckHNLAnalyzer      import CheckHNLAnalyzer

# import samples, signal
# from CMGTools.HNL.samples.signal import all_signals as samples
# from CMGTools.HNL.samples.signal import all_signals_e as samples
from CMGTools.HNL.samples.signal import all_signals_mu as samples
# from CMGTools.HNL.samples.signal import signals_mass_3 as samples
# from CMGTools.HNL.samples.signal import signals_test as samples
# from CMGTools.HNL.samples.signal import signals_mass_1
# from CMGTools.HNL.samples.signal import signals_mass_2p1

# from CMGTools.HNL.samples.signal import HN3L_M_2p5_V_0p0173205080757_e_onshell
# from CMGTools.HNL.samples.signal import HN3L_M_2p5_V_0p0173205080757_e_onshell
# from CMGTools.HNL.samples.localsignal import TTJets_amcat as TTJets_amcat
# from CMGTools.HNL.samples.samples_mc_2017 import TTJets_amcat
# from CMGTools.HNL.samples.signal import disp1plus as samples
from CMGTools.HNL.samples.localsignal import TTJets_amcat, HN3L_M_2p5_V_0p0173205080757_e_onshell
# from CMGTools.HNL.samples.localsignal import HN3L_M_2p5_V_0p0173205080757_e_onshell, HN3L_M_2p5_V_0p00707106781187_e_onshell

cfg.PromptLeptonMode = 'ele' # 'ele', 'mu'
# cfg.PromptLeptonMode = 'mu' # 'ele', 'mu'
# cfg.DataSignalMode = 'signal' # 'signal', 'data'
cfg.DataSignalMode = 'data' # 'signal', 'data'
## this should be changed to bkg&data / signal 

puFileMC   = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/MC_Moriond17_PU25ns_V1.root'
puFileData = '/afs/cern.ch/user/a/anehrkor/public/Data_Pileup_2016_271036-284044_80bins.root'

###################################################
###                   OPTIONS                   ###
###################################################
# Get all heppy options; set via "-o production" or "-o production=True"
# production = True run on batch, production = False (or unset) run locally

# production         = getHeppyOption('production' , False)
production         = getHeppyOption('production' , False)
pick_events        = getHeppyOption('pick_events', False)

###################################################
###               HANDLE SAMPLES                ###
###################################################

# samples = [HN3L_M_2p5_V_0p00707106781187_e_onshell, HN3L_M_2p5_V_0p0173205080757_e_onshell, TTJets_amcat] #comment if you want to use all samples
samples = [TTJets_amcat]

for sample in samples:
    if cfg.PromptLeptonMode == 'ele':
        sample.triggers  = ['HLT_Ele27_WPTight_Gsf_v%d'          %i for i in range(1, 15)] #electron trigger
        sample.triggers += ['HLT_Ele32_WPTight_Gsf_v%d'          %i for i in range(1, 15)] #electron trigger
        sample.triggers += ['HLT_Ele35_WPTight_Gsf_v%d'          %i for i in range(1, 15)] #electron trigger
        sample.triggers += ['HLT_Ele115_CaloIdVT_GsfTrkIdT_v%d'  %i for i in range(1, 15)] #electron trigger
        sample.triggers += ['HLT_Ele135_CaloIdVT_GsfTrkIdT_v%d'  %i for i in range(1, 15)] #electron trigger
    if cfg.PromptLeptonMode == 'mu':
        sample.triggers  = ['HLT_IsoMu24_v%d'                    %i for i in range(1, 15)] #muon trigger
        sample.triggers += ['HLT_IsoMu27_v%d'                    %i for i in range(1, 15)] #muon trigger
        sample.triggers += ['HLT_Mu50_v%d'                       %i for i in range(1, 15)] #muon trigger

    sample.splitFactor = splitFactor(sample, 1e5)
    sample.puFileData = puFileData
    sample.puFileMC   = puFileMC

selectedComponents = samples

###################################################
###                  ANALYSERS                  ###
###################################################
eventSelector = cfg.Analyzer(
    EventSelector,
    name='EventSelector',
    # toSelect=[]
    toSelect=[326]
)

lheWeightAna = cfg.Analyzer(
    LHEWeightAnalyzer, name="LHEWeightAnalyzer",
    useLumiInfo=False
)

jsonAna = cfg.Analyzer(
    JSONAnalyzer,
    name='JSONAnalyzer',
)

skimAna = cfg.Analyzer(
    SkimAnalyzerCount,
    name='SkimAnalyzerCount'
)

if cfg.DataSignalMode == 'data': # or bkg for that matter
    sampleTriggerHandles = ['slimmedPatTrigger','','']   # for bkg MC
if cfg.DataSignalMode == 'signal':
    sampleTriggerHandles = ['selectedPatTrigger','','']  # for signal MC

triggerAna = cfg.Analyzer(
    TriggerAnalyzer,
    name='TriggerAnalyzer',
    addTriggerObjects=True,
    requireTrigger=True,
    triggerObjectsHandle=sampleTriggerHandles,
    usePrescaled=False
)

vertexAna = cfg.Analyzer(
    VertexAnalyzer,
    name='VertexAnalyzer',
    fixedWeight=1,
    keepFailingEvents=True,
    verbose=False
)

pileUpAna = cfg.Analyzer(
    PileUpAnalyzer,
    name='PileUpAnalyzer',
    true=True
)

# for each path specify which filters you want the muons to match to
triggers_and_filters = OrderedDict()
if cfg.PromptLeptonMode == 'mu':
    triggers_and_filters['HLT_IsoMu24'] = ['hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07']
    triggers_and_filters['HLT_IsoMu27'] = ['hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07']
    triggers_and_filters['HLT_Mu50']    = ['hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q']
if cfg.PromptLeptonMode == 'ele':
    triggers_and_filters['HLT_Ele27_WPTight_Gsf']         = ['hltEle27WPTightGsfTrackIsoFilter']
    triggers_and_filters['HLT_Ele32_WPTight_Gsf']         = ['hltEle32WPTightGsfTrackIsoFilter']
    triggers_and_filters['HLT_Ele35_WPTight_Gsf']         = ['hltEle35noerWPTightGsfTrackIsoFilter']
    triggers_and_filters['HLT_Ele115_CaloIdVT_GsfTrkIdT'] = ['hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter']
    triggers_and_filters['HLT_Ele135_CaloIdVT_GsfTrkIdT'] = ['hltEle135CaloIdVTGsfTrkIdTGsfDphiFilter']

HNLAnalyzer = cfg.Analyzer(
    HNLAnalyzer,
    name='HNLAnalyzer',
)

if cfg.DataSignalMode == 'signal': # 'signal', 'data'
    HNLTreeProducer = cfg.Analyzer(
        HNLTreeProducerSignal,
        name='HNLTreeProducerSignal',
        # fillL1=False,
    )
if cfg.DataSignalMode == 'data': # 'signal', 'data'
    HNLTreeProducer = cfg.Analyzer(
        HNLTreeProducerData,
        name='HNLTreeProducerData',
        # fillL1=False,
    )

HNLGenTreeAnalyzer = cfg.Analyzer(
    HNLGenTreeAnalyzer,
    name='HNLGenTreeAnalyzer',
)

RecoGenAnalyzer = cfg.Analyzer(
    RecoGenAnalyzer,
    name='RecoGenAnalyzer',
)

CheckHNLAnalyzer = cfg.Analyzer(
    CheckHNLAnalyzer,
    name='CheckHNLAnalyzer',
)

# see SM HTT TWiki
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016#Jet_Energy_Corrections
jetAna = cfg.Analyzer(
    JetAnalyzer,
    name              = 'JetAnalyzer',
    jetCol            = 'slimmedJets',
    jetPt             = 20.,
    jetEta            = 2.4,
    relaxJetId        = False, # relax = do not apply jet ID
    relaxPuJetId      = True, # relax = do not apply pileup jet ID
    jerCorr           = True,
    puJetIDDisc       = 'pileupJetId:fullDiscriminant',
    recalibrateJets   = True,
    applyL2L3Residual = 'MC',
#    mcGT              = '80X_mcRun2_asymptotic_2016_TrancheIV_v8',
#    dataGT            = '80X_dataRun2_2016SeptRepro_v7',
    #jesCorr = 1., # Shift jet energy scale in terms of uncertainties (1 = +1 sigma)
)
###################################################
###                  SEQUENCE                   ###
###################################################
if cfg.DataSignalMode == 'data':
    sequence = cfg.Sequence([
    #     eventSelector,
        lheWeightAna, # les houche
        jsonAna,
        skimAna,
        triggerAna,
        vertexAna,
        pileUpAna,
        HNLAnalyzer,
        jetAna,
        HNLTreeProducer,
    ])

if cfg.DataSignalMode == 'signal':
    sequence = cfg.Sequence([
    #     eventSelector,
        lheWeightAna, # les houche
        jsonAna,
        skimAna,
        triggerAna,
        vertexAna,
        pileUpAna,
        HNLGenTreeAnalyzer,
        RecoGenAnalyzer,
        HNLAnalyzer,
        jetAna,
        CheckHNLAnalyzer,
        HNLTreeProducer,
    ])

###################################################
###            SET BATCH OR LOCAL               ###
###################################################
if not production:
    # comp                 = HN3L_M_2p5_V_0p0173205080757_e_onshell
    # comp                 = HN3L_M_2p5_V_0p00707106781187_e_onshell
    # comp                 = samples
    comp                 = TTJets_amcat
    selectedComponents   = [comp]
    comp.splitFactor     = 1
    comp.fineSplitFactor = 1
    comp.files           = comp.files[:]

# the following is declared in case this cfg is used in input to the
# heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config(
    components   = selectedComponents,
    sequence     = sequence,
    services     = [],
    preprocessor = None,
    events_class = Events
)

printComps(config.components, True)

