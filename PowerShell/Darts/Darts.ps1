Function Invoke-Darts() {
    <#
    .SYNOPSIS
    Calculate the earned points in a single toss of a Darts game.

    .DESCRIPTION
    Take a coordinate of a point and calculate the distance from the center of the dartboard.
    Then depending on the distance and which concentric circle the point lies in, return the
    number of points earned.

    .PARAMETER X
    The X coordinate of the dart.

    .PARAMETER Y
    The Y coordinate of the dart.

    .EXAMPLE
    Invoke-Darts -X 0 -Y 10
    #>
    [CmdletBinding()]
    Param(
        [Double]$X,
        [Double]$Y
    )
    
    $x = [System.Math]::Abs($x)
    $y = [System.Math]::Abs($y)
    
    $z = [Math]::Sqrt( [Math]::Pow($x, 2) + [Math]::Pow($y, 2) )

    if ($z -le 1) {
        return 10
    }
    elseif ($z -le 5) {
        return 5
    }
    elseif ($z -le 10) {
        return 1
    }
    else {
        return 0
    }
}