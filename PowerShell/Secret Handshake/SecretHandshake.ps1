Function Invoke-SecretHandshake() {
    <#
    .SYNOPSIS
    Convert a number between 1 and 31 to a sequence of actions in the secret handshake.

    .DESCRIPTION
    The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary.
    Start at the right-most digit and move left.

    The actions for each number place are:
    00001 = wink
    00010 = double blink
    00100 = close your eyes
    01000 = jump
    10000 = Reverse the order of the operations in the secret handshake.
    
    .PARAMETER Number
    The value to be converted into a sequence of actions.

    .EXAMPLE
    Invoke-SecretHandshake -Number 2
    Returns: @("double blink")
    #>
    [CmdletBinding()]
    Param(
        [int]$Number
    )

    $binary = [System.Convert]::ToString($number, 2)

    $toReturn = @()
    
    if ($binary.substring($binary.length - 1, 1) -eq '1') {
        $toReturn += 'wink'
    }
    if ($binary.length -gt 1 -and $binary.substring($binary.length - 2, 1) -eq '1') {
        $toReturn += 'double blink'
    }
    if ($binary.length -gt 2 -and $binary.substring($binary.length - 3, 1) -eq '1') {
        $toReturn += 'close your eyes'
    }
    if ($binary.length -gt 3 -and $binary.substring($binary.length - 4, 1) -eq '1') {
        $toReturn += 'jump'
    }
    if ($binary.length -gt 4 -and $binary.substring($binary.length - 5, 1) -eq '1') {
        $toReturn = [System.Collections.ArrayList]::new($toReturn)
        $toReturn.reverse()
    }
    
    return $toReturn
}