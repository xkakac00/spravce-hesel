const { test, expect } = require('@playwright/test');

test('TS03 – Chybné přihlášení', async ({ page }) => {
  // 1. Otevření přihlašovací stránky
  await page.goto('https://example.com/login');

  // 2. Vyplnění formuláře s chybnými údaji
  await page.fill('input[name="user_name"]', 'WrongUser');
  await page.fill('input[name="password"]', 'WrongPassword');

  // 3. Kliknutí na tlačítko "Login"
  await page.click('input[type="submit"]');

  // 4. Ověření, že se zobrazí chybová zpráva
  const errorMessage = await page.locator('text=Invalid username or password');
  await expect(errorMessage).toBeVisible();

  console.log('Chybné přihlášení bylo správně detekováno .... [PASS]');
});
