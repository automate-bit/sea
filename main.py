
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivmob import KivMob ,TestIds
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *
from kivy.uix.textinput import TextInput
import random
from nltk import word_tokenize

import plyer
import time
class myfuck(GridLayout):
    def __init__(self,**kwargs):
        super(myfuck, self).__init__(**kwargs)
        Window.size=(300,590)
        Window.clearcolor=(1,1,1,1)
        



        with self.canvas.before :
            Rectangle(source='letty.png',pos=(0,535),size=(300,60))

        with self.canvas.before :
            Rectangle(source='label.png',pos=(0,50),size=(300,450))

        self.i=TextInput(text='',size=(230,30),background_color=(0.7,0.7,0.7,0.4),multiline=True,font_size='15sp')
        self.add_widget(self.i)
        self.b=Button(text="send",pos=(230,0),size_hint=(None,None),size=(70,30),background_color=(0,0.6,0,1))
        self.b.bind(on_press=self.sen)
        self.add_widget(self.b)
        self.ad=Button(text='S T A T U S    ',pos=(-10,500),size_hint=(None,None),size=(320,40),background_color=(0.5,0.8,0,1))
        self.ad.bind(on_press=self.lol)
        self.add_widget(self.ad)
        self.camera=Button(text='AD',pos=(220,40),size=(30,30),background_color=(20,0,0,1))
        self.camera.bind(on_press=self.tuhin)
        self.add_widget(self.camera)
        self.add_widget(Label(text='i am your pocket doctor \n you can ask me \n any things about health \n(please type in small letter)',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))

    

            
    def sen(self,instance):
        self.wrd=word_tokenize(self.i.text)
        for m in self.wrd :
            if m=='hi' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='hello ! how an i help you',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))

            if m=='hello' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='hello ! how an i help you',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))


            if m=='hallo' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='hello ! how an i help you',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))


            if m=='hey' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='hello ! how an i help you',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))

            if m=='hii' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='hello ! how an i help you',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))

                
            if m=='heyy' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='hello ! how an i help you',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))
            

            if self.wrd=='what can you do for me' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='i am your pocket doctor',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))



