from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase_flow(page):
    # 1. Login
    login=LoginPage(page)
    login.navigate()
    login.login("standard_user","secret_sauce")
    
    # 2. Agregar al carrito
    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    
    # Verificación intermedia: ¿Hay 1 item en el carrito?
    assert inventory.cart_badge.text_content() == "1"
    
    # 3. Ir al carrito
    inventory.go_to_cart()
    assert "cart.html" in page.url
    
    # 4. ir al checkout
    checkout = CheckoutPage(page)
    # Ir al checkout (puedes usar el botón directamente)
    page.locator("[data-test='checkout']").click()
    
    checkout.fill_checkout_info("Juan", "Perez", "05001")
    checkout.finish_checkout()
    
    # Verificación final: ¿Salió el mensaje de éxito?
    assert checkout.success_message.text_content() == "Thank you for your order!"