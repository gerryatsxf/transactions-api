from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.category import Category


T = TypeVar("T", bound="CategoryGroupWithCategories")


@attr.s(auto_attribs=True)
class CategoryGroupWithCategories:
    """
    Attributes:
        id (str):
        name (str):
        hidden (bool): Whether or not the category group is hidden
        deleted (bool): Whether or not the category group has been deleted.  Deleted category groups will only be
            included in delta requests.
        categories (List['Category']): Category group categories.  Amounts (budgeted, activity, balance, etc.) are
            specific to the current budget month (UTC).
    """

    id: str
    name: str
    hidden: bool
    deleted: bool
    categories: List["Category"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        hidden = self.hidden
        deleted = self.deleted
        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()

            categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "hidden": hidden,
                "deleted": deleted,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category import Category

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        hidden = d.pop("hidden")

        deleted = d.pop("deleted")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = Category.from_dict(categories_item_data)

            categories.append(categories_item)

        category_group_with_categories = cls(
            id=id,
            name=name,
            hidden=hidden,
            deleted=deleted,
            categories=categories,
        )

        category_group_with_categories.additional_properties = d
        return category_group_with_categories

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
