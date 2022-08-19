from curses.ascii import isspace
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import AnkenList
# from django import request
# from django.http import HttpResponse   #add

# def index(request):    #add
#    message = 'Hello Django!!'
#    return HttpResponse(message)

class PrimeappView(TemplateView):
    template_name = 'book/number_treat.html'

class NumberTreatView(TemplateView):
    template_name = 'book/n_treat.html'

class RtnTopView(TemplateView):
    template_name = 'book/top_menu.html'  



def page_n0(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    if (q[0].keiriShonin) == True:
        request.session['sessionDisplayCode'] = 'dp11'             
        return render(request, 'book/page_n.html', ctx)
    request.session['sessionDisplayCode'] = 'dp01'    
    return render(request, 'book/page_n0.html', ctx) 

def initialStart(request):
    request.session['sessionDisplayCode'] = 'dp02'    ## tempolary setting !!!
    print('sessionDisplayCode =', request.session['sessionDisplayCode'])
    print('L37 in intialStart!!!!!!')
    return redirect('page_n')



def page_n(request):
    print('request.session[sessionDisplayCode] =', request.session['sessionDisplayCode'] )
    model = AnkenList
    print("Current point is L45 !!")
    if request.session['sessionDisplayCode'] == 'dp02' and request.method == "POST":
        inData = request.POST.get('inputNo')
        request.session['sessionKanriNo'] = inData
        print("inData =", inData)
        print(' You are right !!!!!')
        if not (inData is None) or  inData == "" :          ### 空文字検出　いまいち！

#        if str(inData).isspace() == True:
            print("L53 Here! indata !=0 ")
            inData = request.POST.get('inputNo')
            context = contextSet(inData)
            # ctx = {}
            # q = AnkenList.objects.filter(kanriNo=str(inData)) # テーブルにあるinputKanriNoを含むレコードを取得
            # request.session['sessionKanriNo'] = inData
            # ctx["object"] = q
            # badgeName = ["案件入力済\n(STATUS = 1)", \
            #             "見積書依頼処理\n(STATUS = 2)", \
            #             "見積書入手処理\n(STATUS = 3)", \
            #             "稟議承認処理\n(STATUS = 4)", \
            #             "契約書_作成完了\n(STATUS = 5)",\
            #             "契約書_締結完了\n(STATUS = 6)", \
            #             "注文処理\n(STATUS = 7)", \
            #             "納品処理\n(STATUS = 8)", \
            #             "請求書処理\n(STATUS = 9)", \
            #             "支払処理済\n(STATUS = 10)"
            #             ]
            # buttonName = ["案件入力を終了しました", "見積書の作成依頼を終了しました", \
            #             "見積書を入手しました", "稟議決裁を終了しました", \
            #             "契約書の作成が終了しました", "契約書の締結が終了しました", \
            #             "注文処理が終了しました", "納品処理が終了しました", \
            #             "請求書処理が終了しました", "支払処理が終了しました"
            #             ]
            # buttonName2 = ["ankenNyuuryokuKan1", "mitsumorisyoIraiKan2", \
            #             "mitumorisyoNyuusyuKan3", "ringiShoninKan4", \
            #             "keiyakusyoSakuseiKan5", "keiyakusyoTeiketsuKan6", \
            #             "cyuumonKan7", "nouhinKan8", \
            #             "seikyuusyoNyuusyu9", "shiharaiKan10" 
            #             ]
            # badgeGray = q[0].statusCode
            # buttonGray = q[0].statusCode
            # list_a = ["太郎", "次郎", "三郎", "四郎"]
            # list_b = ["東京", "神奈川", "群馬", "静岡"]
            # context = {
            #     'badgeName': badgeName,
            #     'buttonName': buttonName,
            #     'buttonName2': buttonName2,
            #     'badgeGray': badgeGray,
            #     'buttonGray': buttonGray,
            #     'list_a': list_a,
            #     'list_b': list_b,
            #     'q': q,
            # }
            print(" arrived at L86 !!You are right!!!")
            request.session['sessionDisplayCode'] = 'dp11' 
            return render(request, 'book/page_n.html', context)
        else:
            request.session['sessionDisplayCode'] = 'dp02'             
            return render(request, 'book/number_treat.html')            

    if request.session['sessionDisplayCode'] == 'dp02':
        request.session['sessionDisplayCode'] = 'dp02'   
        return render(request, 'book/number_treat.html')
    elif request.session['sessionDisplayCode'] ==  'dp10':
        if  "pageN" in request.POST:
                request.session['sessionDisplayCode'] = 'dp11' 
                context = contextSet( request.session['sessionKanriNo'] )
                return render(request, 'book/page_n.html', context)
        elif "pageTop" in request.POST:
                request.session['sessionDisplayCode'] = 'dp00' 
                return render(request, 'book/top_menu.html')
        else:
            return render(request, 'book/ankenNyuuryokuKan1.html')

    elif request.session['sessionDisplayCode'] ==  'dp20':
        if  "pageN" in request.POST:
                request.session['sessionDisplayCode'] = 'dp11' 
                context = contextSet( request.session['sessionKanriNo'] )
                return render(request, 'book/page_n.html', context)
        elif "pageTop" in request.POST:
                request.session['sessionDisplayCode'] = 'dp00' 
                return render(request, 'book/top_menu.html')
        else:
            return render(request, 'book/mitsumorisyoIraiKan2.html')

    elif request.session['sessionDisplayCode'] ==  'dp30':
        if  "pageN" in request.POST:
                request.session['sessionDisplayCode'] = 'dp11' 
                context = contextSet( request.session['sessionKanriNo'] )
                return render(request, 'book/page_n.html', context)
        elif "pageTop" in request.POST:
                request.session['sessionDisplayCode'] = 'dp00' 
                return render(request, 'book/top_menu.html')
        else:
            return render(request, 'book/mitumorisyoNyuusyuKan3.html')

    else:
        print( "arrived L118 !!")
        if  "ankenNyuuryokuKan1"  in request.POST:  # (クリックしたボタンに応じたHTMLへ分岐させる)
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 1
            )
            print("Detected the button1")
            request.session['sessionDisplayCode'] = 'dp10'   
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/ankenNyuuryokuKan1.html', context)

        elif "mitsumorisyoIraiKan2" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 2
            )
            print("Detected the button2")
            request.session['sessionDisplayCode'] = 'dp20'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/mitsumorisyoIraiKan2.html', context)

        elif "mitumorisyoNyuusyuKan3" in request.POST:
            print(" L138 is here !!")
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 3
            )
            print("Detected the button3")
            request.session['sessionDisplayCode'] = 'dp30'
            context = contextSet( request.session['sessionKanriNo'] )
            print(" L145 is here !!")
            return render(request, 'book/mitumorisyoNyuusyuKan3.html', context)
        
        elif "skipPage3to4" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 4
            )
            print("Detected the skip-button(in dp40)")
            request.session['sessionDisplayCode'] = 'dp40'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "ringiShoninKan4" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 4
            )
            print("Detected the button4")
            request.session['sessionDisplayCode'] = 'dp40'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/ringiShoninKan4.html', context)

        elif "skipPage4to5" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 5
            )
            print("Detected the skip-button(in dp50)")
            request.session['sessionDisplayCode'] = 'dp50'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "keiyakusyoSakuseiKan5" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 5
            )
            print("Detected the button5")
            request.session['sessionDisplayCode'] = 'dp50'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/keiyakusyoSakuseiKan5.html', context)

        elif "skipPage5to6" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 6
            )
            print("Detected the skip-button(in dp60)")
            request.session['sessionDisplayCode'] = 'dp60'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "keiyakusyoTeiketsuKan6" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 6
            )
            print("Detected the button6")
            request.session['sessionDisplayCode'] = 'dp60'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/keiyakusyoTeiketsuKan6.html', context)

        elif "skipPage6to7" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 7
            )
            print("Detected the skip-button(in dp70)")
            request.session['sessionDisplayCode'] = 'dp70'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "cyuumonKan7" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 7
            )
            print("Detected the button7")
            request.session['sessionDisplayCode'] = 'dp70'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/cyuumonKan7.html', context)

        elif "skipPage7to8" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 8
            )
            print("Detected the skip-button(in dp80)")
            request.session['sessionDisplayCode'] = 'dp70'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "nouhinKan8" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 8
            )
            print("Detected the button8")
            request.session['sessionDisplayCode'] = 'dp80'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/nouhinKan8.html', context)

        elif "skipPage8to9" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 9
            )
            print("Detected the skip-button(in dp90)")
            request.session['sessionDisplayCode'] = 'dp70'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "seikyuusyoNyuusyu9" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 9
            )
            print("Detected the button9")
            request.session['sessionDisplayCode'] = 'dp90'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/seikyuusyoNyuusyu9.html', context)

        elif "skipPage9to10" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 10
            )
            print("Detected the skip-button(in dp100)")
            request.session['sessionDisplayCode'] = 'dp100'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/page_n.html', context)

        elif "shiharaiKan10" in request.POST:
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 10
            )
            print("Detected the button10")
            request.session['sessionDisplayCode'] = 'dp100'
            context = contextSet( request.session['sessionKanriNo'] )
            return render(request, 'book/shiharaiKan10.html', context)
        else:
            request.session['sessionDisplayCode'] = 'dp02'   
            return render(request, 'book/number_treat.html')

    request.session['sessionDisplayCode'] = 'dp02'   
    return render(request, 'book/number_treat.html')


