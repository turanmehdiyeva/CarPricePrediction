def get_car_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find('div', class_='product-properties-container')
    info_rows = info.find_all('li')
    
    car_info={}
    for index, row in enumerate(info_rows):
        try:
            content_key = row.find('label').get_text()
            content_value = row.find('div', class_ ='product-properties-value' ).get_text()
            car_info[content_key] = content_value
        except:
            continue
    return car_info
    
base_path = 'https://turbo.az/'
car_info_list = []
lst = []
link_list = []

for j in range(1,35):
    url = 'https://turbo.az/autos?page={}'.format(j)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cars = soup.select('.products a')
    for i in cars:
        lst.append(i['href'])


for i in lst:
    if i.startswith('/autos')==True and i.endswith('bookmarks')==False:
        link_list.append(base_path+i)
    
for i in link_list:
    try:
        car_info_list.append(get_car_info(i))
    except:
        continue
     

import json

def save_data(title,data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
        
def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)
      
save_data('turbo_az.json', car_info_list)
car_data = load_data('turbo_az.json')
