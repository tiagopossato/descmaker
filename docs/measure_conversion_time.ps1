function Measure-ExecutionTime {
    param (
        [string]$input_file,
        [string]$language,
        [string]$output_file
    )

    if (-not $input_file -or -not $language -or -not $output_file) {
        Write-Host "Usage: Measure-ExecutionTime -input_file <path_to_input_file> -language <language> -output_file <path_to_output_file>"
        return
    }

    # Variable to store the total time in milliseconds
    $total_time_ms = 0

    # Loop to execute the command 10 times
    for ($i = 1; $i -le 20; $i++) {
        # Check if the directory exists and remove it if it does
        if (Test-Path -Path "generated_code") {
            Remove-Item -Recurse -Force "generated_code"
        }
        # Measure the execution time using the Measure-Time function
        $start_time = [datetime]::Now
        python.exe ../descmaker.py -l $language -i $input_file > $null 2>&1
        $end_time = [datetime]::Now
        $exec_time = ($end_time - $start_time).TotalMilliseconds
        $total_time_ms += [math]::Round($exec_time)
    }

    # Calculate the average time in milliseconds
    $average_time_ms = [math]::Round($total_time_ms / 20)

    # Display the average execution time in milliseconds
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $result = "Average execution time for {0} with language {1}; {2} milliseconds" -f $input_file, $language, $average_time_ms
    Write-Host $result

    # Save the result to the output file with date and time
    $current_datetime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $result_with_datetime = "$current_datetime; $result"
    Add-Content -Path $output_file -Value $result_with_datetime
}


# Call the function with different parameters
Measure-ExecutionTime -input_file "..\examples\other_examples\1_PequenaFabrica.wmod" -language "python" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\2_Labirinto.wmod" -language "python" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\3_syncTransferLine.wmod" -language "python" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\4_MesaMontagem.wmod" -language "python" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\5_poultryprocess.wmod" -language "python" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\6_automotiveline.wmod" -language "python" -output_file "results.txt"


# Measure-ExecutionTime -input_file "..\examples\other_examples\1_PequenaFabrica.wmod" -language "c" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\2_Labirinto.wmod" -language "c" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\3_syncTransferLine.wmod" -language "c" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\4_MesaMontagem.wmod" -language "c" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\5_poultryprocess.wmod" -language "c" -output_file "results.txt"
# Measure-ExecutionTime -input_file "..\examples\other_examples\6_automotiveline.wmod" -language "c" -output_file "results.txt"
