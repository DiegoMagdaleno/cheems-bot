function Get-ProcessOutput($FileName, $Arguments) {
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo.UseShellExecute = $false
    $process.StartInfo.RedirectStandardOutput = $true
    $process.StartInfo.RedirectStandardError = $true
    $process.StartInfo.FileName = $FileName
    if ($Arguments) {
        $process.StartInfo.Arguments = $Arguments
    }

    $process.Start()

    $StandardOutput = $process.StandardOutput.ReadToEnd()
    $StandardError = $process.StandardError.ReadToEnd()

    $output = New-Object psobject
    $output | Add-Member -type NoteProperty -name StandardOutput -Value $StandardOutput
    $output | Add-Member -type NoteProperty -name StandardError -Value $StandardError
    
    return $output
}

function Get-PythonVersion() {
    $output = Get-ProcessOutput -FileName "cmd.exe" -Arguments "/c python --version"
    $version_string = $output.StandardOutput
    return [version]$version_string.split()[1]
}


function Find-Command($cmdname) {
    return [bool](Get-Command -Name $cmdname -ErrorAction SilentlyContinue)
}

function Get-Configuration() {
    $RedditClientID = Read-Host -Prompt 'What is your Reddit client ID?'
    $RedditClientSecret = Read-Host -Prompt 'What is your Reddit client secret?'
    $RedditUserAgent = Read-Host -Prompt 'What is your Reddit user agent?'
    $RedditUserName = Read-Host -Prompt 'What is your Reddit username?'
    $RedditPassword = Read-Host -Prompt 'What is your Reddit password?'
    $DiscordToken = Read-Host -Prompt 'What is your Discord token?'
    $GoogleAPIKey = Read-Host -Prompt 'What is your Google API Key?'
    $GoogleCX = Read-Host -Prompt 'What is your Google CX?'
    $MongoURL = Read-Host -Prompt 'What is your Mongo URL?'

    $conf_obj = [PSCustomObject]@{
        redditClientID = $RedditClientID
        redditClientSecret = $RedditClientSecret
        redditUserAgent = $RedditUserAgent
        redditUsername = $RedditUserName
        redditPassword = $RedditPassword
        discordToken = $DiscordToken
        googleAPIKey = $GoogleAPIKey
        googleCx = $GoogleCX
        mongoUrl = $MongoURL
    }

    return $conf_obj
}


if (-Not (Find-Command -cmdname 'python')) {
    Write-Output "Python is not installed, please install it."
}

$minPythonVersion = [version]"3.9" 
$installedPythonVersion = Get-PythonVersion


if (-not ($installedPythonVersion -gt $minPythonVersion)) {
    Write-Output "Sorry your Python version is too old, make sure to have, at least Python '$minPythonVersion'"
}

if (-Not (Find-Command -cmdname 'pipenv')) {
    Write-Output "Sorry, pipenv is not installed, make sure to install pipenv"
}

Write-Output "Running pipenv install..."
$pipenvPath = Get-Command "pipenv"
Start-Process -NoNewWindow -Wait -FilePath $pipenvPath.Source -ArgumentList "install"

$file = "settings.json"

# Leaf == File, for some weird Microsoft reason
if (-Not (Test-Path -Path $file -PathType Leaf)) {
    try {
        $null = New-Item -ItemType File -Path $file -Force -ErrorAction Stop
        Write-Host "Sucessfully created file $file."
        $conf_object = Get-Configuration
        $conf_object| ConvertTo-Json | Set-Content -Path "settings.json"
    } catch {
        throw $_.Exception.Message
    }
}
else {
    Write-Host "settings.json is already created."
}