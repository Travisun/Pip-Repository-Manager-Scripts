<?php
// 定义文件路径
$windows_script = "switch_pip.windows.tcmd";
$linux_mac_script = "switch_pip.unix.tcmd";

// 获取User-Agent字符串
$user_agent = $_SERVER['HTTP_USER_AGENT'];

// 检查User-Agent以区分操作系统
if (strpos($user_agent, 'Windows') !== false) {
    // 如果是Windows操作系统，读取Windows脚本文件内容
    $file_path = $windows_script;
    $content_type = 'application/octet-stream'; // 设置适当的Content-Type
    $file_name = 'windows_switch_pip.cmd';
} else {
    // 如果是Mac或Linux操作系统，读取Unix脚本文件内容
    $file_path = $linux_mac_script;
    $content_type = 'application/octet-stream'; // 设置适当的Content-Type
    $file_name = 'unix_switch_pip.sh';
}

// 检查文件是否存在
if (file_exists($file_path)) {
    // 读取文件内容
    $file_content = file_get_contents($file_path);

    // 设置适当的Content-Type和Content-Disposition头
    header('Content-Type: ' . $content_type);
    header('Content-Disposition: attachment; filename="' . $file_name . '"');

    // 返回文件内容
    echo $file_content;
} else {
    // 如果文件不存在，返回404错误
    header("HTTP/1.0 404 Not Found");
    echo "文件未找到。";
}
exit;
?>