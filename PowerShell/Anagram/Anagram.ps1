Function Invoke-Anagram() {
    <#
    .SYNOPSIS
    Determine if a word is an anagram of other words in a list.

    .DESCRIPTION
    An anagram is a word formed by rearranging the letters of another word, e.g., spar, formed from rasp.
    Given a word and a list of possible anagrams, find the anagrams in the list.

    .PARAMETER Subject
    The word to check

    .PARAMETER Candidates
    The list of possible anagrams

    .EXAMPLE
    Invoke-Anagram -Subject "listen" -Candidates @("enlists" "google" "inlets" "banana")
    #>
    [CmdletBinding()]
    Param(
        [string]$Subject,
        [string[]]$Candidates
    )

    $toReturn = @()
    foreach ($c in $Candidates) {

        if ($c.Length -eq $Subject.Length -and $Subject -ne $c) {
            $charC = [char []]$c
            $charS = [char []]$Subject
            for ($i = 0; $i -lt $charC.length; $i++) {
                $charC[$i] = [char](([string]($charC[$i])).ToLower())
            }
            for ($i = 0; $i -lt $charS.length; $i++) {
                $charS[$i] = [char](([string]($charS[$i])).ToLower())
            }
            $charC = $charC | Sort-Object
            $charS = $charS | Sort-Object
            $charC = -join $charC
            $charS = -join $charS
            if ($charC -ieq $charS) {
                $toReturn += $c
            }
        }

    }
    
    return $toReturn
}
Invoke-Anagram -Subject "listen" -Candidates @("enlists", "google", "inlets", "banana")