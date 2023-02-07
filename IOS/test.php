<?php
header('Content-Type: text/html; charset=UTF-8');

$sentence = "最近の天気はどうですか。";
$search_text = "近";

exec("python3 result.py  {$sentence} {$search_text}", $arr);
$result = implode("\n", $arr)."\n";
echo $result."<br>";
?>