class CarInfoDTO:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.vin = kwargs.get("vin")
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.fuel = kwargs.get("fuel")
        self.power = kwargs.get("power")
        self.horse_power = kwargs.get("horse_power")
        self.plate = kwargs.get("plate")
    
    def to_dict(self):
        return self.__dict__
    
    # @classmethod
    # def from_dict(cls, dict_obj):
    #     return cls(**dict_obj)

    @classmethod
    def to_dto(cls, query_set):
        return cls(**query_set)
    
    @classmethod
    def to_list_of_dto(cls, query_set):
        list_of_car_item = []
        for item in query_set:
            list_of_car_item.append(cls(**item.__dict__))
        return list_of_car_item
    
    @classmethod
    def to_list_of_dict(cls, list_of_dto):
        list_of_car_item = []
        for item in list_of_dto:
            list_of_car_item.append(item.__dict__)
        return list_of_car_item