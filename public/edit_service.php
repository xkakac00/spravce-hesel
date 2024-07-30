<?php
session_start();

use App\Database;
use App\Service;

require '../init.php';

// Kontrola, zda je uživatel přihlášen
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$user = $_SESSION['user'];
$userId = $user['id'];

// Připojení k databázi a vytvoření instance třídy Service
$database = new Database();
$service = new Service($database);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $serviceId = $_POST['id'];
    $serviceName = $_POST['service_name'];
    $serviceUserName = $_POST['service_user_name'];
    $servicePassword = $_POST['service_password'];

    if ($service->editService($serviceId, $userId, $serviceName, $serviceUserName, $servicePassword)) {
        header("Location: view_services.php");
        exit();
    } else {
        $error = "Nastala chyba při aktualizaci služby.";
    }
} else {
    if (isset($_GET['id'])) {
        $serviceId = $_GET['id'];
        $serviceDetails = $service->getServiceById($serviceId, $userId);
        if (!$serviceDetails) {
            $error = "Passwords not found.";
        }
    } else {
        header("Location: view_services.php");
        exit();
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editing password</title>
    <link rel="stylesheet" href="../static/css/dashboard.css">
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

        .dashboard {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 800px;
        }

        .dashboard-body h2 {
            margin-top: 0;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        form input[type="text"], form input[type="password"] {
            padding: 10px;
            margin: 5px 0 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        form button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        form button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <section class="dashboard">
        <section class="dashboard-body">
            <h2>Editing password</h2>
            <?php require("menu.php"); ?>
            <?php if (isset($error)): ?>
                <p><?php echo htmlspecialchars($error); ?></p>
            <?php endif; ?>
            <?php if (isset($serviceDetails)): ?>
                <form action="edit_service.php" method="POST">
                    <input type="hidden" name="id" value="<?php echo htmlspecialchars($serviceDetails['id']); ?>">
                    <input type="text" name="service_name" placeholder="Service name" value="<?php echo htmlspecialchars($serviceDetails['service_name']); ?>" required>
                    <input type="text" name="service_user_name" placeholder="Service user name" value="<?php echo htmlspecialchars($serviceDetails['user_name']); ?>" required>
                    <input type="password" name="service_password" placeholder="Service user password" value="<?php echo htmlspecialchars($serviceDetails['user_password']); ?>" required>
                    <button type="submit">Update the password</button>
                </form>
            <?php endif; ?>
            <nav>
                <ul>
                    <li><a href="view_services.php">Back to show all passwords</a></li>
                </ul>
            </nav>
        </section>
    </section>
</body>
</html>
