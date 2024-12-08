```bash
docker pull davep80/gemini_cards:latest
```
### Instructions
run the image in docker desktop and declare and Environment Variable called `API_KEY`, use an openai key.
### Program Notes
When the image/container runs the program navigates to pursuit codetrack website, information is scraped with selenium, and a csv file is created. 12 random rows from the csv is chosen, and then with openai trading card information and descriptions are written and then dumped to a `cards.json` file.