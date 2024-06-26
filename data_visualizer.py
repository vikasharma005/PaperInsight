import matplotlib.pyplot as plt
import io
import base64

def create_visualizations(results):
    visualizations = []
    
    for result in results:
        # Word frequency bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(result['analysis']['top_words'].keys(), result['analysis']['top_words'].values())
        plt.title(f'Top 10 Most Frequent Words - {result["filename"]}')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        visualizations.append({
            'filename': result['filename'],
            'type': 'word_frequency',
            'data': plt_to_base64()
        })
        
        # Phrase frequency bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(result['analysis']['top_phrases'].keys(), result['analysis']['top_phrases'].values())
        plt.title(f'Top 5 Most Frequent Phrases - {result["filename"]}')
        plt.xlabel('Phrases')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        visualizations.append({
            'filename': result['filename'],
            'type': 'phrase_frequency',
            'data': plt_to_base64()
        })
    
    return visualizations

def plt_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')