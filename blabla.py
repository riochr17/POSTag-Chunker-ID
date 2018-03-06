# import codecs
# import re

# r = re.compile(r"""\\(.)""") # Note the parethesis, that's a capturing group

# f = codecs.open('postagged.txt')
# lines = f.read().split('\n')
# f.close()

# emit = {}
# transition = {}
# context = {}

# for line in lines:
# 	fx_line = r.sub(r'\1', line)

# 	previous = "<s>"
# 	if previous in context:
# 		context[previous] += 1
# 	else:
# 		context[previous] = 0

# 	for word_tag in fx_line.split(" "):
# 		splitter_index = word_tag.rfind("/")
# 		word = word_tag[:splitter_index]
# 		tag  = word_tag[splitter_index + 1:]

# 		tr_idx = previous + " " + tag
# 		if tr_idx in transition:
# 			transition[tr_idx] += 1
# 		else:
# 			transition[tr_idx] = 0

# 		cx_idx = tag
# 		if cx_idx in context:
# 			context[cx_idx] += 1
# 		else:
# 			context[cx_idx] = 0

# 		em_idx = tag + " " + word
# 		if em_idx in emit:
# 			emit[em_idx] += 1
# 		else:
# 			emit[em_idx] = 0

# 		previous = tag

# 	tr_idx = previous + " " + "</s>"
# 	if tr_idx in transition:
# 		transition[tr_idx] += 1
# 	else:
# 		transition[tr_idx] = 0

# print transition