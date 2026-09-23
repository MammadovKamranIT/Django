from django.middleware.csrf import get_token
from django.utils.html import escape

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls import reverse

from notes import data

# Create your views here.


def html_shell(title: str, body: str ) ->str:


    safe_title = escape(title)

    return f"""

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{safe_title}</title>

         <style>
        * {{
    box-sizing: border-box;
}}

::selection {{
    background: #111;
    color: #d8ff00;
}}

body {{
    margin: 0;
    min-height: 100vh;
    padding: 70px 8vw 100px;

    background:
        linear-gradient(rgba(0, 0, 0, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 0, 0, 0.035) 1px, transparent 1px),
        #f2f0e9;

    background-size: 24px 24px;

    color: #111;

    font-family:
        "Courier New",
        Courier,
        monospace;
}}


/* =========================
   ГЛАВНЫЙ ЗАГОЛОВОК
   ========================= */

h1 {{
    max-width: 950px;

    margin: 0 auto 45px;
    padding: 0 0 18px;

    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(42px, 7vw, 85px);
    font-weight: 900;

    line-height: 0.9;
    letter-spacing: -4px;
    text-transform: uppercase;

    border-bottom: 8px solid #111;
}}


/* Маленькая декоративная метка */

h1::before {{
    content: "KNOWLEDGE / HUB";
    display: block;

    margin-bottom: 18px;

    font-family: "Courier New", monospace;
    font-size: 12px;
    font-weight: normal;

    letter-spacing: 4px;

    color: #555;
}}


/* =========================
   ТЕКСТ
   ========================= */

body > p {{
    max-width: 950px;

    margin: 25px auto;

    font-size: 17px;
    line-height: 1.7;
}}

p {{
    line-height: 1.6;
}}


/* =========================
   ССЫЛКИ
   ========================= */

a {{
    color: #111;
    text-decoration: none;
    font-weight: 700;
}}

a:hover {{
    background: #d8ff00;
    color: #111;
}}


/* =========================
   СПИСОК
   ========================= */

ul {{
    max-width: 950px;

    margin: 50px auto 0;
    padding: 0;

    list-style: none;

    border-top: 5px solid #111;
}}


/* =========================
   ЗАМЕТКА
   ========================= */

li {{
    position: relative;

    margin: 0;
    padding: 28px 25px 28px 70px;

    border-bottom: 2px solid #111;

    transition:
        padding-left 0.15s ease,
        background 0.15s ease;
}}


/* Стрелка слева */

li::before {{
    content: "↳";

    position: absolute;

    left: 15px;
    top: 23px;

    font-size: 30px;
    font-weight: bold;
}}


/* Нестандартный hover */

li:hover {{
    padding-left: 85px;

    background: #d8ff00;
}}


/* Название заметки */

li a {{
    display: inline-block;

    font-family: Arial, Helvetica, sans-serif;

    font-size: clamp(24px, 4vw, 40px);
    font-weight: 900;

    letter-spacing: -1.5px;
    line-height: 1;

    text-transform: uppercase;
}}

li a:hover {{
    background: #111;
    color: #d8ff00;
}}


/* =========================
   CATEGORY / TAG
   ========================= */

small {{
    display: inline-block;

    margin-top: 12px;
    margin-right: 5px;

    padding: 4px 8px;

    background: #111;
    color: #f2f0e9;

    font-size: 11px;

    letter-spacing: 1px;
    text-transform: uppercase;
}}


/* =========================
   DETAIL PAGE
   ========================= */

body > p:not(:last-child) {{
    font-family: Georgia, serif;

    font-size: 21px;
    line-height: 1.8;
}}


/* Последняя ссылка — Return */

body > p:last-child a {{
    display: inline-block;

    margin-top: 35px;

    padding: 14px 20px;

    border: 3px solid #111;

    font-family: "Courier New", monospace;
    font-size: 14px;

    text-transform: uppercase;

    box-shadow: 6px 6px 0 #111;

    transition: 0.15s;
}}

body > p:last-child a:hover {{
    background: #d8ff00;

    transform: translate(3px, 3px);

    box-shadow: 3px 3px 0 #111;
}}


/* =========================
   MOBILE
   ========================= */

@media (max-width: 600px) {{

    body {{
        padding: 40px 20px 70px;
    }}

    h1 {{
        font-size: 44px;
        letter-spacing: -2px;
    }}

    li {{
        padding-left: 50px;
    }}

    li:hover {{
        padding-left: 55px;
    }}

    li::before {{
        left: 8px;
    }}
}}

/* =========================
   FORM
   ========================= */

form {{
    max-width: 950px;
    margin: 0 auto;

    padding: 0;

    font-family: "Courier New", Courier, monospace;
}}


/* Заголовок внутри формы */

form h1 {{
    margin-bottom: 50px;
}}


/* Каждый блок формы */

form p {{
    margin: 0 0 20px;
}}


/* =========================
   LABEL
   ========================= */

form label {{
    display: inline-block;

    margin-bottom: 4px;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 2px;
    text-transform: uppercase;
}}


/* Добавляем декоративный символ */

form label::before {{
    content: "→ ";
    color: #111;
}}


/* =========================
   INPUT
   ========================= */

form input[type="text"] {{
    width: 100%;

    padding: 17px 18px;

    background: transparent;
    color: #111;

    border: 0;
    border-bottom: 3px solid #111;

    outline: none;

    font-family: "Courier New", Courier, monospace;
    font-size: 19px;

    transition: 0.15s;
}}


/* При клике */

form input[type="text"]:focus {{
    background: #d8ff00;

    border-bottom-width: 6px;

    padding-left: 25px;
}}


/* Placeholder */

form input::placeholder {{
    color: #777;
}}


/* =========================
   BUTTON
   ========================= */

form button {{
    margin-top: 30px;

    padding: 17px 32px;

    background: #111;
    color: #d8ff00;

    border: 3px solid #111;

    font-family: "Courier New", Courier, monospace;

    font-size: 15px;
    font-weight: 700;

    letter-spacing: 2px;
    text-transform: uppercase;

    cursor: pointer;

    box-shadow: 7px 7px 0 #d8ff00;

    transition: 0.15s;
}}


form button::after {{
    content: "  →";
}}


form button:hover {{
    background: #d8ff00;
    color: #111;

    box-shadow: 7px 7px 0 #111;

    transform: translate(-2px, -2px);
}}


form button:active {{
    transform: translate(5px, 5px);

    box-shadow: 2px 2px 0 #111;
}}


/* =========================
   REQUIRED
   ========================= */

form input:required {{
    border-left: 5px solid #111;
}}


form input:required:valid {{
    border-left-color: #d8ff00;
}}


/* =========================
   ERROR
   ========================= */

/*
   Сейчас err у вас обычный <p>.
   Поэтому первый p перед h1 будет
   оформлен как сообщение об ошибке.
*/

form > p:first-child {{
    padding: 15px 20px;

    background: #111;
    color: #d8ff00;

    border-left: 10px solid #d8ff00;

    font-size: 14px;
    font-weight: 700;

    text-transform: uppercase;

    box-shadow: 6px 6px 0 #d8ff00;
}}
    </style>
    </head>
    <body>
        {body}
    </body>
    </html>
"""


