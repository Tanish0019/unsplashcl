# Requirements

- Python3
- pipenv

## Setting Up

- Run the following commands in the terminal

  ```bash
  pipenv shell
  pipenv install
  ```

- Make a new file - `config.py` in the root directory of the repository and paste the following in it.

  ```python
  client_id = <Your_Unsplash_Client_ID>
  secret_key = <Your_Unsplash_Secret_Key>
	```

## Running The Script

### picture of the day

```bash
python scrape_image.py
```

### Set Background

```bash
python change_bg.py <Image Path>
```
