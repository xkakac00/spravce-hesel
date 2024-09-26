const { test, expect } = require('@playwright/test');

test('TS04 – Přidání hesla', async ({ page }) => {
  // 1. Přihlášení uživatele
  await page.goto('https://example.com/login');
  await page.fill('input[name="user_name"]', 'DonS');
  await page.fill('input[name="password"]', 'P.lb.45_?1!');
  await page.click('input[type="submit"]');

  // 2. Přejít na stránku pro přidání hesla
  await page.click('text=Add Password');

  // 3. Vyplnění formuláře pro přidání hesla
  await page.fill('input[name="service_name"]', 'Facebook');
  await page.fill('input[name="service_user_name"]', 'DonS_F');
  await page.fill('input[name="service_user_password"]', '123456');

  // 4. Kliknutí na tlačítko "Add password"
  await page.click('input[type="submit"]');

  // 5. Ověření, že heslo bylo úspěšně přidáno
  const successMessage = await page.locator('text=Password added successfully');
  await expect(successMessage).toBeVisible();

  console.log('Heslo bylo úspěšně přidáno .... [PASS]');
});
