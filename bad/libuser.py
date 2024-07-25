{% extends "appbuilder/base.html" %}
{% import 'appbuilder/general/lib.html' as lib %}

{% block content %}
{{ lib.panel_begin(title) }}

{% block show_form %}
    {{ widgets.get('show')()|safe }}
{% endblock show_form %}

{% block related_views %}
    {% if related_views is defined %}
        {% for view in related_views %}
            {% call lib.accordion_tag(view.__class__.__name__,view.title, False) %}
                {{ widgets.get('related_views')[loop.index - 1](pk = pk)|safe }}
            {% endcall %}
        {% endfor %}
    {% endif %}
{% endblock related_views %}


{{ lib.panel_end() }}

{% endblock %}

{% block add_tail_js %}
<script src="{{url_for('appbuilder.static',filename='js/ab_keep_tab.js')}}" nonce="{{ baselib.get_nonce() }}"></script>
{% endblock %}
