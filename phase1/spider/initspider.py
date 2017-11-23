import os
import json
import ast
import collections
import tldextract


# allowed_domains = ['nytimes.com', 'bloomberg.com']
# start_urls = ['http://nytimes.com/', 'http://bloomberg.com']

# file = open('spider/spiders/runner.py', 'r').readlines()

# file[6] = str('    allowed_domains = {}\n'.format(str(allowed_domains)))
# file[7] = str('    start_urls = {}\n'.format(str(start_urls)))

# write = open('spider/spiders/runner.py', 'w')
# write.writelines(file)

# print(os.getcwd())
# os.system('scrapy runspider spider/spiders/runner.py -o outputs.json')

output = open('output.json', 'r').read()
output = json.loads(output)
#output = ast.literal_eval(output)
#print(len(output))

per_website = collections.defaultdict(lambda: {'num_alt': 0, 'num_imgs': 0})
seen = collections.defaultdict(set)
result = {}

for item in output:
	extracted = tldextract.extract(item['page'])
	domain = extracted.domain
	if item['src'] not in seen[domain]:
		per_website[domain]['num_alt'] += int(item['has_alt'])
		per_website[domain]['num_imgs'] += 1
		seen[domain].add(item['src'])

for website in per_website:
	result[website] = float(per_website[website]['num_alt']) / per_website[website]['num_imgs']

print(per_website)
print(result)