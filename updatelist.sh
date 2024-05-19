cd ~/git/cldph
python requestCLD.py
python requestCLD_adguard.py
git add .
git commit -m "update database"
git push
pihole -g
