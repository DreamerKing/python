import asyncio

async def delay(duration: int, tips = "") -> int:
  print(f"{tips} sleeping for {duration} seconds")
  await asyncio.sleep(duration)
  print(f"{tips} finished sleeping for {duration} seconds")
  return duration