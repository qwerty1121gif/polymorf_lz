import pandas as pd

class DataProcessor:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.removed_duplicates = 0

    def split_by_city(self): 
        """Разделяет датасет на Минск и другие города"""
        minsk = self.df[self.df['Место оплаты'] == 'Минск']
        other = self.df[self.df['Место оплаты'] != 'Минск']
        return minsk, other
    
    def save_split_datasets(self):
        """Сохраняет разделённые датасеты в csv-файлы"""
        minsk, other = self.split_by_city()
        minsk.to_csv('minsk.csv', index=False)
        other.to_csv('other_cities.csv', index=False)
        print("Файлы сохранены: minsk.csv и other_cities.csv")
        
    def __neg__(self):
        """Унарный оператор '-' для удаления дубликатов"""
        initial_rows = len(self.df)
        self.df.drop_duplicates(inplace=True)
        self.removed_duplicates = initial_rows - len(self.df)
        return self.removed_duplicates