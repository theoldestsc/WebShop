from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    '''Задача отправки email-уведомлений при успешном оформлении заказа'''
    order = Order.objects.get(id = order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                You order id is {}'.format(order.first_name,order.id)
    mail_sent = send_mail(subject,message,'ferrarigto733@gmail.com',[order.email], fail_silently=False)

    return mail_sent

@task
def debug_task():
    print('Request :{0!r}'.format(1))