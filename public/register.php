<?php
session_start();
require '../init.php';

use App\Database;
use App\User;

$database = new Database();
$user = new User($database);

$error = ''; // Inicializace proměnné pro chybu
$success = ''; // Inicializace proměnné pro úspěch

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Načtení dat z POST požadavku
        $fullName = $_POST['full_name'];
        $userName = $_POST['user_name'];
        $password = $_POST['password'];

        // Kontrola, zda uživatel již existuje
        if ($user->userExists($userName)) {
            $error = "Uživatel s tímto jménem již existuje.";
        } else {
            // Pokus o registraci uživatele
            if ($user->register($fullName, $userName, $password)) {
                $success = "Uživatel byl úspěšně zaregistrován!"; // Nastavení úspěšné hlášky
            } else {
                $error = "Registrace se nezdařila.";
            }
        }
    }
} catch (Exception $e) {
    // getMessage() je metoda z třídy Exception
    $error = $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        table {
            width: 100%;
        }

        td {
            padding: 10px 0;
        }

        input[type="text"],
        input[type="password"] {
            width: calc(100% - 22px);
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="submit"],
        input[type="reset"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        input[type="reset"] {
            background-color: #6c757d;
        }

        input[type="submit"]:hover,
        input[type="reset"]:hover {
            background-color: #0056b3;
        }

        input[type="reset"]:hover {
            background-color: #5a6268;
        }

        a {
            display: block;
            text-align: center;
            margin-top: 10px;
            color: #007BFF;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .error, .success {
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border-radius: 4px;
            margin-top: 20px;
            text-align: center;
        }

        .success {
            background-color: #d4edda;
            color: #155724;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Register Page</h1>
        <form action="register.php" method="POST">
            <table>
                <tr>
                    <td>Full name:</td>
                    <td><input type="text" name="full_name"></td>
                </tr>
                <tr>
                    <td>User name:</td>
                    <td><input type="text" name="user_name"></td>
                </tr>
                <tr>
                    <td>Password:</td>
                    <td><input type="password" name="password"></td>
                </tr>
                <tr>
                    <td><input type="submit" value="Register"></td>
                    <td><input type="reset" value="Reset form"></td>
                </tr>
            </table>
        </form>
        <a href="login.php">Login</a>
        <?php if ($error): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        <?php if ($success): ?>
            <div class="success"><?php echo htmlspecialchars($success); ?></div>
        <?php endif; ?>
    </div>
</body>
</html>
