
~/softwares/MultiBoost/multiboost --stronglearner AdaBoostMH --learnertype TreeLearner --baselearnertype SingleStumpLearner 10 --fileformat arff --train train.arff 2 --outputinfo tmpres ham


~/softwares/MultiBoost/multiboost --stronglearner AdaBoostMH --learnertype TreeLearner --baselearnertype SingleStumpLearner 10 --fileformat arff --posteriors train.arff shyp.xml res 10
