<?php
if (isset($_GET['a']) && isset($_GET['b']) && isset($_GET['c']) && isset($_GET['d']) && isset($_GET['e'])) {
    $a = escapeshellarg($_GET['a']);
    $b = escapeshellarg($_GET['b']);
    $c = escapeshellarg($_GET['c']);
    $d = escapeshellarg($_GET['d']);
    $e = escapeshellarg($_GET['e']);

    $command = escapeshellcmd("python3 data_management.py $a $b $c $d $e");
    $output = shell_exec($command);

    echo "<h1>RESULT - Assignment 4:</h1>";
	echo "<br>$output";
} else {
    echo "<h2>Please provide values for a, b, c, d and e.</h2>";
}
?>