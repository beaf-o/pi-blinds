<?php
if (isset($_GET['r']) && isset($_GET['d'])) {
	$room = $_GET['r'];
	$direction = $_GET['d'];

	if ($python) {
		$cmd = 'python /home/pi/blinds/blinds.py ' . $room . ' ' . $direction;
		exec($cmd);
	} else {
		$cmd = '/home/pi/blinds/blinds.sh ' . $room . ' ' . $direction;
		shell_exec($cmd);
	}
}

header("Location:index.html");
?>
