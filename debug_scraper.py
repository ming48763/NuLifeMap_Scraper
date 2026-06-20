import asyncio
from playwright.async_api import async_playwright

async def debug_scrape_591(url):
    print(f"🚀 正在開啟瀏覽器抓取：{url}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        print("⏳ 正在載入頁面內容...")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        # 稍微等一下確保 JavaScript 執行完成
        await asyncio.sleep(3)
        
        content = await page.content()
        file_name = "debug_page.html"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 成功！網頁原始碼已儲存至：{file_name}")
        print("💡 請用編輯器打開該檔案，搜尋關鍵字「地址」或是您截圖中的路名，看看它在什麼標籤裡！")
        
        await browser.close()

if __name__ == "__main__":
    target_url = input("請貼上您想 debug 的 591 網址：")
    asyncio.run(debug_scrape_591(target_url))