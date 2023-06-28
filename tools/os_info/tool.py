import json
import platform

from langchain.tools.base import BaseTool


class OSInfo(BaseTool):
    """
    Example tool using the LangChain tool base class
    """
    name = "os_info"
    description = "Get the current OS name and version information"

    def _run(self) -> str:
        return json.dumps({"os_name": platform.system(), "os_version": platform.release()})

    async def _arun(self) -> str:
        return self._run()
