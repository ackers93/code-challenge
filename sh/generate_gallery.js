const fs = require('fs');
const path = require('path');

// Path to the portfolio directory
const portfolioDir = path.join(__dirname, 'src/assets/portfolio');

// Read all files in the portfolio directory
fs.readdir(portfolioDir, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err);
        return;
    }

    // Filter for image files and sort them
    const imageFiles = files
        .filter(file => /\.(jpg|jpeg|png|gif|webp)$/i.test(file))
        .sort();

    // Generate the HTML content
    let htmlContent = `---
layout: base.njk
title: "Projects Gallery - Pineworks Construction"
description: "Explore our portfolio of timber frame construction projects and modern rustic designs."
---

<section class="projects-hero">
    <div class="container">
        <h1>Our Projects</h1>
        <p>Discover our craftsmanship through these carefully selected projects that showcase our expertise in timber frame construction and modern rustic design.</p>
    </div>
</section>

<section class="projects-gallery">
    <div class="container">
        <div class="gallery-grid">
`;

    // Add each image to the gallery
    imageFiles.forEach((file, index) => {
        const imagePath = `/assets/portfolio/${file}`;
        const imageNumber = index + 1;
        
        htmlContent += `            <div class="gallery-item" data-aos="fade-up" data-aos-delay="${(index % 6) * 100}">
                <div class="image-container">
                    <img src="${imagePath}" alt="Pineworks Construction Project ${imageNumber}" loading="lazy">
                    <div class="image-overlay">
                        <div class="overlay-content">
                            <span class="project-number">Project ${imageNumber.toString().padStart(2, '0')}</span>
                            <button class="view-full-btn" onclick="openLightbox('${imagePath}', ${imageNumber})">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="11" cy="11" r="8"></circle>
                                    <path d="m21 21-4.35-4.35"></path>
                                    <line x1="11" y1="8" x2="11" y2="14"></line>
                                    <line x1="8" y1="11" x2="14" y2="11"></line>
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
`;
    });

    // Close the gallery and add lightbox
    htmlContent += `        </div>
    </div>
</section>

<!-- Lightbox Modal -->
<div id="lightbox" class="lightbox">
    <div class="lightbox-content">
        <span class="close-lightbox">&times;</span>
        <img id="lightbox-image" src="" alt="">
        <div class="lightbox-nav">
            <button class="nav-btn prev-btn" onclick="changeImage(-1)">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="15,18 9,12 15,6"></polyline>
                </svg>
            </button>
            <span id="image-counter"></span>
            <button class="nav-btn next-btn" onclick="changeImage(1)">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="9,18 15,12 9,6"></polyline>
                </svg>
            </button>
        </div>
    </div>
</div>

<script>
// Lightbox functionality
let currentImageIndex = 0;
const images = [${imageFiles.map((file, index) => `'${file}'`).join(', ')}];

function openLightbox(imagePath, imageNumber) {
    currentImageIndex = imageNumber - 1;
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const imageCounter = document.getElementById('image-counter');
    
    lightboxImage.src = imagePath;
    imageCounter.textContent = \`\${imageNumber} / \${images.length}\`;
    lightbox.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function changeImage(direction) {
    currentImageIndex = (currentImageIndex + direction + images.length) % images.length;
    const imagePath = \`/assets/portfolio/\${images[currentImageIndex]}\`;
    const imageNumber = currentImageIndex + 1;
    
    const lightboxImage = document.getElementById('lightbox-image');
    const imageCounter = document.getElementById('image-counter');
    
    lightboxImage.src = imagePath;
    imageCounter.textContent = \`\${imageNumber} / \${images.length}\`;
}

// Close lightbox when clicking outside or on close button
document.addEventListener('DOMContentLoaded', function() {
    const lightbox = document.getElementById('lightbox');
    const closeBtn = document.querySelector('.close-lightbox');
    
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });
    
    closeBtn.addEventListener('click', closeLightbox);
    
    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (lightbox.style.display === 'flex') {
            if (e.key === 'Escape') {
                closeLightbox();
            } else if (e.key === 'ArrowLeft') {
                changeImage(-1);
            } else if (e.key === 'ArrowRight') {
                changeImage(1);
            }
        }
    });
});
</script>`;

    // Write the content to the projects.njk file
    const outputPath = path.join(__dirname, 'src/projects.njk');
    fs.writeFile(outputPath, htmlContent, (err) => {
        if (err) {
            console.error('Error writing file:', err);
            return;
        }
        console.log(`✅ Projects gallery generated successfully with ${imageFiles.length} images!`);
        console.log(`📁 Output file: ${outputPath}`);
    });
}); 