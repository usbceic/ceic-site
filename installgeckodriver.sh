set -e
# Descargar geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz

# descomprimirlo
tar -xvzf geckodriver-v0.20.1-linux64.tar.gz
rm geckodriver-v0.20.1-linux64.tar.gz


chmod +x geckodriver
echo $PATH | egrep "$HOME/bin(/|\n|:)" &> /dev/null
# Verificar ei el path tiene el $HOME/bin
if [ $? != 0 ]; then
    echo "export PATH=$PATH:$HOME/bin" >> ~/.bashrc
    export PATH=$PATH:$HOME/bin
fi
mkdir -p $HOME/bin
mv geckodriver $HOME/bin
echo "geckodriver instalado"
