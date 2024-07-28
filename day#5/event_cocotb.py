from cocotb.triggers import Event

event = Event()

@cocotb.coroutine
async def wait_for_event():
    await event.wait()

@cocotb.coroutine
async def set_event():
    event.set()



