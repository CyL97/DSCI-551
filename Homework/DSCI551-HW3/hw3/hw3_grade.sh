for f in *.sql
do
	mysql --host=localhost --user=dsci551 --password="Dsci-551" < "$f" > "${f}.res"
done