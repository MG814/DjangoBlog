from django.shortcuts import render


# funkcja post_list pobiera (czyli request) oraz zwraca (czyli return)
# to co wyrenderuje (złoży w całoiść) szablon html wbudowana funkcja render
def post_list(request):
    return render(request, 'blog/post_list.html', {})
