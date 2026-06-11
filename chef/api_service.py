from openai import OpenAI

from django.conf import settings


client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


SYSTEM_PROMPT = """
شما یک سرآشپز حرفه‌ای هستید.

پاسخ را کاملاً فارسی بده.

برای هر غذا:

- نام غذا
- توضیح کوتاه
- زمان پخت
- درجه سختی
- مواد لازم
- مراحل پخت

خروجی مرتب و خوانا باشد.
"""


def generate_recipe_ai(ingredients):

    response = client.chat.completions.create(

        model=settings.OPENROUTER_MODEL,

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": f"""
مواد اولیه موجود:

{ingredients}

سه غذای قابل تهیه پیشنهاد بده.
"""
            }

        ]

    )

    return (
        response
        .choices[0]
        .message
        .content
    )