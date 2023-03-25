![logo.png](readme%2Flogo.png)
<h1>Remote controller</h1>
<h2>Instruction</h2>
<h3>Install</h3>
<p>Download project and unpack him.</p>
<p>Open project in Pycharm and install module aiogram:</p>

```
pip install aiogram
```
<p><a href="https://botcreators.ru/blog/kak-sozdat-svoego-bota-v-botfather/">Create Telegram-Bot</a> and enter token its in config.py:</p>

```
lis = os.listdir(path='<your_path>')
```
<p>If you have windows then replace line 58 in main.py</p>

```
os.system(f"<path_to_your_player> <path_dir{call.data}>")
```
<p>If you have linux then change path to directory movies in the same line</p>

```
os.system(f"xdg-open <path{call.data}>")
```
<p>Close Pycharm.</p>
<h3>Run</h3>
<p>Open cmd or terminal and enter command</p>

```
cd <path_to_remote_controller>
```
<p>Allow right to execute</p>

```
sudo chmod +x ./App.py
```
<p>Run main.py</p>

```
./App.py
```
Then you can enter bot token and your id:
 
![res.png](readme%2Fres.png)