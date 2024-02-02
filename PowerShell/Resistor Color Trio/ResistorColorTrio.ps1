Function Get-ResistorLabel() {
    <#
    .SYNOPSIS
    Implement a function to get the label of a resistor with three color-coded bands.

    .DESCRIPTION
    Given an array of colors from a resistor, decode their resistance values and return a string represent the resistor's label.

    .PARAMETER Colors
    The array repesent the 3 colors from left to right.

    .EXAMPLE
    Get-ResistorLabel -Colors @("red", "white", "blue")
    Return: "29 megaohms"
    #>
    
    [CmdletBinding()]
    Param(
        [string[]]$Colors
    )

    $colorValues = @{
        "black"=0;
        "brown"=1;
        "red"=2;
        "orange"=3;
        "yellow"=4;
        "green"=5;
        "blue"=6;
        "violet"=7;
        "grey"=8;
        "white"=9
    }

    if($Colors.Length -gt 3){
        $colors=$colors[0..2]
    }

    if(([int]$colorValues[$colors[0]]+[int]$colorValues[$colors[1]]) -eq 0){
        return '0 ohms'
    }

    if($Colors[0] -eq 'black'){
        $Colors=@($Colors[1])
    }

    $toReturn=''
    $zeros=0
    foreach($c in $colors){
        if ($toReturn.Length -lt 2){
            $toReturn+=$colorValues[$c]
        }
        else{
            $zeros+=$colorValues[$c]
        }
    }

    if($toReturn[1] -eq '0'){
        $zeros+=1
        $toReturn=$toReturn.substring(0,1)
    }
    
    $word='ohms'

    if($zeros -ge 3){
        $word='kiloohms'
        $zeros-=3
    }

    if($zeros -ge 3){
        $word='megaohms'
        $zeros-=3
    }

    if($zeros -ge 3){
        $word='gigaohms'
        $zeros-=3
    }

    for($i=0;$i -lt $zeros;$i++){
        $toReturn+=0
    }

    $toReturn+=' '+$word

    return $toReturn
}