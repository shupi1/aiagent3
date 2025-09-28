from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import zipfile
import os
import json
from typing import List, Dict

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_code(
    problem_description: str = Form(...),
    code_zip: UploadFile = File(...),
):
    # Save the uploaded zip file
    zip_path = "uploaded_code.zip"
    with open(zip_path, "wb") as f:
        f.write(await code_zip.read())
    
    # Extract the zip file
    extract_dir = "extracted_code"
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    # Analyze the code and generate the report
    report = analyze_codebase(problem_description, extract_dir)
    
    # Clean up
    os.remove(zip_path)
    # Optionally, remove the extracted directory
    # import shutil
    # shutil.rmtree(extract_dir)
    
    return report

def analyze_codebase(problem_description: str, code_dir: str) -> Dict:
    # Placeholder for the actual analysis logic
    # This function should parse the problem_description and code_dir to generate the report
    
    # Example report structure
    report = {
        "feature_analysis": [
            {
                "feature_description": "實現`建立頻道`功能",
                "implementation_location": [
                    {
                        "file": "src/modules/channel/channel.resolver.ts",
                        "function": "createChannel",
                        "lines": "13-16"
                    },
                    {
                        "file": "src/modules/channel/channel.service.ts",
                        "function": "create",
                        "lines": "21-24"
                    }
                ]
            }
        ],
        "execution_plan_suggestion": "要執行此專案，應首先執行 `npm install` 安裝依賴，然後執行 `npm run start:dev` 來啟動服務。該服務是一個GraphQL API，可以在 http://localhost:3000/graphql 訪問。"
    }
    
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)