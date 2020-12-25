import asyncio
from pyppeteer import launch

async def paikka_tekstiksi(paikka: str, page: "Page") -> str:
    try:
        elem = await page.querySelector(paikka)
        return await page.evaluate('(element) => element.textContent', elem)
    except:
        print("Joku virhe\n")
        return "Virhe"

async def main():
    browser = await launch(executablePath='/usr/bin/chromium')
    page = await browser.newPage()
    # await page.goto('https://www.fantasycritic.games/league/fb4b4799-2b50-45d1-803b-658a7dddf3f6/2020')
    await page.goto('https://www.fantasycritic.games/league/c5a1211e-cfd3-423c-9936-915c1da93569/2021')
    
    
    while True:
        syote = input("Anna CSS-osoite: ")
        if syote == "q":
            break
        elementin_teksti = await paikka_tekstiksi(syote, page)
        print(f"Siinä lukee: \n{elementin_teksti}")
        

    await browser.close()
asyncio.get_event_loop().run_until_complete(main())

# div.table-responsive:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)
# div.table-responsive:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > span:nth-child(1) 

#__BVID__97 > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > 

# div.table-responsive:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)