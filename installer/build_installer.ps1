# Inno Setup wrapper for crimson-desert-save-editor
param([string]$Version = "0.9.3")
$iscc = "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe"
if (-not (Test-Path $iscc)) { Write-Error "Inno Setup 6 required"; exit 1 }
& $iscc "/DMyAppVersion=$Version" "installer\cdse.iss"