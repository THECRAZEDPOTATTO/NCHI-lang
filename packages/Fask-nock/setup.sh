sudo apt install gnupg ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt update
sudo apt install mono-devel
sudo apt install g++
sudo apt install build-essential
sudo apt install default-jre
javac -version
sudo apt-get install ruby-full
python3 --version
echo 'If python is not installed run this: sudo apt-get install python3'
curl -L http://xrl.us/installperlnix | bash
sudo apt-get install sbcl
