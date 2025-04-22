from data_processor import DataProcessor 

if __name__ == "__main__": 
    # Инициализация обработчика данных 
    processor = DataProcessor('var5.csv') 

    # Удаление повторок через унарный оператор 
    removed_duplicates = -processor 
    print(f"Количество удалённых дубликатов: {removed_duplicates}") 
    
    # Сохранение разделенных датасетов 
    processor.save_split_datasets() 