#!/bin/bash
#Parámetros (opcionales) Unidad de almacenamiento, resolución. 
STG_UNIT_FOLDER="$1" 
THUMBNAILS_FOLDER="$2"
X_RES="$3"
Y_RES="$4"
COLORS="$5"

source $HOME/.bashrc

mkdir -p $THUMBNAILS_FOLDER
for file in $STG_UNIT_FOLDER/*.nc
do
	bn=`basename $file`

	for ds in `gdalinfo $file |grep -Eo "NETCDF.*"`
	do
		if [ ${ds##*\:} != 'dataset' ]
		then

			if [ -f $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png ]
			then
				if [ $file -ot $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png ]
				then
					continue
				fi
			fi

			echo "Escribiendo los thumbnails para el archivo $file y la banda ${ds##*\:}"
			gdal_translate -a_srs EPSG:32618 -a_nodata -9999 -stats -of PNG -scale -outsize $X_RES $Y_RES $ds $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png
			convert -transparent "#000000" $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png $COLORS -clut $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png
			convert $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png -background Khaki label:"${bn%.nc}.${ds##*\:}" -gravity Center -append $THUMBNAILS_FOLDER/${bn%.nc}.${ds##*\:}.png
		fi
	done
done
