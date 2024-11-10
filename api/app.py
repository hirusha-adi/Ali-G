from fastapi import FastAPI, Form, HTTPException
import g4f

app = FastAPI()


@app.post("/ali_g_chat/")
async def ali_g_chat(
    message: str = Form(...),
    style: str = Form(...),  # e.g., "short", "medium", "long"
    nsfw: int = Form(...),  # 0 for NSFW, 1 for no NSFW
):
    # Construct the prompt with the style and nsfw preferences
    nsfw_text = "keep it clean" if nsfw == 1 else "no filter"
    ali_g_prompt = (
        f"Make this sound like Ali G with a {style} style and {nsfw_text}: '{message}'"
    )

    try:
        # Generate Ali G styled response
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": ali_g_prompt}],
        )

        if not response:
            raise HTTPException(status_code=500, detail="No response from provider.")

        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the server with: uvicorn main:app --reload
