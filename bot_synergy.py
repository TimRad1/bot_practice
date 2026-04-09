# =============================================================================
# ЧАТ-БОТ ДЛЯ УНИВЕРСИТЕТА "СИНЕРГИЯ" — ВЕРСИЯ 2.0
# С поддержкой многошагового выбора: Специальность → Кафедра
# =============================================================================

import sys
import string

# =============================================================================
# 🎓 БАЗА ЗНАНИЙ
# =============================================================================

# Специальности: ключевые слова → русское название
SPECIALTIES = {
    'it_programming': {
        'name': 'IT и программирование',
        'keywords': ['программист', 'программирование', 'it', 'айти', 'ай-ти',
                     'разработчик', 'кодер', 'софт', 'software', 'python',
                     'java', 'веб', 'сайт', 'приложение', 'app', 'информатика'],
        'faculty': 'faculty_it',
    },
    'cybersecurity': {
        'name': 'Кибербезопасность',
        'keywords': ['кибербезопасность', 'кибер', 'безопасность', 'защита',
                     'хакер', 'информационная безопасность'],
        'faculty': 'faculty_cyber',
    },
    'ai_ml': {
        'name': 'Искусственный интеллект',
        'keywords': ['искусственный интеллект', 'нейросеть', 'нейро', 'нейросети',
                     'машинное обучение', 'машинное', 'обучение', 'ml', 'ai',
                     'data science', 'аналитик данных'],
        'faculty': 'faculty_ai',
    },
    'gamedev': {
        'name': 'Геймдизайн',
        'keywords': ['геймдизайн', 'разработка игр', 'игры', 'игровая индустрия',
                     'юнити', 'unreal', 'gamedev', 'геймдев', 'игровой'],
        'faculty': 'faculty_gamedev',
    },
    'design': {
        'name': 'Дизайн',
        'keywords': ['дизайн', 'графический дизайн', 'веб-дизайн', 'визуал',
                     'figma', 'photoshop', 'художник', 'дизайнер'],
        'faculty': 'faculty_design',
    },
    'management': {
        'name': 'Менеджмент',
        'keywords': ['менеджмент', 'управление', 'бизнес', 'руководитель',
                     'менеджер', 'администрирование', 'предприниматель'],
        'faculty': 'faculty_business',
    },
    'economics': {
        'name': 'Экономика и финансы',
        'keywords': ['экономика', 'финансы', 'бухгалтер', 'аудит', 'налоги',
                     'экономист', 'финансовый', 'бухгалтерия', 'банк'],
        'faculty': 'faculty_economics',
    },
    'law': {
        'name': 'Юриспруденция',
        'keywords': ['юриспруденция', 'право', 'юрист', 'адвокат', 'закон',
                     'суд', 'правоведение', 'нотариус', 'юридический'],
        'faculty': 'faculty_law',
    },
    'psychology': {
        'name': 'Психология',
        'keywords': ['психология', 'психолог', 'психо', 'психотерапия',
                     'ментальное здоровье', 'терапия', 'консультация'],
        'faculty': 'faculty_psychology',
    },
    'media': {
        'name': 'Медиа и кино',
        'keywords': ['медиа', 'журналистика', 'телевидение', 'контент', 'блогер',
                     'смм', 'маркетинг', 'продвижение', 'реклама', 'журналист'],
        'faculty': 'faculty_media',
    },
    'medicine': {
        'name': 'Медицина',
        'keywords': ['медицина', 'медецина', 'врач', 'лечение', 'медик',
                     'здравоохранение', 'клиника', 'терапевт', 'больница',
                     'хирург', 'стоматолог', 'анатомия'],
        'faculty': 'faculty_medicine',
    },
    'education': {
        'name': 'Педагогика',
        'keywords': ['педагогика', 'учитель', 'преподаватель', 'образование',
                     'воспитатель', 'методист', 'тьютор', 'педагог', 'преподавание'],
        'faculty': 'faculty_pedagogy',
    },
}

