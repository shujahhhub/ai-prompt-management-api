
prompts = [
    {
        "id": 1,
        "topic": "Python",
        "prompt": "Explain Python fundamentals",
        "active": True
    },
    {
        "id": 2,
        "topic": "RAG",
        "prompt": "Explain retrieval augmented generation",
        "active": True
    },
    {
        "id": 3,
        "topic": "AI Agents",
        "prompt": "Explain AI agents",
        "active": False
    }
]

next_prompt_id = 4


def get_all_prompts(active=None):
    if active is None:
        return prompts

    return [
        prompt for prompt in prompts
        if prompt["active"] == active
    ]


def find_prompt(prompt_id: int):
    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt

    return None


def create_prompt(prompt_data):
    global next_prompt_id

    new_prompt = {
        "id": next_prompt_id,
        **prompt_data.model_dump()
    }

    prompts.append(new_prompt)
    next_prompt_id += 1

    return new_prompt


def update_prompt(prompt_id: int, prompt_data):
    prompt = find_prompt(prompt_id)

    if prompt is None:
        return None

    prompt.update(prompt_data.model_dump())

    return prompt


def patch_prompt(prompt_id: int, prompt_data):
    prompt = find_prompt(prompt_id)

    if prompt is None:
        return None

    updates = prompt_data.model_dump(exclude_unset=True)
    prompt.update(updates)

    return prompt


def delete_prompt(prompt_id: int):
    prompt = find_prompt(prompt_id)

    if prompt is None:
        return None

    prompts.remove(prompt)

    return prompt


def search_prompts(topic: str):
    return [
        prompt for prompt in prompts
        if prompt["topic"].lower() == topic.lower()
    ]
