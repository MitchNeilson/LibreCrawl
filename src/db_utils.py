"""
Database utility module
Handles database path configuration and related utilities
"""
import os


def get_database_path(database_name):
    """
    Get the database file path, using DATABASE_DIR env var as prefix if set,
    otherwise using the default location (data/ directory in project root)
    
    Returns:
        str: Full path to the database file (users.db)
    """
    database_dir = os.getenv('DATABASE_DIR')
    if database_dir:
        # Use DATABASE_DIR as the prefix
        return os.path.join(database_dir, database_name)
    else:
        # Use default location: data/ directory in project root
        return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', database_name)
