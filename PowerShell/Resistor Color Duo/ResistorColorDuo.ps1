Function Get-ColorCodeValue() {
    <#
    .SYNOPSIS
    Translate a list of colors to their corresponding color code values.

    .DESCRIPTION
    Given 2 colors, take the first one and times it by 10 and add the second color to it.

    .PARAMETER Colors
    The colors to translate to their corresponding color codes.

    .EXAMPLE
    Get-ColorCodeValue -Colors @("black", "brown")
    #>
    [CmdletBinding()]
    Param(
        [string[]]$Colors
    )

    $colorDict = @{
        'Black'  = 0
        'Brown'  = 1
        'Red'    = 2
        'Orange' = 3
        'Yellow' = 4
        'Green'  = 5
        'Blue'   = 6
        'Violet' = 7
        'Grey'   = 8
        'White'  = 9
    }

    $toReturn = ''

    foreach ($c in $Colors[0..1]) {
        if ($c -in $colorDict.Keys) {
            $toReturn += [string]$colorDict[$c]
        }
    }

    return $toReturn
}