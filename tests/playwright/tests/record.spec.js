import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost/spravce-hesel/');
  await page.goto('http://localhost/spravce/public/login.php');
  await page.locator('input[name="user_name"]').click();
  await page.locator('input[name="user_name"]').fill('ssss');
  await page.locator('input[name="password"]').click();
  await page.locator('input[name="password"]').fill('ssss');
  await page.getByRole('heading', { name: 'Login Page' }).click();
  await page.getByRole('button', { name: 'Login user' }).click();
});