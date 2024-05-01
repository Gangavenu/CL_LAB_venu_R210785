inputfile='/home/r210785/Documents/CL_LAB/week-8/Chorus.wav'
outputfile='/home/r210785/Documents/CL_LAB/week-8/Chorus.wav'
[y,Fs]=audioread(inputfile);
reversedData=flipud(y);
audiowrite(outputfile,reversedData,Fs);
disp('audio is reversed and successfully saved')