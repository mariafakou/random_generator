import pandas as pd
import names
import random

class GenerateRandomInfo:
    
    def __init__(self): 
        self.NO_NAMES = 30 
        self.COUNTRY_CODES = ['DE', 'GR', 'BG', 'TH']
        self.PROJECTS = ['A', 'B', 'C']
        self.MIN_LEVEL = 2 
        self.MAX_LEVEL = 5
        self.df = pd.DataFrame(columns=['name', 'surname', 'name_surname_combined', 'country_code', 'level', 'project'])

    def generate_full_names(self):
        # randomly create a list of names 
        self.df.name_surname_combined = [names.get_full_name() for i in range(self.NO_NAMES)]

    def generate_countries(self):
        # create a list of countries from the given country codes
        self.df.country_code = [random.choice(self.COUNTRY_CODES) for i in range(self.NO_NAMES)]

    def generate_levels(self):
        # create a list of levels by randomly choosing a number between the min and max level 
        self.df.level = [random.randint(self.MIN_LEVEL, self.MAX_LEVEL) for i in range(self.NO_NAMES)]

    def generate_projects(self):
        # create a list of numbers between 1 and 2 if the given level is not 2 
        # else the project number is between 1 and 3  
        # the list is used to define the number of projects that a person participates 
        self.df.project = self.df.level.apply(lambda x: random.randint(1, 3) if x==2 else random.randint(1, 2))

    def split_full_name(self):
        # split the full name into name and surname and create new dataframe columns
        self.df[['name','surname']] = self.df['name_surname_combined'].str.split(' ', expand=True)
        
    def explode_column_project(self):
        # replace the number of projects with the actual project name(s) from the given list 
        # sample without replacement and use the explode function to create a row for every project that 
        # a person is involved
        self.df.project = self.df.project.apply(lambda x: random.sample(self.PROJECTS, x))
        self.df = self.df.explode('project', ignore_index=True)   

    def save_final_df_to_csv(self):
        try:
            self.df.to_csv('report.csv', index=False)
        except:
            print('Failed to write the file')         

def main():
    info = GenerateRandomInfo()
    info.generate_full_names()
    info.generate_countries()
    info.generate_levels()
    info.generate_projects()
    info.split_full_name()
    info.explode_column_project()
    info.save_final_df_to_csv()


if __name__ == "__main__":
    main()