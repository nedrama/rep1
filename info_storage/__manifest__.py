{
    "name": "Informacijos saugykla",
    "summary": "Saugo informaciją apie dokumentus/knygas",
    "description": "",
    "author": "Vardas Pavarde",
    "website": "https://github.com/nedrama/rep1/tree/main",
    "category": "Storage",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/menu.xml",
        "views/book_list_template.xml",
        "wizard/filter_wizard.xml",
    ],
    "application": True,
    "demo": [
        "data/worker.csv",
        "data/info_storage.book.csv",
    ],
    'post_init_hook': 'add_workers',
}
