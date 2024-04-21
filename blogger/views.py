from django.shortcuts import render
from PIL import Image
from .forms import UploadForm
from .utils import get_gemini_response

def home(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the input text and uploaded file from the form
            input_text = form.cleaned_data.get('input', '')
            uploaded_file = form.cleaned_data.get('image', None)
            
            # Convert the uploaded image file to a PIL.Image.Image object
            if uploaded_file:
                image = Image.open(uploaded_file)
            else:
                image = None
            
            # Call get_gemini_response 
            response = get_gemini_response(input_text, image)
            
            # Render the response in the 'result.html' template
            return render(request, 'result.html', {'response': response})
        else:
            # Handle form errors if any
            response = "Invalid form data."
            return render(request, 'result.html', {'response': response})
    
    # Render the form template for GET requests
    form = UploadForm()
    return render(request, 'form.html', {'form': form})
