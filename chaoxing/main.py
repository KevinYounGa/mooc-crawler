
import requests
import re
import sys



urlInit = 'https://mooc1.chaoxing.com/course/{{courseId}}.html'


def __getKnowledgeIds(courseId,cookies):
        # 组装初始URL，获取第一个包含knowledge
        url = urlInit.replace('{{courseId}}', courseId)
        header = {
                'Upgrade-Insecure-Requests':'1',
                'Host': 'mooc1.chaoxing.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
                'Content-Type': 'application/json',
                'Cookie':cookies
            }
        htmls = requests.get(url, headers=header)
        # print('htmls---')
        # print(htmls.text)
        re_rule = 'courseId='+courseId+'&knowledgeId=(.*)">'
        url_frist = re.findall(re_rule, htmls.text)
        # print('url_frist---')
        # print(url_frist)
        if len(url_frist) > 0:
            return url_frist
        else:
            print('courseId错误！')


        
        



from ChaoXing.getCourseInfo import getPartInfo
from ChaoXing.getCourseInfo import getVideoInfo
from ChaoXing.buildData import buildRequset
from ChaoXing.login import getCookies
from Utils.TimeUtils import getTimeStampMilliSecond
import requests
import json






# time_start = getTimeStampMilliSecond()


# # 登录太赶就没写了，大家可以自己完善




# # step3 获取视频信息
# knowledgeIds = __getKnowledgeIds('200892785',COOK) 
# print('knowledgeIds')
# print(knowledgeIds)
# vDatas = []
# if len(knowledgeIds) > 0:
#     for kid in knowledgeIds:
#         # step1 获取章节信息
#         detail,default = getPartInfo('0','200892785','116491573',COOK)

#         # step2 获取任务信息
#         task = detail[0] # 测试第一个任务
#         # if(task['isPassed'] == False):
#         #     print("任务状态：当前任务未完成")
#         # else:
#         #     print("任务状态：当前任务已是完成状态")
#         #     exit()
#         vData = getVideoInfo(task['objectId'],COOK)
#         print('vData---------')
#         print(vData)
#         dtime = int(vData['duration'])
#         vDatas.append(vData)

#         # step4 构造参数
#         params = {
#             'reportUrl':default['reportUrl'],
#             'token':vData['dtoken'],
#             'cId':default['clazzId'],
#             'pTime':dtime,
#             'dTime':dtime,
#             'cTime':'0_{}'.format(dtime),
#             'objId':task['objectId'],
#             'info':task['otherInfo'],
#             'jId':task['jobid'],
#             'uId':default['userid']
#         }

#         reqData = buildRequset( **params,cookies = COOK)

#         print('reqData---------')
#         print(reqData)
#         print('reqData url---------')
#         print(reqData['url'])
#         print('reqData headers---------')
#         print(reqData['headers'])
#         # 发送请求
#         res = requests.get(url=reqData['url'],headers =  reqData['headers'])
#         try:
#             print('res---------')
#             print(res)
#             if res.status_code == 200:
#                 res = json.loads(res.text)
#                 if res['isPassed'] == True:
#                     print("任务完成")
#                 else:
#                     print("任务失败")
#             else:
#                 print("任务失败")
#         except:
#             raise Exception("失败")

#         time_end = getTimeStampMilliSecond()
#         print("消耗时间:{} 秒".format((time_end - time_start)/1000))

# print('vDatas')
# print(vDatas)

def getChaoXingCourse(username,password,courseId):
    # print("username1")
    # print(username)
    # print("password1")
    # print(password)
    # print("courseId1")
    # print(courseId)
    # courseId = '200892785'
    # print("username2")
    # print(username)
    # print("password2")
    # print(password)
    # print("courseId2")
    # print(courseId)
    #time_start = getTimeStampMilliSecond()
    # 登录太赶就没写了，大家可以自己完善
    COOK = getCookies(username,password)

    # step3 获取视频信息
    knowledgeIds = __getKnowledgeIds(courseId,COOK) 
    # print('knowledgeIds')
    # print(knowledgeIds)
    vDatas = []
    if len(knowledgeIds) > 0:
        for kid in knowledgeIds:
            # step1 获取章节信息
            # print('kid')
            # print(kid)
            #116491572  116491573
            detail,default = getPartInfo('0',courseId,kid,COOK)
            # print('detail')
            # print(detail)
            if detail:
                # step2 获取任务信息
                #task = detail[0] # 测试第一个任务
                # if(task['isPassed'] == False):
                #     print("任务状态：当前任务未完成")
                # else:
                #     print("任务状态：当前任务已是完成状态")
                #     exit()
                for task in detail:
                    vData = getVideoInfo(task['objectId'],COOK)
                    # print('vData---------')
                    # print(vData)
                    dtime = int(vData['duration'])
                    vDatas.append(vData)

                    # step4 构造参数
                    params = {
                        'reportUrl':default['reportUrl'],
                        'token':vData['dtoken'],
                        'cId':default['clazzId'],
                        'pTime':dtime,
                        'dTime':dtime,
                        'cTime':'0_{}'.format(dtime),
                        'objId':task['objectId'],
                        'info':task['otherInfo'],
                        'jId':task['jobid'],
                        'uId':default['userid']
                    }

                    reqData = buildRequset( **params,cookies = COOK)
                

                # print('reqData---------')
                # print(reqData)
                # print('reqData url---------')
                # print(reqData['url'])
                # print('reqData headers---------')
                # print(reqData['headers'])
                # 发送请求
                # res = requests.get(url=reqData['url'],headers =  reqData['headers'])
                # try:
                #     print('res---------')
                #     print(res)
                #     if res.status_code == 200:
                #         res = json.loads(res.text)
                #         if res['isPassed'] == True:
                #             print("任务完成")
                #         else:
                #             print("任务失败")
                #     else:
                #         print("任务失败")
                # except:
                #     raise Exception("失败")

                #time_end = getTimeStampMilliSecond()
                #print("消耗时间:{} 秒".format((time_end - time_start)/1000))
            

    # print('vDatas')
    # print(vDatas)
    return vDatas



if __name__ == '__main__':
    # for i in range(1, len(sys.argv)):
    #     print(sys.argv[i])
    username = sys.argv[1].replace("'","")
    password = sys.argv[2].replace("'","")
    courseId = sys.argv[3].replace("'","")
    # print("username")
    # print(username)
    # print("password")
    # print(password)
    # print("courseId")
    # print(courseId)
    result = getChaoXingCourse(username,password,courseId)
    print(result)


