const { test, expect } = require('@playwright/test');


test.beforeEach(async ({ page }) => {
  await page.goto(`file://${process.cwd()}/frontend/index.html`);
  
  
  const deleteButtons = page.locator('button:has-text("Delete")');
  const count = await deleteButtons.count();
  
  for (let i = 0; i < count; i++) {
    await deleteButtons.first().click();
    await page.waitForTimeout(200); 
  }
});

test('Page loads without crashing', async ({ page }) => {
  await page.goto(`file://${process.cwd()}/frontend/index.html`);
  await expect(page).toHaveTitle(/Task/i); 
});

test('Add a task', async ({ page }) => {
  await page.goto(`file://${process.cwd()}/frontend/index.html`);

  await page.fill('#title', 'Clean');
  await page.fill('#description', 'Vaccum the room');
  await page.click('#taskForm button');

  
  await page.waitForTimeout(300);

  
  await expect(page.locator('li').first()).toContainText('Clean');
});

test('Mark task as completed', async ({ page }) => {
  await page.goto(`file://${process.cwd()}/frontend/index.html`);

 
  await page.fill('#title', 'Test task');
  await page.click('#taskForm button');
  await page.waitForTimeout(300);

  
  await page.check('input[type=checkbox]');
  await page.waitForTimeout(200);
  
  
  await expect(page.locator('li').first()).toHaveClass(/completed/);
});

test('Delete a task', async ({ page }) => {
  await page.goto(`file://${process.cwd()}/frontend/index.html`);

  
  await page.fill('#title', 'Task to delete');
  await page.click('#taskForm button');
  await page.waitForTimeout(300);

  
  await expect(page.locator('li')).toHaveCount(1);

  
  await page.click('button:has-text("Delete")');
  await page.waitForTimeout(300);

  
  await expect(page.locator('li')).toHaveCount(0);
});

test('Do not allow empty task', async ({ page }) => {
  await page.goto(`file://${process.cwd()}/frontend/index.html`);

  
  await page.click('#taskForm button');
  await page.waitForTimeout(300);

  
  await expect(page.locator('li')).toHaveCount(0);
});