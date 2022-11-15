import pandas as pd
import names
import random

class GenerateRandomInfo:
    NO_NAMES = 30 
    COUNTRY_CODES = ['DE', 'GR', 'BG', 'TH']
    PROJECTS = ['A', 'B', 'C']
    MIN_LEVEL = 2 
    MAX_LEVEL = 5

    def __init__(self): 
        self.full_names = None
        self.countries = None
        self.levels = None
        self.no_projects = None
        self.df = None

    def generate_full_names(self):
        # randomly create a list of names 
        self.full_names = [names.get_full_name() for i in range(self.NO_NAMES)]

    def generate_countries(self):
        # create a list of countries from the given country codes
        self.countries = [random.choice(self.COUNTRY_CODES) for i in range(self.NO_NAMES)]

    def generate_levels(self):
        # create a list of levels by randomly choosing a number between the min and max level 
        self.levels = [random.randint(self.MIN_LEVEL, self.MAX_LEVEL) for i in range(self.NO_NAMES)]

    def generate_projects(self):
        # create a list of numbers between 1 and lenght of the given projects (3 in our case)
        # the list is used to define the number of projects that a person participates 
        self.no_projects = [random.randint(1, len(self.PROJECTS)) for i in range(self.NO_NAMES)]    
    
    def create_df_split_full_name(self):
        # create a dataframe given the current information (full names, country codes, levels, number of projects)
        dict = {'name_surname_combined': self.full_names, 'country_code': self.countries, 
        'level': self.levels, 'project': self.no_projects} 
        self.df = pd.DataFrame(dict)

        # split the full name into name and surname and create new dataframe columns
        self.df[['name','surname']] = self.df['name_surname_combined'].str.split(' ', expand=True)
        
    def explode_column_project(self):
        # replace the number of projects with the actual project name(s) from the given list 
        # sample without replacement and use the explode function to create a row for every project that 
        # a person is involved
        self.df.project = self.df.project.apply(lambda x: random.sample(self.PROJECTS, x))
        self.df = self.df.explode('project')   

    def save_final_df_to_csv(self):
        # change the column order and save the final dataframe
        self.df = self.df[['name', 'surname', 'name_surname_combined', 'country_code', 'level', 'project']].reset_index()

        self.df.to_csv('report.csv', index=False)     

def main():
    info = GenerateRandomInfo()
    info.generate_full_names()
    info.generate_countries()
    info.generate_levels()
    info.generate_projects()
    info.create_df_split_full_name()
    info.explode_column_project()
    info.save_final_df_to_csv()


if __name__ == "__main__":
    main()