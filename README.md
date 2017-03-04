# python-ordered-uuid

Overrides Python's UUID class to implement "Ordered UUID".

For more info about "Ordered UUID" see: https://www.percona.com/blog/2014/12/19/store-uuid-optimized-way/

Usage
=====

    from ordered_uuid import OrderedUUID

    hex_string = 'cdef89ab012345670123456789abcdef'
    OrderedUUID(hex_string)

    some_bytes = b'\xcd\xef\x89\xab\x01\x23\x45\x67\x01\x23\x45\x67\x89\xab\xcd\xef'
    OrderedUUID(bytes=some_bytes)


Installation
============

    pip install python-ordered-uuid