def mitsumoriSave(request):   # 入力した見積情報をＤＢに書き込んでpage_n.htmlへ遷移する
    print("Arrived L349 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif  "confirm" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 3,
            mitsumoriTanka = request.POST.get('mitsumoriTanka'),
            mitsumoriSuu = request.POST.get('mitsumoriSuu'),
            mitsumoriLink = request.POST.get('mitsumoriLink')
        )
        print("見積金額、リンク情報をDBへ格納しました。Detected the 確定ボタン")
        request.session['sessionDisplayCode'] = 'dp11'  
        return render(request, 'book/page_n.html', context)
    else:
        request.session['sessionDisplayCode'] = 'dp30'
        return render(request, 'book/mitumorisyoNyuusyuKan3.html')

def ringiShoninSave(request):   
    print("Arrived L325 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif "skipPage3to4" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 4
        )
        print("Detected the skip-button(in dp40)")
        request.session['sessionDisplayCode'] = 'dp40'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)
    elif  "confirm" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 4,
            ringiTanka = request.POST.get('ringiTanka'),
            ringiSuu = request.POST.get('ringiSuu'),
            ringiGokei = int(request.POST.get('ringiTanka'))*int(request.POST.get('ringiSuu')),
            ringishoLink = request.POST.get('ringishoLink')
        )
        print("稟議書番号をDBへ格納しました。Detected the 確定ボタン。Detected the 確定ボタン")
        request.session['sessionDisplayCode'] = 'dp11'  
        return render(request, 'book/page_n.html', context)
    else:
        request.session['sessionDisplayCode'] = 'dp40'
        return render(request, 'book/ringiShoninKan4.html')

