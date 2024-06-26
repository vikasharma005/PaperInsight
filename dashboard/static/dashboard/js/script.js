document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const fileList = document.getElementById('file-list');
    const uploadBtn = document.getElementById('upload-btn');
    const resultsSection = document.getElementById('results-section');
    const resultsContainer = document.getElementById('results-container');

    let files = [];

    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });
    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
    dropZone.addEventListener('drop', handleDrop);
    fileInput.addEventListener('change', handleFileSelect);
    uploadBtn.addEventListener('click', uploadFiles);

    function handleDrop(e) {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const droppedFiles = e.dataTransfer.files;
        handleFiles(droppedFiles);
    }

    function handleFileSelect(e) {
        const selectedFiles = e.target.files;
        handleFiles(selectedFiles);
    }

    function handleFiles(newFiles) {
        files = [...files, ...Array.from(newFiles)];
        updateFileList();
        uploadBtn.disabled = files.length === 0;
    }

    function updateFileList() {
        fileList.innerHTML = '';
        files.forEach((file, index) => {
            const fileItem = document.createElement('div');
            fileItem.classList.add('file-item');
            fileItem.textContent = file.name;
            const removeBtn = document.createElement('button');
            removeBtn.textContent = 'Remove';
            removeBtn.onclick = () => removeFile(index);
            fileItem.appendChild(removeBtn);
            fileList.appendChild(fileItem);
        });
    }

    function removeFile(index) {
        files.splice(index, 1);
        updateFileList();
        uploadBtn.disabled = files.length === 0;
    }

    function uploadFiles() {
        const formData = new FormData();
        files.forEach(file => formData.append('files[]', file));

        fetch('/api/upload/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing the files.');
        });
    }

    function displayResults(data) {
        resultsContainer.innerHTML = '';
        data.results.forEach((result, index) => {
            const resultItem = document.createElement('div');
            resultItem.classList.add('result-item');
            
            const title = document.createElement('h3');
            title.textContent = result.filename;
            resultItem.appendChild(title);

            const wordCount = document.createElement('p');
            wordCount.textContent = `Word count: ${result.analysis.word_count}`;
            resultItem.appendChild(wordCount);

            const sentenceCount = document.createElement('p');
            sentenceCount.textContent = `Sentence count: ${result.analysis.sentence_count}`;
            resultItem.appendChild(sentenceCount);

            const wordFreqViz = document.createElement('img');
            wordFreqViz.src = `data:image/png;base64,${data.visualizations[index * 2].data}`;
            wordFreqViz.alt = 'Word Frequency Visualization';
            wordFreqViz.classList.add('visualization');
            resultItem.appendChild(wordFreqViz);

            const phraseFreqViz = document.createElement('img');
            phraseFreqViz.src = `data:image/png;base64,${data.visualizations[index * 2 + 1].data}`;
            phraseFreqViz.alt = 'Phrase Frequency Visualization';
            phraseFreqViz.classList.add('visualization');
            resultItem.appendChild(phraseFreqViz);

            resultsContainer.appendChild(resultItem);
        });

        resultsSection.style.display = 'block';
    }
});