#-------------------------------------------------------------------------love---------------------------------------------------------------------------------------------------

            if m=='who' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='i am your pocket doctor',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))
            if m=='your' and 'name' :
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text='letty\n(letty mean joy)',pos=(50,200),size=(200,200),font_size="20sp",color=(0,0,0,1)))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            if m=='gain' and 'weight':
                weight_gain="There are some foods and exrecises \n  can help you \n to gain weight \n FOOD:-milk,cheese,whole egg,dark chocolate \n Protein Supplements,oily fish or salmon,\n red meats \n EXERCISES :- pushup,pullups, \n bench press"

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight_gain,pos=(40,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='loss' and 'weight':
                weight_loss="There are some foods and exrecises \n  can help you \n to loss weight \n FOOD:-Eat a high protein breakfast\n Avoid sugary drinks and fruit juice \n Drink water before meals.,\n take tea,eat slowly \n take water before meal \n EXERCISES :- running ,cycling, \n weight lifting,yoga \n swimming"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight_loss,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='healthy' and 'food' :
                healthy=" BEST HEALTHY FOODS :- \n fruits:-apple,banana,blueberries,orange \n strawberries \n eggs \n meats:-lean bief,chicken breasts,lamb \n vegetables:-tomato,onion,cucumber,cauliflower \n carrots,Bell Papper ,garlic \n seafoods:- salmon,tuna,shrimp \n shellfish\n dairy:-cheese,whole milk,yogurt \n an apple a day keeps the doctor away. "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=healthy,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='diet':
                weight=" BEST FOODS FOR DIETERS :- \n fruits,Whole grains \n don't avoid your morning meal \n Dips,\n Calorie-Controlled Snacks \n Healthier Fast Food \n Low-Fat and Fat-Free Dairy Products \n Rotisserie Chicken \n Diet-Friendly Desserts \n Light Salad "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='routine':
                weight=" POWER FULL DAILY ROUTINE :- \n start your day with a glass of lemon water  \n exercise,take a good break fast \n saty hydrated\n get a healthy launch \n and dinner \n walk for some munites \n sleep"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='daily':
                weight=" POWER FULL DAILY ROUTINE :- \n start your day with a glass of lemon water  \n exercise,take a good break fast \n saty hydrated\n get a healthy launch \n and dinner \n walk for some munites \n sleep"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))
                




            if m=='sleep':
                weight=" Official recommendations for sleep :- \n Older adults (65+): 7–8 hours \n Adults (18–64 years): 7–9 hours \n Teenagers (14–17 years): 8–10 hours \n School children (6–13 years): 9–11 hours \n Preschoolers (3–5 years): 10–13 hours \n Toddlers (1–2 years): 11–14 hours \n Infants (4–11 months): 12–15 hours \n Newborns (0–3 months): 14–17 hours \n Einstein slept for 10 hours a day \n Elon musk takes 4 hours sleep a day"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

                

            if m=='anxiety':
                weight=" 6 TIPS TO DEAL WITH ANXIETY:- \n connect to others  \n connect to the nature \n identify triggers for anxiety\n connect with good thing \n chewing gum is best for temporary \n solution of anxiety.\n sleep enough"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='anxious':
                weight=" 6 TIPS TO DEAL WITH ANXIETY:- \n connect to others  \n connect to the nature \n identify triggers for anxiety\n connect with good thing \n chewing gum is best for temporary \n solution of anxiety.\n sleep enough"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='sad':
                weight="TIPS TO DEAL WITH SADNESS:- \n make a smile and say 'i am fine '  \n connect to the nature \n identify triggers of sadness\n connect with good thing \n watch a funny show\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='fatigue':
                weight="Fatigue:- \nlack of exercise\nlack of sleep\nmuscle disease\nanemia\ndiabetes\nthe flu,or other fever"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='down':
                weight="TIPS TO DEAL WITH SADNESS:- \n make a smile and say 'i am fine '  \n connect to the nature \n identify triggers of sadness\n connect with good thing \n watch a funny show\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))









            if m=='acromegaly':
                weight="ACROMEGALY:- \n Enlarged hands and feet\n Coarsened, enlarged \n facial features \n Coarse, oily, thickened skin \n Excessive sweating and body odor \n Small outgrowths of skin \n tissue (skin tags) \n Fatigue and muscle weakness \n A deepened, husky voice \n due to enlarged \n vocal cords and sinuses \n Severe snoring due to obstruction \nof the upper airway \n Impaired vision \n Headaches \n Enlarged tongue \n Pain and limited joint mobility \n Menstrual cycle irregularities in women \n Loss of interest in sex \n Erectile dysfunction in men"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(80,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='addison':
                weight="ADDISON DISEASES:- \n Extreme fatigue\n Weight loss and decreased appetite,enlarged \n Darkening of your skin (hyperpigmentation) \n Low blood pressure, even fainting \n Salt craving \n Low blood sugar \n Nausea, diarrhea or vomiting \n Abdominal pain \n Muscle or joint pains \n Irritability \n Depression \n Body hair loss or sexual \n dysfunction in women "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(80,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))






            if m=='ards':
                weight="Acute respiratory distress syndrome\n(HIV):- \n Severe shortness of breath\nLabored and unusually rapid breathing \n Labored and unusually rapid breathing \n Confusion and extreme tiredness \n low blood pressure "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='aids':
                weight="Acquired immunodeficiency syndrome\n(HIV):- \n fever \n headache\n joint pain and muscle aches \n rash\n Sore throat and painful mouth sores \n Swollen lymph glands, mainly \n on the neck \n Diarrhea \n Weight loss \n Cough \n Night sweats"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='hiv':
                weight="Acquired immunodeficiency syndrome\n(HIV):- \n fever \n headache\n joint pain and muscle aches \n rash\n Sore throat and painful mouth sores \n Swollen lymph glands, mainly \n on the neck \n Diarrhea \n Weight loss \n Cough \n Night sweats"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='AIDS':
                weight="Acquired immunodeficiency syndrome:- \n fever \n headache\n joint pain and muscle aches \n rash\n Sore throat and painful mouth sores \n Swollen lymph glands, mainly \n on the neck \n Diarrhea \n Weight loss \n Cough \n Night sweats"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
            if m=='HIV':
                weight="Acquired immunodeficiency syndrome:- \n fever \n headache\n joint pain and muscle aches \n rash\n Sore throat and painful mouth sores \n Swollen lymph glands, mainly \n on the neck \n Diarrhea \n Weight loss \n Cough \n Night sweats"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))





            if m=='als':
                weight=":-ALS :- \n Stumbling \nA hard time holding items with your hands\n Slurred speech \nSwallowing problems\n Muscle cramps \n Worsening posture \n A hard time holding your \n head up\n muscle stifness "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='ALS':
                weight=":-ALS :- \n Stumbling \nA hard time holding items \n with your hands\n Slurred speech \nSwallowing problems\n Muscle cramps \n Worsening posture \n A hard time holding your \n head up\n muscle stifness "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='amyloidosis':
                weight="AMYLOIDOSIS:- \n headache \n Dilated pupils.\nBlurred or double vision.\nPain above and behind an eye.\nDrooping eyelid.\nHard time speaking.\n weakness\numbness"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='aneurysms':
                weight="aneurysms :- \n  \nA hard time holding items with your hands\n Slurred speech \nSwallowing problems\n Muscle cramps \n Worsening posture \n A hard time holding your \n head up\n muscle stifness "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='spondylitis':
                weight="Spondylitis:- \nYou might have pain or \n stiffness in your:\nLower back,Buttocks\nShoulders\nHands\nRib cage\nHips \n Thighs\n Heels\n feet "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='arteritis':
                weight="Arteritis:- \ndouble vision \n stiffness,hip,shoulder pain\n fatigue\n weekness\nloss of appetite\njaw pain\nfever \n weight loss\n tenderness in the \n scalp and temple areas\n "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='arthritis':
                weight="Arthritis:- \n pain \n stiffness\n swelling \n redness\n Decreased range of motion "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='artheritis':
                weight="Arthritis:- \n pain \n stiffness\n swelling \n redness\n Decreased range of motion "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='artharitis':
                weight="Arthritis:- \n pain \n stiffness\n swelling \n redness\n Decreased range of motion "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))








    
            if m=='asthma':
                weight="Asthma:- \n Shortness of breath \n Chest tightness or pain\n touble to sleep\ncoughing and wheezing \n Coughing or wheezing attacks \n that are worsened by a respiratory virus,\n such as a cold or the flu"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

                



            if m=='arthritis':
                weight="Arthritis:- \n pain \n stiffness\n swelling \n redness\n Decreased range of motion "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='atherosclerosis':
                weight="Atherosclerosis:-\n chest pain or angina.\n pain in leg or arm \n short ness of breath \n fatigue\nmuscle weakness \n confusion "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='autoimmune':
                weight="Autoimmune disease:- \nfatigue \nachy muscles\nswelling and redness\n low-grade fever\n trouble concentrating \n numbness \n hair loss \n skin rashes  "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='hemophilia':
                weight="Hemophilia:-\nblood in the urine\nblood in the stool\ndeep bruises\nexcessive bleeding\nbleeding gums\nfrequent nosebleeds\npain in the joint\nirritability (in children)"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='brainherniation':

                
                weight="Brain herniation:- \ndilated pupils\nheadache\nhigh blood pressure\ndrowsiness\ndifficulty concentrating\nloss of reflexes\nseizures\ncoma  "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

                
            if m=='breast' and 'cancer':
                weight="breast cancer:-\n1)Skin changes, such as\nswelling, redness, or other visible\ndifferences in one\nor both breasts\n2)An increase in size or change\nin shape of the breast(s)\n3)Changes in the appearance of\n one or both nipples\n4)General pain in any part of the breast\n5)Lumps or nodes felt on or \n inside of the breast"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='cardiomyopathy':
                weight="cardiomyopathy :-\nchest pain\ndizziness\nfatigue\nexcessive bleeding\nbleeding gums\nfrequent nosebleeds\npain in the joint\nirritability (in children)"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='cirrhosis ':
                weight="Cirrhosis :-\nyellowing of the skin(jaundis)\nfatigue\nweakness\nLoss of appetite\nitching\nEasy bruising from decreased\n production of blood clotting\n factors by the diseased liver"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='jaundis':
                weight="Cirrhosis :-\nyellowing of the skin(jaundis)\nfatigue\nweakness\nLoss of appetite\nitching\nEasy bruising from decreased\n production of blood clotting\n factors by the diseased liver"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='congenital':
                weight="Congenital heart disease :-\nrapid breathing\nshort breath\neasily tiring during exercise or activity\nFainting during exercise or activity\nitching\nSwelling in the hands\nankles or feet\npale,grey and blue skin colour\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='emphysema':
                weight="Emphysema :-\nfrequent lung infections\nloss appetite\nfatigue\ndepression\nheadaches in morning\nmake difficulty in night breathing\nsleep problem"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='bronchitis':
                weight="Chronic bronchitis :-\ncough,often with mucus\nWheezing\ntight chest\nShortness of breath\nFeeling tired"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='coronary':
                weight="Coronary Heart Disease :-\nshortness of breath\nWheezing\ndizziness\nShortness of breath\nweakness\nrapid heartbeat"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='angina':
                weight="Coronary Heart Disease :-\nshortness of breath\nWheezing\ndizziness\nShortness of breath\nweakness\nrapid heartbeat"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='crohn':
                weight="crohn disease symptoms :-\nDiarrhea,fever\nAbdominal pain and cramping\nblood in your stool\nfatigue\nMouth sores\nloss appetite\nweightloss"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='cushing':
                weight="Cushing Syndrome:-\nweight gain\nthin arms and legs\na round face\nincreased fat around the\n base of the neck.\neasy bruising\nweak muscles"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='dementia ':
                weight="Dementia :-\nmemory problem\nincreasing confusion\nreduced concentration\npersonality or behaviour changes\nloss of \nability to do everyday tasks\ndepression"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='dermatitis':
                weight="Dermatitis :-\nA red rash\nItching\nDry, cracked, scaly skin\nBumps and blisters\nsometimes with oozing and crusting\nSwelling, burning or tenderness"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='insipidus':
                weight="diabetes insipidus :-\nExtreme thirst\nProducing large\n amounts of urine\nFrequent need to get up to\nurinate during the night\nPreference for cold drinks"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='mellitus':
                weight="diabetes mellitus :-\nExtreme thirst\nBlurred vision\nFatigue\Irritability\nSlow-healing sores\nExtreme hunger\nUnexplained weight loss"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            


            if m=='diabetes':
                weight="please type any one :-\n1)insipidus\n2)mellitus"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
            if m=='sugar':
                weight="please type any one :-\n1)insipidus\n2)mellitus"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='diarrhea':
                weight="diarrhea :-Loose, watery stools\nAbdominal cramps\nAbdominal pain,Fever\nBlood in the stool\nMucus in the stool\nBloating\nUrgent need to \nhave a bowel movement"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='diaria':
                weight="diarrhea :-Loose, watery stools\nAbdominal cramps\nAbdominal pain,Fever\nBlood in the stool\nMucus in the stool\nBloating\nUrgent need to \nhave a bowel movement"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))





            if m=='diarhea':
                weight="diarrhea :-Loose, watery stools\nAbdominal cramps\nAbdominal pain,Fever\nBlood in the stool\nMucus in the stool\nBloating\nUrgent need to \nhave a bowel movement"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='dysphagia':
                weight="Having pain while \nswallowing\nBeing unable to swallow\nDrooling\nBeing hoarse\nBringing food back up\nUnexpectedly\n losing weight\nCoughing or gagging \nwhen swallowing"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='tuberculosis':
                weight="Tuberculosis:-\nCoughing that lasts\n three or more weeks\nCoughing up blood\nChest pain\npain with breathing or coughing\nUnintentional weight loss\nNight sweats\nFatigue\nLoss of appetite\nChills\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='tb':
                weight="Tuberculosis:-\nCoughing that lasts\n three or more weeks\nCoughing up blood\nChest pain\npain with breathing or coughing\nUnintentional weight loss\nNight sweats\nFatigue\nLoss of appetite\nChills\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='dengue':
                weight="Dengue:-\nSudden, high fever\nSevere headaches\nPain behind the eyes\nSevere joint and muscle pain\nNausea\nrash and red spot \nvomiting\nFatigue"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='dengu':
                weight="Dengue:-\nSudden, high fever\nSevere headaches\nPain behind the eyes\nSevere joint and muscle pain\nNausea\nrash and red spot \nvomiting\nFatigue"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))





            if m=='diverticulitis':
                weight="Diverticulitis:-\nNausea\nrash and red spot \nvomiting\nAbdominal tenderness\nThe lower left side of the\n abdomen is the usual\n site of the pain\nFever"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='pneumonia':
                weight="Pneumonia:-\nCough, which may produce \ngreenish, yellow or even\n bloody mucus\nFever, sweating\nand shaking chills\nShortness of breath\nRapid, shallow breathing\nchest pain\nfatigue\nloss of appetite\nNausea and vomiting\nespecially in small children\nConfusion, especially \nin older people"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='fibromyalgia':
                weight="Fibromyalgia:-\npain in back,neck or abdomen\npain occur at night\nSleep problems\nAnxiety or depression\nMorning stiffness\nNumbness\nheadache\nPainful menstrual cramps\nProblems with urinating"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='scabies':
                weight="scabies:-\nSkin: bumps or redness\nitching or skin burrow"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='chlamydia':
                weight="Chlamydia:-\npain or burning while peeing\npain during sex\nlower belly pain\nabnormal vaginal discharge\nbleeding between periods\npus or a watery/milky \ndischarge from the penis\nswollen or tender testicles\npain, discharge and/or \nbleeding around the anus"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='endometriosis':
                weight="Endometriosis:-\npain in abdomen,lower back,pelvis\nabnormal menstruation\nheavy menstruation\nirregular menstruation\n painful menstruation\nInfertility\nExcessive bleeding"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='strep throat':
                weight="Strep throat:-\nThroat pain that usually comes on quickly\nPainful swallowing\nRed and swollen tonsils\nSwollen\ntender lymph nodes in your neck\nFever\nHeadache\nRash\nNausea or vomiting\nBody aches"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='yeast':
                weight="yeast infection :-\npain in vagina\npain during sex\npain during urination\nsoreness\nredness\nRash"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='lupus':
                weight="lupus:-\nfever\nfatigue\nhair loss\nrash\npulmonary problems\nkidney problems\nswollen joints\ngastrointestinal problems\nthyroid problems\ndry mouth and eyes"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='shingles':
                weight="Shingles :-\npain in the skin\nblister\nscab\nulcers\nredness\nSensory: oversensitivity\npins and needles\nburning sensation\nfatigue\nitching"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='hemorrhoid':
                weight="Hemorrhoid:-\nextreme itching around the anus\nirritation and pain around the anus\nfecal leakage\npainful bowel movements\nblood on your tissue\n after having a bowel movement"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='hemorhoid':
                weight="Hemorrhoid:-\nextreme itching around the anus\nirritation and pain around the anus\nfecal leakage\npainful bowel movements\nblood on your tissue\n after having a bowel movement"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
                



            if m=='psoriasis':
                weight="Psoriasis:-\njoint pain\ndry skin that may crack and bleed\nsoreness around patches\nitching and burning\nsensations around patches\nthick, pitted nails"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
                

            if m=='hpv':
                weight="HPV:-\nitching or warts and verrucas\n(thease are the common symptoms)"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

                


            if m=='lyme':
                weight="Lyme disease:-\npain in the joints \nfatigue\nfever\nstifness in joint\nred eye and head ache"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))






            if m=='typhoid':
                weight="Typhoid:-\nhigh fever(103 F-104 F)\nhead ache,weakness\nfatigue,muscle aches\nsweating,dry cough\nloss of appetite\nAbdominal pain\nDiarrhea "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='high' and 'pressure':
                weight="Symptoms of High Blood Pressure:-\nheadache\nfatigue and confusion\nVision problems\nchest pain\nDifficulty breathing\nIrregular heartbeat\nBlood in the urine "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='low' and 'pressure':
                weight="Symptoms of Low Blood Pressure:-\nDizziness\nFainting \nBlurred vision\nNausea\nFatigue\nLack of concentration\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='cold':
                weight="common cold:-\nrunny nose\nSore throat\ncough,Congestion\nlow grade fever\nsneezing\nmild head ache "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='corona':
                weight="People may experience:-\ncough\nfever\ndifficulty breathing\ntiredness\nplease stay at home "
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='rid':
                weight="i just say you symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))



            if m=='treatment':
                weight="i just say you symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))

            

            if m=='cure':
                weight="i just say you symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))



            if m=='love':
                weight=random.choice(['so sweet !','so pretty !','oh !'])
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))

