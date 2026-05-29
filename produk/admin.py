from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # =========================
    # LIST PAGE
    # =========================
    list_display = (
        'image_preview',
        'name',
        'category_badge',
        'price',
        'availability',
        'created_at',
    )

    list_display_links = (
        'image_preview',
        'name',
    )
    
    list_editable = (
        'price',
        'availability',
    )
    
    search_fields = (
        'name',
        'category',
        'sub_category',
    )

    list_filter = (
        'category',
        'availability',
    )

    ordering = ('-created_at',)

    list_per_page = 10

    # =========================
    # DETAIL PAGE
    # =========================
    readonly_fields = (
        'image_large_preview',
        'created_at',
    )

    fieldsets = (

        ('Basic Information', {
            'classes': ('wide',),
            'fields': (
                'name',
                'tagline',
                'description',
            )
        }),

        ('Category & Pricing', {
            'classes': ('wide',),
            'fields': (
                ('category', 'sub_category'),
                'price',
            )
        }),

        ('Product Specifications', {
            'classes': ('wide',),
            'fields': (
                ('material', 'dimension'),
                'availability',
            )
        }),

        ('Product Image', {
            'classes': ('wide',),
            'fields': (
                'image',
                'image_large_preview',
            )
        }),

        ('System Information', {
            'classes': ('collapse',),
            'fields': (
                'created_at',
            )
        }),

    )

    # =========================
    # IMAGE PREVIEW
    # =========================
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '''
                <div style="
                    width:72px;
                    height:72px;
                    overflow:hidden;
                    border-radius:14px;
                    border:1px solid rgba(0,0,0,.08);
                    background:#f8f6f3;
                ">
                    <img src="{}"
                         style="
                            width:100%;
                            height:100%;
                            object-fit:cover;
                         "
                    />
                </div>
                ''',
                obj.image.url
            )
        return "-"

    image_preview.short_description = ''

    # =========================
    # CATEGORY BADGE
    # =========================
    def category_badge(self, obj):
        return format_html(
            '''
            <span style="
                padding:6px 14px;
                border-radius:999px;
                background:#f3eee7;
                color:#8b6f4e;
                font-size:12px;
                font-weight:500;
                letter-spacing:.02em;
            ">
                {}
            </span>
            ''',
            obj.category
        )

    category_badge.short_description = 'Category'

    # =========================
    # PRICE FORMAT
    # =========================
    def formatted_price(self, obj):

        try:
            price = float(obj.price)
            return f"{price:,.0f}".replace(",", ".")
        except:
            return f"{obj.price}"

    formatted_price.short_description = 'Price'

    # =========================
    # STOCK BADGE
    # =========================
    def availability_badge(self, obj):

        color = "#4a8c5e"
        bg = "rgba(74,140,94,.12)"

        if obj.availability.lower() != "in stock":
            color = "#c0392b"
            bg = "rgba(192,57,43,.10)"

        return format_html(
            '''
            <span style="
                padding:6px 12px;
                border-radius:999px;
                background:{};
                color:{};
                font-size:12px;
                font-weight:500;
                letter-spacing:.02em;
            ">
                {}
            </span>
            ''',
            bg,
            color,
            obj.availability
        )

    availability_badge.short_description = 'Availability'

    # =========================
    # LARGE IMAGE PREVIEW
    # =========================
    def image_large_preview(self, obj):

        if obj.image:
            return format_html(
                '''
                <div style="
                    margin-top:10px;
                ">
                    <img src="{}"
                         style="
                            width:340px;
                            border-radius:18px;
                            object-fit:cover;
                            border:1px solid rgba(0,0,0,.08);
                            box-shadow:0 10px 30px rgba(0,0,0,.06);
                         "
                    />
                </div>
                ''',
                obj.image.url
            )

        return format_html(
            '''
            <div style="
                padding:30px;
                border:1px dashed #d6cec3;
                border-radius:14px;
                color:#9b9288;
                width:340px;
                text-align:center;
                background:#faf8f5;
            ">
                No image uploaded
            </div>
            '''
        )

    image_large_preview.short_description = 'Preview'