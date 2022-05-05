<?php
	$url =
	'file';
	$file_name = basename($url);
	if (file_put_contents($file_name, file_get_contents($url)))
	{
		echo "File downloaded successfully";
	}
	else
	{
		echo "File downloading failed.";
	}
?>
