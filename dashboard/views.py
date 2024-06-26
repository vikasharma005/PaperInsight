from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ResearchPaper
from nlp_processor import process_files
from data_visualizer import create_visualizations

def index(request):
    return render(request, 'dashboard/index.html')

@csrf_exempt
def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files[]')
        if not files:
            return JsonResponse({'error': 'No files uploaded'}, status=400)

        uploaded_files = []
        for file in files:
            research_paper = ResearchPaper(file=file)
            research_paper.save()
            uploaded_files.append(research_paper.file.path)

        results = process_files(uploaded_files)
        visualizations = create_visualizations(results)

        for result, research_paper in zip(results, ResearchPaper.objects.all().order_by('-uploaded_at')[:len(results)]):
            research_paper.word_count = result['analysis']['word_count']
            research_paper.sentence_count = result['analysis']['sentence_count']
            research_paper.top_words = result['analysis']['top_words']
            research_paper.top_phrases = result['analysis']['top_phrases']
            research_paper.save()

        return JsonResponse({
            'message': f'{len(files)} files uploaded and processed successfully',
            'results': results,
            'visualizations': visualizations
        })
    return JsonResponse({'error': 'Invalid request method'}, status=405)