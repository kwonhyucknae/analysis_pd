#메인에서 사용
#파라미터화 했다
import os
#configuration
#딕셔너리 형태로 만듬
#startyear,servicekey 등 공통되는 부분
#common에 저장
CONFIG = {
    'district':'서울특별시',
    'countries':[('중국', 112), ('일본', 130), ('미국', 275)],
    'common':{
        #'service_key':'%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
        'start_year':2017,
        'end_year':2017,
        'fetch':True,
        'result_directory':'__results__/crawling'

    }


}



if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])