def keiyakusyoSakuseiSave(request): 
    print("Arrived L353 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif "skipPage4to5" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 5
        )
        print("Detected the skip-button(in dp50)")
        request.session['sessionDisplayCode'] = 'dp50'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)
    elif  "confirm" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 5,
            wfNo = request.POST.get('wfNo'),
            keiyakushoNo = request.POST.get('keiyakushoNo'),
            keiyakuKingaku = request.POST.get('keiyakuKingaku'),
            keiyakushoLink = request.POST.get('keiyakushoLink')
        )
        print("wfno、契約書番号、金額、urlをDBへ格納しました。Detected the 確定ボタン")
        request.session['sessionDisplayCode'] = 'dp11'  
        return render(request, 'book/page_n.html', context)
    else:
        request.session['sessionDisplayCode'] = 'dp50'
        return render(request, 'book/keiyakusyoSakuseiKan5.html')

def keiyakusyoTeiketsuSave(request):
    print("Arrived L381 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        print("Detected the pageTop-button(in dp60)")
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif "skipPage5to6" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 6
        )
        print("Detected the skip-button(in dp60)")
        request.session['sessionDisplayCode'] = 'dp60'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)
    elif  "confirm" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 6,
            onatsuRingiNo = request.POST.get('onatsuRingiNo'),
            onatsuRingiLink = request.POST.get('onatsuRingiLink')
        )
        print("Detected the confirm button in dp60 button6")
        request.session['sessionDisplayCode'] = 'dp11'  
        return render(request, 'book/page_n.html', context)
    else:
        request.session['sessionDisplayCode'] = 'dp60'
        return render(request, 'book/keiyakusyoTeiketsuKan6.html')    

