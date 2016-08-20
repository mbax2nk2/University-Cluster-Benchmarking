while read p; 
do sed "s/TEMPLATE/$p/" TEMPLATE.txt > $p.txt;
done < clustersWithPrinterData.txt
