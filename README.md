# AI Agent for Code Analysis

This is an AI Agent that analyzes code and generates a structured report based on the provided problem description.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the FastAPI server:
   ```bash
   python main.py
   ```

## Usage

Send a `POST` request to `/analyze` with the following form data:
- `problem_description`: A string describing the features to be implemented.
- `code_zip`: A zip file containing the project source code.

## Example Request

```bash
curl -X POST -F "problem_description=實現建立頻道功能" -F "code_zip=@project_code.zip" http://localhost:8000/analyze
```

## Response

The response will be a JSON report detailing the key implementation points for each feature.