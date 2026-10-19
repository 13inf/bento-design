#requires -Version 7.0
[CmdletBinding()]
param(
    [string]$SkillsDirectory
)

$ErrorActionPreference = 'Stop'
$sourceRoot = Split-Path -Parent $PSScriptRoot
$itemsToInstall = @('SKILL.md', 'agents', 'assets', 'references', 'LICENSE', 'NOTICE.md')

foreach ($itemName in $itemsToInstall) {
    $sourceItem = Join-Path $sourceRoot $itemName
    if (-not (Test-Path -LiteralPath $sourceItem)) {
        throw "Incomplete source package: $itemName"
    }
}

if ([string]::IsNullOrWhiteSpace($SkillsDirectory)) {
    if (-not [string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
        $SkillsDirectory = Join-Path $env:CODEX_HOME 'skills'
    }
    else {
        $profileRoot = [Environment]::GetFolderPath('UserProfile')
        $SkillsDirectory = Join-Path $profileRoot '.codex/skills'
    }
}

$skillsRoot = [IO.Path]::GetFullPath($SkillsDirectory)
$targetDirectory = Join-Path $skillsRoot 'bento-design'
if (Test-Path -LiteralPath $targetDirectory) {
    throw "Already exists: $targetDirectory. Back it up outside the skills directory before installing."
}

New-Item -ItemType Directory -Path $targetDirectory | Out-Null
foreach ($itemName in $itemsToInstall) {
    Copy-Item -LiteralPath (Join-Path $sourceRoot $itemName) -Destination $targetDirectory -Recurse
}

Write-Output "Installed: $targetDirectory"
Write-Output 'Invoke as $bento-design in a new conversation.'
