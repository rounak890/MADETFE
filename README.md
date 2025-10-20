# MADETFE

Official code of MADETFE (Mask Aware Dual Expert with Transformers and FFC based Ensembling)

although this is not neccesary but this repo also might be containing something:- https://github.com/rounak890/image_blend_data/tree/master

if you think it have something then keeep it else delete it 



## notebooks which i think can be useful

   1 7300_train_lama_mat => its the foremost and most important and the mainest notebook in which both denoisers and the ensembler are       	trained on the 7300 imgs as i have mentioned in the paper and alaos evaluation is done there

2. 1700 one : im little unsure abt this one as it contains the similar code as the first one but will check it out later
3. final_lama_mat_denoise_combine - it conatinas the similar train trest code but on a very little subset of abt 1500 imgs
4. inpainting_premade :- conatins code where i made the inference from the lama model and stored them on gdrive
5. MAT.ipynb - shows the inference of mat imgs and dont show there storage to gdrive as there were some error so to present it i will first need to edit it
6. lama_mat_multiscale_ensemble :- good to show to show experimentations as there i had tried different combination techniques for lama and mat imgs, but again it have diff in no. of imgs of lama(22-27k) and MAT(7300)
