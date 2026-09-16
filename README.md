# Siguranta Psihologica.ro

Platforma "Siguranta Psihologica.ro" este un proiect modern, sigur și scalabil, construit cu Python, Django și Wagtail CMS. Proiectul este gândit ca o platformă de conținut și resurse, fiind pregătit arhitectural să găzduiască module de training interactive și SCORM.

## 1. Arhitectura Proiectului

Aplicația este structurată pe următoarele module (`django apps`):

*   **`home`**: Conține modelele pentru pagina principală (Homepage), care detaliază viziunea managementului despre siguranța psihologică și descrie serviciile oferite.
*   **`blog`**: Modulul CMS (Wagtail) destinat articolelor și resurselor educaționale (ex: ISO 45003). Permite construirea de pagini bogate vizual utilizând funcționalitatea `StreamField`.
*   **`evaluations`**: Modul pentru "Formulare de Evaluare" ce gestionează colectarea datelor confidențiale de la utilizatori (ex: chestionare de evaluare a climatului de echipă). Utilizează pachetul `django-fernet-fields` pentru a oferi "best-in-class GDPR compliance" prin criptarea la nivel de câmp direct în baza de date.
*   **`lms`**: Modul pregătitor pentru faza 2. Conține structurile de bază (`Course`, `ScormPackage`, `UserCourseProgress`) pentru a permite integrarea facilă a pachetelor SCORM (e-learning).

### Integrare Vercel & Supabase
*   **Vercel**: Fișierele `vercel.json` și `build.sh` sunt incluse, asigurând o implementare de tip serverless prin Vercel Python Runtime. Pachetul `whitenoise` este utilizat pentru servirea eficientă a fișierelor statice.
*   **Supabase**: `dj-database-url` a fost configurat în `settings.py` pentru a permite conectarea la baza de date PostgreSQL gestionată de Supabase prin intermediul variabilelor de mediu.

## 2. Design System

Am implementat un design clar, curat și profesionist (Medical/Corporate blend), bazat pe **Tailwind CSS**. Paleta cromatică este setată în `base.html`:
*   **Navy (`#0f172a`)**: Exprimă profesionalism, încredere, viziune de management.
*   **Slate (`#64748b`)**: Gri neutru pentru text, oferă claritate.
*   **Accent (`#38bdf8`)**: Albastru deschis pentru call-to-actions și link-uri, inspirând claritate psihologică.

Interactivitatea este gestionată prin **HTMX**, inclus asincron fără a construi un SPA complet.

## 3. Ghid de Inițializare Locală

Urmează acești pași în terminal pentru a porni proiectul pe mașina ta locală:

### Cerințe
*   Python 3.10+
*   Git

### Pași

1.  **Clonează repository-ul (dacă este cazul):**
    ```bash
    git clone <URL_REPO>
    cd <NUME_FOLDER>
    ```

2.  **Creează și activează mediul virtual:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Pe Windows: .venv\Scripts\activate
    ```

3.  **Instalează dependențele:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplică migrațiile (inițializează baza de date SQLite locală):**
    ```bash
    python manage.py migrate
    ```

5.  **Creează un cont de administrator Wagtail:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Porniți serverul de dezvoltare:**
    ```bash
    python manage.py runserver
    ```

Accesează:
*   Frontend-ul public la: `http://127.0.0.1:8000/`
*   Interfața de administrare Wagtail la: `http://127.0.0.1:8000/admin/` (folosește contul creat la pasul 5).

## 4. Modelele de Date (Rezumat MVP)

*   `home/models.py`: `HomePage` cu câmpuri pentru Hero section (titlu, subtitlu), filozofie și servicii (StructBlock).
*   `blog/models.py`: `BlogIndexPage` și `BlogPage` cu un `StreamField` extins pentru articole.
*   `evaluations/models.py`: `EvaluationForm` care criptează datele PII (nume, prenume, email, feedback) pentru conformitate GDPR.
*   `lms/models.py`: Modele pregătite pentru SCORM (`Course`, `ScormPackage`, `UserCourseProgress`).
