'''

Title: locustfile.py
Description: Defines the behavior of the locust threads to load test Pretix by swarming it with ticket purchase requests of fictitious users.
Notes: Install requirements before running this file. Change the values of the global variables for your own usage.

Authors: Filipe Pires (85122) and João Alegria (85048)

'''

from locust import * #HttpLocust, TaskSet, between, task

token = "yesixqytjfmbdqgzn1gkn1xqqxrsbof7frx6eeur4w2toiuqmdglbdn8bzprc4om" # generated in Pretix's website in admin mode

organizer = "ws"
event = "ws2020"
question = 1
host = "http://localhost:8888/"

r = [
    [
        host+""+organizer+"/"+event+"/",
        host+"static/CACHE/css/e69921ab2b6e.css",
        host+"media/pub/"+organizer+"/"+event+"/presale.a37ec5cea5997d87.css",
        host+"static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
        host+"static/jsi18n/en/djangojs.366c16383242.js",
        host+"static/fonts/opensans_regular_macroman/OpenSans-Regular-webfont.79515ad07889.woff",
        host+"static/fontawesome/fonts/fontawesome-webfont.af7ae505a9ee.woff2",
        host+"static/fonts/opensans_bold_macroman/OpenSans-Bold-webfont.2e90d5152ce9.woff",
        host+"static/lightbox/images/prev.84b76dee6b27.png",
        host+"static/lightbox/images/next.31f15875975a.png",
        host+"static/lightbox/images/loading.2299ad0b3f63.gif",
        host+"static/lightbox/images/close.d9d2d0b1308c.png",
        host+"static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
        host+"static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png",
    ],
    [
        host+""+organizer+"/"+event+"/?require_cookie=true",
        host+"static/CACHE/css/e69921ab2b6e.css",
        host+"media/pub/"+organizer+"/"+event+"/presale.a37ec5cea5997d87.css",
        host+"static/CACHE/js/5b8f603ac609.js",
        host+"static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
        host+"static/jsi18n/en/djangojs.366c16383242.js",
        host+"static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
        host+"static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png",
        host+"static/fonts/opensans_italic_macroman/OpenSans-Italic-webfont.f42641eed834.woff"
    ],
    [
        host+""+organizer+"/"+event+"/checkout/start",
        host+""+organizer+"/"+event+"/checkout/questions/",
        host+"static/CACHE/css/e69921ab2b6e.css",
        host+"media/pub/"+organizer+"/"+event+"/presale.a37ec5cea5997d87.css",
        host+"static/CACHE/js/5b8f603ac609.js",
        host+"static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
        host+"static/jsi18n/en/djangojs.366c16383242.js",
        host+"static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
        host+"static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
    ],
    [
        #host+""+organizer+"/"+event+"/checkout/questions/", # post
        host+""+organizer+"/"+event+"/checkout/payment/",
        host+"static/CACHE/css/e69921ab2b6e.css",
        host+"media/pub/"+organizer+"/"+event+"/presale.a37ec5cea5997d87.css",
        host+"static/CACHE/js/5b8f603ac609.js",
        host+"static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
        host+"static/jsi18n/en/djangojs.366c16383242.js",
        host+"static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
        host+"static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
    ],
    [
        #host+""+organizer+"/"+event+"/checkout/payment/", # post
        host+""+organizer+"/"+event+"/checkout/confirm/",
        host+"static/CACHE/css/e69921ab2b6e.css",
        host+"media/pub/"+organizer+"/"+event+"/presale.a37ec5cea5997d87.css",
        host+"static/CACHE/js/5b8f603ac609.js",
        host+"static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
        host+"static/jsi18n/en/djangojs.366c16383242.js",
        host+"static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
        host+"static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
    ],
    [
        host+"api/v1/organizers/"+organizer+"/events/"+event+"/orders/", # post
        #host+""+organizer+"/"+event+"/order/WBWFT/14xhln2apnqkl1r7/pay/1/complete",
        #host+""+organizer+"/"+event+"/order/WBWFT/14xhln2apnqkl1r7/?thanks=yes",
        host+"static/CACHE/css/e69921ab2b6e.css",
        host+"media/pub/"+organizer+"/"+event+"/presale.a37ec5cea5997d87.css",
        host+"static/CACHE/js/5b8f603ac609.js",
        host+"static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
        host+"static/jsi18n/en/djangojs.366c16383242.js",
        host+"static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
        host+"static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
    ]
]

class UserBehavior(TaskSet):
    
    totalPurchaseAttempts = 0
    maxPurchaseAttempts = 800
    
    #def on_start(self):
    #    pass

    #def on_stop(self):
    #    pass

    @task
    def get(self):
        
        if UserBehavior.totalPurchaseAttempts == UserBehavior.maxPurchaseAttempts:
            return
        
        UserBehavior.totalPurchaseAttempts+=1
        print("Total Purchase Attempts: "+str(UserBehavior.totalPurchaseAttempts))
        
        global r
        global token
        global question
        user_email = 'user'+str(UserBehavior.totalPurchaseAttempts)+'@example.org'
        
        for i in range(0,len(r)):
            for j in range(0,len(r[i])):
                if i==(len(r)-1) and j==0:
                    body = '{"detail":"", "email": "' + user_email + '","locale": "en","sales_channel": "web","invoice_address": {"is_business": "false","company": "Sample company","name_parts": {"full_name": "John Doe"},"street": "Sesam Street 12","zipcode": "12345","city": "Sample City","state": "","internal_reference": "","vat_id": ""},"positions": [{"item": 1,"attendee_name_parts": {"full_name": "Peter"},"answers": [{"question": '+str(question)+',"answer": "23","options": []}]}] }'
                    self.client.post(r[i][j], headers={"Authorization": "Token " + token, "Content-Type": "application/json"}, data=body)
                self.client.get(r[i][j], headers={"Authorization": "Token " + token})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(0.1, 0.9)
