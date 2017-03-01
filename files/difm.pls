[playlist]
Version=2
NumberOfEntries={{ entries | count }}
{% for entry in entries | sort(attribute='title') %}
File{{ loop.index * 2 - 1 }}=http://prem3.di.fm:80/{{ entry.name }}?{{ lookup('secret', keys.difm) -}}
Title{{ loop.index * 2 - 1 }}={{ entry.title }} (192)
Length{{ loop.index * 2 - 1 }}=-1
File{{ loop.index * 2 }}=http://prem3.di.fm:80/{{ entry.name }}_hi?{{ lookup('secret', keys.difm) -}}
Title{{ loop.index * 2 }}={{ entry.title }} (320)
Length{{ loop.index * 2 }}=-1
{% endfor %}
