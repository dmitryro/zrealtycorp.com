{% extends 'base.html' %}

{% load pagination_tags %}

{% block title %}Latest Published Properties{% endblock %}

{% block content %}



<ul>
   <li>
      <a href="{% url 'socialauth_begin' 'google-oauth2' %}">Login with Google</a>
   </li>
   <li>
      <a href="{% url 'socialauth_begin' 'facebook' %}">Login with Facebook</a>
   </li>
   <li>
      <a href="{% url 'socialauth_begin' 'twitter' %}">Login with Twitter</a>
   </li>
</ul>
{% autopaginate front_properties 10 %}
{% if front_properties %}
   <div>
     <div style="float:left;width:5%;">
        ID
     </div>
     <div style="float:left;width:12%;">
        Property
     </div>
     <div style="float:left;width:10%;">
        Type
     </div>

     <div style="float:left;width:6%;">
        Rooms
     </div>

     <div style="float:left;width:7%;">
        Size
     </div>

     <div style="float:left;width:7%;">
        Cateogry
     </div>

    <div style="float:left;width:7%;">
        Price
    </div>

    <div style="float:left;width:18%;">
        Location
    </div>
    <div style="clear:both;"></div>
   </div>
  <div>
   {% for property in front_properties %}
      
    <div style="float:top;width:100%;">
           <div style="float:left;width:5%;">
                 {{ property.property_id}}
           </div>
           <div style="float:left;width:12%;">
                 {{ property.title }}
           </div>
           <div style="float:left;width:10%;">
                 {{ property.type }}
           </div>

           <div style="float:left;width:6%;">
                 {{ property.rooms }}
           </div>

           <div style="float:left;width:7%;">
                 {{ property.size }}
           </div>
     
           <div style="float:left;width:7%;">
                 {{ property.category }}
           </div>

           <div style="float:left;width:7%;">
                 {{ property.price }}
           </div>
           <div style="float:left;width:18%;">
                 {{ property.borough }}&nbsp;/&nbsp;{{ property.neighborhood }}
           </div>
           <div style="clear:both;"></div>
      </div>
   {% endfor %}
   </div>
{% else %}
    <p>No properties were found.</p>
{% endif %}

{% paginate %}

{% endblock %}


