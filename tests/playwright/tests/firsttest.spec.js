const { test, expect } = require('@playwright/test');

test('Validace Youtube title', async ({ page }) => {
    // Otevři YouTube
    await page.goto('https://www.youtube.com');

    // Klikni na tlačítko "Přijmout vše" pokud je zobrazeno
    const acceptButton = page.locator('button:text("Accept all")');
    if (await acceptButton.isVisible()) {
        await acceptButton.click();
    }

    // Pokračuj ve vyhledávání elementů nebo jiných akcí na stránce

});
