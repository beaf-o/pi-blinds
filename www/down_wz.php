<?php
var_dump($_GET);die();
shell_exec('/home/pi/blinds/down_wz.sh');
header("Location:index.html");
?>
