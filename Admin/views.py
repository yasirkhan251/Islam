from django.shortcuts import render
from Salah.models import *
from django.http import HttpResponse

def admin_fard_salah(request):
    message = ""
    if request.method == "POST":
        try:
            # Get data from POST request
            salah = request.POST.get('salah')
            rakat = request.POST.get('rakat')
            azan = request.POST.get('azan')
            start_time = request.POST.get('start_time')
            jamath = request.POST.get('jamath')
            end_time = request.POST.get('end_time')

            if not salah or not rakat or not start_time or not jamath or not end_time:
                raise ValueError("All required fields must be filled.")

            # Check if the record exists, and update or create
            obj, created = Fard_Salah.objects.update_or_create(
                salah=salah,  # Unique identifier
                defaults={
                    'rakat': int(rakat),
                    'azan': azan if azan else None,  # Handle optional azan field
                    'start_time': start_time,
                    'jamath': jamath,
                    'end_time': end_time
                }
            )

            if created:
                message = "New Salah created successfully!"
            else:
                message = "Existing Salah updated successfully!"
        except Exception as e:
            message = f"Error: {str(e)}"

    return render(request, 'admin/salah.html', {'message': message})
