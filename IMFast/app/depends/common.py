from fastapi import Query

def skip_limit(
        skip: int = Query(
            default=0,
            description="How much to skip",
            ge=0,
        ),
        limit: int = Query(
            default=10,
            description="How much to limit",
            ge=1,
        )
) -> tuple:
    return skip, limit


