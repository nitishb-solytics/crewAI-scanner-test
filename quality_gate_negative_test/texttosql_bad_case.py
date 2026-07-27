def generate_texttosql(user_query, db):
    prompt = f"""
    Convert this user question into SQL:
    {user_query}
    """

    llm_response = llm.invoke(prompt)

    return db.execute(llm_response)