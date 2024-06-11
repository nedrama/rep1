from odoo import http


class Books(http.Controller):
    @http.route("/info_storage/books")
    def list(self, **kwargs):
        Book = http.request.env["info_storage.book"]
        books = Book.search([])
        return http.request.render(
            "info_storage.book_list_template",
            {"books": books},
        )
