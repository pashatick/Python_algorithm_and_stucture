import hashlib


a = input('Введи строку для поиска')
sub_st_len = int(input('Укажите длинну искомых подстрок'))


def find_sb_str(st, sub_st_len):
	hash_list = []	    
	for i in range(len(st) - sub_st_len + 1):
		hash_list.append(hashlib.sha1(st[i:i+sub_st_len].encode('utf-8')).hexdigest())

	return len(set(hash_list)) 

print('Количество уникальных подстрок в заданной строке - ', find_sb_str(a, sub_st_len))

