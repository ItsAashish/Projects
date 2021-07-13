from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponseRedirect
)
from cuser.forms import RegisterForm
from django.forms import inlineformset_factory
from .forms import (
    UserForm,
    RecipeForm,
    RIForm,
    CommentForm,
    ReportForm,
)
from django.contrib.auth.views import LoginView 
from django.views.generic import DeleteView
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from .models import ( 
    UserInfo,
    Category, 
    Recipe,
    Comment,
    Report,
    Recipe_Ingredient,
    CustomUser
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):
    user = get_object_or_404(CustomUser,id = 2)
    # last_ten = Messages.objects.filter(since=since).order_by('-id')[:10]
    recipe = Recipe.objects.filter(created_by= user)
    print(request.user, recipe)
    """ The function to render homepage of the app """
    return render(request, 'app_recipe/cookit1.html', {'recipes' : recipe})

def all_recipes(request):
    recipe = Recipe.objects.all()
    return render(request,'app_recipe/all_recipes.html',{ 'recipes': recipe })
def reviews(request):
    return render(request,'app_recipe/reviews.html')

def logoutV(request):
    if request.user:
        logout(request)
        return redirect('/')
    else:
        return redirect(reverse('login_view'))

class UserLogin(LoginView):
    """ The login view for the user """
    template_name = 'app_recipe/login.html'
    # success_url = 'app_recipe:index_page'
    LOGIN_REDIRECT_URL = 'app_recipe:index_page'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('app_recipe:index_page'))
        return super(UserLogin, self).get(request, *args, **kwargs)

def RegisterUser(request):
    """ User registration """
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST or None)
        user_form = UserForm(request.POST or None)
        if user_form.is_valid() and reg_form.is_valid():
            print(user_form.cleaned_data, reg_form.cleaned_data)
            reg_user    = reg_form.save()
            user_data   = user_form.save(commit= False)
            user_data.user = reg_user
            user_data.save()
            return redirect(reverse('app_recipe:login_view'))
    else:
        reg_form = RegisterForm()
        user_form = UserForm()
    return render(request, 'app_recipe/register.html', {
        'form1' : reg_form,
        'form2' : user_form,
    })

@login_required(login_url = 'app_recipe:login_view')
def AddRecipe(request):
    """ Function to add recipes """
    user    = request.user
    RForm   = RecipeForm(initial = {'created_by' : user})
    RIFForm = inlineformset_factory(Recipe, Recipe_Ingredient, fields= ('ingredient', 'amount'),extra= 5, can_delete= False )
    formset = RIFForm(instance= None)
    if request.method == 'POST':
        RForm   = RecipeForm(request.POST or None, request.FILES)
        if RForm.is_valid():
            recipedata      = RForm.save(commit=False)
            recipedata.created_by = request.user
            recipedata.save()
            # saveFormSet     = formset.save(commit= False)
            formset = RIFForm(request.POST or None, instance= recipedata)
            if formset.is_valid():
                formset.save()
            return redirect(reverse('app_recipe:index_page'))

    return render(request,
     'app_recipe/recipe_add.html',
     {
        'RForm' : RForm,
        'formset' : formset,  
     }
    )


def viewRecipe(request, id):
    commentform = CommentForm()
    recipe      = Recipe.objects.get(id = id)
    comments    = Comment.objects.filter(recipe= recipe)
    ingredients = Recipe_Ingredient.objects.filter(recipe= recipe)
    if not recipe:
        raise Http404
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            print('it is valid')
            form_save = commentform.save(commit = False)
            form_save.created_by = request.user
            form_save.recipe = recipe
            form_save.save()

    return render(request, 'app_recipe/recipe_details.html',{
        'recipeInfo' : recipe,
        'comments'   : comments,
        'ingredients': ingredients,
        'form'       : commentform,

    })

# @login_required(login_url = 'app_recipe:login_view')
# def viewRecipe(request, id):
#     """ The function to view the info about a certain recipe """
#     recipe      = get_object_or_404(Recipe,id = id )
#     comments    = Comment.objects.filter(recipe = recipe)
#     print(request.user, recipe)
#     ingredients = {}
#     if recipe:
#         if request.method == "POST":
#             recipe      = get_object_or_404(Recipe,id = id )
#             user_obj    = get_object_or_404(CustomUser, id = request.user.id)
#             # comments    = Comment.objects.filter(recipe = recipe)
#             form_r = CommentForm(request.POST or None )
#             if form_r.is_valid():
#                 # user = get_object_or_404(CustomUser)
#                 form_r.save(commit = False)
#                 form_r.created_by = user_obj
#                 # recipe_id = Recipe.objects.get(id = id)
#                 form_r.recipe = recipe
#                 print("Comment before")
#                 form_r.save()
#                 print("Comment")
#         ingredients   = Recipe_Ingredient.objects.filter(recipe = recipe)
#     # print(recipe[0].recipe_name, "and" , ingredients)
#         return render(request, 'app_recipe/recipe_details.html',
#             {
#                 'recipeInfo' : recipe,
#                 'ingredients' : ingredients,
#                 'message'     : None,
#                 'form'        : CommentForm(),
#                 'comments'     : comments
#             }
#         )
#     return render(request, 'app_recipe/recipe_details.html',
#             {
#                 'recipeInfo' : None,
#                 'ingredients' : ingredients,
#                 'form'        : CommentForm(), 
#                 'message'     : "Recipe doesn't exist",
#             })

