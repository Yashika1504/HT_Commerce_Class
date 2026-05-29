from django.shortcuts import render, redirect
from .models import ContactMessage  # Import your model

def process_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')

        # Basic validation (you might want to add more robust validation)
        if name and contact_number and message:
            # Create a new ContactMessage object and save it
            contact_message = ContactMessage(
                name=name,
                contact_number=contact_number,
                message=message
            )
            contact_message.save()
            return redirect('thankyou')
        else:
            # Handle the case where required fields are missing
            return render(request, 'contact.html', {'error': 'Please fill in all required fields.'})
    else:
        # If it's a GET request to this URL, you might want to redirect back to the form
        return redirect('contact') # Assuming you have a URL for the form

def thankyou_view(request):
    return render(request, 'thank-you.html')# # In your app's views.py file

# from django.shortcuts import render, redirect
# from .models import ContactMessage 

def contact_view(request):
   return render(request, 'contact.html')

# def thank_you_view(request):
#     return render(request, 'thank-you.html')

# Create your views here.
def index(request):
    return render(request ,"index.html")

def about(request):
    return render(request , "about.html")



def Class11(request):
    return render(request , "class11.html")
    
def Class12(request):
    return render(request , "Class12.html")
    
def bcom(request):
    return render(request , "bcom.html")
    
def bcom_01(request):
    return render(request , "1st.html")
    
def bcom_02(request):
    return render(request , "2nd.html")

def bcom_03(request):
    return render(request , "3rd.html")

def result(request):
    images = [
        "images/2501.jpeg", "images/250.png", "images/241.jpg", "images/242.jpg", "images/243.jpg",
        "images/244.jpg", "images/245.jpg", "images/246.jpg", "images/247.jpg", "images/248.jpg",
        "images/231.jpg", "images/232.jpg", "images/233.jpg", "images/221.jpg", "images/222.jpg",
        "images/211.jpg", "images/201.jpg", "images/202.jpg"
    ]
    gallery_images = [(img, i * 100) for i, img in enumerate(images)]  # delay by 100ms each
    return render(request, 'result.html', {'gallery_images': gallery_images})

    
# def contact_view(request):
#     return render(request,"contact.html")
def index(request):
    reviews = [
        {"name": "Mahak Gupta", "text": "Amazing teacher with understandable and easy-to-learn techniques!", "time": "2 months ago"},
        {"name": "Poojan Jwell", "text": "Expert teacher with interactive classes and effortless doubt clearing. 100% recommended!", "time": "2 months ago"},
        {"name": "Akshat Raghuvanshi", "text": "Sir's real-life examples help grasp difficult topics easily. Very engaging!", "time": "4 months ago"},
        {"name": "Aayush Jain", "text": "I was an average student but here I transformed my dreams into reality.", "time": "5 months ago"},
        {"name": "Shreya Jaiswal", "text": "Sir gives awesome explanations. If you want to score high, join here!", "time": "2 months ago"},
        {"name": "HARSHIL Workspace", "text": "Sir acts as a mentor too. A powerful combination for great results.", "time": "2 months ago"},
        {"name": "Manthan Nagpal", "text": "Sir Harsh Tongia is highly motivating. Helped transform my journey.", "time": "3 months ago"},
        {"name": "Kratagya Yadav", "text": "If you’re facing issues in commerce, this is the place to solve them.", "time": "3 months ago"},
        {"name": "Shorya Agarwal", "text": "Your teaching is clear, engaging, and inspiring. Thank you!", "time": "4 months ago"},
    ]

    return render(request, 'index.html', {'reviews': reviews})