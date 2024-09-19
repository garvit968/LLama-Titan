import base64
import os
import boto3
import json

prompt_data = """blue backpack on a table"""

bedrock = boto3.client(service_name = 'bedrock-runtime')

payload = {
    "textToImageParams":{
    "text": prompt_data},
    "taskType":"TEXT_IMAGE",
    "imageGenerationConfig":{
        "cfgScale":8,
        "seed":0,
        "quality":"standard",
        "width":1024,
        "height":1024,
        "numberOfImages":3
        },
}

body = json.dumps(payload)
print(body)
model_id = "amazon.titan-image-generator-v2:0"
response = bedrock.invoke_model(
    body = body,
    modelId = model_id,
    accept = "application/json",
    contentType = "application/json"
) 

response_body = json.loads(response.get("body").read())
print(response_body)
artifact = response_body["images"][0]

# Save the generated image to a local folder.
i, output_dir = 1, "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
while os.path.exists(os.path.join(output_dir, f"image_{i}.png")):
    i += 1

image_data = base64.b64decode(artifact)

image_path = os.path.join(output_dir, f"image_{i}.png")
with open(image_path, "wb") as file:
    file.write(image_data)

print(f"The generated image has been saved to {image_path}.")
