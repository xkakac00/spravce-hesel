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


$user=$_SESSION['user'];
//$userName=$user['user_name'];
$userId=$user['id'];

// připojeni k databazi a Service instance
$database=new Database();
$service=new Service($database);

// načtení všech služeb pro přihlášeného uživatele
$services=$service->getAllServices($userId);

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

            <h2>Your passwords</h2>
            <?php require("menu.php"); ?>
            <table>
                <thead>
                    <tr>
                        <th>Service name</th>
                        <th>User name</th>
                        <th>Password</th>
                        <th>Edit</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (!empty($services)): ?>
                        <?php foreach ($services as $service): ?>
                            <tr>
                                <td><?php echo htmlspecialchars($service['service_name']); ?></td>
                                <td><?php echo htmlspecialchars($service['user_name']); ?></td>
                                <td><?php echo htmlspecialchars($service['user_password']); ?></td>
                                <td><a href="edit_service.php?id=<?php echo $service['id']; ?>" name="edit">Edit</a></td>
                            </tr>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <tr>
                            <td colspan="3">No services were found.</td>
                        </tr>
                    <?php endif; ?>
                </tbody>
            </table>
        </section>

</body>
</html>
