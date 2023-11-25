small_containers = int(input("Введіть кількість контейнерів розміром 1 літр або менше: "))
large_containers = int(input("Введіть кількість контейнерів розміром понад 1 літр: "))
small_deposit = 0.10
large_deposit = 0.25  
refund = (small_containers * small_deposit) + (large_containers * large_deposit)
print(f"Відшкодування за повернення контейнерів: ${refund:.2f}")
