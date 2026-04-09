from pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    
    # Verificamos que entramos a la tienda
    assert "inventory.html" in page.url

def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("usuario_erroneo", "clave_falsa")
    
    # Verificamos que aparezca el mensaje de error
    assert login.error_msg.is_visible()