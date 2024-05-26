import asyncio
import time

async def hello(message: str, second: int) -> str:
  await asyncio.sleep(second)
  return message

async def main():
  t1 = time.time()
  message1 = await hello("Hello king", 2)
  print(message1)
  t2 = time.time()
  print("t2-t1:", t2 - t1)

  message2 = await hello("Hi, dreamer", 1)
  print(message2)
  t3 = time.time()
  print("t3-t1:", t3 - t1)


asyncio.run(main())