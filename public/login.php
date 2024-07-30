<?php
session_start();
require '../init.php';

use App\Database;
use App\User;

$database = new Database();
$user = new User($database);

$error = ''; // Inicializace proměnné pro chybu

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Načtení dat z POST požadavku
        $userName = $_POST['user_name'];
        $password = $_POST['password'];

        // Pokus o přihlášení uživatele
        if ($user->login($userName, $password)) {
            header("Location: dashboard.php");
            exit(); // zde už nepotřebuji, aby se další kod vykonal
        } else {
            $error = "Přihlášení se nezdařilo!";
        }
    }
} catch (Exception $e) {
    // getMessage() je metoda z třídy Exception
    $error = "Error: " . $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="../static/css/login.css">
</head>
<body>
    <div class="login-container">
        <h1>Login Page</h1>
        <form action="login.php" method="POST">
            <table>
                <tr>
                    <td>User name:</td>
                    <td><input type="text" name="user_name"></td>
                </tr>
                <tr>
                    <td>Password:</td>
                    <td><input type="password" name="password"></td>
                </tr>
                <tr>
                    <td><input type="submit" value="Login user"></td>
                    <td><input type="reset" value="Reset form"></td>
                </tr>
            </table>
        </form>
        <a href="register.php">Register</a>
        <?php if ($error): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
    </div>
</body>
</html>
