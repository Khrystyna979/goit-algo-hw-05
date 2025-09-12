import sys
from collections import defaultdict
from pathlib import Path
from colorama import Fore, Style

def parse_log_line(line: str) -> dict:
    """
    Function for parsing information from line to dict
    """
    date_log, time_log, level_of_log, *args = line.strip().split(sep=' ') # Розбиваємо рядок за пробілом

    log_dict = {
    'date': date_log,
    'time': time_log,
    'level': level_of_log,
    'message': ' '.join(args)
    }

    return log_dict

def load_logs(file_path: str) -> list:
    """
    Function to unite parsing data into list
    """
    logs = []
    
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            logs.append(parse_log_line(line))
    
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Function for filter logs list by level
    """
    filter_list = [log for log in logs if log.get('level') == level] # генеруємо список логів які мають однаковий рівень
    
    return filter_list

def count_logs_by_level(logs: list) -> dict:
    """
    Function which form new dict that counts logs by level
    """
    count_of_logs = defaultdict(int) # створюємо defaultdict де значення за замовчуванням буде 0

    for log in logs:
        count_of_logs[log['level']] += 1

    return dict(count_of_logs)


def display_log_counts(counts: dict):
    """
    Function that forms table based on dict counts logs 
    """
    print(Fore.GREEN + f'{'Рівень Логування':<17}' + Style.RESET_ALL + '|' + Fore.GREEN + f'{' Кількість':<15}'+ Style.RESET_ALL)
    print(f'{'-' * 17}|{'-' * 10}')

    for key, value in counts.items():
        print(f'{key:<16} | {value:<15}')

def main():
    try:
        path = Path(sys.argv[1])

        if len(sys.argv) < 2: # Перевіряємо чи надано шлях
            print('Please provide a path') 
            sys.exit(1)
        elif not path.exists(): # Перевіряємо наданий шлях існує
            print('Path is not existing')
            sys.exit(1)
        else:
            display_log_counts(count_logs_by_level(load_logs(path)))

        if len(sys.argv) > 2: # Перевіряємо чи передано аргумент для виведення інформації про конкретний лог
            level = sys.argv[2].lower()  

            if level in ("error", "info", "debug", "warning"):
                print(f'Деталі логів для рівня "{level.upper()}":')
                for log in filter_logs_by_level(load_logs(path), level.upper()):
                    print(log['date'], log['time'],'-', log['message'])
            else:
                print(f'Невідомий рівень логів: {level}')
        
    except IndexError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
