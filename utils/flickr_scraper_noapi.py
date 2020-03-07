import urllib.request

import numpy as np

fp = urllib.request.urlopen(
    "https://www.flickr.com/search?text=flowers&structured=yes&page=2")

str = fp.read().decode("utf8")  # print(str)
fp.close()

# res = [i for i in range(len(str)) if str.startswith('//live.staticflickr.com/', i)]
# print(len(res))
# for i in res:
#     s = 'https:' + str[i:i+80].split(')')[0]
#     print(s)

res = [i for i in range(len(str)) if str.startswith('_b.jpg', i)]
a = []
for i in res:
    s = 'https://' + str[i - 70:i + 6].replace('\\', '').split('//')[-1]
    a.append(s)
a = list(np.unique(np.array(a)))
print(len(a), a)
