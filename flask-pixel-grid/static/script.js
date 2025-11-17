document.addEventListener('DOMContentLoaded', () => {
    const gridContainer = document.getElementById('gridContainer');
    const sizeSlider = document.getElementById('gridSize');
    const sizeValueDisplay = document.getElementById('sizeValue');
    const clearButton = document.getElementById('clearBtn');
    const colorPicker = document.getElementById('colorPicker');

    // --- Core Grid Creation Function ---
    function createGrid(size) {
        gridContainer.innerHTML = '';
        gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
        gridContainer.style.gridTemplateRows = `repeat(${size}, 1fr)`;

        for (let i = 0; i < size * size; i++) {
            const cell = document.createElement('div');
            cell.classList.add('grid-cell');

            // 💡 SIMPLIFIED LOGIC: One 'mouseover' listener handles all drawing
            cell.addEventListener('mouseover', function(e) {
                // e.buttons === 1 means the left mouse button is currently pressed.
                if (e.buttons === 1) {
                    this.style.backgroundColor = colorPicker.value;
                }
                // Optional: visual feedback outline (same as before)
                this.style.outline = `1px solid ${colorPicker.value}50`;
            });

            // A 'mousedown' is still useful to color the FIRST cell immediately
            cell.addEventListener('mousedown', function(e) {
                e.preventDefault(); // Prevents image/text dragging
                this.style.backgroundColor = colorPicker.value;
            });

            cell.addEventListener('mouseout', function() {
                this.style.outline = 'none';
            });

            gridContainer.appendChild(cell);
        }

        sizeValueDisplay.textContent = `${size}x${size}`;
    }

    // --- Initial setup and event listeners (Unchanged) ---
    const initialSize = parseInt(sizeSlider.value);
    createGrid(initialSize);

    sizeSlider.addEventListener('input', (e) => {
        const newSize = parseInt(e.target.value);
        createGrid(newSize);
    });

    clearButton.addEventListener('click', () => {
        const cells = document.querySelectorAll('.grid-cell');
        cells.forEach(cell => {
            cell.style.backgroundColor = 'var(--secondary-color)';
        });
    });
});