def cyuumonSave(request):
    print("Arrived L412 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        print("Detected the pageTop-button(in dp70)")
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif "skipPage6to7" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 7
        )
        print("Detected the skip-button(in dp70)")
        request.session['sessionDisplayCode'] = 'dp70'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)
    elif  "confirm" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 7,
            chumonTanka = request.POST.get('chumonTanka'),
            chumonSuu = request.POST.get('chumonSuu'),
            chumonGokei = int(request.POST.get('chumonTanka'))*int(request.POST.get('chumonSuu')),
            chumonLink = request.POST.get('chumonLink'),
            nohinKigen = request.POST.get('nohinKigen'),
            kenshuKigen = request.POST.get('kenshuKigen'),
            shiharaiKigen = request.POST.get('shiharaiKigen')
        )
        print("Detected the confirm button in dp70 button7")
        request.session['sessionDisplayCode'] = 'dp11'  
        return render(request, 'book/page_n.html', context)
    else:
        request.session['sessionDisplayCode'] = 'dp70'
        return render(request, 'book/cyuumonKan7.html')    

def nouhinSave(request):  
    print("Arrived L445 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        print("Detected the pageTop-button(in dp80)")
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif "skipPage7to8" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 8
        )
        print("Detected the skip-button(in dp80)")
        request.session['sessionDisplayCode'] = 'dp80'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)
    elif  "confirm" in request.POST:
        if (request.POST.get('nohinTanka') is None) or (request.POST.get('nohinTanka') == "") :          ### 空文字検出　いまいち！
            print('Detect 空文字！')
            request.session['sessionDisplayCode'] = 'dp80' 
            return render(request, 'book/nouhinKan8.html', context)
        q = AnkenList.objects.filter(kanriNo=str(request.session['sessionKanriNo']))
        if q[0].chumonGokei == int(request.POST.get('nohinTanka'))*int(request.POST.get('nohinSuu')):
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 8,
            nohinTanka = request.POST.get('nohinTanka'),
            nohinSuu = request.POST.get('nohinSuu'),
            nohinGokei = int(request.POST.get('nohinTanka'))*int(request.POST.get('nohinSuu')),
            nohinLink = request.POST.get('nohinLink')
            )
            print("請求書金額などをDBへ格納しました。Detected the 確定ボタン")
            request.session['sessionDisplayCode'] = 'dp11'   
            return render(request, 'book/page_n.html', context)
        else:
            return render(request, 'book/kingakuWarning2.html', context)

    else:
        request.session['sessionDisplayCode'] = 'dp80'
        return render(request, 'book/nouhinKan8.html')  

