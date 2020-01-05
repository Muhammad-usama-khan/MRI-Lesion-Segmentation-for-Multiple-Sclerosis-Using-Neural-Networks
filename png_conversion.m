dir_vol = ('D:\Neural_Nets\Project\4. Training_Testing_Validating\Validating\FLAIR')
dir_gt =('D:\Neural_Nets\Project\4. Training_Testing_Validating\Validating\GT')

dir_vol_patients_raw = dir(dir_vol)
dir_vol_patients_gt = dir(dir_gt)

dir_vol_save = ('D:\Neural_Nets\Project\5. Data_png\Testing\FLAIR')
dir_gt_save = ('D:\Neural_Nets\Project\5. Data_png\Testing\GT')

%%
for i=3:1:length(dir_vol_patients_raw)
    i
    cd (dir_vol)
    vol_raw = double(niftiread(dir_vol_patients_raw(i).name));
    cd (dir_gt)
    vol_gt = double(niftiread(dir_vol_patients_gt(i).name));
    
    cd (dir_vol_save)
    
    dash= '_slice_'
    name_raw = dir_vol_patients_raw(i).name
    name_raw = name_raw(1:end-7)
    name_raw = strcat(name_raw,dash)
    png = '.png'
    
    for j=1:1: size(vol_raw,3)
        img_raw = vol_raw(:,:,j);
        imwrite(img_raw,strcat(name_raw,num2str(j),png))
    end
    
    
    cd (dir_gt_save)
    
    dash= '_slice_'
    name_gt = dir_vol_patients_gt(i).name
    name_gt = name_gt(1:end-7)
    name_gt = strcat(name_gt,dash)
    png = '.png'
    
    for j=1:1: size(vol_gt,3)
        img_gt = vol_gt(:,:,j);
        imwrite(img_gt,strcat(name_gt,num2str(j),png))
    end
        
end
