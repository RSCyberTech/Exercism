Function Invoke-RnaTranscription() {
    <#
    .SYNOPSIS
    Transcribe a DNA strand into RNA.

    .DESCRIPTION
    Given a DNA strand, return its RNA complement (per RNA transcription).

    .PARAMETER Strand
    The DNA strand to transcribe.

    .EXAMPLE
    Invoke-RnaTranscription -Strand "A"
    #>
    [CmdletBinding()]
    Param(
        [string]$Strand
    )
    
    [char []]$strand = $Strand.ToCharArray()

    $dict = @{
        G = 'C';
        C = 'G';
        T = 'A';
        A = 'U'
    }

    $toReturn = ''

    foreach ($s in $Strand) {
        $toReturn += $dict[$s.ToString()]
    }

    return $toReturn
}
