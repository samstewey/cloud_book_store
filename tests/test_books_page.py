from playwright.sync_api import Page, expect

def test_book_page_has_title(page: Page):
    page.goto('http://127.0.0.1:5001/books')
    h1 = page.locator('h1')
    expect(h1).to_have_text("Books")

# def test_book_page_has_books(page: Page):
#     page.goto('http://127.0.0.1:5001/books')
#     books = page.locator('li')
#     expected_books = [
#         'The Gruffalo by Julia Donaldson',
#         'Ada Twist, Scientist by Andrea Beaty',
#         'The Girl Who Drank the Moon by Kelly Barnhill',
#         'Dragons in a Bag by Zetta Elliott'
#     ]
#     actual_books = books.all_inner_texts()
#     assert actual_books == expected_books

def test_form_adds_book_to_page(page: Page):
    page.goto('http://127.0.0.1:5001/books')
    books = page.locator('li')
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott',
        'The Chroicles of Geronimo (the cat) by Geronimo'
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books