import wikipedia as w
from wikipedia.exceptions import WikipediaException
print(w.languages())
w.set_lang('hi')
res=w.summary("papaya",)
final=""
try:
    res_crop=w.summary('Papaya')
except:
    res_crop=""
final=res
if res_crop:
    final=final+"\n"+res_crop

print(final)