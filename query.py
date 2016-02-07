"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
# Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
# Model.query.filter(Model.year < 1960).all()
#
# I know this should work, but I only get the first two results, for some reason...
# [<Model id=1 brand = Ford name = Model T>, <Model id=2 brand = Chrysler name = Imperial>, Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 25: ordinal not in range(128)
# The opposite, looking for models newer than 1960, using the '>' key works fine.

# Get all brands that were founded after 1920.
# Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
# Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
# Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands with that are either discontinued or founded before 1950.
#Brand.query.filter((Brand.discontinued == None) | (Brand.founded < 1950)).all()
#I get the same type of error I got with #3:
#[<Brand id=1, name = Ford>, <Brand id=2, name = Chrysler>, Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 25: ordinal not in range(128)


# Get any model whose brand_name is not Chevrolet.
#Model.query.filter(Model.brand_name != 'Chevrolet').all()
#Gives me the same type of unicode error, even though Model.brand_name == 'Chevrolet' works great!
#Aargh!

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_list = db.session.query(Model,
                                  Brand).filter(Model.year == year).outerjoin(Brand).all()

    for model, brand in model_list:
        if brand is not None:
            print model.name, model.brand_name, brand.headquarters
        else:
            print model.name, model.brand_name, "headquarters unknown"


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_list = Brand.query.options(db.joinedload('models')).all()
    for brand in brand_list:
        brand_name = brand.name
        model_list = []
        models = brand.models
        for model in models:
            model_list.append(model.name)
        print "Brand: %s \n %s \n\n" % (brand_name, model_list)



# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Takes in any string as parameter, and returns a list of objects
    that are brands whose name contains or is equal to the input string."""

    like_str = '%' + mystr + '%'
    brand_list = Brand.query.filter(Brand.name.like(like_str)).all()

    return brand_list


def get_models_between(start_year, end_year):
    """Takes in a start year and end year (two integers), and
    returns a list of objects that are models with years that fall between the
    start year and end year."""

    model_list = Model.query.filter(Model.year > start_year, Model.year < end_year).all()
    
    return model_list


# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# Since we did not attach a .all() or .first() or .one() at the end, we receive
# the actual sqlalchemy query object itself, and its location in memory, rather than
# a meaningful record. 


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a table that doesn't have any important inherent data of
# its own. Rather, it is a placeholder table to organize a many-to-many relationship
# between two meaningful tables. An association table would have foreign keys to 
# both of the other tables, and organizationally be placed between the other two.

