<?php include 'db.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Register - LinkMe</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST" action="">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        Location: <input type="text" name="location"><br><br>
        <button type="submit" name="register">Register</button>
    </form>

<?php
if (isset($_POST['register'])) {
    $name     = $_POST['name'];
    $email    = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    $location = $_POST['location'];

    // check if email exists
    $check = $conn->query("SELECT * FROM users WHERE email = '$email'");
    if ($check->num_rows > 0) {
        echo "Email already exists!";
    } else {
        $sql = "INSERT INTO users (name, email, password, location) 
                VALUES ('$name', '$email', '$password', '$location')";

        if ($conn->query($sql) === TRUE) {
            echo "Registration successful! <a href='login.php'>Login here</a>";
        } else {
            echo "Error: " . $conn->error;
        }
    }
}
?>
</body>
</html>



<?php include 'db.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - LinkUp</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="form-container">
        <h2>User Registration</h2>
        <form method="POST" action="">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            
            <label for="location">Location:</label>
            <input type="text" id="location" name="location"><br><br>
            
            <button type="submit" name="register" class="btn">Register</button>
        </form>
    </div>
</body>
</html>
