# Create the JavaScript file
js_content = '''// Data
const menuData = {
    storeName: "فسخاني المختار",
    whatsappNumber: "+201000348425",
    noteText: "سعر الكيلو قبل التخلي (ليس بعد التخلي)",
    
    categories: {
        "salted-fish": {
            name: "الأسماك المملحة",
            products: [
                { name: "كيلو فسيخ بورى بلدى", price: 500 },
                { name: "نص فسيخ بورى بلدى", price: 250 },
                { name: "ربع فسيخ بورى بلدى", price: 125 },
                { name: "كيلو رنجة هولندى سوبر", price: 180 },
                { name: "نص رنجة هولندى سوبر", price: 90 },
                { name: "ربع رنجة هولندى سوبر", price: 45 },
                { name: "كيلو سلطة رنجة", price: 260 },
                { name: "نص سلطة رنجة", price: 130 },
                { name: "ربع سلطة رنجة", price: 65 },
                { name: "كيلو رنجة بطارخ هولندى", price: 220 },
                { name: "نص رنجة بطارخ هولندى", price: 110 },
                { name: "ربع رنجة بطارخ هولندى", price: 55 },
                { name: "كيلو سلطة رنجة بطارخ", price: 300 },
                { name: "نص سلطة رنجة بطارخ", price: 150 },
                { name: "ربع سلطة رنجة بطارخ", price: 75 },
                { name: "كيلو سردين بلدى –", price: 240 },
                { name: "نص سردين بلدى –", price: 120 },
                { name: "ربع سردين بلدى –", price: 60 },
                { name: "كيلو سلطة تونة", price: 360 },
                { name: "نص سلطة تونة", price: 180 },
                { name: "ربع سلطة تونة", price: 90 },
                { name: "كيلو ملوحة اسوانى كبير", price: 400 },
                { name: "نص ملوحة اسوانى كبير", price: 200 },
                { name: "ربع ملوحة اسوانى كبير", price: 100 },
                { name: "كيلو ملوحة اسوانى وسط", price: 360 },
                { name: "نص ملوحة اسوانى وسط", price: 180 },
                { name: "ربع ملوحة اسوانى وسط", price: 90 }
            ]
        },
        
        "fillet-fish": {
            name: "الأسماك الفيليه",
            products: [
                { name: "كيلو فسيخ فيليه", price: 900 },
                { name: "نص فسيخ فيليه", price: 450 },
                { name: "ربع فسيخ فيليه", price: 225 },
                { name: "كيلو ملوحة فيليه لحم", price: 600 },
                { name: "نص ملوحة فيليه لحم", price: 300 },
                { name: "ربع ملوحة فيليه لحم", price: 150 },
                { name: "كيلو رنجة فيليه هولندى بزيت الزيتون", price: 220 },
                { name: "نص رنجة فيليه هولندى بزيت الزيتون", price: 110 },
                { name: "ربع رنجة فيليه هولندى بزيت الزيتون", price: 55 },
                { name: "كيلو رنجة فيليه بالزيت والليمون", price: 200 },
                { name: "نص رنجة فيليه بالزيت والليمون", price: 100 },
                { name: "ربع رنجة فيليه بالزيت والليمون", price: 50 },
                { name: "كيلو سردين مخلى بالزيت والليمون", price: 240 },
                { name: "نص سردين مخلى بالزيت والليمون", price: 120 },
                { name: "ربع سردين مخلى بالزيت والليمون", price: 60 },
                { name: "كيلو سردين مخلى بزيت الزيتون", price: 280 },
                { name: "نص سردين مخلى بزيت الزيتون", price: 140 },
                { name: "ربع سردين مخلى بزيت الزيتون", price: 70 }
            ]
        },
        
        "caviar-roe": {
            name: "البطارخ والكافيار",
            products: [
                { name: "كيلو بطارخ خرز", price: 800 },
                { name: "نص بطارخ خرز", price: 400 },
                { name: "ربع بطارخ خرز", price: 200 },
                { name: "كيلو بطارخ ناعمة", price: 500 },
                { name: "نص بطارخ ناعمة", price: 250 },
                { name: "ربع بطارخ ناعمة", price: 125 },
                { name: "كيلوا بطارخ بورى بلدى", price: 3400 },
                { name: "نص بطارخ بورى بلدى", price: 1700 },
                { name: "ربع بطارخ بورى بلدى", price: 850 },
                { name: "100 جرام بطارخ بورى بلدى", price: 340 }
            ]
        },
        
        "other-items": {
            name: "أصناف أخرى",
            products: [
                { name: "كيلو بساريه بلدى", price: 140 },
                { name: "نص بساريه بلدى", price: 70 },
                { name: "ربع بساريه بلدى", price: 35 },
                { name: "كيلو انشوجة", price: 360 },
                { name: "كيلو انشوجة", price: 180 },
                { name: "كيلو انشوجة", price: 90 }
            ]
        },
        
        "individual-meals": {
            name: "وجبات فردية",
            products: [
                { name: "وجبة رنجة فيليه هولندى", price: 100 },
                { name: "وجبة رنجة هولندى بزيت الزيتون", price: 120 },
                { name: "وجبة فسيخ بزيت والليمون", price: 170 },
                { name: "وجبة فسيخ بالفلفل الحار", price: 180 },
                { name: "وجبة فسيخ بزيت الزيتون", price: 190 },
                { name: "وجبة سردين فيليه بالزيت والليمون", price: 110 },
                { name: "وجبة سردين فيليه بزيت الزيتون", price: 120 },
                { name: "وجبة سردين فيليه بالطحينة والبصل", price: 120 },
                { name: "وجبة بطارخ خرز", price: 230 },
                { name: "وجبة بطارخ ناعمة", price: 140 },
                { name: "وجبة بطارخ ميكس", price: 189 },
                { name: "وجبة ملوحة اسوانى فيليه", price: 180 },
                { name: "وجبة ملوحة وسط", price: 160 }
            ]
        },
        
        "appetizers": {
            name: "مقبلات",
            products: [
                { name: "رنجة موس ( رنجة مفرومة بالخضار والمايونيز والمستردة تقدم مع عيش بلدى وبصل اخضر )", price: 180 },
                { name: "رنجة بوبس ( مكعبات رنجه مع صوص رانش وعيش بلدي وبصل وليمون )", price: 130 },
                { name: "لوديد شيبس بالبطارخ ( شيبسي بصوص الشيدر وعليها بطارخ وبصل اخضر وهلابينو سلايز )", price: 150 }
            ]
        },
        
        "sandwiches": {
            name: "سندويشات",
            products: [
                { name: "ساندوتش تونة", price: 40 },
                { name: "ساندوتش بطارخ خرز", price: 130 },
                { name: "ساندوتش ملوحة بالطحينة سبريت", price: 70 },
                { name: "ساندوتش فسيخ", price: 90 },
                { name: "ساندوتش فسيخ بالليمون وزيت الزيتون", price: 100 },
                { name: "ساندوتش رنجة", price: 50 },
                { name: "ساندوتش سردين", price: 40 }
            ]
        },
        
        "salads-additions": {
            name: "السلطات والإضافات",
            products: [
                { name: "سلطة طحينه بالكافيار", price: 100 },
                { name: "سلطة طحينه بالبطارخ جنيه", price: 50 },
                { name: "بصل اخضر", price: 20 },
                { name: "طحينه", price: 20 },
                { name: "ليمون", price: 10 },
                { name: "خضار مشكل", price: 40 },
                { name: "باسكت عيش", price: 20 }
            ]
        },
        
        "family-meals": {
            name: "وجبات عائلية",
            products: [
                { 
                    name: "وجبه الحادقه", 
                    price: 260,
                    description: "١/٤ ملوحه - ١/٢ رنجه - طبق بصل - طبق طحينه - عيش - طبق يساريا"
                },
                { 
                    name: "وجبه المدلعه", 
                    price: 370,
                    description: "١/٤ فسيخ - ١/٢ رنجه - طبق بصل - طبق طحينه - طبق بساريا - عيش - طبق سردين"
                },
                { 
                    name: "وجبه الصحاب", 
                    price: 470,
                    description: "١/٤ فسيخ - ١/٤ ملوحه - ١/٢ رنجه - طبق سردين - طبق بساريا - عيش - طبق بصل"
                },
                { 
                    name: "وجبه العيله", 
                    price: 570,
                    description: "١/٢ فسيخ - ١/٤ ملوحه - ١/٢ رنجه - طبق بساريا - طبق طحينه - طبق بصل - طبق خضار مشكل - عيش"
                },
                { 
                    name: "وجبه الجامدين", 
                    price: 1100,
                    description: "كيلوافسيخ - نص ملوحه - كيلوا رنجه - طبق بساريا - 2طبق طحينه - 2طبق بصل - 2طبق خضار مشكل - عيش - سلطه بطارخ - سلطه كافيار"
                },
                { 
                    name: "وجبه العيله الكبيره", 
                    price: 1800,
                    description: "كيلوا ونص فسيخ - كيلوا إلا ربع ملوحه - كيلوا ونص رنجه - ٢ طحينه - ٢ بصل - ٢طبق خضار مشكل - ٢سلطه بطارخ - ٢سلطه كافيار - عيش بلدي"
                }
            ]
        }
    },
    
    branches: [
        {
            name: "دار السلام",
            address: "٣ ش احمد ذكي بجوار بنزينة موبيل",
            phone: "01003378244",
            mapLink: "https://maps.google.com/?q=Ahmed+Zaki%2C+Ezbet+Nafie%2C+El+Basatin%2C+Cairo+Governorate&ftid=0x145847842755ea5d:0xf7e90d83945450cb"
        },
        {
            name: "جمال عبد الناصر جسر السويس",
            address: "٣ ش القرش متفرع من ش جمال عبد الناصر امام مستشفى تبارك",
            phone: "01003387644",
            mapLink: "https://goo.gl/maps/w8PZYhuo6sDCFqwy6"
        },
        {
            name: "شارع الأربعين",
            address: "ش الأربعين متفرع من جسر السويس - خلف حديقة بدر",
            phone: "01040669910",
            mapLink: "https://goo.gl/maps/DiX9rTVi2JfyTn2x6"
        },
        {
            name: "الخصوص",
            address: "1 ش السيدة خديجة - ميدان الخصوص",
            phone: "01003362446",
            mapLink: "https://goo.gl/maps/WjHH9AG25oZGt1Wb7"
        },
        {
            name: "مدينة السلام",
            address: "ميدان اسبيكو",
            phone: "01040659000",
            mapLink: "https://goo.gl/maps/E2bxdoNyhnjq71mj6"
        },
        {
            name: "مصر الجديدة",
            address: "10أبوبكر الصديق بجوار اولاد رجب وأسماك ابو غالي",
            phone: "01003362446",
            mapLink: "https://maps.app.goo.gl/3QKXn1FHUjtZQjLt9"
        },
        {
            name: "العبور",
            address: "شارع الشباب العمومي امام الجامع الكبير بجوار صيدليه العزبي",
            phone: "01000348425",
            mapLink: "https://maps.app.goo.gl/zhuLh4XPZwbDD5R47?g_st=iwb"
        },
        {
            name: "فيصل",
            address: "شارع كعابيش بجوار التوحيد والنور امام أوكازيون ماركت",
            phone: "01040668870",
            mapLink: "https://maps.app.goo.gl/6YKDjzJEqywJpcav6?g_st=com.google.maps.preview.copy"
        }
    ]
};

// Application State
let currentPage = 'home';
let currentCategory = null;
let cart = JSON.parse(localStorage.getItem('feskhany-cart') || '[]');
let customerLocation = null;

// DOM Elements
const pages = {
    home: document.getElementById('home-page'),
    category: document.getElementById('category-page'),
    cart: document.getElementById('cart-page'),
    checkout: document.getElementById('checkout-page'),
    branches: document.getElementById('branches-page')
};

// Initialize App
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    updateCartCount();
    loadBranches();
    showPage('home');
});

// Event Listeners
function setupEventListeners() {
    // Category buttons
    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const categoryId = e.currentTarget.getAttribute('data-category');
            showCategory(categoryId);
        });
    });
    
    // Navigation buttons
    document.getElementById('back-to-home').addEventListener('click', () => showPage('home'));
    document.getElementById('back-from-cart').addEventListener('click', () => showPage(currentPage === 'checkout' ? 'home' : 'category'));
    document.getElementById('back-from-checkout').addEventListener('click', () => showPage('cart'));
    document.getElementById('back-from-branches').addEventListener('click', () => showPage('home'));
    
    // Cart button
    document.getElementById('cart-btn').addEventListener('click', () => showPage('cart'));
    
    // Checkout button
    document.getElementById('checkout-btn').addEventListener('click', () => showPage('checkout'));
    
    // Branches button
    document.getElementById('branches-btn').addEventListener('click', () => showPage('branches'));
    
    // Location button
    document.getElementById('location-btn').addEventListener('click', getCurrentLocation);
    
    // Checkout form
    document.getElementById('checkout-form').addEventListener('submit', handleCheckout);
}

// Page Navigation
function showPage(pageName) {
    // Hide all pages
    Object.values(pages).forEach(page => page.classList.remove('active'));
    
    // Show target page
    if (pages[pageName]) {
        pages[pageName].classList.add('active');
        currentPage = pageName;
        
        // Special handling for specific pages
        if (pageName === 'cart') {
            loadCartItems();
        }
    }
}

function showCategory(categoryId) {
    currentCategory = categoryId;
    const category = menuData.categories[categoryId];
    
    if (!category) return;
    
    // Update category title
    document.getElementById('category-title').textContent = category.name;
    
    // Load products
    loadCategoryProducts(category.products);
    
    showPage('category');
}

// Product Loading
function loadCategoryProducts(products) {
    const container = document.getElementById('products-container');
    container.innerHTML = '';
    
    products.forEach((product, index) => {
        const productCard = createProductCard(product, index);
        container.appendChild(productCard);
    });
}

function createProductCard(product, index) {
    const card = document.createElement('div');
    card.className = 'product-card';
    
    const description = product.description ? `<div class="product-description">${product.description}</div>` : '';
    
    card.innerHTML = `
        <div class="product-name">${product.name}</div>
        ${description}
        <div class="product-note">${menuData.noteText}</div>
        <div class="product-footer">
            <div class="product-price">${product.price} جنيه</div>
            <button class="add-to-cart" onclick="addToCart('${currentCategory}', ${index})">
                إضافة للسلة
            </button>
        </div>
    `;
    
    return card;
}

// Cart Functions
function addToCart(categoryId, productIndex) {
    const category = menuData.categories[categoryId];
    const product = category.products[productIndex];
    
    const existingItem = cart.find(item => 
        item.name === product.name && item.category === categoryId
    );
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            name: product.name,
            price: product.price,
            quantity: 1,
            category: categoryId,
            description: product.description || ''
        });
    }
    
    saveCart();
    updateCartCount();
    
    // Visual feedback
    const btn = event.target;
    const originalText = btn.textContent;
    btn.textContent = 'تم الإضافة ✓';
    btn.style.background = '#27ae60';
    
    setTimeout(() => {
        btn.textContent = originalText;
        btn.style.background = '';
    }, 1000);
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
    updateCartCount();
    loadCartItems();
}

function updateQuantity(index, change) {
    if (cart[index]) {
        cart[index].quantity += change;
        
        if (cart[index].quantity <= 0) {
            removeFromCart(index);
            return;
        }
        
        saveCart();
        updateCartCount();
        loadCartItems();
    }
}

function loadCartItems() {
    const container = document.getElementById('cart-items');
    const summary = document.getElementById('cart-summary');
    
    if (cart.length === 0) {
        container.innerHTML = `
            <div class="empty-cart">
                <h3>السلة فارغة</h3>
                <p>لم تقم بإضافة أي منتجات بعد</p>
            </div>
        `;
        summary.style.display = 'none';
        return;
    }
    
    summary.style.display = 'block';
    container.innerHTML = '';
    
    let subtotal = 0;
    
    cart.forEach((item, index) => {
        const lineTotal = item.price * item.quantity;
        subtotal += lineTotal;
        
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <div class="item-info">
                <h4>${item.name}</h4>
                <p>${item.price} جنيه × ${item.quantity} = ${lineTotal} جنيه</p>
            </div>
            <div class="item-controls">
                <div class="quantity-controls">
                    <button class="qty-btn" onclick="updateQuantity(${index}, -1)">-</button>
                    <span class="quantity">${item.quantity}</span>
                    <button class="qty-btn" onclick="updateQuantity(${index}, 1)">+</button>
                </div>
                <button class="remove-item" onclick="removeFromCart(${index})">×</button>
            </div>
        `;
        
        container.appendChild(cartItem);
    });
    
    // Update totals
    document.getElementById('subtotal').textContent = `${subtotal} جنيه`;
    document.getElementById('total').textContent = `${subtotal} جنيه`;
}

function updateCartCount() {
    const count = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.getElementById('cart-count').textContent = count;
}

function saveCart() {
    localStorage.setItem('feskhany-cart', JSON.stringify(cart));
}

// Location Functions
function getCurrentLocation() {
    const btn = document.getElementById('location-btn');
    const status = document.getElementById('location-status');
    const info = document.getElementById('location-info');
    
    if (!navigator.geolocation) {
        showLocationStatus('error', 'الجهاز لا يدعم تحديد الموقع الجغرافي');
        return;
    }
    
    btn.disabled = true;
    btn.textContent = 'جاري تحديد الموقع...';
    showLocationStatus('loading', 'يتم طلب إذن الوصول للموقع...');
    
    const options = {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 60000
    };
    
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const { latitude, longitude } = position.coords;
            customerLocation = { lat: latitude, lng: longitude };
            
            btn.disabled = false;
            btn.textContent = 'تم تحديد الموقع ✓';
            btn.style.background = '#27ae60';
            
            showLocationStatus('success', 'تم تحديد موقعك بنجاح');
            info.innerHTML = `
                <strong>الإحداثيات:</strong> ${latitude.toFixed(6)}, ${longitude.toFixed(6)}<br>
                <strong>رابط الموقع:</strong> <a href="https://maps.google.com/?q=${latitude},${longitude}" target="_blank">عرض على الخريطة</a>
            `;
        },
        (error) => {
            btn.disabled = false;
            btn.textContent = 'تحديد موقعي';
            btn.style.background = '';
            
            let message = '';
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    message = 'تم رفض الإذن. يرجى السماح بالوصول للموقع في إعدادات المتصفح';
                    break;
                case error.POSITION_UNAVAILABLE:
                    message = 'لا يمكن تحديد الموقع. تأكد من تفعيل GPS';
                    break;
                case error.TIMEOUT:
                    message = 'انتهت مهلة تحديد الموقع. حاول مرة أخرى';
                    break;
                default:
                    message = 'حدث خطأ في تحديد الموقع';
                    break;
            }
            
            showLocationStatus('error', message);
        },
        options
    );
}

function showLocationStatus(type, message) {
    const status = document.getElementById('location-status');
    status.className = type;
    status.textContent = message;
    status.style.display = 'block';
}

// Checkout Functions
function handleCheckout(e) {
    e.preventDefault();
    
    if (cart.length === 0) {
        alert('السلة فارغة');
        return;
    }
    
    const name = document.getElementById('customer-name').value.trim();
    const phone = document.getElementById('customer-phone').value.trim();
    const address = document.getElementById('customer-address').value.trim();
    
    if (!name || !phone || !address) {
        alert('يرجى ملء جميع البيانات المطلوبة');
        return;
    }
    
    // Validate phone number
    const phoneRegex = /^(\+20|0)[0-9]{10}$/;
    if (!phoneRegex.test(phone)) {
        alert('رقم الهاتف غير صحيح. يجب أن يكون 11 رقم مصري أو يبدأ بـ +20');
        return;
    }
    
    // Generate WhatsApp message
    const message = generateWhatsAppMessage(name, phone, address);
    const whatsappUrl = `https://wa.me/${menuData.whatsappNumber.replace('+', '')}?text=${encodeURIComponent(message)}`;
    
    // Open WhatsApp
    window.open(whatsappUrl, '_blank');
}

function generateWhatsAppMessage(name, phone, address) {
    let message = `طلب جديد - ${menuData.storeName}\n\n`;
    message += `الاسم: ${name}\n`;
    message += `الهاتف: ${phone}\n`;
    message += `العنوان: ${address}\n`;
    
    if (customerLocation) {
        message += `الإحداثيات: ${customerLocation.lat}, ${customerLocation.lng}\n`;
        message += `رابط الموقع: https://maps.google.com/?q=${customerLocation.lat},${customerLocation.lng}\n`;
    }
    
    message += '\nالأصناف:\n';
    
    let total = 0;
    cart.forEach(item => {
        const lineTotal = item.price * item.quantity;
        total += lineTotal;
        message += `- ${item.name} × ${item.quantity} = ${lineTotal} جنيه\n`;
    });
    
    message += `\nالإجمالي: ${total} جنيه`;
    
    return message;
}

// Branches
function loadBranches() {
    const container = document.querySelector('.branches-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    menuData.branches.forEach(branch => {
        const branchCard = document.createElement('div');
        branchCard.className = 'branch-card';
        branchCard.innerHTML = `
            <div class="branch-name">${branch.name}</div>
            <div class="branch-address">📍 ${branch.address}</div>
            <div class="branch-phone">📞 ${branch.phone}</div>
            <a href="${branch.mapLink}" target="_blank" class="branch-map">
                🗺️ عرض على الخريطة
            </a>
        `;
        
        container.appendChild(branchCard);
    });
}

// Make functions global for onclick handlers
window.addToCart = addToCart;
window.removeFromCart = removeFromCart;
window.updateQuantity = updateQuantity;'''

# Write JavaScript file
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ script.js file created successfully")
print("✅ جميع الملفات تم إنشاؤها بنجاح!")
print("\nالملفات المُنشأة:")
print("- index.html")
print("- style.css") 
print("- script.js")
print("\nيمكنك الآن فتح ملف index.html في المتصفح لاستخدام المنيو الإلكتروني.")