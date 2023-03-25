# define paramteres
param(
    [Parameter(Mandatory=$true, HelpMessage="Input file")]
    [string]$i,
    [Parameter(Mandatory=$false, HelpMessage="Output directory")]
    [string]$o = "generated_code",
    [Parameter(Mandatory=$false, HelpMessage="Execute the generated code")]
    [string]$e = "y"
)

#This will set the $BASEDIR variable to the directory where the script is located.
$BASEDIR = Split-Path -Parent $MyInvocation.MyCommand.Path

# function to print help
function print_help {
    Write-Host "Usage: despythonmaker.ps1 -i <input> -o <output>"
    Write-Host " -i <input>: input file (required)"
    Write-Host " -o <output>: output directory. Default: generated_code"
}


#print received parameters
# Write-Host "Input file: $i"
# Write-Host "Output directory: $o"
# Write-Host "Execute: $e"
# Write-Host "Script location: $BASEDIR"

# verify if output directory exists
if (Test-Path $o -PathType Container) {
    # Read single character from user input
    Write-Host ""
    Write-Host ""
    Write-Host "Output directory exists. Do you want to overwrite it? [y/n]"
    $keyInfo = [Console]::ReadKey($true)
    # verify if response is diferent from y
    if ($keyInfo.Key -ne "y") {
        exit 1
    }
    Remove-Item $o -Recurse -Force
}


# copy base code to output directory
# "Supervisor/supervisors/sup.py" is excluded because it is a example of a supervisor. Other example files are subscribed by the maker.py script
Copy-Item -Path "$BASEDIR\base_code" -Destination "$o" -Recurse -Exclude build,sup.c,sup.h

# activate virtual environment on BASEDIR parent directory env
$env:VIRTUAL_ENV = "$BASEDIR\..\env"
$env:PATH = "$env:VIRTUAL_ENV\Scripts;$env:PATH"

# get the path where the prompt is being executed
$SCRIPTPWD = Get-Location

# join the full path on the output directory
$o = Join-Path -Path $SCRIPTPWD -ChildPath $o

Write-Host ""
Write-Host ""
Write-Host ""
# message to user
Write-Host "-------------------GENERATING----------------------"
Write-Host ""
# run maker.py script
python "$BASEDIR\maker.py" --input "$i" --output "$o"

# execute if user wants and if the generation was successful
if ($LASTEXITCODE -eq 0) {
    # sucessful generation message
    # break line
    Write-Host ""
    Write-Host ""
    Write-Host ""
    Write-Host "-------------------CONGRATULATIONS----------------------"
    Write-Host ""
    Write-Host "Generation successful!"
    Write-Host ""
    Write-Host ""
    Write-Host ""

    if ($e -eq "y") {
        Write-Host "-------------------EXECUTING----------------------"
        Write-Host ""
        Write-Host ""
        Write-Host ""
        # change to output directory
        Set-Location $o
        # run the generated code
        python main.py
        # change to previous directory
        Set-Location $SCRIPTPWD
    }

    Write-Host ""
    Write-Host ""
    Write-Host "-------------------INSTRUCTIONS----------------------"
    Write-Host ""
    Write-Host ""
    Write-Host "You can find the generated code on $o"
    Write-Host "The file main.py is the entry point of the generated code and the only file you need to run and change."
    Write-Host ""
    Write-Host ""
}
else {
    Write-Host ""
    Write-Host ""
    Write-Host ""
    Write-Host "-------------------ERROR----------------------"
    Write-Host ""
    Write-Host "Generation failed!"
    Write-Host ""
    Write-Host ""
}
