Function Get-ResistorLabel() {
    <#
    .SYNOPSIS
    Implement a function to get the label of a resistor from its color-coded bands.

    .DESCRIPTION
    Given an array of 1, 4 or 5 colors from a resistor, decode their resistance values and return a string represent the resistor's label.

    .PARAMETER Colors
    The array represent the colors from left to right.

    .EXAMPLE
    Get-ResistorLabel -Colors @("red", "black", "green", "red")
    Return: "2 megaohms ±2%"

    Get-ResistorLabel -Colors @("blue", "blue", "blue", "blue", "blue")
    Return: "666 megaohms ±0.25%"
    #>
    
    [CmdletBinding()]
    Param(
        [string[]]$Colors
    )

    $colorDict = @{
        "black"  = 0
        "brown"  = 1
        "red"    = 2
        "orange" = 3
        "yellow" = 4
        "green"  = 5
        "blue"   = 6
        "violet" = 7
        "grey"   = 8
        "white"  = 9
    }

    $colorPercentage = @{
        "grey"   = 0.05
        "violet" = 0.1
        "blue"   = 0.25
        "green"  = 0.5
        "brown"  = 1
        "red"    = 2
        "gold"   = 5
        "silver" = 10
    }

    $size = $Colors.count
    $value = ""
    $measure = "ohms"
    $multiplier = ""
    $variation = ""
    if ($size -eq 1) {
        return "$($colordict[$colors[0]]) ohms"
    }
    else {
        
        for ($i = 0; $i -lt ($colors.count - 2); $i++) {
            $value = $value + [string]$colordict[$colors[$i]]
        }
        Write-Host Value=$value
        
        $multiplier = [int]$colordict[$colors[-2]]
        for ($i = 0; $i -lt $multiplier; $i++) {
            $value += '0'
        }

        if ([int]$value -gt 1000) {
            if ([int]$value -gt 1000000) {
                $value = [string]([int]$value / 1000000)
                $measure = "megaohms"
            }
            else {
                $value = [string]([int]$value / 1000)
                $measure = "kiloohms"
            }
        }

        $variation = $colorPercentage[$colors[-1]]
    }

    return "$value $measure ±$variation%"
}