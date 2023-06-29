import json

import psutil
from langchain.tools import BaseTool


class DiskUsageTool(BaseTool):
    """
    An example tool without any base classes that implements the bare minimum needed to adhere to the interface.
    """

    name = "disk_usage"
    description = (
        "Useful for when you want to know the disk usage on the current system"
    )

    def _run(self, directory: str = "/") -> str:
        disk_usage = psutil.disk_usage(directory)

        return json.dumps(
            {
                "total": disk_usage.total,
                "used": disk_usage.used,
                "free": disk_usage.free,
                "percent": disk_usage.percent,
            }
        )

    async def _arun(self, directory: str = "/") -> str:
        return self._run()
