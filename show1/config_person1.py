# 输入自己的token
token = ''
# 项目id，必填
show_id = '6438d4bbdbb44f0001ef5a06' # 周杰伦

# 指定场次id，不指定则默认从第一场开始遍历
session_id = '6438d4e2532bff0001072d8d' # 周四
# session_id = '6438d4e2532bff0001072d8f' # 周五
# session_id = '6438d4e2532bff0001072d91' # 周六
# session_id = '6438d4e2532bff0001072d93' # 周日

# 指定价格, 不指定则默认价格不限
# https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v3/show/6438d4bbdbb44f0001ef5a06/show_session/6438d4e2532bff0001072d8d/seat_plans_from_marketing_countdown?src=WEB&channelId=&terminalSrc=WEB
seat_plan_id=''
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 2
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0,1]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
