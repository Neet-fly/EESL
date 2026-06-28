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

    // Floating Quick Menu Toggle (now jumps to pages instead of scroll spy)
    const quickMenuToggle = document.querySelector('.quick-menu-toggle');
    const quickMenuContent = document.querySelector('.quick-menu-content');
    const quickLinks = document.querySelectorAll('.quick-link');

    if (quickMenuToggle && quickMenuContent) {
        quickMenuToggle.addEventListener('click', () => {
            quickMenuToggle.classList.toggle('active');
            quickMenuContent.classList.toggle('show');
        });

        // Close quick menu on link click and handle smooth scrolling on the same page
        quickLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                if (href && href.startsWith('index.html#')) {
                    const targetId = href.split('#')[1];
                    const targetElement = document.getElementById(targetId);
                    
                    // If target section is on the current page (i.e. we are already on index.html)
                    if (targetElement) {
                        e.preventDefault(); // prevent reload
                        targetElement.scrollIntoView({ behavior: 'smooth' });
                        window.history.pushState(null, null, `#${targetId}`);
                    }
                }
                quickMenuToggle.classList.remove('active');
                quickMenuContent.classList.remove('show');
            });
        });

        // Close quick menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.floating-quick-menu')) {
                quickMenuToggle.classList.remove('active');
                quickMenuContent.classList.remove('show');
            }
        });
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
});