def _csfr_field (request:HttpRequest) -> str:
    token = get_token(request)
    return( 
        f"<input" 
        f"type='hidden'" 
        f"name ='csrfmiddlewaretoken'" 
        f"value = '{escape(token)}'"
        f">"

)


def index(request: HttpRequest):

    return render(request, 'notes/home.html')


def about(request: HttpRequest):

    return render(request, 'notes/about.html')


def notes_view_list(request: HttpRequest) -> HttpResponse:

    
    notes = data.list_notes()


    return render(request, 'notes/notes_list.html', {'notes': notes})



def notes_detail (request: HttpRequest, note_id: int) -> HttpResponse:


    note = data.get_note(note_id)
   

    return render(request, 'notes/note_detail.html', {'note': note})



def notes_create (request: HttpRequest) -> HttpResponse:


    error = ""


    if request.method == "POST":

        title = request.POST.get ("title", "")
        note_body = request.POST.get ('body', "")
        tag = request.POST.get ("tag", "")
        category = request.POST.get ("category", "")


        if not title.strip():

            error = """  
            <div class = "form-error"> Title can not be empty </div>
            
            """


        else:

            created = data.create_note(

                title=title,
                body=note_body,
                tag=(tag or 'mixed'),
                category = (category or 'main'),

            )

            return redirect(
                "notes_detail",
                note_id=created["id"]
            )
       

    action = f"{escape(reverse('notes_create'))}"
    
    list_url = escape(
        reverse("notes_list")
    )
    form=f"""
    <form method = "post" action = "{action}">
        {error}
        {_csfr_field(request)}
        <h1>New note </h1>

        <p><label>Title:</label></p>
        <p><input type = "text" name = "title" placeholder="Введите заголовок" required></p>
        <p><label>Заметка:</label></p>
        <p><textarea name="body"   placeholder="Введите текст заметки" required></textarea></p>
        <p><label>Category: </label></p>
        <p><input type="text" name="category"       placeholder="Бэкенд" required></p>
        <p><label>Тэг:</label></p>
        <p><input type="text" name="tag"   placeholder="Django" required></p>
        <p><button type="submit">Создать</button></p>
        <div class="actions">

                <a
                    class="action-link"
                    href="{list_url}"
                >
                    Отмена
                </a>

            </div>

    </form> 

    """

    return HttpResponse(html_shell("Create new note", form)) 



