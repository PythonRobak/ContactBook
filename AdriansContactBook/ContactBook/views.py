from django.shortcuts import render, HttpResponse, redirect
from ContactBook.models import MemberGroup, MemberAddress, MemberEmail, MemberPhone, Member

# Create your views here.

def main_window_view(request):
    all_members = Member.objects.all().order_by('last_name', 'first_name')
    ctx = {
        'all_members': all_members
    }
    return render(request, template_name="members_view.html", context=ctx)

def show_group_view(request, group_number):

    group = MemberGroup.objects.get(pk=group_number)
    members = group.member_group.all()

    ctx = {
        'group': group,
        'members': members
    }
    return render(request, template_name="group_details.html", context=ctx)

def show_groups_view(request):
    groups = MemberGroup.objects.all()
    ctx = {
        'groups': groups
    }
    return render(request, template_name="groups_view.html", context=ctx)

def add_group_view(request):
    if request.method == 'GET':
        return render(request, template_name="add_group_view.html")

    elif request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_to_add = MemberGroup.objects.create(name=group_name)

        try:
            group_to_add.save()
            groups = MemberGroup.objects.all()
            ctx = {
                'groups': groups
            }
            return render(request, template_name="groups_view.html", context=ctx)

        except Exception:
            return HttpResponse("Zapisywanie do bazy nie powiodło się!")

def delete_group_view(request, group_number):
    if request.method == 'GET':
        group = MemberGroup.objects.get(id=group_number)
        ctx = {
            'group': group
        }
        group.delete()

        return render(request, template_name="delete_group_view.html", context=ctx)

def show_address_view(request, member_number):

    address = MemberAddress.objects.get(pk=member_number)
    # address_name = address.name
    # country = address.country
    # state = address.state
    # city = address.city
    # street = address.street
    # house_nr = address.house_number
    # apartment_nr = address.apartment_number

    ctx = {
        'address' : address
    }

    return render(request, template_name="member_details.html", ctx=ctx)



def add_member_view(request):
    if request.method == 'GET':
        return render(request, template_name="add_member.html")

    elif request.method == 'POST':
        nick_name = request.POST.get('nick_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        member_to_add = Member.objects.create(nick=nick_name, first_name=first_name, last_name=last_name)
        ctx = {
            'nick_name': nick_name
        }

        try:
            member_to_add.save()
            return render(request, template_name="member_added.html", context=ctx)



        except Exception:
            return HttpResponse("Zapisywanie do bazy nie powiodło się!")


def show_member_view(request, member_number):


    member = Member.objects.get(pk=member_number)
    adresses = member.adress
    groups = member.group.all()

    ctx = {
        'member': member,
        'address': adresses,
        'groups': groups
    }

    return render(request, template_name="member_details.html", context=ctx)

def modify_member_view(request, member_number):
    member = Member.objects.get(pk=member_number)
    addresses = member.adress
    groups = member.group.all()

    ctx = {
        'member': member,
        'address': addresses,
        'groups': groups
    }
    if request.method == 'POST':
        member.nick = request.POST.get('nick_name')
        member.first_name = request.POST.get('first_name')
        member.last_name = request.POST.get('last_name')
        member.description = request.POST.get('description')
        member.save()

        return redirect('/')
        # return render(request, template_name="modify_member_view.html", context=ctx)

    elif request.method == 'GET':
        return render(request, template_name="modify_member_view.html", context=ctx)


def delete_member_view(request, member_number):
    if request.method == 'GET':
        member = Member.objects.get(id=member_number)
        ctx = {
            'member': member
        }
        member.delete()
        return render(request, template_name="member_deleted.html", context=ctx)

def add_to_group_view(request, member_number):
    member = Member.objects.get(pk=member_number)
    if request.method == 'POST':
        selected_groups = request.POST.getlist('selected_groups')

        for i in selected_groups:
            group = MemberGroup.objects.get(pk=i)
            group.member_group.add(member_number)
            group.save()

        response_view = redirect(f"/show/{member_number}")

        return response_view

    elif request.method == 'GET':

        member_groups = member.group.all()
        avaliable_groups = []

        for element in MemberGroup.objects.all():
            if not element in member_groups:
                avaliable_groups.append(element)

        ctx = {
            'member': member,
            'avaliable_groups': avaliable_groups
        }

        return render(request, template_name="add_to_group_view.html", context=ctx)

def remove_from_group_view(request, member_number):
    member = Member.objects.get(pk=member_number)
    adresses = member.adress
    groups = member.group.all()
    ctx = {
        'adresses': adresses,
        'groups': groups
    }

    if request.method == 'POST':
        selected_groups = request.POST.getlist('selected_groups')
        print(selected_groups)

        # Member.group.through.objects.filter(id__in=selected_groups).delete()  <--- do opanowania wieczorem

        for i in selected_groups:
            group = MemberGroup.objects.get(pk=i)
            member.group.remove(group)

        response_view = redirect(f"/show/{member_number}")

        return response_view

        # return render(request, template_name="member_details.html", context=ctx)

    elif request.method == 'GET':

        member_groups = member.group.all()

        ctx = {
            'member': member,
            'avaliable_groups': member_groups
        }

        return render(request, template_name="remove_from_group_view.html", context=ctx)

# def add_details_view(request, member_number):
#     if request.method == "POST":
#         member = Member.objects.get(pk=member_number)
#         member.adress = request.POST.get()
#
#     if request.method == "GET":
#         member = Member.objects.get(pk=member_number)









