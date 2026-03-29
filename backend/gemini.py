from google import genai

def uploadRecording(filepath):
    client = genai.Client()
    myfile = client.files.upload(file=filepath)
    print(f"{myfile=}")

    result = client.models.generate_content(
        model="gemini-2.5-flash", contents=[myfile, "Describe this audio clip"]
    )
    print(f"{result.text=}")
    return myfile

def delete(file):
    client = genai.Client()
   # myfile = client.files.upload(file=media / filename)

    client.files.delete(name=file.name)

    try:
        result = client.models.generate_content(
            model="gemini-2.0-flash", contents=[file, "Describe this file."]
        )
        print(result)
        return(result)
    except genai.errors.ClientError:
        return("error")
    
def analyzeSpeach(file):
    client = genai.Client()
    result = client.models.generate_content(
    model="gemini-2.5-flash", contents=[file, "You are an expert in public speaking. Please analyze the included"
    "file for the effectiveness of the speach. Please pay particular attention to the tone, clarity of expression, and word choice."
    "Please return only valid json in the following format: {ToneClarity: '<clarity of>', WordChoiceSuggestons:{'Original word or phrase, 'suggested alternative'"
    "}, Expression: 'expression description' }"]
    )

    print("result of analaysis", result)
    return result