# -*-coding:utf-8-*-
"""
@author:Mark
@file: baidu_nlp_try.py 
@time: 2018/05/30
"""
import sys

reload(sys)

from aip import AipNlp

u""" 你的 APPID AK SK """
APP_ID = '11320699'
API_KEY = 'EnQGDVOVcrLmjpNIV3HXuSzP'
SECRET_KEY = 'OBpuMvlL2ygTlXL5iUdZcH628x4PrGc9 '

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = """
让人工智能成为强大动能 　　 近日，百度与中国长城宣布协力构建国内首家“软硬创”三位一体人工智能平台，为传统智慧城市提供一揽子解决方案，促进行业转型升级。 　　 此前，在腾讯AI Lab(人工智能实验室)第二届学术论坛上，腾讯发布其在人工智能方面的三大战略方向：打造通用AI(人工智能)之路；成立机器人实验室；聚焦“AI+医疗”战略，探索落地场景…… 　　 从连续两次写入政府工作报告，到业内积极部署推进智能产业，“人工智能”无疑已经成为当下热门话题。我们将迎来怎样的智能生活，人工智能和实体经济如何深度融合，哪些发展瓶颈亟待突破，都值得思考。 　　“人工智能让城市变得更聪明” 　　 阿里巴巴的人工智能设计师“鲁班”，去年双11购物节期间，针对不同消费者自主设计了4.1亿张商品海报。 　　 京东配送机器人，会自行拐弯，规避路障，礼让行人，一切操作自动完成。 　　 小偷打碎玻璃时，智能摄像机就能自动拍下小偷照片，并传送到用户手机，为破案提供重要证据。 　　 患者做完心电图，智能系统直接给出初步分析报告，同时提醒需要注意的数值事项，辅助医生做诊断。 　　 …… 　　 发展智能产业，拓展智能生活，政府工作报告描绘的蓝图正在逐步成为现实。 　　 “党的十八大以来，我国人工智能技术迅勐发展，获得重要进展的人工智能应用，都是与对应行业、产品或服务相结合的，服务用户、服务大众是技术发展的必然结果。从长期看，人工智能作为未来提高生产力的关键技术，其发展会是一个螺旋上升的过程。”360集团董事长兼首席执行官周鸿祎表示。 　　 “从基础的预约挂号、获取检查结果，到手术机器人、远程智能诊治等新手段的运用，人工智能技术正逐渐运用在医疗行业方方面面。”北京大学党委副书记、医学部党委书记刘玉村指出，人工智能技术一定程度上改善了群众的看病就医环境，给患者带来便利的同时也提高了就医效率，缓解了公共资源的压力。 　　 “如今，居民电梯也有了‘黑匣子’，事故率下降了50%。”中新天津生态城管理委员会副主任罗家均告诉记者，生态城美林园小区目前安装了54台智慧电梯，用户扫描电梯轿厢二维码，就能了解电梯维保信息；电梯“黑匣子”实现全天候运行监控，乘梯人一旦被困，可立即通过4G高清摄像头与救援人员对话。 　　 “人工智能技术的飞速发展，让城市变得更聪明”，罗家均深有感触，“收垃圾、预约家庭医生、掌握区内交通状况、远程控制智能家电……生态城的居民通过网站和手机APP，足不出户便可享受30项社区智慧生活服务；智慧网厅、智慧大厅也实现了互联网和电子政府的融合。” 　　“新技术也在创造新的就业岗位” 　　 火灾现场，消防员的“逆火而行”令人动容。危险的作业一线，能否不用人工？答案是，行！ 　　 “中信重工的特种消防机器人可实现准确到位，代替消防救援人员实施无人灭火。”中信重工机械股份有限公司董事长俞章法自豪地说。 　　 “人工智能的生命在于应用。”俞章法说，通过运用“机器逆学习算法”，中信重工还研制了防爆轮式巡检机器人、国内首台铁路列检机器人、综合管廊机器人、水下机器人、水泥码垛机器人、高压水射流机器人……2017年中信重工机器人及智能装备产业板块营业额突破10亿元人民币，真正实现了“传统动能+新动能”双轮驱动。 　　 会包边，能上件，会焊接，能涂胶……在东风柳汽柳东乘用车基地，一排橘黄色的“机械手”自动运转，冲压、焊接、涂装、总装四大工艺及配套设施，全部实现了机器人自动化作业。 　　 “目前柳州市工业机器人存量近4000台，并以每年1000台的增量递增。”广西柳州市市长吴炜说，2017年引导社会固定资产在工业机器人方面投资3.6亿元，为企业降低成本30%，节约人工40%，提高效率30%。 　　 借助人工智能技术，不仅在工业上实现了“黑灯工厂”，农业也能自动化。 　　 “这条生产线，由全自动播种线、补苗设备、移栽机、跳移机、喷灌机等组成，实现了种苗全自动快速繁育，大幅提升了生产效率。”谈起自家的“植物工厂”，内蒙古蒙草生态环境(集团)股份有限公司董事长王召明脸上写满了兴奋。 　　 “发展智慧农业，需要构建大数据平台。”王召明建议国家出台政策，支持有能力的农业企业构建生态大数据平台，运用卫星遥感、大数据、人工智能等技术，集成水、土、空气、微生物等多种数据。“该浇多少水、该施什么肥，让农民一目了然，再运用互联网实现一键操作。” 　　 智能制造、机器人、高档数控机床和其他新兴技术的兴起，会不会造成失业问题？ 　　 “新技术在冲击传统就业的同时，也在创造新的就业岗位。”中华全国总工会研究室主任吕国泉表示，技术革新将倒逼产业结构调整，创造新型就业机会。他建议抓住机遇，把促进“创业式就业”与发展“三新”更好结合起来，发展就业新形态，形成经济发展和扩大就业的联动效应。 　　“缺少重大原创成果困扰行业发展” 　　 当前，我国的人工智能产业成绩喜人，但也存在着诸多发展难题和障碍，亟待破解。 　　 业内人士纷纷表示，缺少重大原创成果、缺乏系统的超前研发布局、人工智能尖端人才远远不能满足需求、政策法规和标准体系欠缺，是困扰我国人工智能发展的难题，时代在呼唤体制机制改革创新。 　　 “政策与技术进步是否匹配，一定程度上决定了产业创新速度和竞争力。”百度公司董事长李彦宏建议国家出台政策，鼓励企业打造高水平人工智能开放平台；加快研究自动驾驶运营政策，尽快明确自动驾驶汽车运营的资质要求；提高自动驾驶领域网络安全和风险防范意识；推进智能化道路基础设施规划建设，打造支持自动驾驶汽车的新型城市交通环境。 　　 “目前的硬件特别是移动端或者物联网设备，很难满足人工智能算法需求，需进一步优化算法；当前人工智能技术的理论仍然不太完备，需要继续加强基础理论研究。”周鸿祎表示。 　　 “人才是第一资源，要吸引和培养人工智能高端人才和创新创业人才，支持一批领军人才和青年拔尖人才成长。”商务部电子商务和信息化司司长骞芳莉建议，支持加强人工智能相关学科专业建设，引导培养产业发展急需的技能型人才。 　　 “要形成人工智能产业发展的科研‘生态圈’，发挥整体竞争优势。”中科院合肥物质科学研究院先进制造技术研究所所长王容川建议，通过发展联盟、联合等方式，对现有从事人工智能研究的机构进行整合，并配套相关的整体研究规则。同时进一步促进大数据融合，打破信息壁垒，让各有侧重、单打独斗，转变为科学布局、互为支撑、发挥合力。 　　 “对于因人工智能产业发展可能带来的改变，立法上要有充分考虑。”王容川建议开展人工智能相关政策和法律法规研究，推动行业合理开放数据。充分考虑社会伦理问题，比如明确机器人有无社会属性、无人驾驶汽车交通事故的责任主体认定等。(本报记者李翔、庞革平、温素威、杨倩、靳博、史鹏飞、吴姗、许晴、孙振、李纵、张枨) 相关新闻 伪人工智能扎堆圈钱：2万元高费用培训班只是教编程2018-03-20 08:21 "智能+"时代，人工智能如何颠覆未来战争2018-01-02 11:07 责编：马晓春
"""

u""" 调用词法分析 """
while True:
    result = client.lexer(text)
