import json
import psutil


class DiskUsageTool:
    """
    An example tool without any base classes that implements the bare minimum needed to adhere to the interface.
    """
    name = "disk_usage"
    description = "Useful for when you want to know the disk usage on the current system"

    def run(self, *args, **kwargs) -> str:
        disk_usage = psutil.disk_usage('/')

        return json.dumps({
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "percent": disk_usage.percent
        })

    async def arun(self, *args, **kwargs) -> str:
        return self.run(*args, **kwargs)
