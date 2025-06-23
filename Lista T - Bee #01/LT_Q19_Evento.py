def main():
    obter_dia_inicio = input().split()
    dia_inicio = int(obter_dia_inicio[1])

    obter_hora_inicio = input().split(":")
    hora_inicio = int(obter_hora_inicio[0].strip())
    minuto_inicio = int(obter_hora_inicio[1].strip())
    segundo_inicio = int(obter_hora_inicio[2].strip())

    obter_dia_fim = input().split(" ")
    dia_fim = int(obter_dia_fim[1])

    obter_hora_fim = input().split(":")
    hora_fim = int(obter_hora_fim[0].strip())
    minuto_fim = int(obter_hora_fim[1].strip())
    segundo_fim = int(obter_hora_fim[2].strip())

    total_segundos_inicio = segundo_inicio + (minuto_inicio * 60) + (hora_inicio * 3600) +  (dia_inicio * 86400)

    total_segundos_fim = segundo_fim + (minuto_fim * 60) + (hora_fim * 3600) + (dia_fim * 86400)

    duracao_total_segundos = total_segundos_fim - total_segundos_inicio

    dias_duracao = duracao_total_segundos // 86400
    segundos_restantes = duracao_total_segundos % 86400

    horas_duracao = segundos_restantes // 3600
    segundos_restantes %= 3600

    minutos_duracao = segundos_restantes // 60
    segundos_duracao = segundos_restantes % 60

    print(f"{dias_duracao} dia(s)")
    print(f"{horas_duracao} hora(s)")
    print(f"{minutos_duracao} minuto(s)")
    print(f"{segundos_duracao} segundo(s)")
main()