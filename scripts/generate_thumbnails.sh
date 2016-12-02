#!/bin/bash
#Parámetros (opcionales) Unidad de almacenamiento, resolución. 
STG_UNIT_FOLDER="$1" 
THUMBNAILS_FOLDER="$2"
X_RES="$3"
Y_RES="$4"

mkdir -p $THUMBNAILS_FOLDER
for file in $STG_UNIT_FOLDER/*.nc
do
	for ds in `gdalinfo $file |grep -Eo "NETCDF.*"`
	do
		bn=`basename $file`
		if [ ${ds##*\:} != 'dataset' ]
		then
			echo "Escribiendo los thumbnails para el archivo $file y la banda ${ds##*\:}"
			gdal_translate -a_srs EPSG:32618 -a_nodata -9999 -stats -of PNG -scale -outsize $X_RES $Y_RES $ds $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png
			convert -transparent "#000000" $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png  $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png
		fi
	done
done
