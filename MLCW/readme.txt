To run my code, 

Open the CSV file in the zip file:  processed.cleaveland.csv 
Make sure there are not no gaps between the observations, if there are any gaps fill delete the gaps. 
(Open with excel)

Then from the zip file open the MLCW.mlx file and put it in the download directory along with the processed.cleveland.csv file.   

Change the third line of the mlx script to 
dataset = readtable(“downloads/processed.cleveland.csv”) 

Then run it by section Or you can run the whole script (it will take long to load)

% My optimal model is from line 383 to 450 for logistic regression 
% My optimal model is from line 506 to 564 for naive bases.
% My additional optimal plots is from line 565 to 586