Set-Location -Path .\IM
Start-Process -FilePath .\start.bat

Set-Location -Path ..\FusionEngine
Start-Process -FilePath .\start.bat

Set-Location -Path ..
conda activate rasa-env
Set-Location -Path .\rasaDemo
Start-Process -FilePath rasa -ArgumentList 'run', '--enable-api', '-m', '.\models\', '--cors', '*'

Set-Location -Path ..\WebApps_wihout_WakeUpWord\WebAppAssistantV2
Start-Process -FilePath .\start_web_app.bat
Set-Location -Path ..

