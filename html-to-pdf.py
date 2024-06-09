import asyncio
from pyppeteer import launch

async def generate_pdf(url, pdf_path):
  # Option 1: Update pyppeteer (Recommended)
  # Update pyppeteer using pip before running this code

  # Option 2: Specify Chromium executable path (Less Recommended)
  # Download the appropriate Chromium executable from https://www.chromium.org/getting-involved/download-chromium/
  # Replace 'path/to/downloaded/chromium.exe' with the actual path
  # browser = await launch(executablePath='path/to/downloaded/chromium.exe')

  browser = await launch(executablePath="C:\\Users\\HP\\Downloads\\chrome-win\\chrome-win\\chrome.exe")
  page = await browser.newPage()
  
  await page.goto(url)
  
  await page.pdf({'path': pdf_path, 'format': 'A3'})
  
  await browser.close()

# Run the function using asyncio.run (no deprecation warning)
asyncio.run(generate_pdf('https://shakil-khatri-resume.vercel.app/', 'example.pdf'))


#NOT WORKING AS EXPECTED, CHANGING SOME CSS