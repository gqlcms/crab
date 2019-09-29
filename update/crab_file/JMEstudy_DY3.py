from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = Configuration()
config.section_("General")
config.General.requestName   = 'JMEstudy_DY4'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName='Analysis'
config.JobType.sendExternalFolder = True
#config.JobType.inputFiles = ['Summer16_23Sep2016BCDV3_DATA_L1FastJet_AK4PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L2Relative_AK4PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L3Absolute_AK4PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L2L3Residual_AK4PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L1FastJet_AK8PFchs.txt','Summer16_23Sep2016BCDV3_DATA_L2Relative_AK8PFchs.txt','Summer16_23Sep2016BCDV3_DATA_L3Absolute_AK8PFchs.txt','Summer16_23Sep2016BCDV3_DATA_L2L3Residual_AK8PFchs.txt','Summer16_23Sep2016BCDV3_DATA_L1FastJet_AK8PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L2Relative_AK8PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L3Absolute_AK8PFPuppi.txt','Summer16_23Sep2016BCDV3_DATA_L2L3Residual_AK8PFPuppi.txt']
# Name of the CMSSW configuration file
config.JobType.inputFiles = ['Autumn18_RunABCD_V17_DATA.db','Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt']
config.JobType.psetName    = 'JMEanalysis.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 8000

config.section_("Data")
config.Data.inputDataset = '/DYToMuMuorEleEle_M-20_14TeV_pythia8/PhaseIITDRSpring19MiniAOD-NoPU_106X_upgrade2023_realistic_v3-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
#config.Data.lumiMask = 'Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'#'Cert_246908-254879_13TeV_PromptReco_Collisions15_JSON.txt' #'Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON.txt'#Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.txt'#'lumiSummary_13_07_2015_JSON.txt'#https://twiki.cern.ch/twiki/pub/CMS/ExoDijet13TeV/lumiSummary_13_07_2015_JetHT.json'#https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
#config.Data.runRange = ''#'250843-250932' # '193093-194075'

config.Data.outLFNDirBase='/store/user/%s/Guo/JMEstudy/update' % (getUsernameFromSiteDB())#='/store/user/%s/Guo' % (getUsernameFromSiteDB())#+'/'+name+'/'
config.Data.publication = False
config.Data.outputDatasetTag = 'JMEqgl_2'

config.section_("Site")
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T3_US_FNALLPC'
