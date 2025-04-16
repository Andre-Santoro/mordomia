# Arquivo: mordom_IA.spec

# -- IMPORTS --
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
import os

# -- DADOS ADICIONAIS --
flet_data = collect_data_files("flet_desktop")

# Caminho do ícone (coloque o .ico na mesma pasta do .py)
icone_path = os.path.join(os.getcwd(), "favicon.ico")

# -- ANALYSIS --
a = Analysis(
    ['mordom_IA.py'],
    pathex=[],
    binaries=[],
    datas=flet_data,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MordomIA',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # se quiser mostrar terminal, mude para True
    icon=icone_path
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MordomIA'
)