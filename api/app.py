from fastapi import FastAPI, Form, HTTPException
import g4f

app = FastAPI()


@app.post("/v1/text/")
async def ali_g_chat(
    message: str = Form(...),
    style: str = Form(...),  # e.g., "short", "medium", "long"
    nsfw: int = Form(...),  # 0 for NSFW, 1 for no NSFW
):
    """
    Chat with Ali G.

    Parameters
    ----------
    message : str
        The message to be transformed into an Ali G style response.
    style : str
        The style of the response. One of "short", "medium", or "long".
    nsfw : int
        Whether the response should be NSFW or not. 0 for no NSFW, 1 for NSFW.

    Returns
    -------
    response : str
        The transformed response in the style of Ali G.

    Raises
    ------
    HTTPException
        400 if the style or nsfw values are invalid.
        500 if there is an error with the provider (e.g. no response).

    """

    # input validation
    # -----
    if style not in ("short", "medium", "long"):
        raise HTTPException(status_code=400, detail="Invalid style")
    
    if not isinstance(nsfw, int) or nsfw not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid nsfw value")

    # construct the prompt
    # -----
    nsfw_status = "keep it clean" if nsfw == 1 else "no filter"
    prompt = f"Make this sound like Ali G with a {style} style and {nsfw_status}: '{message}'"

    # generate response
    # -----
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )

        if not response:
            raise HTTPException(status_code=500, detail="No response from provider.")

        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the server with: uvicorn main:app --reload
