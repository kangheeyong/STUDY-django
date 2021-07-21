# STUDY-django

### command

- `django-admin`
  - make new project: `django-addmin startproject {proejct name}`
  - make new app: `python manage.py startapp {app name}`
  - migration
    - `python manage.py makemigrations {app name}`: migration 파일을 만듬
    - `python manage.py sqlmigrate {app name} {number}`: 명령어 확인
    - `python manage.py migrate`: 적용

### documents

- [template grammer](https://docs.djangoproject.com/en/3.2/ref/templates/language/)
- [forms doc](https://docs.djangoproject.com/en/3.2/topics/forms/)

### know-how

- setting 분리: https://whatisthenext.tistory.com/125
- middleware([reperence](https://www.youtube.com/watch?v=JSEoK0pMVbc))
  - audit & remove unnecessary middleware
  - use
    - Canditional GET middleware
    - GzipMiddleware
    - Cache Sessions
- FE frameworks
  - [bootstrap](https://getbootstrap.com), [Foundation](https://get.foundation), [Gestalt](https://pinterest.github.io/gestalt/#/), [Ant Design](https://ant.design), [Atlas Kit](https://atlaskit.atlassian.com/)

## todo-study
- form <-> models
- django Signals setting?
- html form tag에서 GET and POST
### todo

- How to Build an E-commerce Website with Django and Python: https://www.youtube.com/watch?v=YZvRrldjf1Y
- Python Microservices Web App (with React, Django, Flask) - Full Course: https://www.youtube.com/watch?v=0iB5IPoTDts
