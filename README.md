# Big Box Challenge
By: Carabajal, Félix Humberto  
Email: felixhumbertocarabajal@gmail.com, felixhumbertocarabajal5@gmail.com  

## Quick start
### Installing this repo with git:
```console
foo@bar:~$ git clone https://github.com/InfinityLoopA-Z/BigBoxChallenge.git
```
Go inside downloaded repo and running poetry to install dependences
```console
foo@bar:~$ poetry install
```
### Create migrations:
```console
foo@bar:~$ python manage.py makemigrations
```
### Create relation in DB:
```console
foo@bar:~$ python manage.py migrate
```
### Running Server:
```console
foo@bar:~$ python manage.py runserver
```



## Readme inside challenge
Ejemplo de url Box

- http://127.0.0.1:8000/api/boxes/
- http://127.0.0.1:8000/api/boxes/cover-people-sell/

Ejemplo del Serializer Box

```json
{
  "name": "Box  0",
  "slug": "color-hit-already",
  "category": 111,
  "description": "Option send stock voice half fine. Term her present determine series. Politics difficult make room sport. Loss cultural green end beautiful everybody available every. Though white me majority agreement worry.",
  "purchase_available": false,
  "price": "7308.28",
  "boximage_set": [
    {
      "id": 417,
      "order": 8,
      "upload": "https://placeimg.com/600/600/tech"
    },
    {
      "id": 418,
      "order": 3,
      "upload": "https://placeimg.com/600/600/tech"
    }
  ]
}
```

Ejemplo de url Activity

- http://127.0.0.1:8000/api/activities/
- http://127.0.0.1:8000/api/activities/?box_slug=color-hit-already
- http://127.0.0.1:8000/api/activities/?category_id=111
- http://127.0.0.1:8000/api/activities/?reason_id=94
- http://127.0.0.1:8000/api/activities/&limit=20&offset=2
- http://127.0.0.1:8000/api/activities/?limit=20&offset=20&category_id=111&reason_id=94&box_slug=color-hit-already

Ejemplo del Serializer Activity

```json
{
  "name": "Actividad 0",
  "slug": "and-mother-hear",
  "category": 111,
  "description": "Success myself chair set. Raise live sign practice stay. Eye wrong give argue know push. Quickly gun special speak service success. Cold role enjoy at describe.",
  "purchase_available": false,
  "reasons": [
    {
      "name": "Razon 0",
      "order": 3,
      "slug": "step-share-increase"
    },
    {
      "order": 3,
      "name": "Razon 8",
      "slug": "well-ago"
    }
  ],
  "activityimage_set": [
    {
      "id": 8102,
      "order": 3,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8103,
      "order": 8,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8104,
      "order": 4,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8105,
      "order": 1,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8106,
      "order": 2,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8107,
      "order": 5,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8108,
      "order": 3,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8109,
      "order": 10,
      "upload": "https://placeimg.com/600/600/arch"
    },
    {
      "id": 8110,
      "order": 10,
      "upload": "https://placeimg.com/600/600/arch"
    }
  ]
}
```

Ejemplo de las url Category

- http://127.0.0.1:8000/api/category/
- http://127.0.0.1:8000/api/category/focus-meeting-art/

Ejemplo del Serializer Category

```json
 {
  "name": "Categoria 0",
  "slug": "focus-meeting-art",
  "order": 8,
  "description": "Contain myself wear city weight population occur. Close effort four analysis. Hundred back top age physical office entire. Sound general democratic speak. Stay own important chair significant assume.",
  "box_set": [
    {
      "name": "Box  0",
      "slug": "color-hit-already",
      "price": "7308.28"
    }
  ]
}
 ```
