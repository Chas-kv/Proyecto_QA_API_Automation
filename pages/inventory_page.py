# Logica de la pagina de inventario
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack_btn=page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge=page.locator(".shopping_cart_badge")   
        self.cart_link=page.locator(".shopping_cart_link")
        
    def add_backpack_to_cart(self):
        self.add_backpack_btn.click()
        
    def go_to_cart(self):
        self.cart_link.click()
        
    