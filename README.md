# hongkongese-identifier

Simple statistical detector for the following languages:

* Hong Kongese / Yue / Cantonese
* Standard Chinese
* English

## Files

* hky_id.py - Hong Kongese identifier
* hky-classification/ - handmade data set for demo

## Algorithm

1. Hong Kongese-ness = Hong Kongese markers / All characters
2. Chinese-ness = Chinese markers / All characters
3. If (Hong Kongese-ness - Chinese-ness) > 0.02, then it is Hong Kongese
4. Otherwise it is Standard Chinese