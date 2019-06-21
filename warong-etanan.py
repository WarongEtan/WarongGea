clear
figlet Warong Etan | lolcat
echo "________________________________________________________________"
echo "\033[34;1m Selamat Datang Di Tools Warong Etan"
sleep 2
echo "\033[35;1m Kalian Dapat Menginstall Berbagai Tools" | lolcat
sleep 2
echo "\033[31;1m:)  Salam Warong Etan (:"
sleep 2
echo "_________________________________________________________________"

echo "==============================>" | lolcat
echo "\033[34;1m[01] Lacak Ip"
echo "==============================>" | lolcat
echo "[02] install Taek By Luter"
echo "==============================>" | lolcat
echo "[03] Hack Wifi Khusus Root"
echo "==============================>" | lolcat
echo "[04] Hack Instagram"
echo "==============================>" | lolcat
echo "[05] MBF Hack Fb"
echo "==============================>" | lolcat
echo "[06] Memutar Music Di Termux"
echo "==============================>" | lolcat
echo "[07] Tembak Kuota XL"
echo "==============================>" | lolcat


echo "\033[35;1m Silakan Pilih Angkanya Kemudian Enter"

read -p "Warong Etan ➡" pilihan


if [ $pilihan = "01" ] || [ $pilihan = "1" ]
then
apt update
apt upgrade
pkg install git
pkg install python
git clone https://github.com/maldevel/IPGeolocation
cd IPGeolocation
chmod +x ipgeolocation.py
pip install -r requirements.txt
python ipgeolocation.py -m
python ipgeolocation.py -t IP yang ingin dilacak
fi

if [ $pilihan = "02" ] || [ $pilihan = "2" ]
then
pkg update
pkg upgrade
pkg install git
pkg install python
pkg install python2
git clone https://github.com/trio7210/TAEK
cd TAEK
python2 TAEK.py
fi

if [ $pilihan = "04" ] || [ $pilihan = "4" ]
then
pkg update
pkg upgrade
pkg install python
pkg install nano
git clone https://github.com/avramit/instahack.git
ls
cd instahack
ls
pip install requests
cd instahack
nano instahack.txt
fi

if [ $pilihan = "03" ] || [ $pilihan = "3" ]
then
pkg update
pkg upgrade
pkg install git 
git clone https://github.com/esc0rtd3w/wifi-hacker
cd wifi-hacker
ls
chmod +x wifi-hacker.sh
ls
./wifi-hacker.sh
fi

if [ $pilihan = "05" ] || [ $pilihan = "05" ]
then
pkg update
pkg upgrade
pkg install git
pkg install python2
pip2 install mechanize
git clone http://github.com/pirmansx/mbf
ls
cd mbf
python2 mbf.py
fi

if [ $pilihan = "06" ] || [ $pilihan = "6" ]
then
pip install mps_youtube
pip install youtube_dl
apt install mpv
mpsyt
/Enak Susunya
fi 

if [ $pilihan = "07" ] || [ $pilihan = "7" ]
then
apt update && apt upgrade
pkg install git
pkg install python
pkg install python2
git clone https://github.com/albertoanggi/xl-py
pip install -r requirements.txt
chmod +x app.py
python2 app.py
fi
echo "====================================================" | lolcat
echo "Kalau ingin lihat lebih lengkap kalian copy link youtube di bawah ini" | lolcat
echo "_____________________________________________________________________"
echo "		https://www.youtube.com/channel/UCYtIaiNL2DhdhYnv2wg0bAw		" | lolcat
echo "====================================================" | lolcat
fi