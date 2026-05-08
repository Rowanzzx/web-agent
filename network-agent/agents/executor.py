import json
from tools.clash_controller import ClashController

class ExecutorAgent:

    def execute(self, plan):

        clash = ClashController()

        try:
            data = json.loads(plan)
        except:
            return "plan parse failed"

        results = []

        if "switch_proxy" in data:
            item = data["switch_proxy"]

            result = clash.switch_proxy(
                item["group"],
                item["proxy"]
            )

            results.append(result)

        return results
