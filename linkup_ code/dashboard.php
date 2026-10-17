<?php include 'db.php'; session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

$user_id = $_SESSION['user_id'];
$user = $conn->query("SELECT * FROM users WHERE id = $user_id")->fetch_assoc();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - LinkMe</title>
</head>
<body>
    <h2>Welcome, <?php echo $user['name']; ?>!</h2>
    <p>Email: <?php echo $user['email']; ?></p>
    <p>Location: <?php echo $user['location']; ?></p>
    <a href="logout.php">Logout</a>
</body>
</html>


<?php include 'db.php'; session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

$user_id = $_SESSION['user_id'];
$user = $conn->query("SELECT * FROM users WHERE id = $user_id")->fetch_assoc();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - LinkUp</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="profile">
            <h2>Welcome, <?php echo $user['name']; ?></h2>
            <img src="profile_pictures/<?php echo $user['id']; ?>.jpg" alt="Profile Picture" class="profile-img">
            <p>Email: <?php echo $user['email']; ?></p>
            <p>Location: <?php echo $user['location']; ?></p>
            <a href="logout.php" class="logout-btn">Logout</a>
        </div>
    </div>
</body>
</html>




<?php 
include 'db.php'; 
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

$user_id = $_SESSION['user_id'];
$result = $conn->query("SELECT * FROM posts ORDER BY created_at DESC");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Your Feed</h2>

        <?php while($post = $result->fetch_assoc()): ?>
            <div class="post">
                <p><?php echo $post['content']; ?></p>
                <small>Posted on <?php echo $post['created_at']; ?></small>
            </div>
        <?php endwhile; ?>
    </div>
</body>
</html>


<?php
include 'db.php'; 
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

$result = $conn->query("SELECT posts.*, COUNT(likes.id) AS like_count FROM posts LEFT JOIN likes ON posts.id = likes.post_id GROUP BY posts.id ORDER BY posts.created_at DESC");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Your Feed</h2>

        <?php while($post = $result->fetch_assoc()): ?>
            <div class="post">
                <p><?php echo $post['content']; ?></p>
                <small>Posted on <?php echo $post['created_at']; ?></small>

                <a href="like_post.php?post_id=<?php echo $post['id']; ?>" class="like-btn">
                    <?php echo $post['like_count']; ?> Likes
                </a>
            </div>
        <?php endwhile; ?>
    </div>
</body>
</html>


<?php
$result = $conn->query("SELECT posts.*, COUNT(likes.id) AS like_count, 
    GROUP_CONCAT(comments.comment ORDER BY comments.created_at DESC) AS comments 
    FROM posts 
    LEFT JOIN likes ON posts.id = likes.post_id 
    LEFT JOIN comments ON posts.id = comments.post_id
    GROUP BY posts.id ORDER BY posts.created_at DESC");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Your Feed</h2>

        <?php while($post = $result->fetch_assoc()): ?>
            <div class="post">
                <p><?php echo $post['content']; ?></p>
                <small>Posted on <?php echo $post['created_at']; ?></small>

                <a href="like_post.php?post_id=<?php echo $post['id']; ?>" class="like-btn">
                    <?php echo $post['like_count']; ?> Likes
                </a>

                <form action="comment_post.php" method="POST">
                    <input type="hidden" name="post_id" value="<?php echo $post['id']; ?>">
                    <textarea name="comment_content" placeholder="Add a comment..." required></textarea>
                    <button type="submit" name="comment">Comment</button>
                </form>

                <div class="comments">
                    <?php echo $post['comments']; ?>
                </div>
            </div>
        <?php endwhile; ?>
    </div>
</body>
</html>