"""
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 8,
            nohinTanka = request.POST.get('nohinTanka'),
            nohinSuu = request.POST.get('nohinSuu'),
            nohinGokei = int(request.POST.get('nohinTanka'))*int(request.POST.get('nohinSuu')),
            nohinLink = request.POST.get('nohinLink')
        )
        print("Detected the confirm button in dp80 button8")
        request.session['sessionDisplayCode'] = 'dp11'  
        return render(request, 'book/page_n.html', context)
"""
def seikyuusyoSave(request): 
    print("Arrived L475 !!!")
    context = contextSet( request.session['sessionKanriNo'] )
    if "pageTop" in request.POST:
        print("Detected the pageTop-button(in dp90)")
        request.session['sessionDisplayCode'] = 'dp00' 
        return render(request, 'book/top_menu.html')
    elif "skipPage8to9" in request.POST:
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 9
        )
        print("Detected the skip-button(in dp90)")
        request.session['sessionDisplayCode'] = 'dp90'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)
    elif  "confirm" in request.POST:
        if (request.POST.get('shiharaiTanka') is None) or (request.POST.get('shiharaiTanka') == "") :          ### 空文字検出　いまいち！
            print('Detect 空文字！')
            request.session['sessionDisplayCode'] = 'dp90' 
            return render(request, 'book/seikyuusyoNyuusyu9.html', context)
        q = AnkenList.objects.filter(kanriNo=str(request.session['sessionKanriNo']))
        if q[0].chumonGokei == int(request.POST.get('shiharaiTanka'))*int(request.POST.get('konyuSuu')):
            AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
                statusCode = 9,
                shiharaiTanka = request.POST.get('shiharaiTanka'),
                konyuSuu = request.POST.get('konyuSuu'),
                seikyushoLink = request.POST.get('seikyushoLink')
            )
            print("請求書金額などをDBへ格納しました。Detected the 確定ボタン")
            request.session['sessionDisplayCode'] = 'dp11'   
            return render(request, 'book/page_n.html', context)
        else:
            return render(request, 'book/kingakuWarning2.html', context)
    else:
        request.session['sessionDisplayCode'] = 'dp90'
        return render(request, 'book/seikyuusyoNyuusyu9.html')  

"""
def seikyuusyoSave(request): 
    context = contextSet( request.session['sessionKanriNo'] )

    print(' L499 in seikyuusyoSave here!!!')

    if (request.method == "POST") and (request.session['sessionDisplayCode'] == 'dp90') \
        and ("skipPage8to9" in request.POST):
        print(' you are OK !')
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 9
        )
        print("Detected the skip button in dp90")
        request.session['sessionDisplayCode'] = 'dp90'
        context = contextSet( request.session['sessionKanriNo'] )
        return render(request, 'book/page_n.html', context)

    if (request.POST.get('shiharaiTanka') is None) or (request.POST.get('shiharaiTanka') == "") :          ### 空文字検出　いまいち！
        print('Detect 空文字！')
        request.session['sessionDisplayCode'] = 'dp90' 
        return render(request, 'book/seikyuusyoNyuusyu9.html', context)

    q = AnkenList.objects.filter(kanriNo=str(request.session['sessionKanriNo']))
    if q[0].chumonGokei == int(request.POST.get('shiharaiTanka'))*int(request.POST.get('konyuSuu')):
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            shiharaiTanka = request.POST.get('shiharaiTanka'),
            konyuSuu = request.POST.get('konyuSuu'),
            seikyushoLink = request.POST.get('seikyushoLink')
        )
        print("請求書金額などをDBへ格納しました。Detected the 確定ボタン")
        request.session['sessionDisplayCode'] = 'dp11'   
        return render(request, 'book/page_n.html', context)
    else:
        return render(request, 'book/kingakuWarning2.html', context)
"""

def kingakuInputAgain(request):
    context = contextSet( request.session['sessionKanriNo'] )
    return render(request, 'book/nouhinKan8.html', context)

def kingakuInputAgain2(request):
    context = contextSet( request.session['sessionKanriNo'] )
    return render(request, 'book/seikyuusyoNyuusyu9.html', context)

def shiharaiSave(request):     ## 多分、支払処理が終わっときのここで、DBへの登録はないでしょう。
    context = contextSet( request.session['sessionKanriNo'] )
