# Comparison entre FIFO et SRTF

print("=== FIFO Scheduling ===")

fifo_processes = [
    {"name": "P1", "burst": 5},
    {"name": "P2", "burst": 3},
    {"name": "P3", "burst": 8}
]

fifo_time = 0

for p in fifo_processes:
    print(f"{p['name']} execute pendant {p['burst']} secondes")
    fifo_time += p['burst']

print("Temps total FIFO :", fifo_time)


print("\n=== SRTF Scheduling ===")

srtf_processes = [
    {"name": "P1", "remaining": 5},
    {"name": "P2", "remaining": 3},
    {"name": "P3", "remaining": 8}
]

srtf_time = 0

while True:

    available = [p for p in srtf_processes if p["remaining"] > 0]

    if not available:
        break

    shortest = min(available, key=lambda x: x["remaining"])

    print(f"Execution de {shortest['name']}")

    shortest["remaining"] -= 1
    srtf_time += 1

print("Temps total SRTF :", srtf_time)


print("\n=== Comparaison ===")

print("FIFO execute les processus selon l'ordre d'arrivée.")
print("SRTF choisit toujours le processus le plus court.")

if fifo_time > srtf_time:
    print("SRTF est plus rapide.")
else:
    print("FIFO est plus rapide.")