# [Link - Merge](https://www.merge.dev/docs/get-started/link/)

## Issue:

Following the steps to make Link appear in the frontend [here](https://www.merge.dev/docs/get-started/link/#step-2), I am unable to get it working.

On initiation of MergeLink `MergeLink.initialize()`, the `onSuccess()` callback function does not seem to be called. There are console logs added on each step of initialization process.

### Demo of issue:
https://user-images.githubusercontent.com/9460504/179392305-13b4895e-758c-4fd7-b084-9efdc7d1d981.mp4


### Tech stack:

- Python for the backend
- Vanilla HTML/JS for the frontend

## Steps to reproduce:

### Pre-requisite:

- Have Python3.9 installed on your machine 🐍
- Have an IDE installed on your machine - this project is tested on VSCode and PyCharm

1. Clone the repository `git clone https://github.com/shrestaz/merge.git`
2. Open the project in IDE of your choice
3. Install the requirements for the project using `python3.9 -m pip install -r requirements.txt`, _ideally in a virtual environment_
4. Open `services.py` file and add values for `api_key` on line 3 and update body object with end user info on line 7 onwards.
5. Run the server `uvicorn main:app --reload` from the terminal in the project root
6. Open the file `link.html` through the IDE
   - For VS Code, right click on the file and select "Open with Live Serve"
   - For PyCharm, right click on the file > Open in > Browser > Choose your favorite browser
   - For other IDES, make sure to add the url location host to the origins list in file `main.py` to avoid CORS error
7. While having the browser console open, click the only button `Start Linking`
   - Console logs are added for each steps
8. **Expected**: Link should appear in the frontend. **Reality**: Link does not appear in the frontend 😔
