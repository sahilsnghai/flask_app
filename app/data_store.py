# In-memory storage simulation
memory_store = {}

def store_data(data):
    global memory_store
    memory_store = data

def get_stored_data():
    return memory_store
