const { test, expect } = require('@playwright/test');

test('TS01 – Platná registrace uživatele', async ({ page }) => {
  // 1. Otevření registrační stránky
  await page.goto('https://example.com/register');

  // 2. Vyplnění formuláře
  await page.fill('input[name="full_name"]', 'Don Salieri');
  await page.fill('input[name="user_name"]', 'DonS');
  await page.fill('input[name="password"]', 'P.lb.45_?1!');

  // 3. Kliknutí na tlačítko "Register"
  await page.click('input[type="submit"]');

  // 4. Ověření, že se zobrazí zpráva o úspěšné registraci
  const successMessage = await page.locator('text=Registration successful');
  await expect(successMessage).toBeVisible();

  console.log('Registrace byla úspěšná .... [PASS]');
});
