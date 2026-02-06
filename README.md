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



## RESOUCES


UNET Pretrained Weights :- !gdown 1M_qtAZ0X7v97jZL3w6DM0zkXCcfztF-k 

LaMa Denoiser Pretrained weights :- !gdown 1K6JDi8l2QHYpHSmXZUYowEoFWAI60LYz

Final Denoiser Pretrained weights :- !gdown 1MoOIfk4j-1jrRIVDYgpmv6I_IixUYJIz

LaMa Infered Images(36,500) :- )!gdown 1m5dd3hd51p-EDHj05Pqsgspoiy5Gs6f_ 

MAT infered Images(First 17091) :- !gdown 1kUMW5pec4JVR0AKMkH49aoIOTGnnPmuP

MAT infered Images(rest) :- !gdown 154biIksdcBovAmEDvARfg5V1HPZQNZVP

Masks(36,500) :- !gdown 14-0t8X0pZBv_tyhs-PxNISdokKqO-aUN 

Train Data(20 imgs each scene) :- !gdown 13otq0aAzCB9l9MIZpJhOJACIJeboS0NY



_____________________________________________________________________________________________________________________________________________________________________________________________________________________

For the pretrained models that we have used for the obtaining the LaMa and MAT infered images, below are the links and version that we used

1. LaMa -> The weigths were trained on Places dataset (https://drive.google.com/drive/folders/1B2x7eQDgecTL0oh3LSIBDGj0fTxs6Ips)

so the above one is the official link for LAMA resources also it includes all the weights available for the lama model and we have specifically used “LaMa Fourier(best.ckpt)” weight for our purpose

2. MAT -> The weights were trained on Places Dataset(https://drive.google.com/uc?id=15gbGYCGZY__Hchja-wPbqZqGj431-8ih&confirm=t&uuid=5f9edf14-9450-433e-bf76-18d924e55578)

filename is - “Places_512.pkl”

NOTE - CURRENTLY(AT TIME OF PUBLISHING THIS PAPER), THE MODEL DOWNLOAD LINK OF MAT MODEL'S ARE NOT WORKING SO WE HAVE SERVED THE EARLIER DOWNLOADED MODEL FILE ON GOOGLE DRIVE AND PROVIDED ITS DOWNLOAD LINK

# Executing

refer to train and test notebook