#    if request.POST.get('mitsumoriTanka') is None:          ### 空文字検出　いまいち！
#        print('Detect 空文字！')
#        request.session['sessionDisplayCode'] = 'dp100' 
#        return render(request, 'book/shiharaiKan10.html', context)
    print("支払処理完了。とくになにもない。Detected the 確定ボタン")
    request.session['sessionDisplayCode'] = 'dp11'   
    return render(request, 'book/page_n.html', context)


def contextSet( inData ):  #　 inData： 案件管理No.
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=str(inData)) # テーブルにあるinputKanriNoを含むレコードを取得
#            request.session['sessionKanriNo'] = inData
    ctx["object"] = q
    badgeName = ["案件入力済\n(STATUS = 1)", \
                "見積書依頼処理\n(STATUS = 2)", \
                "見積書入手処理\n(STATUS = 3)", \
                "稟議承認処理\n(STATUS = 4)", \
                "契約書_作成完了\n(STATUS = 5)",\
                "契約書_締結完了\n(STATUS = 6)", \
                "注文処理\n(STATUS = 7)", \
                "納品処理\n(STATUS = 8)", \
                "請求書処理\n(STATUS = 9)", \
                "支払処理済\n(STATUS = 10)"
                ]
    buttonName = ["案件入力を終了しました", "見積書の作成依頼を終了しました", \
                "見積書を入手しました", "稟議決裁を終了しました", \
                "契約書の作成が終了しました", "契約書の締結が終了しました", \
                "注文処理が終了しました", "納品処理が終了しました", \
                "請求書処理が終了しました", "支払処理が終了しました"
                ]
    buttonName2 = ["ankenNyuuryokuKan1", "mitsumorisyoIraiKan2", \
                "mitumorisyoNyuusyuKan3", "ringiShoninKan4", \
                "keiyakusyoSakuseiKan5", "keiyakusyoTeiketsuKan6", \
                "cyuumonKan7", "nouhinKan8", \
                "seikyuusyoNyuusyu9", "shiharaiKan10" 
                ]
    badgeGray = q[0].statusCode
    buttonGray = q[0].statusCode
    list_a = ["太郎", "次郎", "三郎", "四郎"]
    list_b = ["東京", "神奈川", "群馬", "静岡"]
    context = {
        'badgeName': badgeName,
        'buttonName': buttonName,
        'buttonName2': buttonName2,
        'badgeGray': badgeGray,
        'buttonGray': buttonGray,
        'list_a': list_a,
        'list_b': list_b,
        'q': q,
    }
    return(context)

def ankennyuuryokucyuu0(request):  # 案件入力中の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page0-1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 0
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def ankenNyuuryokuKan1(request):   # 案件入力が完了したときの処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 1
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def mitsumorisyoIraiKan2(request):  # 見積書依頼が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 2
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def mitumorisyoNyuusyuKan3(request):  # 見積書入手が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 3
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def ringiShoninKan4(request):  # 稟議承認処理が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 4
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def keiyakusyoSakuseiKan5(request):  # 契約書の作成が終了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 5
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def keiyakusyoTeiketsuKan6(request):  # 契約書の締結が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 6
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def cyuumonKan7(request):  # 注文処理が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 7
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def nouhinKan8(request):  # 納品が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 8
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def seikyuusyoNyuusyu9(request):  #  請求書の入手が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 9
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx) 

def shiharaiKan10(request):  # 支払処理が完了した時の処理
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-ankenNyuuryokuKan1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 10
        )
        return render(request, 'book/page_n.html', ctx)
    return render(request, 'book/page_n0.html', ctx)                                



