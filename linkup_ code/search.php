<?php
include 'db.php';
session_start();

if (isset($_GET['search'])) {
    $search_query = $_GET['search'];
    $result = $conn->query("SELECT * FROM users WHERE name LIKE '%$search_query%'");
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Users</title>
</head>
<body>
    <div class="container">
        <form method="GET" action="search.php">
            <input type="text" name="search" placeholder="Search for users..." required>
            <button type="submit">Search</button>
        </form>

        <?php if (isset($result)): ?>
            <h3>Search Results:</h3>
            <ul>
                <?php while($user = $result->fetch_assoc()): ?>
                    <li><?php echo $user['name']; ?> - <?php echo $user['email']; ?></li>
                <?php endwhile; ?>
            </ul>
        <?php endif; ?>
    </div>
</body>
</html>
