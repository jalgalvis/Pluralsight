from reader1.compressed.bzipped import opener as bz2_opener
from reader1.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']