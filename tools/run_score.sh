#!/bin/bash


#chime_scorer.py --just-generate all all $1 $2 #test11 /mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/mreze-2015-05-28/run8/autosave_run8_epoch184.autosave

#chime_scorer.py --just-test val all $1 $2 #test11 /mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/mreze-2015-05-28/run8/autosave_run8_epoch184.autosave  

chime_scorer.py --just-test all all $1 $2
