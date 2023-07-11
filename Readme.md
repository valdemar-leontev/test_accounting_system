### 1. pip install sqlalchemy

### 2. Run migrate_models.bat
    migrate_models.bat

if you run this bat file without any options, you will migrate all models ending in _model.py throughout the project. But if you want to transfer only models from some folder, you should use the following variable. __It is important__ to note that when using a parametric query, filtering will go directly to the folders that contain the models.

    migrate_models.bat Справочники
    
or

    migrate_models.bat СборщикиФорм

### 3. Check database.db file in as_sys_core folder