@login_required(login_url = 'app_recipe:login_view')
def updateRecipe(request,id):
    """ Function to add recipes """
    user    = request.user
    instance= Recipe.objects.get(id = id)
    if user != instance.created_by:
        return redirect(reverse('app_recipe:view_recipe', kwargs={'id' : id}))
    RForm   = RecipeForm(initial = {'created_by' : user}, instance= instance )
    RIFForm = inlineformset_factory(Recipe, Recipe_Ingredient, fields= ('ingredient', 'amount'))
    formset = RIFForm(instance= instance)
    if request.method == 'POST':
        RForm   = RecipeForm(request.POST or None, instance= instance)
        if RForm.is_valid():
            recipedata      = RForm.save(commit=False)
            recipedata.created_by = request.user
            recipedata.save()
            # saveFormSet     = formset.save(commit= False)
            formset = RIFForm(request.POST or None, instance= recipedata)
            if formset.is_valid():
                formset.save()
            return redirect(reverse('app_recipe:index_page'))

    return render(request,
     'app_recipe/recipe_add.html',
     {
        'RForm' : RForm,
        'formset' : formset,  
     }
    )



# class RecipeDeleteView(DeleteView):
#     def get_object(self, queryset=None):
#         """ Hook to ensure object is owned by request.user. """
#         obj = super(RecipeDeleteView, self).get_object()
#         if not obj.created_by == self.request.user:
#             raise Http404
#         return obj

class RecipeDeleteView(LoginRequiredMixin,DeleteView):
    model = Recipe
    template_name = 'app_recipe/delete_recipe.html'
    success_url = '/'
    login_url = '/login/'
    redirect_field_name = 'login_view'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(RecipeDeleteView, self).get_object()
        if not obj.created_by == self.request.user:
            return Http404
        return obj

def userDetails(request, id):
    user = get_object_or_404(CustomUser, id = id)
    extra = get_object_or_404(UserInfo,user = user )
    return render(request, 'app_recipe/user_details.html', 
    {'user' : user, 'extra' : extra})

@login_required(login_url = 'app_recipe:login_view')
def createReport(request, pk):
    reportform = ReportForm()
    recipe      = Recipe.objects.get(id = pk)
    # comments    = Comment.objects.filter(recipe= recipe)
    # ingredients = Recipe_Ingredient.objects.filter(recipe= recipe)
    if not recipe:
        raise Http404
    if request.method == 'POST':
        reportform = ReportForm(request.POST)
        if reportform.is_valid():
            print('it is valid')
            form_save = reportform.save(commit = False)
            form_save.created_by = request.user
            form_save.recipe = recipe
            form_save.save()
            return redirect(reverse('app_recipe:all_recipes'))

    return render(request, 'app_recipe/report_recipe.html',{
        # 'recipeInfo' : recipe,
        # 'comments'   : comments,
        # 'ingredients': ingredients,
        'form'       : reportform,

    })

   
   
   
   
   
   
   
   
    # repo = ReportForm()
    # user = request.user
    # recipe_data = Recipe.objects.get(pk = pk)
    # # recipe_data = get_object_or_404(Recipe, id = pk)
    # # try:
    # #     recipe = Recipe.objects.get(id = id)
    # # except recipe.DoesNotExist:
    # #     return render(request,'app_recipe/report_recipe.html', {
    # #         'message'   : 'Recipe does not exist',
    # #         'form'      : repo,
    # #     })
    # if request.method == "POST":
    #     repo = ReportForm(request.POST)
    #     recipe_data = get_object_or_404(Recipe, id = pk)
    #     print(recipe_data)
    #     if repo.is_valid():
    #         repo.save(commit= False)
    #         repo.created_by = user
    #         repo.recipe     = recipe_data
    #         repo.save()
    #         # return redirect(reverse('view_recipe', kwargs={'id':id, 'message' : 'successifully reported'},))
    #         return redirect(reverse('app_recipe:index_page'))
    # return render(request,'app_recipe/report_recipe.html', {
    #         'message'   : 'Recipe does not exist',
    #         'form'      : repo,
    #     })
    
