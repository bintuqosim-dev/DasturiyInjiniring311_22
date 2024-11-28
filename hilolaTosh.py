import asyncio

async def first():
    await asyncio.sleep(0)  
    return "first"

async def second():
    await asyncio.sleep(0)  
    return "second"

async def third():
    await asyncio.sleep(0)  
    return "third"


async def async_main(nums):
    
    functions = {
        1: first,
        2: second,
        3: third
    }

    
    tasks = [functions[num]() for num in nums]
    
    results = await asyncio.gather(*tasks)

    
    return ''.join(results)


def run(nums):
    return asyncio.run(async_main(nums))


nums = [1, 2, 3]
output = run(nums)
print(output)  