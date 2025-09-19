from .models import (
    Product,
    Category,
    Store,
    Contact,
    Courier,
    CartItem,
    Combo,
    StoreReview,
)
from modeltranslation.translator import TranslationOptions, register


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "product_name",
        "description",
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("category_name",)


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = (
        "store_name",
        "description", "address",
    )


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Courier)
class CourierTranslationOptions(TranslationOptions):
    fields = ("courier",)


@register(CartItem)
class CartItemTranslationOptions(TranslationOptions):
    fields = (
        "cart",
        "product",
        "combo",
    )


@register(Combo)
class ComboTranslationOptions(TranslationOptions):
    fields = (
        "combo_name",
        "description",
    )


@register(StoreReview)
class StoreReviewTranslationOptions(TranslationOptions):
    fields = (
        "client",
        "store",
        "text",
    )
