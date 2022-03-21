import csv
class myra(object):
def __init__(self):
    self.myCsv = csv.writer(open('Item.csv', 'w+b', encoding='utf-8')
    self.myCsv.writerow(['author', 'tag', 'pagenumber','regra','archivename'])

    def process_item(self, item, spider):          
        self.myCsv.writerow([item['quote'], item['tag'], item['author']])
        return item