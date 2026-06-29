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
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');

                if (href && href.startsWith('index.html#')) {
                    const targetId = href.split('#')[1];
                    const targetElement = document.getElementById(targetId);
                    
                    if (targetElement) {
                        e.preventDefault(); // Prevent native instant jump
                        
                        // Fix for iOS Safari bug where smooth scrolling fails at scrollY === 0
                        if (window.scrollY === 0) {
                            window.scrollTo(0, 1);
                        }
                        
                        targetElement.scrollIntoView({ behavior: 'smooth' });
                        
                        try {
                            window.history.pushState(null, null, `#${targetId}`);
                        } catch (err) {
                            // Prevent crash on local file:/// protocol
                        }
                    } else {
                        window.location.href = href;
                    }
                } else if (href) {
                    window.location.href = href;
                }

                // Hide the menu
                quickMenuToggle.classList.remove('active');
                quickMenuContent.classList.remove('show');
            });
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

    // Dynamic Publication Rendering
    if (typeof publicationsData !== 'undefined' && document.querySelector('.publications-container')) {
        const renderList = (papers) => {
            return papers.map(p => `
                <li class="pub-item">
                    <a href="${p.link}" target="_blank" class="pub-link">
                        ${p.authorsAndTitle} <i class="journal">${p.journal}</i> <span class="year">${p.year}</span>${p.details}
                    </a>
                </li>
            `).join('');
        };

        // Render 2026 to 2023
        [2026, 2025, 2024, 2023].forEach(year => {
            const yearTab = document.getElementById(year.toString());
            if (yearTab) {
                const container = yearTab.querySelector('.pub-list');
                if (container) {
                    const yearPapers = publicationsData.filter(p => p.year === year);
                    container.innerHTML = renderList(yearPapers);
                }
            }
        });

        // Render Before 2023
        const beforeArchive = document.getElementById('before-archive');
        if (beforeArchive) {
            let archiveHtml = '';
            // Get unique years before 2023 in descending order
            const oldYears = [...new Set(publicationsData.filter(p => p.year < 2023).map(p => p.year))].sort((a, b) => b - a);
            
            oldYears.forEach(year => {
                const yearPapers = publicationsData.filter(p => p.year === year);
                archiveHtml += `
                    <div class="year-section">
                        <h3 class="year-title">${year}</h3>
                        <ul class="publication-list pub-list">
                            ${renderList(yearPapers)}
                        </ul>
                    </div>
                `;
            });
            beforeArchive.innerHTML = archiveHtml;
        }
    }
});
