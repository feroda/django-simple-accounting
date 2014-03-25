from django.core.management.base import BaseCommand, CommandError
from simple_accounting.models import LedgerEntry, Account

class Command(BaseCommand):
    args = ""
    help = 'Recompute all account balances basing on ledger_entries'

    def handle(self, *args, **options):

        for ac in Account.objects.all():
            prev_balance_current = 0
            for ledger_entry in ac.ledger_entries.order_by('entry_id'):
                ledger_entry.balance_current = prev_balance_current + ledger_entry.amount 
                prev_balance_current = ledger_entry.balance_current
                super(LedgerEntry, ledger_entry).save()
            print("account=%s, balance=%s" % (ac, ac.balance))
