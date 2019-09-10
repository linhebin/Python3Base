from CeleryTask.tasks import add

result = add.delay(55, 8)
print(result.ready())

print(result.get(timeout=1, propagate=False))
result.get()
