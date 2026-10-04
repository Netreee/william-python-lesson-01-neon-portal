param(
    [ValidateSet('1', '2', '3', '4', '5', '6')]
    [string]$Stage = '5'
)

$ErrorActionPreference = 'Stop'
$lessonEnvironment = Join-Path $PSScriptRoot '.venv'
$lessonInterpreter = Join-Path $lessonEnvironment 'Scripts\python.exe'

if (-not (Test-Path -LiteralPath $lessonInterpreter)) {
    $lessonLauncher = Get-Command py.exe -ErrorAction SilentlyContinue
    if ($null -eq $lessonLauncher) {
        throw 'Install Python 3 with the Windows Python launcher, then run this script again.'
    }
    & $lessonLauncher.Source -3 -m venv --without-pip $lessonEnvironment
    if ($LASTEXITCODE -ne 0) {
        throw 'Could not create the lesson virtual environment.'
    }
}

$lessonFiles = @{
    '1' = '01_sequence.py'
    '2' = '02_variables.py'
    '3' = '03_for_loop.py'
    '4' = '04_if_colors.py'
    '5' = '05_neon_portal.py'
    '6' = '06_my_portal.py'
}

$lessonFile = Join-Path $PSScriptRoot $lessonFiles[$Stage]
& $lessonInterpreter $lessonFile
exit $LASTEXITCODE