# Факультеты и кафедры
FACULTIES = {
    'faculty_it': {
        'name': 'Факультет информационных технологий',
        'description': 'Разработка ПО, веб-технологии, системный анализ',
        'departments': {
            'dept_web': {
                'name': 'Кафедра веб-разработки',
                'description': 'Frontend, backend, fullstack',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 Бакалавриат "Веб-разработка", Магистратура "Архитектура веб-систем"\n📚 HTML/CSS, JavaScript, Python, Node.js, React, Vue\n💼 Яндекс, Сбер, Тинькофф\n🔗 synergy.ru/it/web',
            },
            'dept_mobile': {
                'name': 'Кафедра мобильной разработки',
                'description': 'iOS и Android',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "Мобильная разработка", "Кроссплатформенные приложения"\n📚 Swift, Kotlin, Flutter, React Native\n💼 VK, Ozon, Avito\n🔗 synergy.ru/it/mobile',
            },
            'dept_data': {
                'name': 'Кафедра анализа данных',
                'description': 'Big Data и бизнес-аналитика',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "Аналитик данных", "Big Data Engineer"\n📚 Python, SQL, Pandas, ML, Tableau\n💼 Газпром, МТС, Лаборатория Касперского\n🔗 synergy.ru/it/data',
            },
        },
    },
    'faculty_cyber': {
        'name': 'Факультет кибербезопасности',
        'description': 'Защита информации, аудит, этичный хакинг',
        'departments': {
            'dept_netsec': {
                'name': 'Кафедра сетевой безопасности',
                'description': 'Защита сетей и инфраструктуры',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "Сетевая безопасность", "Пентестинг"\n📚 Cisco, Wireshark, Kali Linux, Metasploit\n💼 Ростелеком-Солар, Positive Technologies\n🔗 synergy.ru/cyber/netsec',
            },
            'dept_appsec': {
                'name': 'Кафедра безопасности приложений',
                'description': 'Аудит кода, защита ПО',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "AppSec Engineer"\n📚 OWASP, Burp Suite, SAST/DAST\n💼 Лаборатория Касперского, BI.ZONE\n🔗 synergy.ru/cyber/appsec',
            },
        },
    },
    'faculty_ai': {
        'name': 'Факультет искусственного интеллекта',
        'description': 'ML, нейросети, компьютерное зрение, NLP',
        'departments': {
            'dept_ml': {
                'name': 'Кафедра машинного обучения',
                'description': 'Разработка и обучение моделей ИИ',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "ML Engineer", "Deep Learning"\n📚 PyTorch, TensorFlow, Scikit-learn, Transformers\n💼 Яндекс, Сбер AI, VisionLabs\n🔗 synergy.ru/ai/ml',
            },
            'dept_nlp': {
                'name': 'Кафедра обработки естественного языка',
                'description': 'Чат-боты, перевод, анализ текста',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "NLP Engineer"\n📚 BERT, GPT, spaCy, Hugging Face\n💼 Яндекс.Переводчик, Just AI\n🔗 synergy.ru/ai/nlp',
            },
        },
    },
    'faculty_gamedev': {
        'name': 'Факультет геймдизайна',
        'description': 'Создание игр, 3D-моделирование, нарратив',
        'departments': {
            'dept_gamedesign': {
                'name': 'Кафедра геймдизайна',
                'description': 'Игровые механики и баланс',
                'exams': 'Литература, Русский язык, Творческое испытание',
                'details': '🎓 "Геймдизайнер", "Level Designer"\n📚 Unity, Unreal Engine, Miro, Figma\n💼 MY.GAMES, Pixonic, Innova\n🔗 synergy.ru/gamedev/design',
            },
            'dept_gamedev': {
                'name': 'Кафедра разработки игр',
                'description': 'Программирование игр',
                'exams': 'Математика (профиль), Информатика, Русский язык',
                'details': '🎓 "Game Programmer"\n📚 C#, C++, Blueprint, Shader Graph\n💼 Lesta Studio, Gaijin Entertainment\n🔗 synergy.ru/gamedev/dev',
            },
        },
    },
    'faculty_design': {
        'name': 'Факультет дизайна',
        'description': 'Графический, веб-, UX/UI дизайн',
        'departments': {
            'dept_graphic': {
                'name': 'Кафедра графического дизайна',
                'description': 'Брендинг, иллюстрация',
                'exams': 'Литература, Русский язык, Творческое испытание',
                'details': '🎓 "Графический дизайнер"\n📚 Adobe CC, Figma, Procreate\n💼 Red Keds, Vosmo\n🔗 synergy.ru/design/graphic',
            },
            'dept_uxui': {
                'name': 'Кафедра UX/UI-дизайна',
                'description': 'Пользовательский опыт',
                'exams': 'Литература, Русский язык, Творческое испытание',
                'details': '🎓 "UX/UI Designer"\n📚 User Research, Wireframing, Prototyping\n💼 Яндекс, Тинькофф\n🔗 synergy.ru/design/uxui',
            },
        },
    },
    'faculty_law': {
        'name': 'Юридический факультет',
        'description': 'Юристы, адвокаты, нотариусы',
        'departments': {
            'dept_civil': {
                'name': 'Кафедра гражданского права',
                'description': 'Гражданское, семейное право',
                'exams': 'Обществознание, Русский язык, История',
                'details': '🎓 "Гражданское право"\n📚 ГК РФ, Семейный кодекс\n💼 Адвокатские бюро, нотариусы\n🔗 synergy.ru/law/civil',
            },
            'dept_criminal': {
                'name': 'Кафедра уголовного права',
                'description': 'Уголовное право, криминология',
                'exams': 'Обществознание, Русский язык, История',
                'details': '🎓 "Уголовное право"\n📚 УК РФ, Криминалистика\n💼 СК РФ, Прокуратура\n🔗 synergy.ru/law/criminal',
            },
        },
    },
    'faculty_business': {
        'name': 'Факультет бизнеса и менеджмента',
        'description': 'Управление, предпринимательство, HR',
        'departments': {
            'dept_management': {
                'name': 'Кафедра управления бизнесом',
                'description': 'Стратегический менеджмент',
                'exams': 'Математика, Обществознание, Русский язык',
                'details': '🎓 "Менеджмент организации"\n📚 Стратегия, HR, Финансы\n💼 Сбер, ВТБ, Газпром\n🔗 synergy.ru/business/management',
            },
        },
    },
    'faculty_economics': {
        'name': 'Экономический факультет',
        'description': 'Экономика, бухучёт, аудит',
        'departments': {
            'dept_accounting': {
                'name': 'Кафедра бухучёта и аудита',
                'description': 'Бухгалтерия, налоги',
                'exams': 'Математика, Обществознание, Русский язык',
                'details': '🎓 "Бухгалтерский учёт"\n📚 Бухучёт, Налоговый кодекс\n💼 Big Four, ФНС\n🔗 synergy.ru/economics/accounting',
            },
        },
    },
    'faculty_psychology': {
        'name': 'Факультет психологии',
        'description': 'Клиническая психология, консультирование',
        'departments': {
            'dept_clinical': {
                'name': 'Кафедра клинической психологии',
                'description': 'Психотерапия, реабилитация',
                'exams': 'Биология, Русский язык, Обществознание',
                'details': '🎓 "Клиническая психология"\n📚 Психодиагностика, Нейропсихология\n💼 Психиатрические клиники\n🔗 synergy.ru/psychology/clinical',
            },
        },
    },
    'faculty_media': {
        'name': 'Факультет медиа',
        'description': 'Журналистика, СММ, контент-маркетинг',
        'departments': {
            'dept_journalism': {
                'name': 'Кафедра журналистики',
                'description': 'ТВ, радио, печатные СМИ',
                'exams': 'Литература, Русский язык, Творческое испытание',
                'details': '🎓 "Журналистика"\n📚 Мультимедиа, Редактура\n💼 Первый канал, РБК\n🔗 synergy.ru/media/journalism',
            },
            'dept_smm': {
                'name': 'Кафедра цифрового маркетинга',
                'description': 'СММ, блогинг',
                'exams': 'Литература, Русский язык, Обществознание',
                'details': '🎓 "SMM-менеджер"\n📚 Таргетинг, Копирайтинг\n💼 Яндекс, VK\n🔗 synergy.ru/media/smm',
            },
        },
    },
    'faculty_medicine': {
        'name': 'Медицинский факультет',
        'description': 'Лечебное дело, фармация',
        'departments': {
            'dept_therapy': {
                'name': 'Кафедра терапии',
                'description': 'Внутренние болезни',
                'exams': 'Химия, Биология, Русский язык',
                'details': '🎓 "Лечебное дело"\n📚 Анатомия, Фармакология\n💼 Городские больницы\n🔗 synergy.ru/medicine/therapy',
            },
            'dept_pharmacy': {
                'name': 'Кафедра фармации',
                'description': 'Фармацевтика',
                'exams': 'Химия, Биология, Русский язык',
                'details': '🎓 "Фармация"\n📚 Фармакология, Биотехнология\n💼 Фармкомпании\n🔗 synergy.ru/medicine/pharmacy',
            },
        },
    },
    'faculty_pedagogy': {
        'name': 'Педагогический факультет',
        'description': 'Преподавание, методика',
        'departments': {
            'dept_primary': {
                'name': 'Кафедра начального образования',
                'description': 'Учителя начальных классов',
                'exams': 'Математика, Русский язык, Обществознание',
                'details': '🎓 "Начальное образование"\n📚 Методика, Детская психология\n💼 Школы, Лицеи\n🔗 synergy.ru/pedagogy/primary',
            },
        },
    },
}

