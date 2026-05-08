from openai import OpenAI
from config import OPENAI_API_KEY, BASE_URL, MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=BASE_URL
)

class PlannerAgent:

    def plan(self, analysis):

        prompt = f"""
根据下面的问题分析，生成修复计划：

{analysis}

要求：
- 尽量避免影响整体网络
- 优先切换异常节点
- 必要时修改 DNS
- 输出 JSON
"""

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