def branch_html(request):     #案件入力完了の確認
    model = AnkenList
    inData = request.POST.get('inputNo')
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=str(inData)) # テーブルにあるinputKanriNoを含むレコードを取得
    request.session['sessionKanriNo'] = inData
    ctx["object"] = q
    print("inData =", inData)
    print("q = ", q)

    if request.method == "POST":
        if int(q[0].statusCode) == 0:
            if (q[0].keiriShonin) == True:
                print("views:goto page0_2.html")
                return render(request, 'book/page0_2.html', ctx)
            else:
                print("views:goto page0_1.html")
                return render(request, 'book/page0_1.html', ctx)
        elif int(q[0].statusCode) == 1:
            if (q[0].keiriShonin) == True:
                print("views:goto page1_2.html")
                return render(request, 'book/page1_2.html', ctx)
            else:
                print("views:goto page1_1.html")
                return render(request, 'book/page1_1.html', ctx)
        elif int(q[0].statusCode) == 2:
            if (q[0].keiriShonin) == True:
                print("views:goto page2_2.html")
                return render(request, 'book/page2_2.html', ctx)
            else:
                print("views:goto page2_1.html")
                return render(request, 'book/page2_1.html', ctx)
        elif int(q[0].statusCode) == 3:
            if (q[0].keiriShonin) == True:
                print("views:goto page3_1_1.html")
                return render(request, 'book/page3_1_1.html', ctx)
            else:
                print("views:goto page3_1.html")
                return render(request, 'book/page3_1.html', ctx)
        elif int(q[0].statusCode) == 4:
            if (q[0].keiriShonin) == True:
                print("views:goto page4_2.html")
                return render(request, 'book/page4_2.html', ctx)
            else:
                print("views:goto page5_2.html")
                return render(request, 'book/page4_1.html', ctx)
        elif int(q[0].statusCode) == 5:
            if (q[0].keiriShonin) == True:
                print("views:goto page5_2.html")
                return render(request, 'book/page5_2.html', ctx)
            else:
                print("views:goto page5_1.html")
                return render(request, 'book/page5_1.html', ctx)
        elif int(q[0].statusCode) == 6:
            if (q[0].keiriShonin) == True:
                print("views:goto page6_2.html")
                return render(request, 'book/page6_2.html', ctx)
            else:
                print("views:goto page6_1.html")
                return render(request, 'book/page6_1.html', ctx)
        elif int(q[0].statusCode) == 7:
            if (q[0].keiriShonin) == True:
                print("views:goto page7_2.html")
                return render(request, 'book/page7_2.html', ctx)
            else:
                print("views:goto page7_1.html")
                return render(request, 'book/page7_1.html', ctx)
        elif int(q[0].statusCode) == 8:
            if (q[0].keiriShonin) == True:
                print("views:goto page8_2.html")
                return render(request, 'book/page8_2.html', ctx)
            else:
                print("views:goto page8_1.html")
                return render(request, 'book/page8_1.html', ctx)
        elif int(q[0].statusCode) == 9:
            if (q[0].keiriShonin) == True:
                print("views:goto page9_2.html")
                return render(request, 'book/page9_2.html', ctx)
            else:
                print("views:goto page9_1.html")
                return render(request, 'book/page9_1.html', ctx)
        elif int(q[0].statusCode) == 10:
            if (q[0].keiriShonin) == True:
                print("views:goto page10_2.html")
                return render(request, 'book/page10_2.html', ctx)
            else:
                print("views:goto page10_1.html")
                return render(request, 'book/page10_1.html', ctx)
                       # dummy !
    
#    for_range =  [i for i in range(1, 6)]
#    context = {
#        'for_range': for_range,
#    }
    return render(request, 'book/number_treat.html', ctx) 

def page0_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page0-1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 0
        )
        return render(request, 'book/page0_2.html', ctx)
    return render(request, 'book/page0_1.html', ctx) 

def page0_2(request):     #案件入力の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 1
    )
    ctx["object"] = q
    print("passed the views.py-def-page0-2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page0_2.html', ctx) 

def page1_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page1-1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 1
        )
        return render(request, 'book/page1_2.html', ctx)
    return render(request, 'book/page1_1.html', ctx) 

