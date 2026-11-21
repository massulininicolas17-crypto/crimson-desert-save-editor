#define MyAppName "Crimson Desert Save Editor"
#define MyAppPublisher "cdse-community"
#define MyAppExeName "cdse.exe"
[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\CrimsonDesertSaveEditor
OutputBaseFilename=cdse-setup-{#MyAppVersion}
[Files]
Source: "..\dist\cdse.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\plugins\*.cdse_ext"; DestDir: "{app}\plugins"
[Icons]
Name: "{autoprograms}\Crimson Desert Save Editor"; Filename: "{app}\{#MyAppExeName}"