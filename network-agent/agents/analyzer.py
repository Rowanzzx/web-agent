from openai import OpenAI
from config import OPENAI_API_KEY, BASE_URL, MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=BASE_URL
)

class AnalyzerAgent:

    def analyze(self, logs):

        prompt = f"""
你是一个 OpenWrt 与 OpenClash 网络运维专家。

请分析下面日志中的问题：

{logs}

输出：
1. 问题类型
2. 可能原因
3. 严重等级
4. 修复建议
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
