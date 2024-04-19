
#from django.shortcuts import render, redirect
#from .forms import NewsletterForm
#from django.http import HttpResponse
#from .tasks import send_mail, send_newsletter as send_newsletter_task
# '''
# from django.shortcuts import render, redirect
# from .forms import NewsletterForm
# from django.http import HttpResponse
# from .tasks import send_mail, send_newsletter as send_newsletter_task


#def send_newsletter(request):
    #if request.method == 'POST':
        #form = NewsletterForm(request.POST)
        #if form.is_valid():
            #newsletter = form.save()
            #recipients = newsletter.recipients.all()
            #subject = newsletter.subject
            #message = newsletter.message
            #sender = 'macmassage.za@gmail.com'  # Update with owner's email
            #for recipient in recipients:
                #recipient_email = recipient.email
                #send_mail(subject, message, sender, [recipient_email])
            #return redirect('newsletter_sent')
    #else:
        #form = NewsletterForm()
    #return render(request, 'send_newsletter.html', {'form': form})
# def send_newsletter(request):
#     if request.method == 'POST':
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             newsletter = form.save()
#             recipients = newsletter.recipients.all()
#             subject = newsletter.subject
#             message = newsletter.message
#             sender = 'macmassage.za@gmail.com'  # Update with owner's email
#             for recipient in recipients:
#                 recipient_email = recipient.email
#                 send_mail(subject, message, sender, [recipient_email])
#             return redirect('newsletter_sent')
#     else:
#         form = NewsletterForm()
#     return render(request, 'send_newsletter.html', {'form': form})


#def send_newsletter_view(request):
    #newsletter_id = ...  # Get the newsletter ID from the request
    #send_newsletter_task.delay(newsletter_id)
    #return HttpResponse("Newsletter sent successfully!")

# def send_newsletter_view(request):
#     newsletter_id = ...  # Get the newsletter ID from the request
#     send_newsletter_task.delay(newsletter_id)
#     return HttpResponse("Newsletter sent successfully!")
# '''