# Общие вопросы: ключевые слова → ответ
GENERAL_QUESTIONS = {
    'admission': {
        'keywords': ['поступить', 'поступление', 'как поступить', 'хочу поступить'],
        'answer': 'Для поступления выберите направление, затем кафедру. Я помогу узнать экзамены!',
    },
    'cost': {
        'keywords': ['стоимость', 'цена', 'обучение', 'сколько стоит', 'плата'],
        'answer': 'По стоимости: synergy.ru/prices или ☎ +7 495 800-10-01',
    },
    'documents': {
        'keywords': ['документы', 'паспорт', 'аттестат'],
        'answer': 'Нужны: паспорт, аттестат/диплом, фото 3x4 (6 шт.), справка 086/у, СНИЛС',
    },
    'exams': {
        'keywords': ['экзамены', 'предметы', 'вступительные'],
        'answer': 'Экзамены зависят от направления. Выберите специальность, чтобы узнать подробности.',
    },
    'deadlines': {
        'keywords': ['сроки', 'дедлайн', 'когда подача'],
        'answer': 'Сроки подачи документов устанавливаются ежегодно. Уточните на synergy.ru/admission',
    },
    'budget': {
        'keywords': ['бюджет', 'бесплатно'],
        'answer': 'Да, в университете есть бюджетные места',
    },
    'scholarship': {
        'keywords': ['стипендия'],
        'answer': 'Стипендия предоставляется при выполнении условий',
    },
    'dormitory': {
        'keywords': ['общежитие', 'жилье'],
        'answer': 'Общежитие предоставляется иногородним студентам',
    },
    'contacts': {
        'keywords': ['контакты', 'телефон', 'сайт', 'связаться'],
        'answer': '☎ +7 495 800-10-01 | 🌐 synergy.ru | ✉ admission@synergy.ru',
    },
    'specialties': {
        'keywords': ['специальности', 'направления', 'чему учат', 'факультеты', 'кафедры', 'какие есть'],
        'answer': 'specialties_list',  # специальный маркер
    },
    'distance': {
        'keywords': ['дистанционно', 'онлайн', 'удаленно'],
        'answer': 'Да, доступны дистанционные формы обучения',
    },
    'transfer': {
        'keywords': ['перевестись', 'перевод'],
        'answer': 'Перевод возможен при наличии свободных мест',
    },
}