def notes_update(request: HttpRequest, note_id: int) -> HttpResponse:

    note = data.get_note(note_id)

    if note is None:

        list_url = escape(
            reverse("notes_list")
        )

        body = f"""
        <h1>Can not edit</h1>
        <p>   Запрошенная заметка
        не найдена.</p>

        <div class="actions">

        <a

        class="action-link"
        href="{list_url}"
        >
        Вернуться к списку
        </a>

        </div>

        """

        return HttpResponse(
            html_shell(
                "Заметка не найдена",
                body
            ),
            status=404
        )


    error = ""


    if request.method == "POST":
        title = request.POST.get("title","")
        note_body = request.POST.get("body", "")
        tag = request.POST.get("tag", "")
        category = request.POST.get("category", "")




        if not title.strip():

            error = """
            <div class="form-error">Title can not be empty</div>"""

            note = {

            **note,
            "title": title,
            "body": note_body,
            "tag": tag,
            "category":  category,



            }

        else:
            data.update_note(

        note_id,
        title=title,
        body=note_body,
        tag=tag or 'mixed',
        category=(
                    category
                    or "главная"
                ),
            )


            return redirect(
                    "notes_detail",
                    note_id=note_id
                )


    title_e = escape(note["title"])
    body_e = escape(note["body"])

    tag_e = escape(note["tag"])
    category_e = escape(note["category"])


    action = escape(reverse('notes_edit', kwargs={'note_id': note_id}))
  
    cancel_url = escape(

        reverse(

            "notes_detail",

            kwargs={
                "note_id": note_id
            }

        )
    )


    form = f"""

        <form
        method="post"   
        action="{action}">
        {error}
        {_csfr_field(request)}

        <h1>New note </h1>
        <p><label>Title:</label></p>
        <p><input type = "text" name = "title" required value ={title_e}></p>
        <p><label>Заметка:</label></p>
        <textarea name="body" required value={body_e}></textarea>
        <p><label>Category: </label></p>
        <p><input type="text" name="category" required value = {category_e}></p>
        <p><label>Тэг:</label></p>
        <p><input type="text" name="tag" required value = {tag_e}></p>
        <p><button type="submit">Save changes</button></p>
                   <div class="actions">

                <a
                    class="action-link"
                    href="{cancel_url}"
                >
                    Отмена
                </a>

            </div>


        </form>

    """

    return HttpResponse(html_shell("Edit Note", form))


            



def notes_delete (request: HttpRequest, note_id:int) -> HttpResponse:

    note = data.get_note(note_id)

    if note is None:
        list_url = escape(
            reverse("notes_list")
        )

        body = f"""

            <h1>Can not edit</h1>
            <p>Requested note was not</p>

            <div class="actions">

                <a
                    class="action-link"
                    href="{list_url}"
                >
                    Вернуться к списку
                </a>

            </div>

        """

        return HttpResponse(
            html_shell(
                "Заметка не найдена",
                body
            ),
            status=404
        )




    if request.method == "POST":
        data.delete_note(note_id)
        return redirect ("notes_list")


    action = escape(reverse("notes_delete", kwargs={'note_id': note_id}))
    
    
    cancel_url = escape(

        reverse(

            "notes_detail",

            kwargs={
                "note_id": note_id
            }

        )
    )

    
    
    body = f"""

        <h1>Deletion of Note</h1>


        <div class="delete-warning">


            <span class="delete-warning-label">
                Внимание
            </span>


            <p>

                Вы действительно хотите
                удалить заметку

                <strong>{escape(note['title'])}</strong>


            </p>


            <p>
                Это действие нельзя отменить.
            </p>


        </div>

        <form method = "post" action ="{action}">
 
        {_csfr_field(request)}


            <button type="submit">
                Да, удалить
            </button>


        </form>


        <div class="actions">

            <a
                class="action-link"
                href="{cancel_url}"
            >
                Отмена
            </a>

        </div>


    """

    return HttpResponse(html_shell("Note deletion", body))