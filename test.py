# coding=utf-8

from nlpir.summary import LJSummary
from nlpir.sentiment_analysis import LJSentimentAnalysis
from nlpir.doc_extractor import DocExtractor
from nlpir.key_extract import KeyExtract
from nlpir.nlpir_ictclas import NLPIR

content = """
图为华盛负责的5个车站主体工程之一的大庆车站。（图片来源：台湾《中国时报》）
中国台湾网12月15日讯据台湾《中国时报》报道，承包台中铁路高架化工程的华盛工程公司，为免工程延宕遭罚，去年7月间竟涉嫌教唆黑道掳走交通部门女官员强拍裸照，威逼“不要多管闲事”，事后女官员改调单位。台中地检署昨（14日）将涉嫌掳人拍照的华盛董事长特助苏晓贞、新竹建商卢银龙与警察郭志峰等人，依妨害自由、恐吓与泄密等罪起诉。
检方查出工程延误弊端，将“铁改局”段长林铭益、帮工程司任景成、工程员戴群峰与中兴工程副理张文亮、监造梁哲诚、华盛工地主任林瑛璟，依图利罪、伪造文书等罪起诉。起诉指出，华盛公司2012年6月，以10亿余元（新台币，下同）的标价承揽台中都会区铁路高架捷运计划“531标工程”，包含松竹、太原、精武与五权、大庆共5个车站的主体工程，合约规定依不同施工项目及里程碑，订有4个施工期限，但华盛因工班不足等因素，无法于前年8月完成第1阶段月台工程。
台“交通部铁路改建工程局”内部对是否对华盛开罚有争议，“中工处”第二工程段段长林铭益等主张，应等到工程总完工期限到期，再一并计算是否有延宕、应否开罚；但被害女官员认为，合约既明订4阶段施工期限，就应每阶段分开处理，力主“依法开罚”。华盛担心被罚，去年7月间，眼看“531标”各车站主体工程完工期限将届，华盛董事长特助苏晓贞涉嫌透过建商卢银龙找人跟监女官员长达10天，原想偷拍她跷班与另名同事婚外情，再向媒体爆料，以逼女官员离职。
卢银龙透过新竹警员郭志峰调查女官员个资，发现她未婚，且交往对象丧偶，没有婚外情，改找男子周承广，指派陈姓、彭姓及黄姓小弟（已死亡），趁着女主管准备上班、在宿舍外将她掳至新竹火葬场旁工寮强拍裸照、威吓“叫你好好工作，不要多管闲事”后，丢包在桃园杨梅交流道附近。
饱受惊吓的女官员不愿报警，隔日即调离职位，去年9月间，台中地检署接获检举开始追查，意外发现该工程相关文件上记载“已如期完工”，深入调查再发现“铁改局中工处”与中兴工程监工人员涉嫌包庇华盛伪造不实完工日期，图利华盛免罚违约金3300多万元。
检方昨天侦结，将林铭益、任景成、戴群峰与涉拍裸照的苏晓贞、卢银龙与周姓、陈姓、彭姓小弟等12人起诉。“531标”工程的大庆、太原车站已于今年10月16日第一阶段通车启用，松竹、精武及五权车站，目前正进行第二阶段作业。
“中工处”公关张伸嘉表示，全案已进入司法程序，“铁改局”尊重检调，全力配合调查。“531标”工程整个标案的工期是到2018年底完工，业者执行是否逾期，有认知上的差异。对传出有女主管被黑道掳走，并强拍裸照，内部员工指出“相当震撼”
华盛则发出声明强调，施工进度正常，与女官员间无业务往来或私谊、嫌隙，且工期延展审查非女官员业务范围，且女官员遭侵犯为去年7月，但工程展延工期申请程序已于2013年9月核定，检方起诉有诸多严重错误与不实，对检调单位杜撰故事、草率结案，感到遗憾。（中国台湾网 卢佳静）
责任编辑：向昌明 SN123
文章关键词： 恐吓 台湾
我要反馈 保存网页
"""

key_extract = KeyExtract()
key_extract.open()
print u"========== 关键词组件 =========="
r = key_extract.get_keywords(content)
for key in r:
    print key
key_extract.close()

summary = LJSummary()
summary.open()
print u"========== 摘要组件 =========="
print summary.single_doc(content)
summary.close()

nlpir = NLPIR()
nlpir.open()
print u"========== 分词组件 =========="
r = nlpir.segment(content, pos_english=False)
for word, pos in r:
    print word, pos
nlpir.close()

sentiment_analysis = LJSentimentAnalysis()
sentiment_analysis.open()
r = sentiment_analysis.get_result(content)
print u"========== 情感分析组件 =========="
for k, v in r.items():
    print k, ": ", v
sentiment_analysis.close()

doc_extractor = DocExtractor()
doc_extractor.open()
print u"========== 情感倾向分析组件 =========="
print doc_extractor.get_sentiment_value(content)
doc_extractor.close()