# Системные сообщения
GREETING = 'Привет! 👋 Я бот университета "Синергия". Чем могу помочь?'
GOODBYE = 'Всего доброго! 🎓 Если вопросы — обращайтесь снова!'
HELP = '''📚 Доступные команды:

🎓 Направления: IT, кибербезопасность, ИИ, геймдизайн, дизайн, менеджмент, экономика, юриспруденция, психология, медиа, медицина, педагогика
📝 Вопросы: "поступление", "стоимость", "документы", "экзамены", "контакты"
⚙️ Навигация: "меню" — список кафедр, "назад" — на шаг, "выход" — завершить'''
DEFAULT_REPLY = 'Не понял вопрос. 😕\nПопробуйте: "поступление", "стоимость", "документы" или напишите "меню".'

# Состояния
STATE_IDLE = 'idle'
STATE_SELECTING_DEPT = 'selecting_dept'
STATE_SHOWING_DETAILS = 'showing_details'

DOCUMENTS_TEXT = """📄 Необходимые документы:
  • Паспорт (оригинал + копия)
  • Аттестат/диплом (оригинал + копия)
  • Фотографии 3x4 (6 шт.)
  • Медицинская справка 086/у
  • СНИЛС (копия)"""

CONTACTS_TEXT = """📞 Контакты приёмной комиссии:
  • Телефон: +7 495 800-10-01
  • ВК: https://vk.com/synergyuniversity
  • Сайт: https://synergy.ru/
  • Адрес: г. Москва, ул. Тверская, д. 4"""


