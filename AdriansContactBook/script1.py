
from ContactBook.models import MemberAddress, Member, MemberGroup

adres1 = MemberAddress()
adres1.name = "Domowy"
adres1.save()

adres2 = MemberAddress()
adres2.name = "Praca"
adres2.save()

adres3 = MemberAddress()
adres3.name = "Ulubiony"
adres3.save()

member1 = Member()
member1.nick = "Bolek"
member1.first_name = "Lech"
member1.last_name = "Wałęsa"
member1.description = "Koleś, który niestety został kapusiem"

member1.save()