def page1_2(request):     #見積書依頼の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 1
    )
    ctx["object"] = q
    print("passed the views.py-def-page1-2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page1_2.html', ctx) 

def page2_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("keiriShonin =", q[0].keiriShonin)
    print("passed the views.py-def-page2-1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 2
        )
        return render(request, 'book/page2_2.html', ctx)
    return render(request, 'book/page2_1.html', ctx) 

def page2_2(request):     #見積書依頼の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 2
    )
    ctx["object"] = q
    print("passed the views.py-def-page2-2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page2_2.html', ctx) 

def page3_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page3-1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 3
        )
        return render(request, 'book/page3_1_1.html', ctx)
    return render(request, 'book/page3_1.html', ctx) 

def page3_1_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page3_1_1 ")
    print("statusCode =", q[0].statusCode)
#    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
#        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
#            statusCode = 3
#    )
#        return render(request, 'book/page3_2.html', ctx)
    mitsumoriTanka = int(request.POST.get('mitsumoriTanka'))
    print('mitsumoriTanka =', mitsumoriTanka)
    mitsumoriSuu = int (request.POST.get('mitsumoriSuu'))
    print('mitsumoriSuu =', mitsumoriSuu)
    mitsumoriLink = str(request.POST.get('mitsumoriLink'))
    print('mitsumoriLink =', mitsumoriLink)
    return render(request, 'book/page3_2.html', ctx) 

def page3_2(request):      #見積書入手の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 3
    )
    ctx["object"] = q
    print("passed the views.py-def-page3-2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page3_2.html', ctx) 

def page4_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page4-1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 4
        )
        return render(request, 'book/page4_2.html', ctx)
    return render(request, 'book/page4_1.html', ctx) 

def page4_2(request):       #稟議承認完了の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 4
    )
    ctx["object"] = q
    print("passed the views.py-def-page4-2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page4_2.html', ctx) 

def page5_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page5_1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 5
        )
        return render(request, 'book/page5_2.html', ctx)
    return render(request, 'book/page5_1.html', ctx) 

def page5_2(request):      #契約書(作成完了)の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 5
    )
    ctx["object"] = q
    print("passed the views.py-def-page5_2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page5_2.html', ctx) 

def page6_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page6_1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 6
        )
        return render(request, 'book/page6_2.html', ctx)
    return render(request, 'book/page6_1.html', ctx) 

def page6_2(request):      #契約書(締結完了)の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 6
    )
    ctx["object"] = q
    print("passed the views.py-def-page6_2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page6_2.html', ctx) 

def page7_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page7_1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 7
        )
        return render(request, 'book/page7_2.html', ctx)
    return render(request, 'book/page7_1.html', ctx) 

def page7_2(request):     #注文処理済の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 7
    )
    ctx["object"] = q
    print("passed the views.py-def-page7_2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page7_2.html', ctx)  

def page8_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page8_1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 8
        )
        return render(request, 'book/page8_2.html', ctx)
    return render(request, 'book/page8_1.html', ctx) 

def page8_2(request):     #納品済の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 8
    )
    ctx["object"] = q
    print("passed the views.py-def-page8_2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page8_2.html', ctx)  

def page9_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page9_1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 1
        )
        return render(request, 'book/page9_2.html', ctx)
    return render(request, 'book/page9_1.html', ctx) 

def page9_2(request):      #請求書入手済の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 9
    )
    ctx["object"] = q
    print("passed the views.py-def-page9_2 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page9_2.html', ctx)  

def page10_1(request):
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    ctx["object"] = q
    print("passed the views.py-def-page10_1 ")
    print("statusCode =", q[0].statusCode)
    if (q[0].keiriShonin) == True:             # !!!!! dummy code !!!!!!!
        AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
            statusCode = 10
        )
        return render(request, 'book/page10_2.html', ctx)
    return render(request, 'book/page10_1.html', ctx) 

def page10_2(request):     #支払処理済の確認
    model = AnkenList
    ctx = {}
    q = AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo'])
    AnkenList.objects.filter(kanriNo=request.session['sessionKanriNo']).update(
        statusCode = 10
    )
    ctx["object"] = q
    print("passed the views.py-def-page10_1 ")
    print("statusCode =", q[0].statusCode)
    return render(request, 'book/page10_2.html', ctx) 

