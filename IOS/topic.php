<?php
 
// Create connection
$con=mysqli_connect("localhost","jlv","1@23q~","jlvdb");
 
// Check connection
if (mysqli_connect_errno())
{
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
 
// This SQL statement selects ALL from the table 'Locations'
$secret = $_REQUEST["secretWord"];
$password = "72ak378D";
if (strcmp($password, $secret) != 0 ) exit;
$level_id = $_REQUEST["levelId"];

$sql =  "SELECT t.topic_id, t.topic_name FROM Topic as t Inner Join LevelTopic as lt On t.topic_id = lt.topic_id Where lt.level_id = '".$level_id."';";

// mysqli_query($con, "set name utf8;");
mysqli_query($con, "set session character_set_connection=utf8;");
mysqli_query($con, "set session character_set_results=utf8;");
mysqli_query($con, "set session character_set_client=utf8;");

// Check if there are results
if ($result = mysqli_query($con, $sql))
{
	// If so, then create a results array and a temporary one
	// to hold the data
	$resultArray = array();
	$tempArray = array();
 
	// Loop through each row in the result set
	while($row = $result->fetch_object())
	{
		// Add each row into our results array
		$tempArray = $row;
	    array_push($resultArray, $tempArray);
	}
 
	// Finally, encode the array to JSON and output the results
	echo json_encode($resultArray);
}
 
// Close connections
mysqli_close($con);
?>