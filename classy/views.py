from django.shortcuts import render, redirect
from .models import Classifier


def index(request):
    visible_classifiers = Classifier.objects.filter(is_visible=True)
    classifiers = [(classifier.id, classifier.name) for classifier in visible_classifiers]
    context = {'classifiers': classifiers}
    if request.POST:
        classifier_id = int(request.POST.get('classifier'))
        return redirect('classifier', pk=classifier_id)
    else:
        return render(request, 'classy/index.html', context)


def classifier(request, pk):
    classifier = Classifier.objects.get(pk=pk)
    corpus = classifier.corpus_set.all()
    labels = {corpi.category for corpi in corpus}
    context = {'classifier': classifier, 'labels': labels}
    if request.POST:
        text = request.POST.get('text')
        classifier.train()
        prediction = classifier.predict(text)
        context['text'] = text
        context['prediction'] = prediction
        return render(request, 'classy/classifier.html', context)
    else:
        return render(request, 'classy/classifier.html', context)


def trainer(request, pk):
    classifier = Classifier.objects.get(pk=pk)
    corpus = classifier.corpus_set.all()
    labels = {corpi.category for corpi in corpus}
    context = {'classifier': classifier, 'labels': labels}
    if request.POST:
        print("POSTING")
        text = request.POST.get('training_text')
        label = request.POST.get('label')
        classifier.add_corpus(text, label)
        return render(request, 'classy/trainer.html', context)
    else:
        return render(request, 'classy/trainer.html', context)
