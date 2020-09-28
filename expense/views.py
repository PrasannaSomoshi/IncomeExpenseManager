from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserForm, IncomeForm, ExpenseForm
from .models import Income, Expense, User

# Create your views here.


def home(request):
    return render(request, 'home.html')


def addUser(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        uf.save()
        return redirect("/")
    else:
        uf = UserForm
        message = "User Registration Form"
        return render(request, 'form.html', {'form': uf, 'message': message})


def addIncome(request):
    if request.method == "POST":
        inf = IncomeForm(request.POST)
        inf.save()
        return redirect("/")
    else:
        inf = IncomeForm
        message = "Add your Incomes here"
        return render(request, 'form.html', {'form': inf, 'message': message})


def addExpense(request):
    if request.method == "POST":
        ef = ExpenseForm(request.POST)
        ef.save()
        return redirect("/")
    else:
        ef = ExpenseForm
        message = "Add your Expenses here"
        return render(request, 'form.html', {'form': ef, 'message': message})


def incomeList(request):
    uid = request.session.get('userId')
    inli = Income.objects.filter(user_id=uid)
    d = {
        'il': inli,
    }
    return render(request, 'incomeList.html', d)


def expenseList(request):
    uid = request.session.get('userId')
    exli = Expense.objects.filter(user_id=uid)
    d = {
        'el': exli,
    }
    return render(request, 'expenseList.html', d)


def incomeEdit(request):
    id = request.GET.get('id')
    income = Income.objects.get(id=id)

    if request.method == "POST":
        incf = IncomeForm(request.POST, instance=income)
        incf.save()
        return redirect("/incomeList")

    else:
        incf = IncomeForm(instance=income)
        return render(request, 'form.html', {'form': incf})


def incomeDelete(request):
    id = request.GET.get('id')
    income = Income.objects.get(id=id)
    income.delete()
    return redirect("/incomeList")


def expenseDelete(request):
    id = request.GET.get('id')
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect("/expenseList")


def expenseEdit(request):
    id = request.GET.get('id')
    expense = Expense.objects.get(id=id)

    if request.method == "POST":
        encf = ExpenseForm(request.POST, instance=expense)
        encf.save()
        return redirect("/expenseList")

    else:
        encf = ExpenseForm(instance=expense)
        return render(request, 'form.html', {'form': encf})


"""def flogin(request):
    return render(request, 'forms.html', {'form': f})"""


def loginv(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('pwd')
        usr = authenticate(request, username=uname, password=password)

        if usr is not None:
            request.session['userId'] = usr.id
            login(request, usr)
            return redirect('/')
        else:
            return render(request, 'login.html', {"message": "Invalid Username or Password"})
    else:
        return render(request, 'login.html')


def logoutv(request):
    logout(request)
    return redirect("/")