#----------------------------------------addh--------symptoms analysis--------------------------------------


            if m=='adhd':
                weight="ADHD :-\nImpulsiveness\nDisorganization and problems prioritizing\nProblems focusing on a task\nTrouble multitasking\n depression or learning disability\nmood:anger,boredom\nshort attention span"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='depression':
                weight="yes this is a common problem\nwell,i have 5 most effective tips\nto deal with depression\n1)make a phone call to your old friend\n2)listen your favourite song\n3)connect with good things(drawing,dancing,etc.)\n4)let's walk and buy a icecream(^_^)\n5)watch a funny show"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='depressed':
                weight="yes this is a common problem\nwell,i have 5 most effective tips\nto deal with depression\n1)make a phone call to your old friend\n2)listen your favourite song\n3)connect with good things(drawing,dancing,etc.)\n4)let's walk and buy a icecream(^_^)\n5)watch a funny show"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))






            if m=='hiccups':
                weight="Hiccupping is a symptom\nIt may sometimes be accompanied\nby a slight tightening\nsensation in your chest\nabdomen or throat\ncause:\nDrinking carbonated beverages\n Drinking too much alcohol \nEating too much Excitement or emotional\n stress\n Sudden temperature changes"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='hicups':
                weight="Hiccupping is a symptom\nIt may sometimes be accompanied\nby a slight tightening\nsensation in your chest\nabdomen or throat\ncause:\nDrinking carbonated beverages\n Drinking too much alcohol \nEating too much Excitement or emotional \nstress\n Sudden temperature changes"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(70,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='thanks':
                weight='most welcome'
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))




            if m=='thank you':
                weight='most welcome'
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))




            if m=='great':
                weight='thanks'
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))




            if m=='uninstall':
                weight='no.please no'
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))




            if m=='wow':
                weight='thanks'
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="20sp",color=(1,0,0,1)))


            if m=='kidney':
                weight='kidney stone:-\npain in back,belly or side\npain during urination\nurjent neeed to go\nblood in urine\nsmelly urine\nGoing a small amount at a time\nfever,vomiting '
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='copd':
                weight="COPD symptoms often don't appear\n until significant lung damage has \noccurred:-\nShortness of breath,wheezing\nchest pain or tightness\ncoughmay be yellow,greenish\nweakness\nsome time blood comes up\nin cough"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='foreign':
                weight="A foreign body is something that \nis stuck inside you but\n isn't supposed to be there\n you may inhale or\neat a foreign body\nexample=pins,coins,button of shirt ,etc."
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='lung' and 'cancer':
                weight="Lung cancer:-\nextreme cough\ncoughing up blood\nShortness of breath\nchest pain\nbone pain\nheadache\nweight loss"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='pulmonary':
                weight="Pulmonary embolism :-\nchest pain\nrapid or irregular heartbeat\nShortness of breath\nExcessive sweatin\nFever\nClammy or discolored skin (cyanosis)"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='cough' and 'blood':
                weight="there are many causes\nof coughing up blood:-\ncopd(fatal)\nlung cancer(fatal)\ndrug use(cocaine)\npneomonia\ntb\npulmonary embolism\njust type disease name \n to see symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='mucus' and 'blood':
                weight="there are many causes\nof coughing up blood:-\ncopd(fatal)\nlung cancer(fatal)\ndrug use(cocaine)\npneomonia\ntb\npulmonary embolism\njust type disease name \n to see symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='coughing' and 'blood':
                weight="there are many causes\nof coughing up blood:-\ncopd(fatal)\nlung cancer(fatal)\ndrug use(cocaine)\npneomonia\ntb\npulmonary embolism\n(just type disease name \n to see symptoms)"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='stroke':
                weight="Let's talk about symptoms\nof a stoke\nsudden numbness or weakness in the face\nespecially on one side of the body\nsudden confusion and trouble\nto speaking\nsudden trouble to seeing\n in one or both eyes\nsudden trouble to walk\nloss balance\nsudden headache\nif you see any of thease symptoms\n call some one to revive you"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='heart' and 'attack':
                weight="Let's talk about symptoms\nof a heart attack\nfeeling pain in chest or arms\nor neck.\nshortness of breath\ncold swaet\nfatigue\nLightheadedness or sudden dizziness"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            

            if m=='headache':
                weight="there are many many many causes \nof a headache\nbut i can give you 4 quick tips\nto get rid  from it.\n1)call some one to massage your head\n2)take a hot/cold thing and keep it\non your head\n3)take tea\n4)take a long sleep"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='malaria':
                weight="Malaria:-\nheadache\nhigh fever\nsweating\nvomiting\nanemia\nmuscle pain\nbloody stool\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='fever':
                weight="fever is not a disease\nit is a symptom of a  disease\nthere are many common causes\nof fever\n1)common cold\n2)typhoid\n3)dengue\n4)pneumonia\n5)malaria,etc.\n if you want to know \nsymptom of any disease just type\n in small letter"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='stool' :
                weight="actually there are many causes\nof blood in stool \nbut I just mention some point \n1)anal fissure\n2)polyps\n3)hemorrhoids\n4)crohn\n5)dirrhea\n6)and yes there is a one more\nfatal cause cancer"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='cancer' :
                weight="actually i know only 2 types \nof cancer's symptoms\n1)breast\n2)lung\nif you want to see the symptoms\njust type the name"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='fissure' :
                weight="anal fissure:- \nPain, sometimes severe\nduring bowel movements\nPain after bowel movements\n that can last up to several hours\nBright red blood on the stool \nor toilet paper after a bowel movement\nA visible crack in the\nskin around the anus\nA small lump or skin tag on the\n skin near the anal fissure"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='anal' :
                weight="anal fissure:- \nPain, sometimes severe\nduring bowel movements\nPain after bowel movements\n that can last up to several hours\nBright red blood on the stool \nor toilet paper after a bowel movement\nA visible crack in the\nskin around the anus\nA small lump or skin tag on the\n skin near the anal fissure"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='fissure' :
                weight="anal fissure:- \nPain, sometimes severe\nduring bowel movements\nPain after bowel movements\n that can last up to several hours\nBright red blood on the stool \nor toilet paper after a bowel movement\nA visible crack in the\nskin around the anus\nA small lump or skin tag on the\n skin near the anal fissure"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='cancer' :
                weight="actually i know only 2 types \nof cancer's symptoms\n1)breast\n2)lung\nif you want to see the symptoms\njust type the name"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


  
            if m=='polyps' :
                weight="polyps:-\nBleeding from the rectum\nabdominal pain\na change in the color of stools\nanemia\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


  
            if m=='hemorrhoids' :
                weight="hemorrhoids:-\nextreme itching around the anus\nirritation and pain around the anus\nfecal leakage\npainful bowel movements\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='bowel' :
                weight="the definition of bowel movement is\n'the excretion of solid waste from the body'\nexample:stool"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='breath' :
                weight="let's talk about some cause\nof breathing problem\n1)asthma\n2)copd\n3)lung  cancer\n4)pneumonia\n5)bronchitis\n6)heart attack\nlet's type any name of disease\nto know symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='breathing' :
                weight="let's talk about some cause\nof breathing problem\n1)asthma\n2)copd\n3)lung  cancer\n4)pneumonia\n5)bronchitis\n6)heart attack\nlet's type any name of disease\nto know symptoms"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='stiffness' :
                weight="let's talk about some cause\nof muscle stifness\n1)over exercise\n2)lack of daily exercise\n3)over weight\n4)having a poor diet\n5)not sleeping properly\n6)being in a cold or damp environment\nHIV,Tetanus,lupus,flu,etc\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='muscle' :
                weight="let's talk about some cause\nof muscle stifness\n1)over exercise\n2)lack of daily exercise\n3)over weight\n4)having a poor diet\n5)not sleeping properly\n6)being in a cold or damp environment\nHIV,Tetanus,lupus,flu,etc\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='stiff' :
                weight="let's talk about some cause\nof muscle stifness\n1)over exercise\n2)lack of daily exercise\n3)over weight\n4)having a poor diet\n5)not sleeping properly\n6)being in a cold or damp environment\nHIV,Tetanus,lupus,flu,etc\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='stifness' :
                weight="let's talk about some cause\nof muscle stifness\n1)over exercise\n2)lack of daily exercise\n3)over weight\n4)having a poor diet\n5)not sleeping properly\n6)being in a cold or damp environment\n7)HIV,Tetanus,lupus,flu,etc\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='tetanus' :
                weight="Tetanus:-\nbloody stool\ndiarrhea\nfever\nheadache\nsensitivity to touch\nmuscle stiffness\nrapid heartbeat\nsweating\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='flu' :
                weight="Flu:-\nshortness of breathing\ndiarrheapain in chest or abdomen\nlight fever and cough,headache\nNot urinating\nmuscle stiffness\nweakness\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
                
            if m=='allergy':
                weight="Main allergy symptoms:-\nsneezing and itching\nrunny and blocked nose\nitchy red watery eyes\nabdomen pain\nvommiting\nfeeling sick\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='allergies':
                weight="Main allergy symptoms:-\nsneezing and itching\nrunny and blocked nose\nitchy red watery eyes\nabdomen pain\nvommiting\nfeeling sick\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
                

            if m=='alergy':
                weight="Main allergy symptoms:-\nsneezing and itching\nrunny and blocked nose\nitchy red watery eyes\nabdominal pain\nvommiting\nfeeling sick\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='alargy':
                weight="Main allergy symptoms:-\nsneezing and itching\nrunny and blocked nose\nitchy red watery eyes\nabdomen pain\nvommiting\nfeeling sick\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
            

            if m=='rash':
                weight="There are many many many causes \n of rash.i can't say them all\nbut I can give you 5 types of rashes\nand you should not ignore them\n1)fever or painfull rashes\n2)if this happens within two weeks of\n starting a new medication\n3)Rashes that start to blister\n4)Purple spots that appear \non your hands and feet\n5)if your rash is in circular size"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='rashes':
                weight="There are many many many causes \n of rash.i can't say them all\nbut I can give you 5 types of rashes\nand you should not ignore them\n1)fever or painfull rashes\n2)if this happens within two weeks of\n starting a new medication\n3)Rashes that start to blister\n4)Purple spots that appear \non your hands and feet\n5)if your rash is in circular size"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='blister':
                weight="a small bubble on the skin filled with serum"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

                
 
            if m=='tonsillitis':
                weight="Tonsillitis:-\nRed, swollen tonsils\nWhite or yellow coating or\n patches on the tonsils\nSore throat\n3)high fever\n4stiffneck\nor headache\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='tonsilitis':
                weight="Tonsillitis:-\nRed, swollen tonsils\nWhite or yellow coating or\n patches on the tonsils\nSore throat\n3)high fever\n4stiffneck\nor headache\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='tonsil':
                weight="Tonsillitis:-\nRed, swollen tonsils\nWhite or yellow coating or\n patches on the tonsils\nSore throat\n3)high fever\n4stiffneck\nor headache\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='bleeding'and'anus':
                weight="some causes of rectal bleeding:-\ninternal bleeding\nrectal cancer\npolyps\ndiverticulitis\nhemorrhoids\nanal fissures\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))
            if m=='anus':
                weight="some causes of rectal bleeding:-\ninternal bleeding\nrectal canceror\npolyps\ndiverticulitis\nhemorrhoids\nanal fissures\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='pussy':
                weight="some causes of rectal bleeding:-\ninternal bleeding\nrectal canceror\npolyps\ndiverticulitis\nhemorrhoids\nanal fissures\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='bleeding'and'rectal':
                weight="some causes of rectal bleeding:-\ninternal bleeding\nrectal canceror\npolyps\ndiverticulitis\nhemorrhoids\nanal fissures\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='bleeding':
                weight="some causes of rectal bleeding:-\ninternal bleeding\nrectal canceror\npolyps\ndiverticulitis\nhemorrhoids\nanal fissures\n"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='hives':
                weight="Hives(urticaria):-\nitchy bumps\nor red skin color"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='urticaria':
                weight="Hives(urticaria):-\nitchy bumps\nor red skin color"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='itch':
                weight="there are mainly 2 causes of itching\nhives\nallergy"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='itchy':
                weight="there are mainly 2 causes of itching\nhives\nallergy"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='itching':
                weight="there are mainly 2 causes of itching\nhives\nallergy"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='confusion':
                weight="dementia can be a cause of confusion\nif sudden confusion occurs\nit is may be a symptom of stroke\nalso pnumonea,or high pressure can \nbe a csuse of confusion"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='faint':
                weight="actually fainting happens when your brain\n is not getting enough oxygen\nthere are some causes for fainting\nfear,severe pain\nlow blood pressure\nlow blood diabetes\nstanding in one position\n for too long\nsun stroke\nstanding up too quickly"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='fainting':
                weight="actually fainting happens when your brain\n is not getting enough oxygen\nthere are some causes for fainting\nfear,severe pain\nlow blood pressure\nlow blood diabetes\nstanding in one position\n for too long\nsun stroke\nstanding up too quickly"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='belly':
                weight="there are some reason\nfor belly pain\nconstipation\ndiarrhea\nacidity\nvomiting,stress\nthere are some rare disease\n for belly pain.\nif your belly pain is regular\nyou should not ignore this\ngastroesophageal reflux disease(gerd)\nchron\nkidney stone\nappendicitis"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='abdomial':
                weight="there are some reason\nfor belly pain\nconstipation\ndiarrhea\nacidity\nvomiting,stress\nthere are some rare disease\n for belly pain.\nif your belly pain is regular\nyou should not ignore this\ngastroesophageal reflux disease(gerd)\nchron\nkidney stone\nappendicitis"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='abdomen':
                weight="there are some reason\nfor belly pain\nconstipation\ndiarrhea\nacidity\nvomiting,stress\nthere are some rare disease\n for belly pain.\nif your belly pain is regular\nyou should not ignore this\ngastroesophageal reflux disease(gerd)\nchron\nkidney stone\nappendicitis"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='acid':
                weight="the main symptoms of acidity :-\nburning pain in the chest\nthat usally occurs after eating\nand then feeling discomfort in upper abdomen\nthere are some tips to rid out from acidity:-\nyou have to change your lifestyle\nloss your weight(you can search here)\neat slowly\navoid junk food\ndon't smoke\nwalk for some minutes after dinner"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

    
            if m=='acidity':
                weight="the main symptoms of acidity :-\nburning pain in the chest\nthat usally occurs after eating\nand then feeling discomfort in upper abdomen\nthere are some tips to rid out from acidity:-\nyou have to change your lifestyle\nloss your weight(you can search here)\neat slowly\navoid junk food\ndon't smoke\nwalk for some minutes after dinner"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='gerd':
                weight="the main symptoms of acidity or GERD:-\nburning pain in the chest\nthat usally occurs after eating\nand then feeling discomfort in upper abdomen\nthere are some tips to rid out from acidity:-\nyou have to change your lifestyle\nloss your weight(you can search here)\neat slowly\navoid junk food\ndon't smoke\nwalk for some minutes after dinner"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))                
            

            

            if m=='gas':
                weight="the main symptoms of acidity :-\nburning pain in the chest\nthat usally occurs after eating\nand then feeling discomfort in upper abdomen\nthere are some tips to rid out from acidity:-\nyou have to change your lifestyle\nloss your weight(you can search here)\neat slowly\navoid junk food\ndon't smoke\nwalk for some minutes after dinner"
                

                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))

                self.add_widget(Label(text=weight,pos=(60,230),size=(200,200),font_size="13sp",color=(0,0,0,1)))     



            if m=='period':
                weight="there are some problems about :-\nperiod or mensutral cycle problem\ntype one :-\nblood loss and clots:-\nif you need to change out less than 2 hours\nyou should consult a doctor\nvomiting is normal in period\nskipping or missing a period:-\nIf you miss more than one period\nand you’ve taken a pregnancy test to\nmake sure that’s not the\nreason talk to your doctor"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))




            if m=='menstrual':
                weight="there are some problems about :-\nperiod or mensutral cycle problem\ntype one :-\nblood loss and clots:-\nif you need to change out less than 2 hours\nyou should consult a doctor\nvomiting is normal in period\nskipping or missing a period:-\nIf you miss more than one period\nand you’ve taken a pregnancy test to\nmake sure that’s not the\nreason talk to your doctor"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='period':
                weight="there are some problems about :-\nperiod or mensutral cycle problem\ntype one :-\nblood loss and clots:-\nif you need to change out less than 2 hours\nyou should consult a doctor\nvomiting is normal in period\nskipping or missing a period:-\nIf you miss more than one period\nand you’ve taken a pregnancy test to\nmake sure that’s not the\nreason talk to your doctor"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='pireod':
                weight="there are some problems about :-\nperiod or mensutral cycle problem\ntype one :-\nblood loss and clots:-\nif you need to change out less than 2 hours\nyou should consult a doctor\nvomiting is normal in period\nskipping or missing a period:-\nIf you miss more than one period\nand you’ve taken a pregnancy test to\nmake sure that’s not the\nreason talk to your doctor"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='pee':
                weight="pain during urination:-\npregnant women may feel that\nand any type of disease in blader\nvaginal infection\nurinary track infection\nprostate disease\nblader cancer\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))
            if m=='urine':
                weight="pain during urination:-\npregnant women may feel that\nand any type of disease in blader\nvaginal infection\nurinary track infection\nprostate disease\nblader cancer\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='urination':
                weight="pain during urination:-\npregnant women may feel that\nand any type of disease in blader\nvaginal infection\nurinary track infection\nprostate disease\nblader cancer\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='blader':
                weight="blader cancer:-\nblood in urine\npainfull utination\nfrequent urination\npain  in lower back\nurgent urination\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))
                
            if m=='appendicitis':
                weight="appendicitis:-\n the main symptoms\nof appendicitis is\nsharp pain in  belly\neven vomiting,fever,fatigue also happen\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='appendicite':
                weight="appendicitis:-\n the main symptoms\nof appendicitis is\nsharp pain in  belly\neven vomiting,fever,fatigue also happen\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='apendicite':
                weight="appendicitis:-\n the main symptoms\nof appendicitis is\nsharp pain in  belly\neven vomiting,fever,fatigue also happen\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='weakness':
                weight="weakness:-\n in every disease you can feel weakness\nso yo should understand actual reason\nso type another symptoms\nbut if you have not any reason \nyou should sleep enough\n"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='weak':
                weight="weakness:-\n in every disease you can feel weakness\nso yo should understand actual reason\nso type another symptoms\nbut if you have not any reason \nyou should sleep enough"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='tired':
                weight="weakness:-\n in every disease you can feel weakness\nso yo should understand actual reason\nso type another symptoms\nbut if you have not any reason \nyou should sleep enough"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))


            if m=='rickets':
                weight="rickets:-\npain and tenderness in the bone\nbone fractures\nmuscle cramps\nteeth deformities\nan oddly shaped skull"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='ricket':
                weight="rickets:-\npain and tenderness in the bone\nbone fractures\nmuscle cramps\nteeth deformities\nan oddly shaped skull"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='hepatitis':
                weight="hepatitis:-\ndark urine but pale stool\nabdominal pain\nflu like symptoms\nyellow skin and eyes\nfatigue and weight loss"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))



            if m=='joint':
                weight="the unserious cause is an injury\nbut the serious causes are:-\nlyme\ndengue\nlupus\nan  infection of bone\nrickets\nfibromyalgia\narthritis"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

            if m=='bone':
                weight="the unserious cause is an injury\nbut the serious causes are:-\nlyme\ndengue\nlupus\nan  infection of bone\nrickets\nfibromyalgia\narthritis"
                with self.canvas:
                    Rectangle(source='label.png',pos=(0,50),size=(300,450))
                self.add_widget(Label(text=weight,pos=(70,250),size=(200,200),font_size="13sp",color=(0,0,0,1)))

    

                

              
