# FastAPI
Official Documentation: https://fastapi.tiangolo.com/tutorial/first-steps/

How to run this API locally:

### Installation
- Create a `virtualenv` and **activate** it.
- Install the **requirements.txt** file `pip3 install -r requirements.txt`
  - To check uvicorn version: `uvicorn --version`
  
### Run locally
 
- **Command to run the FastAPI server:** `uvicorn main:app --reload` (by default port: 8000)
    - Here
        - `main` is our filename `main.py`
        - `app` is our FastAPI instance which we created in code (i.e. `app = FastAPI()`)
        - If we change the **filename and intance name** to something else then we have to use those to run the server
    - since we added `--reload` command at the end, after every save, it will be **reloaded** automatically and changes will be affected
    - To run server on different port, run this: `uvicorn main:app --port=9000`

    
### Output in Normal JSON Format
- Check the output in browser: usually at ********8000******** port
    - [`http://localhost:8000/`](http://localhost:8000/)
    - [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)
    
### Output in Swagger UI in Browswer
- [`http://localhost:8000/docs`](http://localhost:8000/docs)
- [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)

### To run the Test Cases
- Official Doc: https://fastapi.tiangolo.com/tutorial/testing/#__tabbed_1_2
- Command to test: `pytest -s`
    - The `-s` flag, which disables output capture and allows the `print()` statements to display to the console