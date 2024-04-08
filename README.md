# python-automacao-sau

# install chrome teste wsl ubuntu

```sh
vwget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install google-chrome-stable

```

# install ubuntu wsl 

```sh
 sudo apt install python3-pip
 pip install selenium
 sudo apt-get install libnss3
 ```

# git

```sh
echo "# python-automacao-sau" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/andredeabreugoncalves/python-automacao-sau.git
git push -u origin main

```