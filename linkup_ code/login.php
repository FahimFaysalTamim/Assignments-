<?php include 'db.php'; session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <title>Login - LinkMe</title>
</head>
<body>
    <h2>User Login</h2>
    <form method="POST" action="">
        Email: <input type="email" name="email" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <button type="submit" name="login">Login</button>
    </form>

<?php
if (isset($_POST['login'])) {
    $email    = $_POST['email'];
    $password = $_POST['password'];

    $query = "SELECT * FROM users WHERE email = '$email'";
    $result = $conn->query($query);

    if ($result->num_rows == 1) {
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            echo "Login successful! <a href='dashboard.php'>Go to Dashboard</a>";
        } else {
            echo "Invalid password!";
        }
    } else {
        echo "No user found!";
    }
}
?>
</body>
</html>
