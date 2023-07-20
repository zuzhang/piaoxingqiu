# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkM1qwzAQhN9lzz5IsqwfHxNSGkgohOTQU1GsNTHYUpDl0Dbk3SOjpvTUHHeYb2dnr-DNFE9r13qo3dT3BUwjhjxf4dh9L71FqOHldfOxhQLG6bj4FQUT0iiCaBlVFWdSiZZyzZMvkTvfz6bF4X21S8oQm8O82s4g1yXl1JLKypYRQiiKylSYwSc2QeBWAH6eu4D7bsDH4Yl8O2Mw0f8b0qaQJqCJPzAVSisqS6YFFang1xhxyAXz3gFDczIu_n1SSs-kJqVkuoALhrHzDmqeP-jM47DbHQAA__8.M1ZqShqRtPP_F3ACLXYhJpDjwFyxwNPYP5Uq2QoaI2LyjjdbM4wMC1DHkTWbgEJPjilUIawfWcX0v-dDPCKnK8LM2P6eyrEjKUkMPXfE_cbBOKmPHBai1ZOMH4-2bl8c0-hZHl5mkQqIhd_abkM9dwdJmKohFPyMjVFoHHP24Vo'
# 项目id，必填
# 伍佰
show_id = '6438d4bbdbb44f0001ef5a06'

# 指定场次id，不指定则默认从第一场开始遍历
session_id = ''  # 伍佰

# 指定价格, 不指定则默认价格不限
seat_plan_id=''
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 2
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0,1]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
