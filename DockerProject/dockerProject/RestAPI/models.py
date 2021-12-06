from django.db import models
import pandas as pd
import os

class Game(models.Model):
    rank = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    platform = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True)
    publisher = models.CharField(max_length=100, null=True)
    NA_Sales = models.FloatField()
    EU_Sales = models.FloatField()
    JP_Sales = models.FloatField()
    Other_Sales = models.FloatField()
    Global_Sales = models.FloatField()

    def __str__(self):
        return self.name

'''
def addInstance():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'data.csv')
    df = pd.read_csv(file_path)
    for i in range(0, len(df)):
        data = df.iloc[i, :]
        if(str(data['Year']).isnumeric()):
            game = Game(rank=data['Rank'], name=data['Name'], platform=data['Platform'],
                        year=data['Year'], genre=data['Genre'], publisher=data['Publisher'],
                        NA_Sales=data['NA_Sales'], EU_Sales=data['EU_Sales'], JP_Sales=data['JP_Sales'],
                        Other_Sales=data['Other_Sales'], Global_Sales=data['Global_Sales'])
            game.save()
        else:
            game = Game(rank=data['Rank'], name=data['Name'], platform=data['Platform'],
                        year=None, genre=data['Genre'], publisher=data['Publisher'],
                        NA_Sales=data['NA_Sales'], EU_Sales=data['EU_Sales'], JP_Sales=data['JP_Sales'],
                        Other_Sales=data['Other_Sales'], Global_Sales=data['Global_Sales'])
            game.save()

addInstance()
'''