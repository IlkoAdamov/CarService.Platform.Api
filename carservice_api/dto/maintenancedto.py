class MaintenanceDTO:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.type = kwargs.get("type")
        self.created_at = kwargs.get("created_at")
        self.car_id = kwargs.get("car_id_id")
    
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