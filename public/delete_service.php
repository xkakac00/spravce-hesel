<?php
session_start();

use App\Database;
use App\Service;

require '../init.php';

// Kontrola, zda je uživatel přihlášen
if (!isset($_SESSION['user'])) {
    echo "Přístup odepřen. Přihlaste se prosím.";
    exit();
}

$user = $_SESSION['user'];
$userId = $user['id'];

// Připojení k databázi a vytvoření instance třídy Service
$database = new Database();
$service = new Service($database);

// Zkontrolujeme, zda byl předán parametr 'id' přes GET
if (isset($_GET['id'])) {
    $serviceId = $_GET['id'];
    if ($service->deleteService($serviceId, $userId)) {
        $message = "Služba byla úspěšně odstraněna.";
    } else {
        $error = "Nastala chyba při odstraňování služby.";
    }
}

// Načtení všech služeb pro přihlášeného uživatele
$services = $service->getAllServices($userId);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odstranit službu</title>
    <link rel="stylesheet" href="../static/css/dashboard.css">
</head>
<body>
    <section class="dashboard">
        <section class="dashboard-body">
            <h2>Vaše služby</h2>
            <?php require("menu.php"); ?>
            <?php if (isset($error)): ?>
                <p><?php echo htmlspecialchars($error); ?></p>
            <?php elseif (isset($message)): ?>
                <p><?php echo htmlspecialchars($message); ?></p>
            <?php endif; ?>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Název služby</th>
                            <th>Uživatelské jméno</th>
                            <th>Heslo</th>
                            <th>Akce</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (!empty($services)): ?>
                            <?php foreach ($services as $service): ?>
                                <tr>
                                    <td><?php echo htmlspecialchars($service['service_name']); ?></td>
                                    <td><?php echo htmlspecialchars($service['user_name']); ?></td>
                                    <td><?php echo htmlspecialchars($service['user_password']); ?></td>
                                    <td>
                                        <a href="delete_service.php?id=<?php echo $service['id']; ?>" onclick="return confirm('Opravdu chcete tuto službu odstranit?');">Odstranit</a>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        <?php else: ?>
                            <tr>
                                <td colspan="4">Žádné služby nebyly nalezeny.</td>
                            </tr>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>
    </section>
</body>
</html>
