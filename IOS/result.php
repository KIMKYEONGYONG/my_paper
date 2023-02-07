<?php
header('Content-Type: text/html; charset=UTF-8');


$password = "72ak378D";
$secret = $_REQUEST["secretWord"];
if (strcmp($password, $secret) != 0 ) exit;

$sentence = $_REQUEST["sentence"];
$search_text = $_REQUEST["keyword"];

exec("python3 result.py  {$sentence} {$search_text}", $output);

// Finally, encode the array to JSON and output the results
//echo json_encode($resultArray);
/*
echo $output[0]."<br>";
echo $output[1]."<br>";
echo $output[2]."<br>";
echo $output[3]."<br>";
echo $output[4]."<br>";
echo $output[5]."<br>";
echo $output[6]."<br>";
echo $output[7]."<br>";
*/

$resultArray = array();
for($i = 0; $i < 8; $i=$i+2){
	array_push($resultArray, [
			"result" =>  $output[$i],
			"percent" => $output[$i+1],
		]);

	// 01, 23, 45, 67
}

echo json_encode($resultArray);

?>