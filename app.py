import pages.about as about
import pages.contact as contact
import pages.cv as cv
from pages.sidebar import sidebar


PAGES = {
    "About me": about,
    "Contact me": contact,
    "CV": cv
}


selection = sidebar(list(PAGES.keys()))
page = PAGES[selection]
page.content()

