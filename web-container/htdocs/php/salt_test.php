<?php 
# Purpose: Demonstrate the output of the password_hash function

$password = "mypassword";
$hash = password_hash($password, PASSWORD_DEFAULT);
echo $hash;

?>