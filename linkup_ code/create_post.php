<?php 
include 'db.php'; 
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

if (isset($_POST['post'])) {
    $user_id = $_SESSION['user_id'];
    $post_content = $_POST['content'];

    $stmt = $conn->prepare("INSERT INTO posts (user_id, content) VALUES (?, ?)");
    $stmt->bind_param("is", $user_id, $post_content);
    $stmt->execute();
    header("Location: dashboard.php"); // Redirect to dashboard
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Post</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <form method="POST" action="create_post.php">
            <textarea name="content" placeholder="What's on your mind?" required></textarea>
            <button type="submit" name="post" class="btn">Post</button>
        </form>
    </div>
</body>
</html>
