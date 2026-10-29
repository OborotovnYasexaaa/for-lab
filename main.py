import json
import logging
from utils.statistics import calculate_average,find_min,find_max
from utils.reader import read_numbers,validate_numbers
from pathlib import Path

def main():
    with open('config.json','r',encoding='utf-8') as file:
        config=json.load(file)#расшифровывает файл config.json и превращает его в удобную картотеку
    input_file=config['input_file']#смотрит в конфиге путь к файлу
    log_file=config['log_file']#смотрит в конфиге путь к логам
    print(input_file)
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )

    logging.info("Программа запущена.")
    
    file_path=Path(input_file)#соединение пути с резудьтатом (объект path)
    print(file_path)#путь
    print(file_path.exists())#существует ли файл
    
    log_dir=Path('logs')#создаёт папку виртуально что бы позже рабоать в ней 
    log_dir.mkdir(exist_ok=True)#физиччески создаёт папку если папка есть то скип

    try:

        numbers=read_numbers(file_path)
        logging.info(f"файл прочитан,количество измерений{len(numbers)}")
        validate_numbers(numbers)
        print(numbers)
        print(calculate_average(numbers))
        print(find_min(numbers))
        print(find_max(numbers))
    
    except FileNotFoundError:
        print('файл не найден')
        logging.error("ОШИБКА файл не найден")
    except ValueError as q:
        print(q)
        logging.error("ОШИБКА файл пустой/не тот тип данных")
    finally:
        logging.info("работа окончена")

if __name__ == "__main__":
    main()