<?php
session_start();

use App\Database;
use App\Service;

require '../init.php';

// Kontrola, zda je uživatel přihlášen
if (!isset($_SESSION['user'])) {
    // Pokud uživatel není přihlášen, přesměrujeme ho na login.php
    header("Location: login.php");
    exit();
}

$user = $_SESSION['user'];
$userId = $user['id'];

// připojeni k databazi a Service instance
$database = new Database();
$service = new Service($database);

// Proměnná pro chybové zprávy
$errorMessage = "";
$success = ''; // Inicializace proměnné pro úspěch

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $serviceName = $_POST['service_name'] ?? '';
    $serviceUserName = $_POST['service_user_name'] ?? '';
    $servicePassword = $_POST['service_user_password'] ?? '';

    // Validace vstupních dat
    if (empty($serviceName) || empty($serviceUserName) || empty($servicePassword)) {
        $errorMessage = "All rows are mandatory!";
    } else {
        // Přidání služby
        if ($service->addService($userId, $serviceName, $serviceUserName, $servicePassword)) {
           $success="Password successfully added!";
        } else {
            $errorMessage = "Failed to add the password.";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="../static/css/dashboard.css">
</head>
<body>
    <section class="dashboard">
        <h2>Add password section</h2>
        <?php require("menu.php");?>
        <form action="add_service.php" method="POST">
            <input type="hidden" name="action" value="add">
            <input type="text" name="service_name" placeholder="Service name">
            <input type="text" name="service_user_name" placeholder="Service user name" >
            <input type="password" name="service_user_password" placeholder="Service user password">
            <input type="submit" value="Add password"><input type="reset" value="Reset form">
        </form>
        <?php if ($errorMessage): ?>
            <div class="error"><?php echo htmlspecialchars($errorMessage); ?></div>
        <?php endif; ?>
        <?php if ($success): ?>
            <div class="success"><?php echo htmlspecialchars($success); ?></div>
        <?php endif; ?>
    </section>
</body>
</html>
