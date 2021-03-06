"""directory Logic."""

from datetime import datetime

from directory.models import AddressEntry
from directory.settings import DATABASE_WRITABLE


def create_directory_entry(name, address):
    """
    Create and save an entry, after checking if one already exists.
    Raise an exception if one is found
    :param name:
    :param address:
    :return:
    """
    entries = AddressEntry.objects.using(DATABASE_WRITABLE).filter(name=name,
                                                          address=address)
    if len(entries) == 0:
        new_item = AddressEntry(name=name, address=address,
                                date_created=datetime.now(), version=1)
        new_item.save(using=DATABASE_WRITABLE)
        return True
    else:
        return False


def update_directory_entry(name, address):
    """
    Update an entry, after checking if one already exists.  This should
        change the date_updated and version fields.
    Raise an exception if one is not found
    :param name:
    :param address:
    :return:
    """
    entries = AddressEntry.objects.using(DATABASE_WRITABLE).filter(name=name,
                                                          address=address)
    if len(entries) > 0:
        entries[0].version += 1
        entries[0].date_updated = datetime.now()
        entries[0].save(using=DATABASE_WRITABLE)
        return True
    else:
        return False


def delete_directory_entry(name, address):
    """
    Delete an entry, after checking if one already exists.
    Raise an exception if one is not found
    :param name:
    :param address:
    :return:
    """

    entries = AddressEntry.objects.using(DATABASE_WRITABLE).filter(name=name,
                                                          address=address)
    if len(entries) > 0:
        entries.delete()
        return True
    else:
        return False
