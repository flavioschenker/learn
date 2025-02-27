# install conda
mkdir -p ~/mconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/mconda/install.sh
bash ~/mconda/install.sh -b -u -p ~/mconda
rm ~/mconda/install.sh
export PATH="$HOME/mconda/bin:$PATH"
conda init --all

# install vscode
conda create -n ml
conda activate ml
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia