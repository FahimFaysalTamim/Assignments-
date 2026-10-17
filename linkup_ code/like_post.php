<?php 
include 'db.php'; 
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

if (isset($_GET['post_id'])) {
    $post_id = $_GET['post_id'];
    $user_id = $_SESSION['user_id'];

    // Check if user already liked the post
    $check_like = $conn->query("SELECT * FROM likes WHERE post_id = $post_id AND user_id = $user_id");
    if ($check_like->num_rows == 0) {
        $conn->query("INSERT INTO likes (post_id, user_id) VALUES ($post_id, $user_id)");
    } else {
        $conn->query("DELETE FROM likes WHERE post_id = $post_id AND user_id = $user_id");
    }
}

header("Location: dashboard.php");
