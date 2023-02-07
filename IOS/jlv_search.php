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
$topic_id = $_REQUEST["topicId"];
$search_text = $_REQUEST["keyword"];

if ( strcmp($search_text, "") == 0) {
   $sql =  "SELECT * FROM Voca Order by RAND() Limit 1;";
   $result = mysqli_query($con, $sql);
   $row = $result->fetch_object();
   $search_text =  $row->search_text;
}


$sql = "SELECT sentence FROM ExaSe where sentence like binary '%".$search_text."%'";
if ( strcmp($level_id,"L999") == 0 and strcmp($topic_id,"T999") == 0) {
	$sql .= " ;";
} elseif (strcmp($level_id,"L999") == 0) {
	$sql .= " and topic_id = '".$topic_id."';";
} elseif (strcmp($topic_id,"T999") == 0) {
	$sql .= " and level_id = '".$level_id."';";
} else{
	$sql .= " and level_id = '".$level_id."' and topic_id = '".$topic_id."';";
}
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