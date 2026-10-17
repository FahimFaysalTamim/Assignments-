<?php 
include 'db.php'; 
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

if (isset($_POST['comment'])) {
    $user_id = $_SESSION['user_id'];
    $post_id = $_POST['post_id'];
    $comment = $_POST['comment_content'];

    $stmt = $conn->prepare("INSERT INTO comments (post_id, user_id, comment) VALUES (?, ?, ?)");
    $stmt->bind_param("iis", $post_id, $user_id, $comment);
    $stmt->execute();
}

header("Location: dashboard.php");
