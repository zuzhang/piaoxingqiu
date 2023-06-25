# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkMsKwjAQRf9l1l0kMY_apaIoKILYhSuJzRQLNZE0FVH676ZUxZUuZzhn7mUe4HQbTktbOshsW9cJtA36YX7AsbpPnUHIYL5YHdaQQNMeJ5-lZFLplCAaRlPBmUplSfmYRy6aW1f30CTfz7Zxcw5F3p82vcjHI8qpIcKokhFCKEqhBQ7iH0wS6BLA26XyuKvO-C4ezc0FvQ7uZ0gZQwqPOrxkKlMlIysUlyLWRF-ctA3fL4lZA6cEHQmVwBV9UzkLGRv-ZfW7RvcEAAD__w.TlOsS9qADyGBPKkSMyORJOJLi06r1nNtJHalRVckjzL3WBp9HYZfglEHmspjdLgy_JNKKSw0A6txuQ0NEEu9fZRtODQtD-DfTAuqEXTHTOZAUqglaijtbUJCfwPVqYEXUE6yLbbGtY4wixr2qZmnpJmX3wqTb2oJ1VmtNkzO81s'
# 项目id，必填
# 伍佰
show_id = '646de1fe243ede0001b49e35'

# 指定场次id，不指定则默认从第一场开始遍历
session_id = ''  # 伍佰

# 指定价格, 不指定则默认价格不限
seat_plan_id=''
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 1
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
