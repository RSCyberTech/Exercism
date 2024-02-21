Function Invoke-Panagram() {
    <#
    .SYNOPSIS
    Determine if a sentence is a pangram.
    
    .DESCRIPTION
    A pangram is a sentence using every letter of the alphabet at least once.
    
    .PARAMETER Sentence
    The sentence to check
    
    .EXAMPLE
    Invoke-Panagram -Sentence "The quick brown fox jumps over the lazy dog"
    
    Returns: $true
    #>
    [CmdletBinding()]
    Param(
        [string]$Sentence
    )

    [char[]]$Sentence = $Sentence.ToCharArray()
    [char[]]$letters = "abcdefghijklmnopqrstuvwxyz".ToCharArray()

    foreach ($l in $letters) {
        if ($l -inotin $Sentence) {
            if ($l -ine " ") {
                return $false
            }
        }
    }

    return $true
}