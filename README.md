# Teams Spambot
 A spambot made with Selenium Python, which spams any given string to a user.

---

## How to
1. Download Repository
2. On Windows: Run `windows_install.bat`, on Linux:
   1. pip install selenium
   2. pip install webdriver-manager
   
3. Download Chrome
4. Run `spammer.py` and pass in the parameters asked for.

---

## Documentation
Dependencies:
1. Python
2. Selenium
3. WebDriver

In addition to those dependencies this also uses: [Automatic Login Microsoft](https://github.com/LucasoDevDotTk/automatic_login_microsoft) used for logging in to Teams. Documentation for that can be found in its respective repository.

### Debugging
For debugging, turn off headless and maximum mode, this can be done by: <br>
Commenting out:
```
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
```

You can also turn on logging, which I've disabled, to enable logging: <br>
Comment out: 
```
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
```

---

## Bug report
Please report any bugs in the GitHub repository of this project.

---
## LICENSE

```
MIT License

Copyright (c) 2023 Lucas Nguyen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
---

Thanks for using my software 🎈

`Happy Coding!`