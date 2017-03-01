[playlist]
Version=2
NumberOfEntries={{ entries | count }}
{% for entry in entries %}
File{{ loop.index }}=http://prem3.di.fm:80/{{ entry.name }}?{{ lookup('secret', keys.difm) -}}
Title{{ loop.index }}={{ entry.title }}
Length{{ loop.index}}=-1
{% endfor %}
