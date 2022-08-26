from flask import Blueprint, render_template, request, redirect, url_for
views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Julien", lastname="Szabados")
# pass parameter first way
@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name3=username)
# QUERY PARAMETER  (GET / POST)
@views.route("/profile2")
def profile2():
    args = request.args
    name2 = args.get('name2')
    age2 = args.get('age2')
    return render_template("index.html", name2=name2, age2=age2)
# REDIRECT
@views.route("/gotoredirection")
def gotoredirection():
    return redirect(url_for("views.profile2"))
@views.route("/gotoaredirect")
def gotoaredirect():
    url = 'https://www.google.com/search?q=test&sxsrf=ALiCzsaJjjxP6pAQvBKH3v4W7y1EwEu8LQ%3A1661245023766&source=hp&ei=X5YEY8zAK4TuaZ7dg6AF&iflsig=AJiK0e8AAAAAYwSkb4_th_LfDaUsBnprnYfRBEkGYAoL&ved=0ahUKEwiM7Jf8y9z5AhUEdxoKHZ7uAFQQ4dUDCAg&uact=5&oq=test&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyCwgAEIAEELEDEIMBMgQIABBDMgQIABBDMggIABCABBCxAzoRCC4QgAQQsQMQgwEQxwEQ0QM6FAguEIAEELEDEIMBEMcBENEDENQCOgQILhBDOggILhCABBCxAzoKCC4QxwEQ0QMQQzoHCCMQ6gIQJzoNCC4QxwEQ0QMQ6gIQJzoFCAAQgAQ6CggAELEDEIMBEEM6EwguELEDEIMBEMcBENEDENQCEENQAFj-MGDoOGgFcAB4AIABkQGIAYwFkgEDNS4ymAEAoAEBsAEK&sclient=gws-wiz'
    return redirect(url)







