from sqlitehandler import read_from_db
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

solution = []

# SELECT de prueba
test = '''SELECT * FROM bedroom_temperature LIMIT 10;'''

# Promedio de algún sensor
solution.append('''
SELECT AVG(value) FROM bedroom_temperature;
''')

# Promedio de todos los sensores
solution.append('''
SELECT AVG(value) FROM (
    SELECT value FROM bedroom_temperature
    UNION ALL
    SELECT value FROM kitchen_temperature
    UNION ALL
    SELECT value FROM livingroom_temperature
);
''')

# SELECT MIN(timestamp) FROM kitchen_temperature;
# SELECT MAX(timestamp) FROM kitchen_temperature;

# Promedio del ultimo dia
solution.append('''
SELECT AVG(value) FROM (
    SELECT * FROM bedroom_temperature
    UNION ALL
    SELECT * FROM kitchen_temperature
    UNION ALL
    SELECT * FROM livingroom_temperature
)
WHERE timestamp > (
    SELECT MAX(timestamp) - 86400 FROM (
        SELECT timestamp FROM bedroom_temperature
        UNION ALL
        SELECT timestamp FROM kitchen_temperature
        UNION ALL
        SELECT timestamp FROM livingroom_temperature
    )
);
''')

# Timestamp del momento más caluroso de la casa
solution.append('''
SELECT timestamp
FROM(
    SELECT * FROM bedroom_temperature
    UNION ALL
    SELECT * FROM kitchen_temperature
    UNION ALL
    SELECT * FROM livingroom_temperature
)
WHERE value = (
    SELECT MAX(value) FROM (
        SELECT value FROM bedroom_temperature
        UNION ALL
        SELECT value FROM kitchen_temperature
        UNION ALL
        SELECT value FROM livingroom_temperature
    )
);
''')

# Evolucion del sensor del dormitorio
solution.append('''SELECT * FROM bedroom_temperature ORDER BY timestamp ASC;''')


def main():
    # result = read_from_db(test)
    # print()
    # for value, unit, timestamp in result:
    #     print(" {:%Y-%m-%d %H:%M}    {:.2f} {:}".format(datetime.fromtimestamp(timestamp), value, unit))

    result = []
    
    for query in solution:
        result.append(read_from_db(query)[0][0])

    print()
    print("El promedio de la temperatura en el dormitorio:   {:.2f}°C" .format(result[0]))
    print("El promedio de todos los sensores de temperatura: {:.2f}°C" .format(result[1]))
    print("El promedio de temperaturas del ultimo día:       {:.2f}°C" .format(result[2]))
    print("El momento más caluroso ocurrió:                  {:%Y-%m-%d %H:%M}" .format(datetime.fromtimestamp(result[3])))
    print()

    result = read_from_db(solution[4])
    # for row in result:
    #     print("{:%Y-%m-%d %H:%M} {:.2f}" .format(datetime.fromtimestamp(row[2]), row[0]))

    xAxis = ['{:%m-%d %H:%M:%S}' .format(datetime.fromtimestamp(row[2])) for row in result]
    yAxis = [row[0] for row in result]

    plt.plot(xAxis, yAxis)
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Temperatura')
    plt.title('Temperatura en el Dormitorio')
    plt.xticks(rotation=60)
    plt.gcf().subplots_adjust(bottom=0.3)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.show()


if __name__ == '__main__':
    main()