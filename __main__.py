import collect
from config import CONFIG

if __name__ == '__main__':
    #collect
    collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common']   #CONFIG['common']['start_year'] 가 가장 무난 딕셔너리로 보내는데 하나로 보내고 싶다면
                             #딕셔너리 형태로 ?
        )

    for country in CONFIG['countries']:
            collect.crawling_foreign_visitor(country,  **CONFIG['common'])



    #analysis



    #visualize