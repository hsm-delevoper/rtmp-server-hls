<?php
$streamUrl = $_POST['stream_url'];
$ffmpegCmd = "ffmpeg -i $streamUrl -c:v libx264 -c:a aac -f hls -hls_list_size