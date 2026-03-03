from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Booking
from django.core.mail import EmailMultiAlternatives

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def halls(request):
    return render(request, 'halls.html')

def rooms(request):
    return render(request, 'rooms.html')

def bookings(request):
    """List all bookings (optional)"""
    all_bookings = Booking.objects.all()
    return render(request, 'my-booking.html', {'bookings': all_bookings})



def booking_contact(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        event_date = request.POST.get("event_date")
        guests = request.POST.get("guests")
        event_type = request.POST.get("event_type")
        requirements = request.POST.get("requirements")

        # Save booking
        Booking.objects.create(
            full_name=full_name,
            phone=phone,
            email=email,
            event_date=event_date,
            guests=guests,
            event_type=event_type,
            requirements=requirements,
        )

        # Prepare HTML email
        subject = "Booking Confirmation - Royal Hospitality"
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        html_content = f"""
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
    <div style="max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 8px;">
      <h2 style="color: #bfa14b;">Royal Hospitality</h2>
      <p>Dear <strong>{full_name}</strong>,</p>
      <p>Thank you for booking with <strong>Royal Hospitality</strong>!</p>
      <table style="width: 100%; margin-top: 20px; border-collapse: collapse;">
        <tr>
          <td style="padding: 8px; border: 1px solid #ddd;">Event Type</td>
          <td style="padding: 8px; border: 1px solid #ddd;">{event_type}</td>
        </tr>
        <tr>
          <td style="padding: 8px; border: 1px solid #ddd;">Event Date</td>
          <td style="padding: 8px; border: 1px solid #ddd;">{event_date}</td>
        </tr>
        <tr>
          <td style="padding: 8px; border: 1px solid #ddd;">Guests</td>
          <td style="padding: 8px; border: 1px solid #ddd;">{guests}</td>
        </tr>
      </table>
      <p style="margin-top: 20px;">Our team will contact you soon for further details.</p>
      <p>Regards,<br>Royal Hospitality Team</p>
    </div>
  </body>
</html>
"""

        # Send HTML email
        email_message = EmailMultiAlternatives(subject, "", from_email, to)
        email_message.attach_alternative(html_content, "text/html")
        email_message.send(fail_silently=False)

        messages.success(request, "Your booking request has been submitted! Check your email for confirmation.")
        return redirect("booking_contact")

    return render(request, "my-booking.html")