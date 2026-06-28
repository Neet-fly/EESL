document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('.nav');

    if (mobileBtn && nav) {
        mobileBtn.addEventListener('click', () => {
            nav.classList.toggle('open');
        });

        // Close mobile menu when a link is clicked
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (nav.classList.contains('open')) {
                    nav.classList.remove('open');
                }
            });
        });
    }

    // Floating Quick Menu Toggle (Optimized for Mobile & Sub-pages)
    const quickMenuToggle = document.querySelector('.quick-menu-toggle');
    const quickMenuContent = document.querySelector('.quick-menu-content');
    const quickLinks = document.querySelectorAll('.quick-link');

    if (quickMenuToggle && quickMenuContent) {
        const toggleMenu = (e) => {
            if (e.type === 'touchstart') {
                e.preventDefault();
                e.stopPropagation();
            }
            quickMenuToggle.classList.toggle('active');
            quickMenuContent.classList.toggle('show');
        };

        quickMenuToggle.addEventListener('click', toggleMenu);
        quickMenuToggle.addEventListener('touchstart', toggleMenu, { passive: false });

        quickLinks.forEach(link => {
            const handleLinkClick = (e) => {
                if (e.type === 'touchstart') {
                    e.preventDefault();
                    e.stopPropagation();
                }

                const href = link.getAttribute('href');

                if (href && href.startsWith('index.html#')) {
                    const targetId = href.split('#')[1];
                    const targetElement = document.getElementById(targetId);
                    
                    if (targetElement) {
                        // On the same page, scroll smoothly
                        if (e.type !== 'touchstart') e.preventDefault(); // Prevent default if click (touchstart already prevented)
                        
                        // Fix for iOS Safari bug where smooth scrolling fails at scrollY === 0
                        const headerOffset = 80;
                        const elementPosition = targetElement.getBoundingClientRect().top;
                        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                        
                        window.scrollTo({
                            top: offsetPosition,
                            behavior: "smooth"
                        });
                        
                        window.history.pushState(null, null, `#${targetId}`);
                    } else {
                        // Not on index.html, so navigate to index.html#targetId naturally
                        window.location.href = href;
                    }
                } else if (href) {
                    window.location.href = href;
                }

                quickMenuToggle.classList.remove('active');
                quickMenuContent.classList.remove('show');
            };

            link.addEventListener('click', handleLinkClick);
            link.addEventListener('touchstart', handleLinkClick, { passive: false });
        });

        // Close quick menu when clicking/touching outside
        const closeMenuOutside = (e) => {
            if (!e.target.closest('.floating-quick-menu')) {
                quickMenuToggle.classList.remove('active');
                quickMenuContent.classList.remove('show');
            }
        };

        document.addEventListener('click', closeMenuOutside);
        document.addEventListener('touchstart', closeMenuOutside, { passive: true });
    }

    // Member Details Toggle
    const toggleBtns = document.querySelectorAll('.toggle-detail-btn');
    toggleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const card = this.closest('.member-card');
            const detailSection = card.querySelector('.research-field-toggle');
            
            detailSection.classList.toggle('open');
            this.classList.toggle('active');
            
            if (this.classList.contains('active')) {
                this.textContent = 'CLOSE';
            } else {
                this.textContent = 'DETAIL';
            }
        });
    });

    // Add shadow to header on scroll
    window.addEventListener('scroll', () => {
        const scrollY = window.pageYOffset;
        const header = document.querySelector('.header');
        if (header) {
            if (scrollY > 50) {
                header.style.boxShadow = '0 4px 15px rgba(0,0,0,0.1)';
            } else {
                header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.05)';
            }
        }
    });

    // Hero Image Slider
    const slides = document.querySelectorAll('.slide-img');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (slides.length > 0 && prevBtn && nextBtn) {
        let currentSlide = 0;

        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove('active'));
            slides[index].classList.add('active');
        }

        prevBtn.addEventListener('click', () => {
            currentSlide = (currentSlide > 0) ? currentSlide - 1 : slides.length - 1;
            showSlide(currentSlide);
        });

        nextBtn.addEventListener('click', () => {
            currentSlide = (currentSlide < slides.length - 1) ? currentSlide + 1 : 0;
            showSlide(currentSlide);
        });
    }

    // Publication Tabs Toggle
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    if (tabBtns.length > 0 && tabContents.length > 0) {
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active classes
                tabBtns.forEach(b => {
                    b.classList.remove('active');
                    b.style.background = '#e0e0e0';
                    b.style.color = '#333';
                });
                tabContents.forEach(content => {
                    content.classList.remove('active');
                    content.style.display = 'none';
                });

                // Add active class to clicked
                btn.classList.add('active');
                btn.style.background = '#0033A0';
                btn.style.color = 'white';
                
                const targetId = btn.getAttribute('data-target') || btn.textContent.trim();
                const targetContent = document.getElementById(targetId);
                if (targetContent) {
                    targetContent.classList.add('active');
                    targetContent.style.display = 'block';
                }
            });
        });
    }
});
