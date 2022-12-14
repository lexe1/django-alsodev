from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Image
from .forms import ItemForm, ImageForm
from .serializers import ItemSerializer


def add(request):
    form = ItemForm()
    image_form = ImageForm
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if form.is_valid():
            item = form.save()
            for image in images:
                Image.objects.create(item=item, image=image)
            # return redirect('/')
    return render(request, 'add.html', {'form': form, 'image_form': image_form})


def index(request):
    return render(request, 'index.html')


@ api_view(['GET'])
def list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def details(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def create(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@ api_view(['POST'])
def update(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@ api_view(['DELETE'])
def delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response('Item deleted.')
