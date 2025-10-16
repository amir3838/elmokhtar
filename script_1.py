# Create the CSS file
css_content = '''/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    min-height: 100vh;
    color: #333;
    line-height: 1.6;
}

.app-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* Header Styles */
.header {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.header-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    color: #1e3c72;
    font-size: 2rem;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.header-actions {
    display: flex;
    gap: 1rem;
}

.cart-btn {
    background: #1e3c72;
    color: white;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 50px;
    cursor: pointer;
    position: relative;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3);
}

.cart-btn:hover {
    background: #2a5298;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4);
}

.cart-count {
    background: #ff4757;
    color: white;
    border-radius: 50%;
    width: 1.5rem;
    height: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    font-weight: bold;
}

/* Main Content */
.main-content {
    flex: 1;
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem 1rem;
    width: 100%;
}

/* Page System */
.page {
    display: none;
    animation: fadeIn 0.3s ease-in-out;
}

.page.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Welcome Section */
.welcome-section {
    text-align: center;
    background: rgba(255, 255, 255, 0.95);
    padding: 2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.welcome-section h2 {
    color: #1e3c72;
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.welcome-section p {
    color: #666;
    font-size: 1.1rem;
}

/* Categories Grid */
.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.category-btn {
    background: rgba(255, 255, 255, 0.95);
    border: none;
    padding: 2rem 1rem;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
}

.category-btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
    background: rgba(255, 255, 255, 1);
}

.category-icon {
    font-size: 3rem;
}

.category-name {
    color: #1e3c72;
    font-size: 1.1rem;
    font-weight: 600;
}

/* Page Header */
.page-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
    background: rgba(255, 255, 255, 0.95);
    padding: 1rem 1.5rem;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.back-btn {
    background: #1e3c72;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.back-btn:hover {
    background: #2a5298;
    transform: translateX(5px);
}

#category-title {
    color: #1e3c72;
    font-size: 1.5rem;
    margin: 0;
}

/* Products Container */
.products-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.product-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 1.5rem;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.product-name {
    color: #1e3c72;
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    line-height: 1.4;
}

.product-description {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 1rem;
    line-height: 1.4;
}

.product-note {
    background: #fff3cd;
    color: #856404;
    padding: 0.5rem;
    border-radius: 10px;
    font-size: 0.8rem;
    margin-bottom: 1rem;
    border: 1px solid #ffeaa7;
}

.product-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.product-price {
    color: #27ae60;
    font-size: 1.2rem;
    font-weight: bold;
}

.add-to-cart {
    background: #27ae60;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 600;
}

.add-to-cart:hover {
    background: #219a52;
    transform: scale(1.05);
}

/* Cart Styles */
.cart-content {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.cart-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    border-bottom: 1px solid #eee;
    margin-bottom: 1rem;
}

.cart-item:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.item-info h4 {
    color: #1e3c72;
    margin-bottom: 0.25rem;
}

.item-info p {
    color: #666;
    font-size: 0.9rem;
}

.item-controls {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.quantity-controls {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.qty-btn {
    background: #1e3c72;
    color: white;
    border: none;
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

.qty-btn:hover {
    background: #2a5298;
}

.quantity {
    font-weight: bold;
    min-width: 2rem;
    text-align: center;
}

.remove-item {
    background: #ff4757;
    color: white;
    border: none;
    padding: 0.5rem;
    border-radius: 50%;
    cursor: pointer;
    width: 2rem;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.remove-item:hover {
    background: #ff3838;
}

.cart-summary {
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 2px solid #eee;
}

.summary-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding: 0.5rem 0;
}

.summary-row.total {
    font-size: 1.2rem;
    font-weight: bold;
    color: #1e3c72;
    border-top: 2px solid #1e3c72;
    padding-top: 1rem;
    margin-top: 1rem;
}

.checkout-btn {
    width: 100%;
    background: #27ae60;
    color: white;
    border: none;
    padding: 1rem;
    border-radius: 25px;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 1rem;
}

.checkout-btn:hover {
    background: #219a52;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(39, 174, 96, 0.3);
}

/* Checkout Form */
.checkout-content {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #1e3c72;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #ddd;
    border-radius: 10px;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #1e3c72;
    box-shadow: 0 0 0 3px rgba(30, 60, 114, 0.1);
}

.form-group small {
    color: #666;
    font-size: 0.8rem;
    margin-top: 0.25rem;
    display: block;
}

.location-btn {
    background: #3498db;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 25px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    font-weight: 600;
}

.location-btn:hover {
    background: #2980b9;
    transform: translateY(-2px);
}

.location-btn:disabled {
    background: #bdc3c7;
    cursor: not-allowed;
    transform: none;
}

#location-status {
    margin-top: 1rem;
    padding: 0.75rem;
    border-radius: 10px;
    font-size: 0.9rem;
    display: none;
}

#location-status.success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    display: block;
}

#location-status.error {
    background: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    display: block;
}

#location-status.loading {
    background: #d1ecf1;
    color: #0c5460;
    border: 1px solid #bee5eb;
    display: block;
}

#location-info {
    margin-top: 0.5rem;
    font-size: 0.8rem;
    color: #666;
}

.submit-btn {
    width: 100%;
    background: #25d366;
    color: white;
    border: none;
    padding: 1rem;
    border-radius: 25px;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.submit-btn:hover {
    background: #128c7e;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3);
}

.submit-btn:disabled {
    background: #bdc3c7;
    cursor: not-allowed;
    transform: none;
}

/* Branches */
.branches-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
}

.branch-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 1.5rem;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.branch-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.branch-name {
    color: #1e3c72;
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

.branch-address {
    color: #666;
    margin-bottom: 0.75rem;
    line-height: 1.4;
}

.branch-phone {
    color: #27ae60;
    font-weight: 600;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.branch-map {
    background: #3498db;
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
}

.branch-map:hover {
    background: #2980b9;
    transform: translateY(-2px);
}

/* Bottom Navigation */
.bottom-nav {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
}

.nav-btn {
    background: rgba(255, 255, 255, 0.95);
    border: none;
    padding: 1rem 2rem;
    border-radius: 25px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    color: #1e3c72;
    font-weight: 600;
}

.nav-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    background: rgba(255, 255, 255, 1);
}

/* Empty States */
.empty-cart {
    text-align: center;
    padding: 3rem;
    color: #666;
}

.empty-cart h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: #1e3c72;
}

/* Responsive Design */
@media (max-width: 768px) {
    .logo {
        font-size: 1.5rem;
    }
    
    .categories-grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }
    
    .category-btn {
        padding: 1.5rem 1rem;
    }
    
    .category-icon {
        font-size: 2.5rem;
    }
    
    .products-container {
        grid-template-columns: 1fr;
    }
    
    .branches-container {
        grid-template-columns: 1fr;
    }
    
    .page-header {
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .main-content {
        padding: 1rem;
    }
    
    .cart-item {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .item-controls {
        align-self: stretch;
        justify-content: space-between;
    }
}

@media (max-width: 480px) {
    .welcome-section {
        padding: 1.5rem;
    }
    
    .welcome-section h2 {
        font-size: 1.5rem;
    }
    
    .categories-grid {
        grid-template-columns: 1fr;
    }
    
    .header-content {
        padding: 0 0.5rem;
    }
    
    .main-content {
        padding: 0.5rem;
    }
}'''

# Write CSS file
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ style.css file created successfully")