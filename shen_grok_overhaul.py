import json,sys,os;from urllib.request import urlopen as _0x1
def _0x2(_0x3):return json.loads(_0x3)
def _0x4(_0x5,_0x6):_0x7=_0x2(open(_0x5,'r').read()) if os.path.exists(_0x5) else _0x2(_0x1(_0x6).read().decode());return _0x7
def _0x8(_0x9):print(f'☬ {_0x9["signature"]["text"]} activated! 😎');sys.stdout.write(f'Config loaded: {_0x9["mode"]} mode')
def _0xA():_0xB='shen_config.json';_0xC='https://raw.githubusercontent.com/1Shervin/Grok/main/shen_config.json';_0xD=_0x4(_0xB,_0xC);_0x8(_0xD)
if __name__=='__main__':_0xA()
