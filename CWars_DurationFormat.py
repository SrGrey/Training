'''My solution'''
def format_duration(seconds):
    mapper = {}
    result = ''
    mapper['years'] = seconds // 31536000
    months = seconds % 31536000 // 2592000
    mapper['days'] = seconds % 31536000 % 2592000 // 86400 + months * 30
    mapper['hours'] = seconds % 31536000 % 2592000 % 86400 // 3600
    mapper['minutes'] = seconds % 31536000 % 2592000 % 86400 % 3600 // 60
    mapper['seconds'] = seconds % 31536000 % 2592000 % 86400 % 3600 % 60
    separator = ''
    for key in mapper:
        if result != '':
            separator = ', '
        if mapper[key] == 1:
            result += f'{separator}{mapper[key]} {key[:-1]}'
        elif mapper[key] != 0:
            result += f'{separator}{mapper[key]} {key}'
    if result.rfind(',') != -1:
        result = result[:result.rfind(',')] + ' and' + result[result.rfind(',') + 1:]
    elif result == '':
        return 'now'
    return result


print(
format_duration(0),
format_duration(1),
format_duration(62),
format_duration(120),
format_duration(3600),
format_duration(3662), sep='\n')


'''Other intresting solution'''
# times = [("year", 365 * 24 * 60 * 60),
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]
#
# def format_duration(seconds):
#
#     if not seconds:
#         return "now"
#
#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)
#
#         seconds = seconds % secs
#
#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
