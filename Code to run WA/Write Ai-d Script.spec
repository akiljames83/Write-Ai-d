# -*- mode: python -*-

block_cipher = None


a = Analysis(['Write Ai-d Script.py'],
             pathex=['C:\\Users\\akilj\\Desktop\\School\\1P10A\\Design Tut\\DP4\\Write Ai-d\\Code to run WA'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Write Ai-d Script',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\akilj\\Desktop\\School\\1P10A\\Design Tut\\DP4\\Write Ai-d\\Code to run WA\\pencil.ico')
