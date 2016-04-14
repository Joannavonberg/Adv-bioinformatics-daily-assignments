I found this JSfiddle script:

http://jsfiddle.net/njbusz3c/2/

Which parses a PDB-file from the RCSB and returns several features. I want to be able to plot the B-factors (preferably of my own data).

I also found this JSfiddle script:

http://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/highcharts/demo/line-basic/

Which plots hard-coded data. I managed to transport the data from PDB-files to the code for plotting, and included an option to display my own experimental data.

This data is of a molecular dynamics simulation of lysozyme in a crystal. I calculated the RMSF, which can be converted to b-factor, and wrote that to the output-PDB-file. I use this to compare my md data to experimental data.

This is the result:

http://jsfiddle.net/joannataart/5wu5zf4u/1/

You first have to click 'load PDB'  and then 'display PDB'. You can change the text to any PDB on the RCSB database, or to 'Joanna' which will show my data.

(actually, my data now shows that the b-factor is 0 for every atom, which is correct, because I hadn't calculated b-factor for this file. Tomorrow morning I will upload a file with b-factors != 0.)
