{% for item in secrets %}
	export "{{ item.var }}=$(comp-secret {{ item.key }})"
{% endfor %}

{% for key, value in env_vars.iteritems() %}
	export {{ key }}={{ value }}
{% endfor %}