#--------------------not complete yet---------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------data analysis------------------------------------------------------------------------------------------------------------------

                







                


                












                
            

            


                
                
                


            


        




                






                


            






    



                


                







                








    def tuhin(self,instance):
        plyer.notification.notify(title='pocket doctor', message="make sure your internet connection")
        
        self.ads = KivMob(TestIds.APP)
        self.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.ads.request_interstitial()
        return Button(text='Show Interstitial',
                      on_release=lambda a:self.ads.show_interstitial())

    def on_resume(self):
        self.ads.request_interstitial()


        
        


                










    def lol(self,instance):
        plyer.notification.notify(title='pocket doctor', message="make sure your internet connection")
        facts=['Laughing is good for the heart and can increase blood flow by 20 percent.','Your skin works hard. Not only is it the largest organ in the body, but it defends against disease and infection, regulates your temperature and aids in vitamin production.','Always look on the bright side: being an optimist can help you live longer','Exercise will give you more energy, even when you’re tired','Sitting and sleeping are great in moderation, but too much can increase your chances of an early death','A lack of exercise now causes as many deaths as smoking.','Nearly 30% of the world’s population is obese.','Between 2000 and 2015, the average global life expectancy increased by five years','Less than 1% of Americans ride their bike to work, while 50% of Copenhagen residents bike to work or school.','The US spends almost three times more on healthcare than any other country in the world, but ranks last in life expectancy among the 12 wealthiest industrialized countries.','Learning a new language or playing a musical instrument gives your brain a boost.','Feeling stressed? Read. Getting lost in a book can lower levels of cortisol, or other unhealthy stress hormones, by 67 percent.','Maintaining good relationships with family and friends is good for your health, memory and longevity.','Drinking coffee can reduce the risk of depression, especially in women.','Smelling rosemary may increase alertness and improve memory so catch a whiff before a test or important meeting.','Swearing can make you feel better when you’re in pain.','Writing things out by hand will help you remember them.','Chewing gum makes you more alert, relieves stress and reduces anxiety levels','Yoga can boost your cognitive function and lowers stress','Walking outside – or spending time in green space – can reduce negative thoughts and boost self-esteem','Chocolate is good for your skin; its antioxidants improve blood flow and protect against UV damage.','Almonds, avocados and arugula (the three ‘A’s) can boost your sex drive and improve fertility','Tea can lower risks of heart attack, certain cancers, type 2 Diabetes and Parkinson’s disease. Just make sure your tea isn’t too sweet!','Eating oatmeal provides a serotonin boost to calm the brain and improve your mood.','Women below the age of 50 need twice the amount of iron per day as men of the same age.','Although it only takes you a few minutes to eat a meal, it takes your body hours to completely digest the food','An apple a day does keep the doctor away. Apples can reduce levels of bad cholesterol to keep your heart healthy.','The amino acid found in eggs can help improve your reflexes.','Extra virgin olive oil is the healthiest fat on the planet.','Vitamin D is as important as calcium in determining bone health, and most people don’t get enough of it','The body has more than 650 muscles.','To lose one pound of fat, you need to burn roughly 3,500 calories.','Walking at a fast pace for three hours or more at least one time a week, you can reduce your risk of heart disease by up to 65%.','Even at rest, muscle is three times more efficient at burning calories than fat.','Running is good for you. People who run 12-18 miles a week have a stronger immune system and can increase their bone mineral density.','Exercising regularly can increase your lifespan by keeping your DNA healthy and young.','The average moderately active person walks approximately 7,500 steps a day, which is the lifetime equivalent of walking around the Earth five times.']
        fac=random.choice(facts)
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()
        return Label(text=fac,font_size='15sp')
        
        





    
            

class TestApp(App):

    def build(self):
        return myfuck()

if __name__ == '__main__':
    TestApp().run()
