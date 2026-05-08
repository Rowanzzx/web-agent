import time
import schedule
from rich import print

from tools.log_reader import LogReader

from agents.analyzer import AnalyzerAgent
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

reader = LogReader()
analyzer = AnalyzerAgent()
planner = PlannerAgent()
executor = ExecutorAgent()
verifier = VerifierAgent()

def workflow():

    print("[cyan]读取日志...[/cyan]")

    logs = reader.get_logs()

    print("[yellow]AI 分析异常...[/yellow]")

    analysis = analyzer.analyze(logs)

    print(analysis)

    print("[green]生成修复计划...[/green]")

    plan = planner.plan(analysis)

    print(plan)

    print("[magenta]执行修复...[/magenta]")

    result = executor.execute(plan)

    print(result)

    print("[blue]验证结果...[/blue]")

    ok = verifier.verify("香港节点")

    if ok:
        print("[green]修复成功[/green]")
    else:
        print("[red]修复失败，准备回滚[/red]")

schedule.every(5).minutes.do(workflow)

print("Agent started...")

workflow()

while True:
    schedule.run_pending()
    time.sleep(1)
