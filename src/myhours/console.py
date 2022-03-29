from rich.console import Console

console = Console()


def info(text: str) -> None:
    console.print(f"[green]>> [/]{text}")


def warn(text: str) -> None:
    console.print(f"[orange]!! [/]{text}")
