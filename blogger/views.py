from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from .forms import UploadForm
from .utils import get_gemini_response

def home(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            input_text = form.cleaned_data.get('input', '')
            uploaded_file = form.cleaned_data.get('image', None)
            
            # Convert uploaded image file to a PIL.Image.Image object
            if uploaded_file:
                image = Image.open(uploaded_file)
            else:
                image = None
            
            # Conditional handling of input text and image
            if input_text and image:
                response = get_gemini_response(input_text, image)
            elif image:
                response = get_gemini_response("", image)
            else:
                response = "Please provide an image."
            
            return render(request, 'result.html', {'response': response})
        else:
            # Handle form errors if any
            response = "Invalid form data."
            return render(request, 'result.html', {'response': response})
    
    # Render the form template for GET requests
    form = UploadForm()
    return render(request, 'form.html', {'form': form})
