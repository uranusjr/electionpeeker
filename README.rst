===============
偷看立委開票狀況
===============

.. raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


我很想即時知道 2016 大選立委最終席次預估，但都沒網站做這種東西。所以就自己做了。

方法既簡單而暴力，就是直接 crawl `中選會的網站`_，把該拿的拿回來，根據選罷法的規則算出目前票數的當選狀況。

爬回來的東西很多，但這次我只想看整體席次分佈，所以只有做了這個東西的輸出。之後如果有人想玩的話，應該可以把 crawler 另外接一接，就可以呈現想要的資訊。

這次也選完了，如果有興趣再連絡我就是，或許可以做一個網站什麼的。


Requirements
=============

* Python 3。我用 3.5.1，不確定可以支援到多低。不過 Python 2 肯定是 out 了。
* ``pip install -r requirements.txt``


_`中選會的網站`: http://www.cec.gov.tw/zh_TW/IDX/indexT.html
