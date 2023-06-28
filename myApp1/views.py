from django.shortcuts import render

from myApp1.models import Worker


def main_page(request):
    new_worker = Worker(name='Вова', last_name='Должанский', salary=100)
    #new_worker.save()
    #Worker.objects.create(name='Ольга', last_name='Колышева', salary=7236)
    #for i in range(3,5):
    #    Worker.objects.get(id=i).delete()
    # worker_to_change = Worker.objects.get(id=1)
    # worker_to_change.name = 'Григорий'
    # worker_to_change.last_name = 'Дологумов'
    # #worker_to_change.save()
    # Worker.objects.filter(id=2).update(name='Иван Иванович')
    # all_workes = Worker.objects.all()
    # for worker in all_workes:
    #     worker.name = 'Левон'
    #     worker.save()
    #     print(worker.name, worker.last_name, worker.salary, worker.id)
    #
    # print(all_workes)
    # workers_filtred = Worker.objects.filter(salary=1)
    # print(workers_filtred)
    # print(Worker.objects.get(id=1))
    # print(type(worker_to_change.last_name))
    return render(request, 'index.html')#, context={'data': all_workes}
