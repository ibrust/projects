__all__ = ['reactiveProperty']

def reactiveProperty(propertyName: str, propertyType):

    internalPropertyName = "_" + propertyName

    @property
    def prop(self):
        return getattr(self, internalPropertyName)

    @prop.setter
    def prop(self, value):
        if value is not None and not isinstance(value, propertyType):
            raise TypeError(f"{propertyName} set to {value} which is not of expected type {propertyType}")
        setattr(self, internalPropertyName, value)
        self.publisher.on_next(value)

    return prop