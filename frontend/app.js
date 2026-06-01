// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// DOM Elements
const promptInput = document.getElementById('prompt');
const bodyTypeContainer = document.getElementById('bodyTypeContainer');
const skinToneContainer = document.getElementById('skinToneContainer');
const languageSelect = document.getElementById('language');
const generateBtn = document.getElementById('generateBtn');
const downloadBtn = document.getElementById('downloadBtn');
const generateNewBtn = document.getElementById('generateNewBtn');

const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');
const resultContainer = document.getElementById('resultContainer');
const emptyState = document.getElementById('emptyState');

const resultImage = document.getElementById('resultImage');
const promptUsedText = document.getElementById('promptUsed');
const bodyTypeUsedText = document.getElementById('bodyTypeUsed');
const skinToneUsedText = document.getElementById('skinToneUsed');
const generationTimeText = document.getElementById('generationTime');

// State
let selectedBodyType = 'average';
let selectedSkinTone = 'medium';
let currentImageData = null;

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
    await loadBodyTypes();
    await loadSkinTones();
    setupEventListeners();
    showEmptyState();
});

// Load Body Types
async function loadBodyTypes() {
    try {
        const response = await fetch(`${API_BASE_URL}/body-types`);
        const data = await response.json();

        bodyTypeContainer.innerHTML = '';
        data.body_types.forEach(bodyType => {
            const div = document.createElement('div');
            div.className = 'option-item' + (bodyType.value === selectedBodyType ? ' selected' : '');
            div.innerHTML = `
                <div>${bodyType.label}</div>
                <div style="font-size: 0.8em; color: #999; margin-top: 4px;">${bodyType.description}</div>
            `;
            div.onclick = () => selectBodyType(bodyType.value);
            bodyTypeContainer.appendChild(div);
        });
    } catch (error) {
        console.error('Errore nel caricamento body types:', error);
        showError('Errore nel caricamento dei tipi di corporatura');
    }
}

// Load Skin Tones
async function loadSkinTones() {
    try {
        const response = await fetch(`${API_BASE_URL}/skin-tones`);
        const data = await response.json();

        skinToneContainer.innerHTML = '';
        data.skin_tones.forEach(skinTone => {
            const div = document.createElement('div');
            div.className = 'option-item' + (skinTone.value === selectedSkinTone ? ' selected' : '');
            div.innerHTML = `
                <div class="option-color" style="background-color: ${skinTone.hex};"></div>
                <div>${skinTone.label}</div>
            `;
            div.onclick = () => selectSkinTone(skinTone.value);
            skinToneContainer.appendChild(div);
        });
    } catch (error) {
        console.error('Errore nel caricamento skin tones:', error);
        showError('Errore nel caricamento dei colori di pelle');
    }
}

// Select Body Type
function selectBodyType(value) {
    selectedBodyType = value;
    updateSelection('bodyType');
}

// Select Skin Tone
function selectSkinTone(value) {
    selectedSkinTone = value;
    updateSelection('skinTone');
}

// Update Selection UI
function updateSelection(type) {
    const container = type === 'bodyType' ? bodyTypeContainer : skinToneContainer;
    const selected = type === 'bodyType' ? selectedBodyType : selectedSkinTone;

    container.querySelectorAll('.option-item').forEach(item => {
        item.classList.remove('selected');
    });

    container.querySelectorAll('.option-item').forEach(item => {
        if (item.textContent.includes(selected)) {
            item.classList.add('selected');
        }
    });
}

// Setup Event Listeners
function setupEventListeners() {
    generateBtn.addEventListener('click', generateStory);
    downloadBtn.addEventListener('click', downloadImage);
    generateNewBtn.addEventListener('click', resetForm);
}

// Generate Story
async function generateStory() {
    const prompt = promptInput.value.trim();

    if (!prompt) {
        showError('Per favore, descrivi la tua storia prima di generare');
        return;
    }

    // Validate
    if (prompt.length < 10) {
        showError('La descrizione deve essere di almeno 10 caratteri');
        return;
    }

    showLoading();
    hideError();

    try {
        const payload = {
            prompt: prompt,
            body_type: selectedBodyType,
            skin_tone: selectedSkinTone,
            language: languageSelect.value,
            representation: 'diverse, inclusive, respectful, empowering, dignified, beautiful, professional'
        };

        const response = await fetch(`${API_BASE_URL}/generate-story`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Errore nella generazione');
        }

        const data = await response.json();
        displayResult(data);
    } catch (error) {
        console.error('Errore:', error);
        showError(`Errore: ${error.message}`);
        hideLoading();
    }
}

// Display Result
function displayResult(data) {
    hideLoading();

    // Store image data
    currentImageData = {
        base64: data.image_base64,
        filename: `inclusive-story-${Date.now()}.png`
    };

    // Display image
    resultImage.src = `data:image/png;base64,${data.image_base64}`;

    // Display info
    promptUsedText.textContent = data.prompt_used;
    bodyTypeUsedText.textContent = capitalizeFirst(data.body_type);
    skinToneUsedText.textContent = capitalizeFirst(data.skin_tone);
    generationTimeText.textContent = `${data.generation_time.toFixed(2)}s`;

    // Show result
    emptyState.classList.add('hidden');
    resultContainer.classList.remove('hidden');
}

// Download Image
function downloadImage() {
    if (!currentImageData) return;

    const link = document.createElement('a');
    link.href = `data:image/png;base64,${currentImageData.base64}`;
    link.download = currentImageData.filename;
    link.click();
}

// Reset Form
function resetForm() {
    promptInput.value = '';
    selectedBodyType = 'average';
    selectedSkinTone = 'medium';
    updateSelection('bodyType');
    updateSelection('skinTone');
    hideError();
    hideLoading();
    resultContainer.classList.add('hidden');
    showEmptyState();
}

// UI Helpers
function showLoading() {
    loadingDiv.classList.remove('hidden');
    generateBtn.disabled = true;
}

function hideLoading() {
    loadingDiv.classList.add('hidden');
    generateBtn.disabled = false;
}

function showError(message) {
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

function hideError() {
    errorDiv.classList.add('hidden');
}

function showEmptyState() {
    emptyState.classList.remove('hidden');
}

function capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).replace(/_/g, ' ');
}
