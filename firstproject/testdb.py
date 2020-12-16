from datetime import datetime

from django.shortcuts import render
from django.utils import timezone

from firstproject.models import Asset


def testdb(request):
    assets = Asset.objects.all()
    va = ""
    for asset in assets:
        va += "id:{},biz_id:{},asset_name:{},asset_category:{},reference_value:{}".format(
            asset.id, asset.biz_id, asset.asset_name, asset.asset_category, asset.reference_value)
    asset1 = Asset.objects.get(biz_id='YG20201209000006')
    asset1.delete()
    asset_new = Asset(created_at=timezone.localtime(), created_by="sys1", updated_at=timezone.localtime(), updated_by="sys1",
                      biz_id="YG20201209000006", asset_name="资产名称6", asset_category="F0000000", reference_value=623.45)
    Asset.save(asset_new)
    asset1 = Asset.objects.get(biz_id='YG20201209000006')
    va += "id:{},biz_id:{},asset_name:{},asset_category:{},reference_value:{}".format(
        asset1.id, asset1.biz_id, asset1.asset_name, asset1.asset_category, asset1.reference_value)

    return render(request, "testdb.html", {"str": va})
