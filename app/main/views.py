@main.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
    title = 'Home - Welcome to The Best cleaning Site Worldwide You Think of It We help share It.'
    return render_template('index.html',title = title)
