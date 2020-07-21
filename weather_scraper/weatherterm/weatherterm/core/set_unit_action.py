from argparse import Action
from weatherterm.core import Unit

#custom action for argparse. Use to associate a custom value with the arg object's attribute - the custom value will be a member of the enum Unit.
class SetUnitAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        unit = Unit[values.upper()]
        setattr(namespace, self.dest, unit)
