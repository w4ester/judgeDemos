# Cyber UXcellence Judges Page Demos

This repository contains seven different design options for the Cyber UXcellence Awards judges page. Each design showcases the distinguished panel of cybersecurity and UX experts in a unique layout while maintaining brand consistency.

## Live Demo

View the live demo at: [https://w4ester.github.io/judgeDemos/](https://w4ester.github.io/judgeDemos/)

## Design Options

1. **Version 1: Grid Layout** - A clean, professional grid-based layout that showcases all judges equally with card-based design.
2. **Version 2: Interactive Cards** - Dynamic, engaging experience with flip cards that reveal more information on hover.
3. **Version 3: Modern Timeline** - Visually interesting timeline layout that tells a story about each judge with alternating positioning.
4. **Version 4: Brand-Aligned Cards** - Custom cards with styling that closely matches the Cyber UXcellence brand colors and aesthetic.
5. **Version 5: Hexagonal Grid** - Innovative hexagonal layout with interactive modals for detailed judge information.
6. **Version 6: Official Brand Colors** - A modern card layout using the actual judges' information and official Cyber UXcellence brand colors.
7. **Version 7: Spotlight Carousel (Recommended)** - A dynamic carousel showcasing judges with thumbnails below for quick navigation. Features elegant animations and a modern, polished interface.

## Repository Structure

- `index.html` - Main landing page with links to all design versions
- `version1.html` through `version7.html` - Individual design options
- `images/` - Directory containing preview images and judge photos
- `download_judge_images.py` - Python script to download judge photos from Google Drive links

## Setup Instructions

### Local Setup

To run this demo locally:

1. Clone the repository:
```bash
git clone https://github.com/w4ester/judgeDemos.git
cd judgeDemos
```

2. (Optional) Run the Python script to download judge photos:
```bash
# Make the script executable
chmod +x download_judge_images.py
# Run the script
python3 download_judge_images.py
```

3. Open `index.html` in your web browser to view the main page.

4. Click on any design card to view the specific design option.

### Deployment with GitHub Pages

1. Fork this repository to your own GitHub account

2. Make sure your repository is set up for GitHub Pages:
   - Go to your repository on GitHub
   - Click on "Settings"
   - Scroll down to the "GitHub Pages" section
   - Under "Source", select "main" branch
   - Click "Save"

3. Your site will be published at `https://[your-username].github.io/judgeDemos/`

## Customization

### Judge Images

The `download_judge_images.py` script attempts to download images from the provided Google Drive links. If it fails to download any images, you'll need to manually add judge photos to the `images/judges/` directory following this naming convention:

- `ron-gula.jpg`
- `troy-wilkinson.jpg`
- `malcolm-harkins.jpg`
- `rinki-sethi.jpg`
- `damian-chung.jpg`
- `nick-shevelyov.jpg`
- `patricia-titus.jpg`
- `michael-baker.jpg`
- `peter-kilpe.jpg`
- `alicia-lynch.jpg`
- `meagan-petri.jpg`

### Preview Images

To replace the placeholder preview images for each design version:

1. Take screenshots of each design version
2. Save them to the `images/` directory as:
   - `preview-version1.jpg`
   - `preview-version2.jpg`
   - `preview-version3.jpg`
   - `preview-version4.jpg`
   - `preview-version5.jpg`
   - `preview-version6.jpg`
   - `preview-version7.jpg`

### Content Updates

To update judge information, you'll need to modify the HTML files. Each design version has its own structure, but generally:

1. Find the section containing the judge information
2. Update the name, title, company, and bio text as needed
3. Save the file and refresh your browser to see the changes

## Technical Details

### Version 7 (Spotlight Carousel) Features

The recommended "Spotlight Carousel" design (Version 7) includes:

- Full-screen hero image with animated text
- Dynamic carousel with smooth transitions
- Staggered animation effects when switching judges
- Responsive design for mobile, tablet, and desktop
- Interactive thumbnail grid with hover effects
- Auto-advancing carousel (every 5 seconds)
- Manual navigation with buttons and indicators
- Image hover effects and smooth transitions
- Custom gradients and subtle background patterns

### Browser Compatibility

These designs have been tested and work well in:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

### Dependencies

All designs use:
- HTML5
- CSS3 (with modern features like CSS Grid, Flexbox, and CSS Variables)
- Vanilla JavaScript (no external libraries)
- Google Fonts (Inter font family)

## Acknowledgements

- Design by [Your Name/Company]
- Created for the [Cyber UXcellence Awards](https://www.cyberuxcellence.com)
- Judges' information provided by the Cyber UXcellence Awards team

## License

This project is available for use by the Cyber UXcellence Awards team. All rights reserved.

## Contact

For questions or support, please contact [Your Contact Information].
