from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
# Create your views here.
from cms.models import Kanmusu, Impression
from cms.forms import KanmusuForm, ImpressionForm

def kanmusu_list(request):
    """艦娘の一覧"""
    #return HttpResponse('艦娘の一覧')
    kanmusutachi = Kanmusu.objects.all().order_by('id')
    return render(request,
                  'cms/kanmusu_list.html',
                  {'kanmusutachi': kanmusutachi})

def kanmusu_edit(request, kanmusu_id=None):
    """艦娘の編集"""
    #   return HttpResponse()
    if kanmusu_id:  # kanmusu_idが指定
        kanmusu = get_object_or_404(Kanmusu, pk=kanmusu_id)
    else:  #kanmusu_id未指定
        kanmusu = Kanmusu()

    if request.method == 'POST':
        form = KanmusuForm(request.POST, instance=kanmusu)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            kanmusu = form.save(commit=False)
            kanmusu.save()
            return redirect('cms:kanmusu_list')
    else:    # GET の時
        form = KanmusuForm(instance=kanmusu)  # kanmusu インスタンスからフォームを作成

    return render(request, 'cms/kanmusu_edit.html', dict(form=form, kanmusu_id=kanmusu_id))



def kanmusu_del(request, kanmusu_id):
    """艦娘の削除"""
    # return HttpResponse('艦娘の削除')
    kanmusu = get_object_or_404(Kanmusu, pk=kanmusu_id)
    kanmusu.delete()
    return redirect('cms:kanmusu_list')


class ImpressionList(ListView):
    """感想の一覧"""
    context_object_name = 'impressions'
    template_name = 'cms/impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        kanmusu = get_object_or_404(Kanmusu, pk=kwargs['kanmusu_id'])  #
        impressions = kanmusu.impressions.all().order_by('id')  #
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, kanmusu=kanmusu)
        return self.render_to_response(context)

def impression_edit(request, kanmusu_id, impression_id=None):
    """感想の編集"""
    book = get_object_or_404(Kanmusu, pk=kanmusu_id)  # 親の書籍を読む
    if impression_id:   # impression_id が指定されている (修正時)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:               # impression_id が指定されていない (追加時)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            impression = form.save(commit=False)
            impression.book = book  # この感想の、親の書籍をセット
            impression.save()
            return redirect('cms:impression_list', kanmusu_id=kanmusu_id)
    else:    # GET の時
        form = ImpressionForm(instance=impression)  # impression インスタンスからフォームを作成

    return render(request,
                  'cms/impression_edit.html',
                  dict(form=form, kanmusu_id=kanmusu_id, impression_id=impression_id))

def impression_del(request, kanmusu_id, impression_id):
    """感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', kanmusu_id=kanmusu_id)