# =============================================================================
# ФУНКЦИИ
# =============================================================================

def preprocess(text: str) -> str:
    """Нижний регистр, удаление пунктуации, нормализация пробелов"""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(text.split())


def find_match(user_input: str, data: dict) -> str | None:
    """Ищет лучшее совпадение по ключевым словам. Возвращает ключ или None"""
    tokens = set(preprocess(user_input).split())
    best_key, best_score = None, 0.0

    for key, item in data.items():
        kws = item if isinstance(item, dict) else item.get('keywords', [])
        kws = item.get('keywords', []) if isinstance(item, dict) else []

        for kw in kws:
            kw_tokens = set(preprocess(kw).split())
            if not kw_tokens:
                continue
            score = len(tokens & kw_tokens) / len(kw_tokens)
            if score > best_score and score >= 0.3:
                best_score = score
                best_key = key

    return best_key


# =============================================================================
# БОТ
# =============================================================================

class SynergyBot:
    def __init__(self):
        self.state = STATE_IDLE
        self.context = {}
        self.active = True

    def _reset(self):
        self.state = STATE_IDLE
        self.context = {}

    def _format_depts(self, depts: dict) -> str:
        lines = ["🏛️ Выберите кафедру (номер или название):\n"]
        for i, (code, d) in enumerate(depts.items(), 1):
            lines.append(f"  {i}. {d['name']} — {d['description']}")
        lines.append("\n💡 Напишите номер или название")
        return '\n'.join(lines)

    def _show_details(self, dept_code: str) -> str:
        dept = self.context['depts'][dept_code]
        faculty = FACULTIES.get(self.context['faculty'], {})
        faculty_name = faculty.get('name', 'Факультет')

        self.state = STATE_SHOWING_DETAILS
        return (f"🎓 {faculty_name}\n"
                f"🏛️ {dept['name']}\n\n"
                f"📝 Экзамены: {dept.get('exams', 'Уточняйте в приёмной')}\n\n"
                f"{DOCUMENTS_TEXT}\n\n"
                f"{dept['details']}\n\n"
                f"{CONTACTS_TEXT}\n\n"
                f"✅ Далее:\n"
                f'  • "меню" — другие кафедры\n'
                f'  • название направления — другая специальность\n'
                f'  • "помощь" — общие вопросы')

    def get_response(self, text: str) -> str:
        processed = preprocess(text)

        # Системные команды
        if any(kw in processed for kw in ['привет', 'здравствуйте', 'добрый', 'хай', 'hello', 'hi']):
            self._reset()
            return GREETING

        if any(kw in processed for kw in ['пока', 'до свидания', 'спасибо', 'завершить', 'выход', 'стоп']):
            self.active = False
            return GOODBYE

        if processed in ['помощь', 'help', 'команды']:
            return HELP

        if processed == 'меню':
            return self._cmd_menu()

        if processed in ['назад', 'вернуться', 'back']:
            return self._cmd_back()

        # Обработка по состоянию
        if self.state == STATE_SHOWING_DETAILS:
            self.state = STATE_IDLE
            # Сразу обрабатываем ввод
            return self._handle_idle(text)

        if self.state == STATE_SELECTING_DEPT:
            return self._handle_dept_select(text)

        # STATE_IDLE
        return self._handle_idle(text)

    def _handle_idle(self, text: str) -> str:
        processed = preprocess(text)

        # 1. Специальность
        spec_code = find_match(text, SPECIALTIES)
        if spec_code:
            spec = SPECIALTIES[spec_code]
            faculty_code = spec['faculty']
            faculty = FACULTIES.get(faculty_code, {})
            depts = faculty.get('departments', {})

            self.context = {'specialty': spec_code, 'faculty': faculty_code, 'depts': depts}

            if depts:
                self.state = STATE_SELECTING_DEPT
                return f"🎓 {faculty['name']}\n\n" + self._format_depts(depts)
            return f"🎓 {faculty.get('name', spec['name'])}\n\n{faculty.get('description', '')}"

        # 2. Общие вопросы
        q_key = find_match(text, GENERAL_QUESTIONS)
        if q_key:
            answer = GENERAL_QUESTIONS[q_key]['answer']
            if answer == 'specialties_list':
                return self._show_specialties()
            return answer

        return DEFAULT_REPLY

    def _show_specialties(self) -> str:
        lines = ["🎓 Доступные направления:\n"]
        for code, spec in SPECIALTIES.items():
            lines.append(f"  • {spec['name']}")
        lines.append("\n💡 Напишите название")
        return '\n'.join(lines)

    def _handle_dept_select(self, text: str) -> str:
        processed = preprocess(text)
        depts = self.context.get('depts', {})
        dept_codes = list(depts.keys())

        if processed.isdigit():
            idx = int(processed) - 1
            if 0 <= idx < len(dept_codes):
                return self._show_details(dept_codes[idx])
            return f"❌ Нет кафедры {idx + 1}. Выберите из списка:\n" + self._format_depts(depts)

        for code, d in depts.items():
            if any(kw in processed for kw in preprocess(d['name']).split()):
                return self._show_details(code)

        return f"❓ Не распознал кафедру:\n" + self._format_depts(depts)

    def _cmd_menu(self) -> str:
        if self.context.get('depts'):
            self.state = STATE_SELECTING_DEPT
            return self._format_depts(self.context['depts'])
        if self.context.get('specialty'):
            spec = SPECIALTIES[self.context['specialty']]
            faculty = FACULTIES.get(spec['faculty'], {})
            depts = faculty.get('departments', {})
            if depts:
                self.context['depts'] = depts
                self.state = STATE_SELECTING_DEPT
                return f"🎓 {faculty['name']}\n\n" + self._format_depts(depts)
        return self._show_specialties()

    def _cmd_back(self) -> str:
        if self.state == STATE_SELECTING_DEPT:
            self._reset()
            return "↩️ Вернулись к началу. Чем помочь?"
        self._reset()
        return "↩️ Готов к новым вопросам!"

    def run(self):
        print(f"🤖 Бот 'Синергия' запущен!\nБот: {GREETING}\n")
        while self.active:
            try:
                text = input("Вы: ").strip()
                if not text or text.startswith('C:\\') or 'conda' in text.lower():
                    continue
                print(f"Бот: {self.get_response(text)}\n")
            except KeyboardInterrupt:
                print("\n👋 Пока!")
                break
            except Exception as e:
                print(f"⚠️ Ошибка: {e}\n")


if __name__ == "__main__":
    SynergyBot().run()