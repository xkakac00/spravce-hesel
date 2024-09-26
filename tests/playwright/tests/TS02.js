const { test, expect } = require('@playwright/test');

test('TS02 – Přihlášení uživatele', async ({ page }) => {
  // 1. Otevření přihlašovací stránky
  await page.goto('https://example.com/login');

  // 2. Vyplnění formuláře
  await page.fill('input[name="user_name"]', 'DonS');
  await page.fill('input[name="password"]', 'P.lb.45_?1!');

  // 3. Kliknutí na tlačítko "Login"
  await page.click('input[type="submit"]');

  // 4. Ověření, že uživatel je přihlášen a přesměrován na dashboard
  const dashboardMessage = await page.locator('text=Welcome, DonS');
  await expect(dashboardMessage).toBeVisible();

  console.log('Přihlášení uživatele bylo úspěšné .... [PASS]');
});
